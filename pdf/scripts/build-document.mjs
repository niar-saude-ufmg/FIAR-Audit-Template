#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { PDFDocument, StandardFonts, rgb } from 'pdf-lib';

const rootDir = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const distDir = path.join(rootDir, 'pdf','output');
const tmpDir = path.join(rootDir, 'pdf', '.tmp-build');
const outputPdf = path.join(distDir, 'relatorio_final.pdf');
const assetsDir = path.join(rootDir, 'pdf', 'assets');

const orderedRoots = [
  'documentacao_projeto',
  'artefatos_projeto',
  'avaliacao_niar',
  'decisao_institucional',
  'auditoria_final'
];

const isSupported = (name) => /\.(pdf|docx)$/i.test(name);
const isIgnored = (name) => name === '.gitkeep' || name.startsWith('~$');
const A4 = { width: 595.28, height: 841.89 };
const COVER_TOC_MARGIN_X = 62.4; // 22mm, igual ao padrão dos outros documentos
const FOOTER_MARGIN_X = 34; // configuracao anterior

function ensureCommand(command) {
  const result = spawnSync('bash', ['-lc', `command -v ${command}`], { stdio: 'pipe', encoding: 'utf8' });
  if (result.status !== 0) throw new Error(`Erro: ${command} nao encontrado.`);
}

function getLibreOfficeBin() {
  const result = spawnSync('bash', ['-lc', 'command -v libreoffice || command -v soffice || test -x /opt/homebrew/bin/soffice && echo /opt/homebrew/bin/soffice'], {
    stdio: 'pipe',
    encoding: 'utf8'
  });
  if (result.status !== 0) throw new Error('Erro: LibreOffice (libreoffice ou soffice) nao encontrado.');
  return result.stdout.trim().split(/\s+/)[0];
}

function run(command, args) {
  const result = spawnSync(command, args, { stdio: 'pipe', encoding: 'utf8' });
  if (result.status !== 0) throw new Error(result.stderr || `Erro executando ${command} ${args.join(' ')}`);
}

function resetOutput() {
  fs.mkdirSync(tmpDir, { recursive: true });
  if (fs.existsSync(outputPdf)) fs.rmSync(outputPdf, { force: true });
  for (const item of fs.readdirSync(tmpDir)) {
    if (/\.(pdf|txt|docx)$/i.test(item)) fs.rmSync(path.join(tmpDir, item), { force: true });
  }
}

function cleanupTemp() {
  if (fs.existsSync(tmpDir)) {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

function walkFiles(absDir, relBase) {
  const entries = fs.readdirSync(absDir, { withFileTypes: true });
  let files = [];

  for (const entry of entries) {
    if (entry.name === '.git') continue;
    const absPath = path.join(absDir, entry.name);
    const relPath = path.join(relBase, entry.name);

    if (entry.isDirectory()) {
      files = files.concat(walkFiles(absPath, relPath));
      continue;
    }

    if (entry.isFile() && isSupported(entry.name) && !isIgnored(entry.name)) {
      files.push({ absPath, relPath: relPath.split(path.sep).join('/') });
    }
  }

  return files;
}

function collectFiles(relRoot) {
  const absRoot = path.join(rootDir, relRoot);
  if (!fs.existsSync(absRoot) || !fs.statSync(absRoot).isDirectory()) return [];
  return walkFiles(absRoot, relRoot).sort((a, b) => a.relPath.localeCompare(b.relPath, 'pt-BR'));
}

function titleFromFilename(relPath) {
  const base = path.basename(relPath, path.extname(relPath));
  const lower = base.toLowerCase();
  if (lower.includes('datacard') || lower.includes('data_card')) return 'DataCard';
  if (lower.includes('modelcard') || lower.includes('model_card')) return 'ModelCard';
  if (lower.includes('ripd')) return 'RIPD';
  return base
    .replace(/[_-]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function classifyToc(relPath) {
  const normalized = relPath.toLowerCase();

  if (normalized.startsWith('documentacao_projeto/')) {
    return {
      section: 'Documentação do projeto',
      item: titleFromFilename(relPath)
    };
  }

  if (normalized.startsWith('artefatos_projeto/operational_artifacts/')) {
    return {
      section: 'Artefatos operacionais',
      item: titleFromFilename(relPath)
    };
  }

  if (normalized.startsWith('artefatos_projeto/')) {
    if (
      normalized.includes('/data_cards/')
      || normalized.includes('datacard')
      || normalized.includes('data_card')
    ) {
      return {
        section: 'Artefatos do projeto',
        item: 'DataCard'
      };
    }

    if (
      normalized.includes('/model_cards/')
      || normalized.includes('modelcard')
      || normalized.includes('model_card')
    ) {
      return {
        section: 'Artefatos do projeto',
        item: 'ModelCard'
      };
    }

    if (
      normalized.includes('/ripd/')
      || normalized.includes('ripd')
    ) {
      return {
        section: 'Artefatos do projeto',
        item: 'RIPD'
      };
    }

    if (normalized.includes('/consolidated_iar_report/')) {
      return {
        section: 'Artefatos do projeto',
        item: 'Relatório Consolidado de IAR'
      };
    }

    return {
      section: 'Artefatos do projeto',
      item: titleFromFilename(relPath)
    };
  }

  if (normalized.startsWith('avaliacao_niar/')) {
    return {
      section: 'Avaliação do NIAR-Saúde',
      item: titleFromFilename(relPath)
    };
  }

  if (normalized.startsWith('decisao_institucional/')) {
    return {
      section: 'Decisões institucionais',
      item: titleFromFilename(relPath)
    };
  }

  if (normalized.startsWith('auditoria_final/')) {
    return {
      section: 'Resultado consolidado do ciclo',
      item: titleFromFilename(relPath)
    };
  }

  return {
    section: 'Documentos',
    item: titleFromFilename(relPath)
  };
}

async function pageCount(pdfPath) {
  const bytes = fs.readFileSync(pdfPath);
  const doc = await PDFDocument.load(bytes);
  return doc.getPageCount();
}

function convertDocxToPdf(libreOfficeBin, sourcePath, targetPath) {
  const tmpName = `${Date.now()}-${Math.random().toString(36).slice(2)}.docx`;
  const tmpDocx = path.join(tmpDir, tmpName);
  fs.copyFileSync(sourcePath, tmpDocx);

  run(libreOfficeBin, ['--headless', '--convert-to', 'pdf', '--outdir', tmpDir, tmpDocx]);

  const converted = path.join(tmpDir, tmpName.replace(/\.docx$/i, '.pdf'));
  if (!fs.existsSync(converted)) throw new Error(`Erro ao converter DOCX: ${sourcePath}`);

  fs.renameSync(converted, targetPath);
  fs.rmSync(tmpDocx, { force: true });
}

function ptDate(isoDate) {
  const [y, m, d] = isoDate.split('-');
  return `${d}/${m}/${y}`;
}

function centerTextX(pageWidth, font, size, text) {
  const textWidth = font.widthOfTextAtSize(text, size);
  return (pageWidth - textWidth) / 2;
}

function rightTextX(rightEdge, font, size, text) {
  return rightEdge - font.widthOfTextAtSize(text, size);
}

function fitTextToWidth(text, font, size, maxWidth) {
  if (font.widthOfTextAtSize(text, size) <= maxWidth) return text;
  const ellipsis = '...';
  let out = text;
  while (out.length > 0 && font.widthOfTextAtSize(`${out}${ellipsis}`, size) > maxWidth) {
    out = out.slice(0, -1);
  }
  return `${out}${ellipsis}`;
}

function drawCover(page, font, fontBold, nowText, assets) {
  const centerX = A4.width / 2;
  if (assets.coverTop) {
    const topW = 250;
    const topH = (assets.coverTop.height / assets.coverTop.width) * topW;
    page.drawImage(assets.coverTop, { x: centerX - topW / 2, y: A4.height - 210, width: topW, height: topH });
  }

  const line1 = 'NIAR-SAÚDE/UFMG';
  const line2 = 'Relatório consolidado do ciclo FIAR-Saúde';
  const line3 = 'Artefatos, avaliação técnica e decisões institucionais';
  const line4 = `Data de geração do relatório: ${ptDate(nowText)}`;

  page.drawText(line1, {
    x: centerTextX(A4.width, fontBold, 12, line1),
    y: A4.height - 315,
    size: 12,
    font: fontBold,
    color: rgb(0.09, 0.27, 0.45)
  });

  page.drawText(line2, {
    x: centerTextX(A4.width, fontBold, 20, line2),
    y: A4.height - 350,
    size: 20,
    font: fontBold,
    color: rgb(0.1, 0.1, 0.1)
  });

  page.drawText(line3, {
    x: centerTextX(A4.width, font, 12, line3),
    y: A4.height - 380,
    size: 12,
    font,
    color: rgb(0.2, 0.2, 0.2)
  });

  page.drawText(line4, {
    x: centerTextX(A4.width, font, 11, line4),
    y: A4.height - 408,
    size: 11,
    font,
    color: rgb(0.25, 0.25, 0.25)
  });

  if (assets.coverBottom) {
    page.drawImage(assets.coverBottom, { x: centerX - 170, y: 82, width: 340, height: 62 });
  }
}

function drawHeaderFooter(page, font, pageNumber, totalNumberedPages, assets) {
  const left = FOOTER_MARGIN_X;
  const right = A4.width - FOOTER_MARGIN_X;

  // Rodape: linha + regua UFMG a esquerda + pagina a direita
  page.drawLine({
    start: { x: left, y: 31 },
    end: { x: right, y: 31 },
    thickness: 0.5,
    color: rgb(0.47, 0.47, 0.47)
  });
  if (assets.footerLogo) {
    page.drawImage(assets.footerLogo, { x: left, y: 10, width: 150, height: 18 });
  }

  const pageText = `Página ${pageNumber} de ${totalNumberedPages}`;
  page.drawText(pageText, {
    x: right - 75,
    y: 16,
    size: 8,
    font,
    color: rgb(0.35, 0.35, 0.35)
  });
}

async function main() {
  const libreOfficeBin = getLibreOfficeBin();
  resetOutput();

  const now = new Date();
  const nowText = now.toISOString().slice(0, 10);

  const docs = [];
  let index = 0;

  for (const relRoot of orderedRoots) {
    const files = collectFiles(relRoot);
    for (const fileMeta of files) {
      const ext = path.extname(fileMeta.absPath).toLowerCase();

      index += 1;
      const prefix = String(index).padStart(3, '0');
      const baseName = path.basename(fileMeta.absPath);
      const outPdf = path.join(tmpDir, `${prefix}-${baseName.replace(/\.(docx|pdf)$/i, '.pdf')}`);

      if (ext === '.pdf') {
        fs.copyFileSync(fileMeta.absPath, outPdf);
      } else if (ext === '.docx') {
        convertDocxToPdf(libreOfficeBin, fileMeta.absPath, outPdf);
      }

      const pages = await pageCount(outPdf);
      const tocMeta = classifyToc(fileMeta.relPath);
      docs.push({ relPath: fileMeta.relPath, pdfPath: outPdf, pages, tocSection: tocMeta.section, tocItem: tocMeta.item });
    }
  }

  if (!docs.length) throw new Error('Erro: nenhum arquivo PDF ou DOCX encontrado nas pastas esperadas.');

  const tocRows = [];
  let lastSectionForRows = '';
  for (const d of docs) {
    if (d.tocSection !== lastSectionForRows) {
      tocRows.push({ type: 'section', text: d.tocSection, page: '' });
      lastSectionForRows = d.tocSection;
    }
    tocRows.push({ type: 'item', text: d.tocItem, page: '' });
  }

  const tocLinesPerPage = 28;
  const tocPages = Math.max(1, Math.ceil(tocRows.length / tocLinesPerPage));

  let runningPage = tocPages + 1; // paginas numeradas: TOC + conteudo (capa excluida)
  const tocEntries = docs.map((d) => {
    const startPage = runningPage;
    runningPage += d.pages;
    return { ...d, startPage };
  });

  // Atualiza numero de pagina dos itens do sumario descritivo
  const tocRowsWithPages = [];
  let lastSection = '';
  for (const entry of tocEntries) {
    if (entry.tocSection !== lastSection) {
      tocRowsWithPages.push({ type: 'section', text: entry.tocSection, page: '' });
      lastSection = entry.tocSection;
    }
    tocRowsWithPages.push({ type: 'item', text: entry.tocItem, page: String(entry.startPage) });
  }

  const finalDoc = await PDFDocument.create();
  const font = await finalDoc.embedFont(StandardFonts.Helvetica);
  const fontBold = await finalDoc.embedFont(StandardFonts.HelveticaBold);
  const assets = {};
  const coverTopPath = path.join(assetsDir, 'capa-niar.jpeg');
  const coverBottomPath = path.join(assetsDir, 'capa-ufmg.jpeg');
  const footerLogoPath = path.join(assetsDir, 'rodape-ufmg.png');
  if (fs.existsSync(coverTopPath)) assets.coverTop = await finalDoc.embedJpg(fs.readFileSync(coverTopPath));
  if (fs.existsSync(coverBottomPath)) assets.coverBottom = await finalDoc.embedJpg(fs.readFileSync(coverBottomPath));
  if (fs.existsSync(footerLogoPath)) assets.footerLogo = await finalDoc.embedPng(fs.readFileSync(footerLogoPath));

  const coverPage = finalDoc.addPage([A4.width, A4.height]);
  drawCover(coverPage, font, fontBold, nowText, assets);

  for (let p = 0; p < tocPages; p += 1) {
    const page = finalDoc.addPage([A4.width, A4.height]);
    page.drawText('SUMÁRIO', {
      x: COVER_TOC_MARGIN_X,
      y: A4.height - 70,
      size: 18,
      font: fontBold,
      color: rgb(0.08, 0.2, 0.38)
    });

    const start = p * tocLinesPerPage;
    const end = Math.min(start + tocLinesPerPage, tocRowsWithPages.length);
    let y = A4.height - 110;

    for (let i = start; i < end; i += 1) {
      const row = tocRowsWithPages[i];
      if (row.type === 'section') {
        page.drawText(row.text, { x: COVER_TOC_MARGIN_X + 4, y, size: 11, font: fontBold, color: rgb(0.1, 0.1, 0.1) });
        y -= 17;
      } else {
        const pageRight = A4.width - COVER_TOC_MARGIN_X - 4;
        const pageNumberX = rightTextX(pageRight, fontBold, 10, row.page);
        const textLeft = COVER_TOC_MARGIN_X + 4;
        const textMaxWidth = pageNumberX - textLeft - 12; // gap entre titulo e numero
        const trimmed = fitTextToWidth(row.text, font, 10, textMaxWidth);
        const titleWidth = font.widthOfTextAtSize(trimmed, 10);
        const dotStartX = textLeft + titleWidth + 6;
        const dotEndX = pageNumberX - 6;

        page.drawText(trimmed, { x: textLeft, y, size: 10, font, color: rgb(0.1, 0.1, 0.1) });
        if (dotEndX > dotStartX + 8) {
          page.drawLine({
            start: { x: dotStartX, y: y + 4.5 },
            end: { x: dotEndX, y: y + 4.5 },
            thickness: 0.5,
            color: rgb(0.65, 0.65, 0.65)
          });
        }
        page.drawText(
          row.page,
          {
            x: pageNumberX,
            y,
            size: 10,
            font: fontBold,
            color: rgb(0.1, 0.1, 0.1)
          }
        );
        y -= 15;
      }
    }
  }

  for (const doc of docs) {
    const source = await PDFDocument.load(fs.readFileSync(doc.pdfPath));
    const copiedPages = await finalDoc.copyPages(source, source.getPageIndices());
    copiedPages.forEach((pg) => finalDoc.addPage(pg));
  }

  const totalPages = finalDoc.getPageCount();
  const numberedPages = totalPages - 1; // capa sem numero

  for (let i = 1; i < totalPages; i += 1) {
    const page = finalDoc.getPage(i);
    const pageNumber = i; // primeira pagina numerada eh o sumario 1
    drawHeaderFooter(page, font, pageNumber, numberedPages, assets);
  }

  fs.mkdirSync(distDir, { recursive: true });
  fs.writeFileSync(outputPdf, await finalDoc.save());
  cleanupTemp();
  console.log(`PDF consolidado gerado em: ${outputPdf}`);
}

main().catch((error) => {
  cleanupTemp();
  console.error(error.message || error);
  process.exit(1);
});

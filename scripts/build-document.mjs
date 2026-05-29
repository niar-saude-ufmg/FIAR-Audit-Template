#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const rootDir = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const distDir = path.join(rootDir, 'dist');
const tmpDir = path.join(distDir, 'intermediarios');
const outputPdf = path.join(distDir, 'documento-auditoria-fiar.pdf');

const orderedRoots = [
  'documentacao_projeto',
  'artefatos_projeto',
  'avaliacao_auditor',
  'auditoria_final'
];

const isSupported = (name) => /\.(pdf|docx|md)$/i.test(name);
const isIgnored = (name) => name === '.gitkeep' || name.startsWith('~$');

function ensureCommand(command) {
  const result = spawnSync('bash', ['-lc', `command -v ${command}`], { stdio: 'pipe', encoding: 'utf8' });
  if (result.status !== 0) {
    throw new Error(`Erro: ${command} nao encontrado.`);
  }
}

function getLibreOfficeBin() {
  const result = spawnSync('bash', ['-lc', 'command -v libreoffice || command -v soffice'], {
    stdio: 'pipe',
    encoding: 'utf8'
  });

  if (result.status !== 0) {
    throw new Error('Erro: LibreOffice (libreoffice ou soffice) nao encontrado.');
  }

  return result.stdout.trim().split(/\s+/)[0];
}

function run(command, args) {
  const result = spawnSync(command, args, { stdio: 'pipe', encoding: 'utf8' });
  if (result.status !== 0) {
    throw new Error(result.stderr || `Erro executando ${command} ${args.join(' ')}`);
  }
}

function resetOutput() {
  fs.mkdirSync(tmpDir, { recursive: true });
  if (fs.existsSync(outputPdf)) fs.rmSync(outputPdf, { force: true });
  for (const item of fs.readdirSync(tmpDir)) {
    if (/\.pdf$/i.test(item) || /\.txt$/i.test(item)) {
      fs.rmSync(path.join(tmpDir, item), { force: true });
    }
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

function createCoverPdf(libreOfficeBin) {
  const now = new Date();
  const dateText = now.toISOString().slice(0, 10);
  const txtName = '000-capa-auditoria-fiar.txt';
  const txtPath = path.join(tmpDir, txtName);
  const coverText = [
    'DOCUMENTO DE AUDITORIA FIAR',
    '',
    'Repositorio base: FIAR-Audit-Template',
    'Gerado automaticamente a partir dos artefatos preenchidos.',
    '',
    `Data de geracao: ${dateText}`,
    '',
    'Observacao: este PDF consolida evidencias; nao preenche conteudo automaticamente.'
  ].join('\n');

  fs.writeFileSync(txtPath, coverText, 'utf8');
  run(libreOfficeBin, ['--headless', '--convert-to', 'pdf', '--outdir', tmpDir, txtPath]);

  const converted = path.join(tmpDir, txtName.replace(/\.txt$/i, '.pdf'));
  if (!fs.existsSync(converted)) {
    throw new Error('Erro ao gerar capa em PDF.');
  }

  const finalCover = path.join(tmpDir, '000-capa-auditoria-fiar.pdf');
  if (converted !== finalCover) fs.renameSync(converted, finalCover);
  return finalCover;
}

function main() {
  const libreOfficeBin = getLibreOfficeBin();
  ensureCommand('qpdf');
  resetOutput();

  const pdfInputs = [];
  const withCover = process.env.FIAR_DISABLE_COVER !== '1';
  if (withCover) {
    pdfInputs.push(createCoverPdf(libreOfficeBin));
  }

  let index = 0;
  for (const relRoot of orderedRoots) {
    const files = collectFiles(relRoot);

    for (const fileMeta of files) {
      const file = fileMeta.absPath;
      index += 1;
      const prefix = String(index).padStart(3, '0');
      const baseName = path.basename(file);
      const ext = path.extname(baseName).toLowerCase();

      if (ext === '.pdf') {
        const out = path.join(tmpDir, `${prefix}-${baseName}`);
        fs.copyFileSync(file, out);
        pdfInputs.push(out);
        continue;
      }

      if (ext === '.docx') {
        run(libreOfficeBin, ['--headless', '--convert-to', 'pdf', '--outdir', tmpDir, file]);
        const converted = path.join(tmpDir, `${path.basename(baseName, ext)}.pdf`);
        if (!fs.existsSync(converted)) {
          throw new Error(`Erro ao converter DOCX: ${file}`);
        }
        const out = path.join(tmpDir, `${prefix}-${path.basename(baseName, ext)}.pdf`);
        fs.renameSync(converted, out);
        pdfInputs.push(out);
        continue;
      }

      if (ext === '.md') {
        console.log(`Aviso: arquivo Markdown ignorado no build atual: ${fileMeta.relPath}`);
      }
    }
  }

  if (!pdfInputs.length || (pdfInputs.length === 1 && withCover)) {
    throw new Error('Erro: nenhum arquivo PDF ou DOCX encontrado nas pastas esperadas.');
  }

  run('qpdf', ['--empty', '--pages', ...pdfInputs, '--', outputPdf]);
  console.log(`PDF consolidado gerado em: ${outputPdf}`);
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}

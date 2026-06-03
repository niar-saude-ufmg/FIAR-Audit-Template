# Geração do Relatório PDF

O build consolida automaticamente todos os artefatos da auditoria em um único PDF: `relatorio/relatorio-auditoria-fiar-saude.pdf`.

---

## O que é incluído

Todos os `.pdf` e `.docx` encontrados nas pastas abaixo, incluindo subpastas, na seguinte ordem:

```text
documentacao_projeto/ → artefatos_projeto/ → avaliacao_niar/ → auditoria_final/
```

Regras:

- `.pdf`: entra direto.
- `.docx`: convertido automaticamente com LibreOffice.
- `.gitkeep` e temporários `~$*.docx`: ignorados.
- Dentro de cada bloco, ordenação por caminho.

O PDF gerado inclui:

- capa automática;
- sumário automático com página inicial de cada documento;
- cabeçalho e rodapé em todas as páginas internas;
- numeração contínua de páginas.

---

## Execução local

Pré-requisitos:

- Node.js
- LibreOffice (binário `libreoffice` ou `soffice`)

Comando:

```bash
npm --prefix pdf install
npm --prefix pdf run build:pdf
```

O PDF final estará em:

```text
relatorio/relatorio-auditoria-fiar-saude.pdf
```

---

## GitHub Actions

O workflow `.github/workflows/build-document.yml` roda em:

- push na `main`
- `pull_request`
- `workflow_dispatch`

Na `main`, se o PDF mudar, a pipeline commita automaticamente a nova versão e publica o arquivo como artifact.

---

## Estrutura dos scripts

```text

pdf/

  assets/            # imagens de capa e rodapé
  scripts/           # script de build do PDF
  package.json       # dependências do build


```

---

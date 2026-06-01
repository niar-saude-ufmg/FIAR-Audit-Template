# FIAR-Audit-Template

Template de repositorio para aplicacao do **FIAR - Framework de Auditoria de IA Responsavel em Saude**.

Este repositorio fornece a estrutura base para documentar um sistema de IA, coletar artefatos tecnicos e realizar a avaliacao de auditoria.

## Como iniciar uma auditoria

1. Clique em **Use this template**.
2. Crie um repositorio novo para o sistema auditado.
3. Preencha a documentacao inicial do projeto.
4. Inclua os artefatos do projeto (data card, model card, RIPD, relatorios tecnicos).
5. Realize as avaliacoes do auditor.
6. Produza o relatorio final.

## Estrutura esperada

```text
documentacao_projeto/
artefatos_projeto/
  data_cards/
  model_cards/
  ripd/
  relatorios_tecnicos/
avaliacao_auditor/
auditoria_final/
```

## PDF consolidado automatico

O build gera **um unico PDF** em `relatorio/documento-auditoria-fiar.pdf` com:

- capa automatica;
- sumario automatico (com pagina inicial de cada documento);
- cabecalho e rodape em todas as paginas internas;
- numeracao continua de paginas (no mesmo PDF);
- consolidacao de todos os `.pdf` e `.docx` salvos nas pastas acima, incluindo subpastas.

Regras:

- `.pdf`: entra direto.
- `.docx`: convertido com LibreOffice.
- `.gitkeep` e temporarios `~$*.docx`: ignorados.
- Ordem por blocos: `documentacao_projeto` -> `artefatos_projeto` -> `avaliacao_auditor` -> `auditoria_final`.
- Dentro de cada bloco, leitura recursiva e ordenacao por caminho.

## Como gerar o relatorio (passo a passo)

1. Adicione ou atualize os arquivos da auditoria nas pastas:
   - `documentacao_projeto/`
   - `artefatos_projeto/`
   - `avaliacao_auditor/`
   - `auditoria_final/`
2. Execute o build local:

```bash
npm --prefix pdf install
npm --prefix pdf run build:pdf
```

3. Abra o PDF final em:
   - `relatorio/documento-auditoria-fiar.pdf`

Observacoes:

- O build inclui automaticamente novos `.docx` e `.pdf` nas pastas acima.
- O sumario e atualizado automaticamente com os itens e paginas.
- O diretorio `relatorio/` guarda somente o PDF final.

## Execucao local

Pre-requisitos:

- Node.js
- LibreOffice (binario `libreoffice` ou `soffice`)

Comando:

```bash
npm --prefix pdf install
npm --prefix pdf run build:pdf
```

## GitHub Actions

O workflow `.github/workflows/build-document.yml` roda em:

- push na `main`
- `pull_request`
- `workflow_dispatch`

Na `main`, se `relatorio/documento-auditoria-fiar.pdf` mudar, a pipeline commita automaticamente a nova versao e publica o PDF como artifact.

## Estrutura da geracao de relatorio

```text
pdf/
  assets/            # imagens de capa e rodape
  scripts/           # script de build do PDF
  package.json       # dependencias do build

relatorio/
  documento-auditoria-fiar.pdf
```

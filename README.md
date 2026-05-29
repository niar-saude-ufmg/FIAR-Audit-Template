# FIAR-Audit-Template

Template de repositório para aplicação do **FIAR – Framework de Auditoria de IA Responsável em Saúde**.

Este repositório fornece a estrutura básica para documentar um sistema de IA, coletar artefatos técnicos e realizar a avaliação de auditoria.

---

# Como iniciar uma auditoria

1. Clique em **Use this template** neste repositório.
2. Crie um novo repositório para o sistema que será auditado.
3. Preencha a **Documentação Inicial do Projeto**.
4. Inclua os **artefatos do projeto** (data card, model card, relatórios técnicos).
5. Realize as **avaliações do auditor** para cada dimensão de Responsible AI.
6. Produza o **relatório final de auditoria**.

---

## Nomeando repositórios de auditoria

Recomenda-se utilizar o seguinte padrão para repositórios criados a partir deste template:

fiar-audit-nome-do-sistema

Exemplos:

fiar-audit-predicao-dengue  
fiar-audit-triagem-covid

---

## Papéis no processo de auditoria

O processo de auditoria FIAR envolve dois papéis principais:

**Equipe do projeto (desenvolvedores ou responsáveis pelo sistema de IA)**  
Responsável por fornecer a documentação e os artefatos técnicos do sistema.

Isso inclui:

- documentação inicial do projeto
- data cards e model cards
- relatórios técnicos produzidos pela equipe
- evidências utilizadas na auditoria

Esses documentos são armazenados nas pastas:

- `documentacao_projeto/`
- `artefatos_projeto/`

**Equipe de auditoria (NIAR)**  
Responsável por avaliar o sistema com base nos artefatos fornecidos pelo projeto.

Os auditores produzem avaliações independentes para cada dimensão de Responsible AI.

Essas avaliações são armazenadas nas pastas:

- `avaliacao_auditor/`
- `auditoria_final/`

---

# Estrutura do repositório

```text
documentacao_projeto/
  *.docx
  *.pdf

artefatos_projeto/
  README.md
  *.docx
  *.pdf
  data_cards/
  model_cards/
  ripd/
  relatorios_tecnicos/

avaliacao_auditor/
  *.docx
  *.pdf

auditoria_final/
  *.docx
  *.pdf
```

Os documentos devem ser preenchidos no Word, LibreOffice ou Google Docs, e versionados no repositório.

---

# PDF consolidado automático

O repositório possui automação para gerar um único PDF consolidado com os documentos existentes.

## Regras do build

- Prioridade por arquivo:
  - `.pdf`: entra direto na consolidação.
  - `.docx`: convertido para PDF com LibreOffice.
  - `.md`: ignorado no build atual.
- Pastas vazias e arquivos ausentes são ignorados.
- Arquivos temporários de Word (`~$*.docx`) e `.gitkeep` são ignorados.
- A ordem de montagem segue os blocos:
  1. `documentacao_projeto/`
  2. `artefatos_projeto/` (incluindo subpastas como `data_cards`, `model_cards`, `ripd`, `relatorios_tecnicos` e novas subpastas)
  3. `avaliacao_auditor/`
  4. `auditoria_final/`
- Dentro de cada bloco, os arquivos sao lidos recursivamente e ordenados por caminho.
- O PDF inclui capa automatica por padrao (desative com `FIAR_DISABLE_COVER=1`).

Saída:

```text
dist/documento-auditoria-fiar.pdf
```

## Execução local

Pré-requisitos:

- `libreoffice`
- `qpdf`

Comandos:

```bash
npm run build:pdf
# opcional: sem capa
npm run build:pdf:no-cover
```

## GitHub Actions

O workflow `.github/workflows/build-document.yml` roda em `push` na `main`, `pull_request` e `workflow_dispatch`. Em `main`, quando o PDF em `dist/documento-auditoria-fiar.pdf` muda, a pipeline commita automaticamente a nova versao e tambem publica o arquivo como artifact.

---

# Templates (Google Docs)

Os templates abaixo são mantidos em **Google Docs** para facilitar edição colaborativa.

Ao acessar o link, será criada automaticamente **uma cópia editável no seu Google Drive**.

| Documento | Template |
|---|---|
| Documentação Inicial do Projeto | https://docs.google.com/document/d/1413BabalmWr3lH9xqPT37aNQ3yF7m-PL-qYjOsisA7I/copy |
| Relatório de Justiça | link |
| Relatório de Explicabilidade | link |
| Relatório de Auditabilidade | link |
| Relatório de Privacidade | link |
| Relatório de Governança | link |

---

# Sobre o FIAR

O FIAR é um framework para documentação e auditoria de sistemas de IA em saúde pública, baseado em:

- evidências documentadas
- artefatos verificáveis
- avaliação por dimensões de Responsible AI
- relatórios de auditoria estruturados

Mais informações:

https://github.com/marisavas/FIAR-Saude/

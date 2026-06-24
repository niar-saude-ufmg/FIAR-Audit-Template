# Geração do Relatório PDF (FIAR-Saúde)

Este módulo gera automaticamente o relatório consolidado da auditoria FIAR-Saúde.

O PDF representa a **visualização final da auditoria** para a combinação:

> (Tarefa, Versão Avaliável)

Ele não contém novos dados ou decisões, apenas consolida os artefatos já validados no fluxo FIAR.

---

## O que é incluído

O relatório é construído a partir dos seguintes blocos:

- documentacao_projeto/
- artefatos_projeto/
- avaliacao_niar/
- auditoria_final/

A consolidação segue sempre essa ordem.

---

## Saída

O arquivo final é gerado em:

```text
relatorio-auditoria-fiar-saude.pdf
```

---

## Execução

```
npm --prefix pdf install
npm --prefix pdf run build:pdf
```

---

## Estrutura do módulo

```text
pdf/
  assets/
  scripts/
  docs/
  package.json
```

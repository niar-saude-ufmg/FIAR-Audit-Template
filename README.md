# FIAR-Audit-Template

Este repositório define a estrutura padrão para criação de instâncias de auditoria do FIAR-Saúde.

Cada repositório derivado representa a auditoria de uma Tarefa e uma Versão Avaliável específicas.

---

## Antes de começar

O FIAR-Saúde organiza a auditoria em torno de três conceitos centrais:

* **Tarefa** : unidade mínima avaliada, definida pela combinação de modelo + dados + algoritmo orientada a um objetivo clínico ou operacional específico.
* **Versão Avaliável** : versão da tarefa que introduziu mudança relevante nas dimensões de IAR e que exige novo ciclo de conformidade.
* **Trilha de Execução** : determina como a tarefa é avaliada e qual o teto de maturidade do projeto.
  * *Trilha Experimental*: tarefas orientadas à publicação científica. Teto de maturidade: N2.
  * *Trilha Produção*: tarefas integradas a sistemas em operação ativa. Permite progressão até N4.

A unidade de avaliação de conformidade no FIAR é a combinação (Tarefa, Versão Avaliável), classificada como: Conforme, Pendente ou Não Conforme.

Para mais detalhes, consulte a [documentação oficial do FIAR-Saúde](https://github.com/niar-saude-ufmg/FIAR-Saude).

---

## Como iniciar uma auditoria

1. Clique em **Use this template**.
2. Crie um repositório novo para o projeto auditado.
3. Preencha os arquivos em `documentacao_projeto/`, incluindo `identificacao_auditoria.md`.
4. Defina a **tarefa**: modelo + dados + algoritmo + objetivo clínico/operacional (incluindo escopo e contexto de uso).
5. Classifique a tarefa na trilha correspondente (**Experimental** ou  **Produção**).
6. Produza os artefatos de desenvolvimento em `artefatos_projeto/`: Data Card, Model Card, Fairness Report, Explainability Report, Registro de Decisão Técnica e Relatório Consolidado de IAR.
7. Se aplicável, inclua o RIPD em `artefatos_projeto/ripd/`.
8. Se a tarefa for da **Trilha Produção**, inclua também os artefatos operacionais em `artefatos_projeto/operational_artifacts/`.
9. Produza o relatorio final em  `auditoria_final/`.

---

## Estrutura esperada

```text
documentacao_projeto/
  identificacao_auditoria.md
artefatos_projeto/
  data_cards/
  model_cards/
  fairness_reports/
  explainability_reports/
  decision_records/
  consolidated_iar_report/
  compliance/
    ripd/
 operational_artifacts/         # exclusivo Trilha Produção (N3–N4)
    monitoring/
    incidents/
    version_history/
    periodic_review/
avaliacao_niar/                  # preenchido exclusivamente pela equipe do NIAR (não editável pelo projeto)
auditoria_final/
```

---

## Governança de Versões

Uma nova Versão Avaliável deve ser criada quando houver alterações relevantes em:

- dados utilizados;
- modelo empregado;
- algoritmo ou pipeline;
- objetivo clínico ou operacional;
- requisitos relacionados às dimensões de IA Responsável.

Cada **Versão Avaliável** deve possuir documentação e evidências próprias de conformidade.

---

## Relatório PDF consolidado

O repositório gera automaticamente um PDF consolidado com todos os artefatos da auditoria.

Consulte [`pdf/README.md`](pdf/README.md) para instruções de geração local.

O relatório consolidado de IAR é produzido em:

- `artefatos_projeto/relatorio_consolidado_iar/`

e posteriormente integrado ao relatório final em:

- `auditoria_final/`

---

## Automação (GitHub Actions)

O repositório possui um workflow automatizado para geração do PDF:

- Executa em `push` na branch `main`
- Executa em `pull_request`
- Pode ser acionado manualmente (`workflow_dispatch`)

O workflow responsável está em:

```text
.github/workflows/build-document.yml
```

Quando o PDF é atualizado, o sistema pode regenerar automaticamente o artefato e versioná-lo no repositório como artifact do pipeline.

---

## Documentação e Referências

- Metodologia → [docs/metodologia_fiar.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/metodologia_fiar.md)
- Ciclo de Auditoria → [docs/ciclo_auditoria.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/ciclo_auditoria.md)
- Dimensões de IAR → [docs/dimensoes_avaliacao.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/dimensoes_avaliacao.md)
- Trilhas de Execução → [docs/trilhas_execucao.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/trilhas_execucao.md)
- Modelo de Maturidade → [docs/modelo_maturidade.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/modelo_maturidade.md)
- Governança → [docs/governanca_auditoria.md](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/governanca_auditoria.md)

---

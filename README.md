# FIAR-Saúde — Template de Ciclo de Avaliação

Este repositório fornece uma estrutura operacional reutilizável para organizar e documentar um ciclo de avaliação do FIAR-Saúde associado a uma **Tarefa de IA**, uma **Versão Avaliável** e um **Contexto de Uso** específicos.

O template pode ser utilizado para criar um repositório privado de um projeto, no qual são organizados:

- a documentação inicial da tarefa;
- os artefatos e evidências produzidos pelo projeto;
- as rodadas de validação documental;
- as avaliações realizadas pelo NIAR-Saúde;
- os registros de decisões técnicas;
- as decisões institucionais, quando aplicáveis;
- os relatórios produzidos ao longo do ciclo.

Este repositório não substitui nem replica a documentação metodológica oficial do FIAR-Saúde.

A fonte oficial para conceitos, dimensões, trilhas, procedimentos de avaliação, governança e modelo de maturidade está disponível em:

<https://github.com/niar-saude-ufmg/FIAR-Saude>

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

---

## Escopo do template

Cada repositório criado a partir deste template corresponde a uma instância documental e técnica de um ciclo FIAR-Saúde.

O ciclo é delimitado por:

- uma Tarefa de IA;
- uma Versão Avaliável;
- um Contexto de Uso;
- uma trilha de execução aplicável.

O repositório pode ser iniciado antes da realização de uma avaliação formal. Nesse caso, os primeiros passos consistem na inspeção dos artefatos existentes, na delimitação preliminar da tarefa e na validação das informações junto à equipe do projeto.

A criação do repositório, o preenchimento dos documentos ou a validação factual das informações não constituem:

- resultado de conformidade;
- certificação técnica;
- validação clínica;
- garantia de que o sistema seja justo, seguro ou ético;
- autorização institucional ou regulatória para implantação.

---

## Conceitos fundamentais

### Tarefa de IA

A Tarefa de IA é a unidade de trabalho avaliada pelo FIAR-Saúde.

Ela é definida pela combinação de modelo, dados, procedimentos de treinamento e inferência, objetivo clínico ou operacional e contexto de uso.

Um mesmo projeto pode conter mais de uma Tarefa de IA.

### Versão Avaliável

A Versão Avaliável corresponde a uma configuração específica da tarefa que introduz mudança relevante no modelo, nos dados, nos procedimentos ou no Contexto de Uso e que, por isso, requer nova avaliação integral ou parcial.

Nem toda alteração técnica constitui uma nova Versão Avaliável.

Os critérios e gatilhos aplicáveis devem seguir a documentação oficial vigente do FIAR-Saúde.

### Contexto de Uso

O Contexto de Uso descreve onde, por quem, para qual finalidade e sob quais condições a tarefa será desenvolvida, avaliada ou utilizada.

Uma mesma combinação de modelo e dados pode exigir avaliações distintas quando aplicada a contextos de uso diferentes.

### Trilhas de execução

A trilha é uma propriedade da Tarefa de IA e deve ser enquadrada conforme o destino previsto e o estágio de uso da tarefa.

- **Trilha Experimental:** tarefas orientadas à pesquisa, experimentação, validação metodológica ou produção científica, sem integração a um sistema em operação ativa.
- **Trilha Produção:** tarefas integradas a sistemas em operação ativa e sujeitas a requisitos adicionais de acompanhamento e produção de evidências operacionais.

A equipe do projeto pode informar o uso atual e o uso pretendido da tarefa. O enquadramento da trilha é validado pelo NIAR-Saúde de acordo com a documentação oficial vigente.

### Conformidade e maturidade

A conformidade é pontual e se refere a uma Tarefa de IA em uma Versão Avaliável e um Contexto de Uso específicos.

A maturidade é longitudinal e pertence ao projeto. Ela é inferida a partir da recorrência, continuidade e rastreabilidade das práticas observadas ao longo do histórico de suas tarefas e versões avaliáveis.

Os estados de conformidade definidos pela documentação oficial não devem ser confundidos com os estados de preparação ou validação dos documentos deste repositório.

---

## Papéis no ciclo

### Equipe do projeto

A equipe do projeto é responsável por:

- desenvolver a tarefa e seus componentes;
- produzir, manter e atualizar os artefatos técnicos;
- fornecer informações factuais sobre dados, modelos, versões e resultados;
- produzir ou executar as análises técnicas sob sua responsabilidade;
- registrar responsáveis, limitações, riscos e decisões técnicas;
- validar e complementar as minutas documentais elaboradas a partir dos
  artefatos fornecidos.

### NIAR-Saúde

O NIAR-Saúde é responsável por:

- orientar a organização das evidências;
- apoiar a delimitação da Tarefa de IA, da Versão Avaliável e do Contexto de Uso;
- validar o enquadramento da trilha;
- avaliar a suficiência, consistência e rastreabilidade dos artefatos;
- identificar lacunas e inconsistências;
- conduzir a avaliação técnica aplicável;
- acompanhar o ciclo de vida das tarefas avaliadas.

A validação factual realizada pela equipe do projeto não substitui a avaliação técnica do NIAR-Saúde.

### Decisão institucional

Questões que ultrapassem o escopo da avaliação técnica, como aceite de risco residual, definição de condicionantes ou outras deliberações institucionais, podem ser encaminhadas à instância competente conforme a governança institucional vigente.

Os Registros de Decisão Técnica produzidos pelo projeto não devem ser confundidos com Registros de Decisão Institucional.


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
  operational_artifacts/        # exclusivo Trilha Produção (N3–N4)
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

- `artefatos_projeto/consolidated_iar_report/`

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

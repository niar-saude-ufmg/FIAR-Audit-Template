# Registro de Pendências

Este arquivo consolida as pendências identificadas durante a inspeção documental, a validação com a equipe do projeto e as etapas posteriores do ciclo FIAR-Saúde.

Seu objetivo é permitir o acompanhamento rastreável de:

- informações faltantes;
- evidências não fornecidas;
- análises ainda não realizadas;
- inconsistências entre artefatos;
- questões de enquadramento;
- decisões institucionais pendentes.

Este registro apresenta o estado atual das pendências.

A origem e a evolução de cada pendência ao longo das rodadas devem também ser registradas em:

```text
historico_validacao.md
````

---

## 1. Identificação do ciclo

| Campo                      | Preenchimento                                        |
| -------------------------- | ---------------------------------------------------- |
| Projeto                    | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Tarefa de IA               | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Versão Avaliável         | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Contexto de Uso            | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Trilha                     | [ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde] |
| Responsável pelo registro | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Data de abertura           | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Última atualização      | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |

---

## 2. Tipos de pendência

Cada pendência deve ser classificada em um dos tipos abaixo.

### Informação

Informação factual necessária, mas ainda não fornecida ou confirmada.

Exemplos:

* nome do responsável;
* versão do dataset;
* data de treinamento;
* contexto de uso;
* estágio de implantação.

Marcador correspondente:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]
```

### Evidência

Documento, arquivo, log, relatório ou outro elemento verificável mencionado, mas ainda não disponibilizado.

Exemplos:

* arquivo de configuração;
* log de execução;
* parecer ético;
* relatório de validação;
* registro de decisão técnica.

### Análise

Avaliação técnica ainda não realizada ou não inferível a partir dos artefatos existentes.

Exemplos:

* análise de justiça;
* análise de explicabilidade;
* validação por subgrupos;
* avaliação de segurança;
* análise de drift.

Marcador correspondente:

```text
[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]
```

### Inconsistência

Divergência, ambiguidade ou contradição entre documentos, versões ou declarações.

Marcador correspondente:

```text
[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]
```

### Enquadramento

Questão metodológica que exige consolidação pelo NIAR-Saúde.

Exemplos:

* delimitação da Tarefa de IA;
* definição da Versão Avaliável;
* separação entre Contextos de Uso;
* enquadramento da trilha.

Marcador correspondente:

```text
[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]
```

### Decisão institucional

Questão que ultrapassa o escopo da avaliação técnica e exige análise da instância competente.

Exemplos:

* aceite de risco residual;
* definição de condicionantes;
* autorização institucional;
* decisão sobre continuidade, suspensão ou restrição de uso.

Marcador correspondente:

```text
[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

---

## 3. Prioridades

As pendências devem ser classificadas em uma das prioridades abaixo.

### Crítica

Pendência que impede:

* delimitar a Tarefa de IA;
* identificar a Versão Avaliável;
* compreender o Contexto de Uso;
* verificar a origem dos dados ou do modelo;
* identificar responsáveis;
* iniciar ou concluir uma avaliação aplicável;
* avaliar risco relevante;
* reconstruir resultado técnico essencial.

### Relevante

Pendência que não impede imediatamente o ciclo, mas afeta:

* completude;
* consistência;
* rastreabilidade;
* interpretação dos resultados;
* avaliação de uma dimensão;
* planejamento de análises adicionais.

### Recomendação

Melhoria desejável de documentação, organização ou rastreabilidade que não impede a continuidade do ciclo atual.

A prioridade não equivale a resultado de conformidade.

---

## 4. Estados das pendências

Utilize um dos seguintes estados:

* `Aberta`
* `Aguardando resposta do projeto`
* `Aguardando evidência`
* `Aguardando análise técnica`
* `Aguardando validação do NIAR`
* `Aguardando decisão institucional`
* `Em tratamento pelo projeto`
* `Em análise pelo NIAR`
* `Respondida — em verificação`
* `Resolvida`
* `Encerrada com limitação registrada`
* `Não aplicável — justificativa registrada`
* `Substituída`
* `Reaberta`

Uma pendência somente deve ser marcada como `Resolvida` quando a resolução estiver sustentada por informação, evidência, análise ou decisão registrada.

---

## 5. Registro consolidado

| ID      | Pendência                                        | Tipo         | Dimensão relacionada | Prioridade | Origem | Responsável | Prazo | Estado | Evidência esperada | Resolução |
| ------- | ------------------------------------------------- | ------------ | --------------------- | ---------- | ------ | ------------ | ----- | ------ | ------------------- | ----------- |
| PEN-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] | Informação |                       |            |        |              |       | Aberta |                     |             |

### Orientações de preenchimento

#### ID

Utilizar numeração sequencial:

```text
PEN-001
PEN-002
PEN-003
```

O identificador não deve ser reutilizado, mesmo após o encerramento da pendência.

#### Pendência

Descrever de forma específica e verificável.

Evitar:

```text
Falta documentação.
```

Preferir:

```text
Não foi informado o commit do código utilizado para treinar o modelo v1.0.0.
```

#### Dimensão relacionada

Quando aplicável, utilizar uma ou mais dimensões:

* Justiça;
* Transparência;
* Responsabilização;
* Privacidade;
* Segurança;
* Governança;
* Rastreabilidade.

Também podem ser usados:

* identificação da tarefa;
* versão avaliável;
* contexto de uso;
* desempenho;
* validação;
* enquadramento.

#### Origem

Indicar onde a pendência foi identificada.

Exemplos:

* inspeção inicial;
* Data Card;
* Model Card;
* inconsistência cruzada;
* rodada 1 de validação;
* entrevista;
* avaliação por dimensão;
* revisão do NIAR-Saúde.

#### Responsável

Indicar a pessoa, equipe ou instância responsável por tratar a pendência.

Exemplos:

* equipe de dados;
* equipe de modelagem;
* responsável técnico;
* responsável institucional;
* NIAR-Saúde;
* instância institucional competente.

#### Evidência esperada

Descrever o que será considerado suficiente para o tratamento da pendência.

Exemplos:

* informar commit e tag;
* fornecer relatório de execução;
* atualizar o Model Card;
* produzir análise de desempenho por grupo;
* registrar decisão técnica;
* apresentar confirmação do responsável;
* registrar decisão institucional.

#### Resolução

Registrar:

* a resposta;
* a evidência utilizada;
* a data;
* o responsável pela verificação;
* o documento atualizado.

---

## 6. Pendências críticas

Esta seção apresenta uma visão resumida das pendências que impedem ou condicionam a continuidade do ciclo.

| ID                                                | Pendência crítica | Impacto | Responsável | Estado | Próximo passo |
| ------------------------------------------------- | ------------------- | ------- | ------------ | ------ | -------------- |
| [INFORMAÇÃO PENDENTE — preencher pelo projeto] |                     |         |              |        |                |

Quando não houver pendências críticas, registrar:

```text
Nenhuma pendência crítica identificada na data de referência.
```

Essa declaração deve ser baseada no registro consolidado e não em ausência de revisão.

---

## 7. Pendências por dimensão

### 7.1 Justiça

| ID                                                                        | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |            |            |              |        |

### 7.2 Transparência

| ID                                                                        | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |            |            |              |        |

### 7.3 Responsabilização

| ID                                                | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [INFORMAÇÃO PENDENTE — preencher pelo projeto] |            |            |              |        |

### 7.4 Privacidade

| ID                                                                        | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |            |            |              |        |

### 7.5 Segurança

| ID                                                                        | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |            |            |              |        |

### 7.6 Governança

| ID                                                | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [INFORMAÇÃO PENDENTE — preencher pelo projeto] |            |            |              |        |

### 7.7 Rastreabilidade

| ID                                                | Pendência | Prioridade | Responsável | Estado |
| ------------------------------------------------- | ---------- | ---------- | ------------ | ------ |
| [INFORMAÇÃO PENDENTE — preencher pelo projeto] |            |            |              |        |

As tabelas desta seção funcionam como resumo. O registro completo deve permanecer na Seção 5.

---

## 8. Inconsistências abertas

| ID da pendência | Documentos envolvidos                                          | Descrição da inconsistência | Impacto | Responsável pelo esclarecimento | Estado |
| ---------------- | -------------------------------------------------------------- | ------------------------------ | ------- | -------------------------------- | ------ |
| PEN-XXX          | [INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos] |                                |         |                                  |        |

A inconsistência deve permanecer aberta enquanto não houver:

* correção documental;
* evidência adicional;
* confirmação do responsável;
* consolidação de enquadramento pelo NIAR-Saúde;
* decisão institucional, quando aplicável.

Não escolher silenciosamente uma das versões.

---

## 9. Análises pendentes

| ID da pendência | Análise necessária                                                      | Objetivo | Dados ou evidências necessários | Responsável | Prazo | Estado |
| ---------------- | ------------------------------------------------------------------------- | -------- | --------------------------------- | ------------ | ----- | ------ |
| PEN-XXX          | [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |          |                                   |              |       |        |

As análises pendentes devem distinguir:

* análise inexistente;
* análise iniciada;
* análise existente, mas não fornecida;
* análise fornecida, mas insuficiente;
* análise que não se aplica, com justificativa.

---

## 10. Questões de enquadramento

| ID da pendência | Questão                                             | Alternativas consideradas | Informação necessária | Responsável pelo enquadramento | Estado |
| ---------------- | ---------------------------------------------------- | ------------------------- | ------------------------ | ------------------------------- | ------ |
| PEN-XXX          | [ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde] |                           |                          | NIAR-Saúde                     |        |

Exemplos de questões de enquadramento:

* uma ou mais Tarefas de IA;
* um ou mais Contextos de Uso;
* definição da Versão Avaliável;
* Trilha Experimental ou Trilha Produção;
* necessidade de nova avaliação integral ou parcial;
* distinção entre mudança técnica e mudança relevante.

---

## 11. Questões institucionais

| ID da pendência | Questão institucional                                                        | Motivo do escalonamento | Evidências relacionadas | Instância responsável | Estado | Decisão relacionada |
| ---------------- | ----------------------------------------------------------------------------- | ----------------------- | ------------------------ | ----------------------- | ------ | -------------------- |
| PEN-XXX          | [DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente] |                         |                          |                         |        |                      |

Este registro não substitui o Registro de Decisão Institucional.

Quando houver decisão, indicar sua localização no repositório.

---

## 12. Pendências respondidas e em verificação

| ID      | Resposta recebida | Fonte apresentada | Data da resposta | Verificação necessária | Responsável pela verificação | Estado                         |
| ------- | ----------------- | ----------------- | ---------------- | ------------------------- | ------------------------------- | ------------------------------ |
| PEN-XXX |                   |                   |                  |                           | NIAR-Saúde                     | Respondida — em verificação |

Uma resposta do projeto não encerra automaticamente a pendência.

O NIAR-Saúde deve verificar:

* se a resposta trata integralmente a questão;
* se a fonte é suficiente;
* se outros documentos precisam ser atualizados;
* se a resposta cria nova inconsistência;
* se a rastreabilidade foi preservada.

---

## 13. Pendências resolvidas

| ID      | Resolução | Evidência | Documento atualizado | Data | Verificado por |
| ------- | ----------- | ---------- | -------------------- | ---- | -------------- |
| PEN-XXX |             |            |                      |      |                |

Pendências resolvidas não devem ser apagadas do histórico.

O registro consolidado pode manter o estado `Resolvida`, enquanto esta seção apresenta a síntese da resolução.

---

## 14. Pendências encerradas com limitação

Uma pendência pode ser encerrada sem resolução integral quando:

* a informação não existe;
* a evidência não pode ser recuperada;
* a análise não pode ser realizada no ciclo atual;
* há restrição de acesso formalmente justificada;
* a limitação foi reconhecida e incorporada aos relatórios.

| ID      | Limitação | Justificativa | Impacto no ciclo | Responsável pelo aceite da limitação | Data |
| ------- | ----------- | ------------- | ---------------- | --------------------------------------- | ---- |
| PEN-XXX |             |               |                  |                                         |      |

Registrar:

```text
Encerrada com limitação registrada
```

Esse estado não significa que o risco ou impacto da ausência tenha sido aceito institucionalmente.

Quando houver necessidade de aceite de risco ou condicionante, abrir também uma pendência do tipo `decisão institucional`.

---

## 15. Resumo do estado atual

| Categoria                         | Quantidade |
| --------------------------------- | ---------: |
| Pendências abertas               |          0 |
| Pendências críticas             |          0 |
| Aguardando resposta do projeto    |          0 |
| Aguardando evidência             |          0 |
| Aguardando análise técnica      |          0 |
| Aguardando validação do NIAR    |          0 |
| Aguardando decisão institucional |          0 |
| Respondidas — em verificação   |          0 |
| Resolvidas                        |          0 |
| Encerradas com limitação        |          0 |

Atualizar este resumo sempre que houver mudança relevante no registro consolidado.

---

## 16. Próximos passos

| Ordem | Ação                                            | Pendências relacionadas | Responsável | Prazo |
| ----- | ------------------------------------------------- | ------------------------ | ------------ | ----- |
| 1     | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |                          |              |       |

Os próximos passos devem refletir as pendências abertas e não uma lista genérica de atividades.

---

## 17. Histórico de versões

| Versão | Data | Responsável | Alteração                          | Status   |
| ------- | ---- | ------------ | ------------------------------------ | -------- |
| 0.1     |      | NIAR-Saúde  | Criação do registro de pendências | Rascunho |



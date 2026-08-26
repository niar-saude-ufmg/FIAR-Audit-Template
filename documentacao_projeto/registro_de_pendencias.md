# Registro de Pendências

Este arquivo consolida as pendências identificadas pelo NIAR-Saúde ao longo do ciclo FIAR-Saúde.

Uma pendência representa uma questão ainda não suficientemente resolvida para determinada finalidade do ciclo, podendo envolver confirmação factual, complementação documental, esclarecimento, verificação pelo NIAR-Saúde, análise técnica adicional ou decisão institucional.

O registro de uma pendência não constitui, por si só:

- não conformidade;
- ausência obrigatória de artefato;
- recomendação;
- inconsistência;
- decisão institucional.

A ausência de um artefato somente deve originar pendência quando houver uma necessidade de evidência previamente identificada que não esteja suficientemente atendida pelas fontes disponíveis.

Pendências podem ser impeditivas ou não impeditivas para a continuidade do ciclo. Essa classificação deve ser explicitamente justificada.

A origem e a evolução de cada pendência ao longo das rodadas devem também ser registradas em:

```text
historico_validacao.md
```

---

## 1. Identificação do ciclo

| Campo                      | Preenchimento                                                     |
| -------------------------- | ----------------------------------------------------------------- |
| Projeto                    | [preencher pelo NIAR-Saúde a partir das evidências verificadas] |
| Tarefa de IA               | [preencher a partir da identificação da avaliação]            |
| Versão Avaliável         | [preencher a partir da identificação da avaliação]            |
| Contexto de Uso            | [preencher a partir da identificação da avaliação]            |
| Trilha de Execução       | [preencher a partir da identificação da avaliação]            |
| Responsável pelo registro | NIAR-Saúde                                                       |
| Data de abertura           | [preencher pelo NIAR-Saúde]                                      |
| Última atualização      | [preencher pelo NIAR-Saúde]                                      |

---

## 2. Tipos de pendência

### Complementação documental

Documento existente precisa ser complementado, corrigido ou atualizado para suprir uma necessidade de evidência já identificada.

### Esclarecimento

Informação documental existente é ambígua ou insuficientemente precisa e requer esclarecimento.

### Confirmação factual

Fato relevante ainda não foi confirmado por fonte verificável.

### Verificação pelo NIAR

Questão que deve ser resolvida primeiramente por análise documental, administrativa ou metodológica realizada pelo NIAR-Saúde antes de eventual solicitação à equipe do projeto.

### Análise técnica adicional

Questão que exige análise técnica específica além da simples verificação documental.

### Decisão institucional

Questão que ultrapassa o escopo da avaliação técnica e requer deliberação da instância institucional competente.

> Uma inconsistência confirmada deve ser registrada em `avaliacao_niar/registro_de_inconsistencias.md`.
>
> Uma inconsistência pode originar uma pendência para seu tratamento, mas inconsistência e pendência não são equivalentes.

---

## 3. Prioridades

As pendências devem ser classificadas em uma das prioridades abaixo.

| Prioridade | Critério                                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Alta       | Impede a delimitação da unidade de avaliação ou outra condição material necessária para prosseguir com a etapa pertinente do ciclo |
| Média     | Não impede imediatamente a continuidade, mas afeta suficiência, consistência, rastreabilidade ou interpretação das evidências       |
| Baixa      | Questão documental, administrativa ou complementar que pode ser tratada durante o ciclo sem impedir sua continuidade                     |

A prioridade não equivale a resultado de conformidade.

Uma recomendação de melhoria não deve ser registrada como pendência apenas por ser desejável.

### Impacto sobre a continuidade

Cada pendência deve ser classificada como:

- `Impeditiva`;
- `Não impeditiva`;
- `Ainda não determinado`.

Uma pendência é impeditiva somente quando sua ausência inviabiliza materialmente a etapa que se pretende iniciar ou concluir.

Pendências não impeditivas podem permanecer abertas em paralelo, desde que seu impacto esteja registrado e que sejam resolvidas antes da etapa em que se tornem materiais.

---

## 4. Estados das pendências

- `Aberta`
- `Aguardando verificação pelo NIAR`
- `Aguardando projeto`
- `Em análise`
- `Parcialmente resolvida`
- `Resolvida`
- `Não aplicável`
- `Escalonada`
- `Cancelada`
- `Reaberta`
- `Respondida — em verificação`

Uma pendência somente deve ser marcada como `Resolvida` quando sua resolução estiver documentada e rastreável.

Uma pendência pode ser marcada como `Cancelada` quando uma reavaliação metodológica demonstrar que a questão não deveria permanecer como pendência. O registro histórico e a justificativa devem ser preservados. `Respondida — em verificação` indica que a equipe apresentou resposta ou evidência, mas o NIAR-Saúde ainda não concluiu sua suficiência e consistência.

---

## 5. Registro consolidado

| ID      | Pendência | Tipo | Dimensão ou etapa relacionada | Prioridade | Impacto na continuidade | Origem | Responsável atual | Próxima ação | Estado | Condição de resolução |
| ------- | ---------- | ---- | ------------------------------ | ---------- | ----------------------- | ------ | ------------------ | --------------- | ------ | ------------------------- |
| PEN-001 |            |      |                                |            |                         |        |                    |                 |        |                           |

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

#### Dimensão ou etapa relacionada

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

#### Responsável atual

Indicar a pessoa, equipe ou instância responsável por tratar a pendência.

Exemplos:

* equipe de dados;
* equipe de modelagem;
* responsável técnico;
* responsável institucional;
* NIAR-Saúde;
* instância institucional competente.

#### Condição de resolução

Descrever qual condição objetiva será considerada suficiente para encerrar a pendência.

A condição de resolução deve expressar primeiro a informação, evidência, análise ou decisão necessária, sem presumir antecipadamente qual artefato deverá fornecê-la.

Exemplos:

- confirmação factual do responsável institucional;
- identificação verificável do commit e da tag utilizados;
- evidência suficiente do procedimento de avaliação;
- esclarecimento de uma informação ambígua;
- conclusão de análise técnica aplicável;
- registro de decisão institucional.

Somente após determinar a condição de resolução deve ser definido, quando necessário, qual artefato ou fonte poderá atendê-la.

#### Resolução

Registrar:

* a resposta;
* a evidência utilizada;
* a data;
* o responsável pela verificação;
* o documento atualizado.

---

## 6. Pendências que impedem a continuidade

Esta seção apresenta uma visão resumida das pendências cuja resolução foi considerada necessária para iniciar ou concluir determinada etapa do ciclo.

| ID | Pendência | Etapa afetada | Motivo da impeditividade | Responsável | Estado | Próximo passo |
| -- | ---------- | ------------- | ------------------------ | ------------ | ------ | -------------- |
|    |            |               |                          |              |        |                |

Quando não houver pendências impeditivas, registrar:

```text
Nenhuma pendência impeditiva identificada na data de referência.
```

---

## 7. Pendências por dimensão

> A existência de uma dimensão não implica a existência de pendência.
>
> Somente registrar nesta seção pendências efetivamente identificadas após análise de aplicabilidade e suficiência das evidências.

### 7.1 Justiça

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.2 Transparência

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.3 Responsabilização

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.4 Privacidade

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.5 Segurança

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.6 Governança

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

### 7.7 Rastreabilidade

| ID | Pendência | Prioridade | Impacto na continuidade | Responsável | Estado |
| -- | ---------- | ---------- | ----------------------- | ------------ | ------ |
|    |            |            |                         |              |        |

As tabelas desta seção funcionam como resumo. O registro completo deve permanecer na Seção 5.

---

## 8. Pendências relacionadas a inconsistências

| ID da pendência | ID da inconsistência | Questão a resolver | Próxima ação | Estado |
| ---------------- | --------------------- | ------------------- | --------------- | ------ |
|                  |                       |                     |                 |        |

> A descrição e o histórico da divergência devem permanecer no `registro_de_inconsistencias.md`.
>
> Este registro deve conter somente a ação ou questão ainda pendente decorrente da inconsistência.

---

## 9. Análises técnicas adicionais pendentes

Registrar somente análises cuja necessidade tenha sido estabelecida a partir de requisito aplicável, lacuna concreta ou questão técnica identificada.

| ID da pendência | Análise necessária | Motivo | Evidências disponíveis | Complemento necessário | Responsável | Estado |
| ---------------- | -------------------- | ------ | ------------------------ | ----------------------- | ------------ | ------ |
|                  |                      |        |                          |                         |              |        |

> A mera existência de template de Fairness Report, Explainability Report, TDR, RIPD ou outro artefato não estabelece a necessidade da análise correspondente.

---

## 10. Questões de enquadramento

| ID da pendência | Questão | Alternativas consideradas | Informação necessária | Responsável pelo enquadramento | Estado |
| ---------------- | -------- | ------------------------- | ------------------------ | ------------------------------- | ------ |
|                  |          |                           |                          |                                 |        |

Exemplos de questões de enquadramento:

* uma ou mais Tarefas de IA;
* um ou mais Contextos de Uso;
* definição da Versão Avaliável;
* Trilha Experimental ou Trilha Produção;
* necessidade de nova avaliação integral ou parcial;
* distinção entre mudança técnica e mudança relevante.

---

## 11. Questões institucionais

| ID da pendência | Questão institucional | Motivo do escalonamento | Evidências relacionadas | Instância responsável | Estado | Decisão relacionada |
| ---------------- | ---------------------- | ----------------------- | ------------------------ | ----------------------- | ------ | -------------------- |
|                  |                        |                         |                          |                         |        |                      |

Este registro não substitui o Registro de Decisão Institucional.

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

## 14. Pendências canceladas ou reenquadradas

Uma pendência pode ser cancelada quando uma reavaliação metodológica demonstra que a questão não deve permanecer caracterizada como pendência.

Exemplos:

- a ausência de determinado artefato havia sido tratada como pendência, mas posteriormente se verificou que o artefato não era obrigatório;
- uma análise havia sido presumida necessária antes da determinação da aplicabilidade do requisito;
- a questão foi absorvida por outro mecanismo de avaliação ou registro mais adequado.

| ID | Questão original | Motivo do reenquadramento | Estado final | Data | Registrado por |
| -- | ----------------- | ------------------------- | ------------ | ---- | -------------- |
|    |                   |                           |              |      |                |

Uma pendência cancelada ou reenquadrada não deve ser apagada.

O registro deve preservar a questão original e justificar por que ela deixou de constituir pendência.

---

## 15. Resumo do estado atual

| Categoria                          | Quantidade |
| ---------------------------------- | ---------: |
| Pendências abertas                |          0 |
| Pendências impeditivas            |          0 |
| Pendências não impeditivas       |          0 |
| Aguardando verificação pelo NIAR |          0 |
| Aguardando projeto                 |          0 |
| Em análise                        |          0 |
| Resolvidas                         |          0 |
| Canceladas ou reenquadradas        |          0 |
| Escalonadas                        |          0 |

Atualizar este resumo sempre que houver mudança relevante no registro consolidado.

---

## 16. Próximos passos

| Ordem | Ação | Pendências relacionadas | Responsável | Prazo |
| ----- | ------ | ------------------------ | ------------ | ----- |
| 1     |        |                          |              |       |

Os próximos passos devem refletir as pendências abertas e não uma lista genérica de atividades.

> Pendências abertas não bloqueiam automaticamente a continuidade do ciclo.
>
> Antes de impedir a progressão para uma nova etapa, o NIAR-Saúde deve registrar qual condição concreta depende da resolução da pendência e por que sua ausência é material naquele momento.

---

## 17. Histórico de versões

| Versão | Data       | Responsável | Alteração                                                                                                                                                                                             | Status   |
| ------- | ---------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 0.1     |            | NIAR-Saúde  | Criação do registro de pendências                                                                                                                                                                    | Rascunho |
| 0.2     | 26/08/2026 | NIAR-Saúde  | Revisão metodológica do registro: distinção entre pendência e inconsistência, inclusão de impacto impeditivo/não impeditivo, verificação prévia pelo NIAR e cancelamento por reenquadramento | Em uso   |

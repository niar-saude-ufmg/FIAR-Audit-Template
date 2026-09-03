# Pré-Avaliação Documental

## Controle do documento

| Campo                 | Preenchimento                                          |
| --------------------- | ------------------------------------------------------ |
| ID da avaliação     | [preencher pelo NIAR-Saúde]                           |
| Versão do documento  | 0.1                                                    |
| Status                | Em elaboração                                        |
| Elaborado por         | NIAR-Saúde                                            |
| Data de elaboração  | [preencher pelo NIAR-Saúde]                           |
| Última atualização | [preencher pelo NIAR-Saúde]                           |
| Projeto               | [preencher a partir das evidências verificadas]       |
| Tarefa de IA          | [preencher a partir da identificação da avaliação] |
| Versão Avaliável    | [preencher a partir da identificação da avaliação] |
| Contexto de Uso       | [preencher a partir da identificação da avaliação] |
| Trilha de Execução  | [preencher a partir da identificação da avaliação] |

> Este documento registra a pré-avaliação documental conduzida pelo NIAR-Saúde antes da avaliação por requisito.
>
> Somente fontes verificadas no ciclo atual podem ser utilizadas como evidência. Informações provenientes de versões históricas, conversas anteriores ou memória podem orientar a busca, mas não constituem evidência até serem novamente verificadas.
>
> A pré-avaliação documental não atribui resultado de conformidade, maturidade, validação clínica, certificação técnica, aceite de risco ou autorização de implantação.

---

## 1. Objetivo

A pré-avaliação documental tem como objetivo verificar se a unidade de avaliação está suficientemente delimitada, identificar e organizar as evidências disponíveis, examinar sua consistência e rastreabilidade e registrar pendências que devam ser tratadas antes ou durante a avaliação por requisito.

A pré-avaliação busca:

- confirmar Tarefa de IA, Versão Avaliável, Contexto de Uso e Trilha de Execução;
- inventariar os artefatos e demais evidências disponíveis;
- identificar as informações efetivamente sustentadas por cada fonte;
- realizar verificações cruzadas entre fontes;
- identificar informações ausentes, ambiguidades e divergências;
- registrar pendências;
- determinar quais evidências adicionais são realmente necessárias;
- estabelecer se existem condições para iniciar a avaliação por requisito.

---

## 2. Unidade de avaliação

| Elemento             | Delimitação atual | Fonte(s) | Situação            |
| -------------------- | ------------------- | -------- | --------------------- |
| Tarefa de IA         |                     |          | Delimitada / Pendente |
| Versão Avaliável   |                     |          | Delimitada / Pendente |
| Contexto de Uso      |                     |          | Delimitado / Pendente |
| Trilha de Execução |                     |          | Definida / Pendente   |

### Observações

[Registrar apenas questões relevantes à delimitação.]

> Pendências materiais que impeçam a delimitação da Tarefa de IA, da Versão Avaliável, do Contexto de Uso ou da Trilha de Execução devem ser resolvidas antes da avaliação por requisito.
>
> Pendências que não impeçam essa delimitação podem permanecer abertas em paralelo, desde que seu impacto esteja explicitamente registrado e que não comprometam os requisitos afetados.

---

## 3. Inventário documental

| ID      | Artefato ou evidência | Versão / data | Fonte ou localização | Estado documental | Observação |
| ------- | ---------------------- | -------------- | ---------------------- | ----------------- | ------------ |
| ART-001 |                        |                |                        |                   |              |

Estados documentais sugeridos:

- disponível e verificado;
- disponível parcialmente;
- não verificado neste ciclo;
- substituído;
- desatualizado;
- não aplicável;
- não disponível.

> A presença de um diretório ou template no repositório não significa que o artefato correspondente seja obrigatório ou que esteja disponível como evidência.

---

## 4. Evidências identificadas

Registrar quais informações são efetivamente sustentadas pelos artefatos verificados.

| Tema                                          | Informação identificada | Fonte | Situação |
| --------------------------------------------- | ------------------------- | ----- | ---------- |
| Tarefa de IA                                  |                           |       |            |
| Finalidade                                    |                           |       |            |
| Contexto de Uso                               |                           |       |            |
| Trilha                                        |                           |       |            |
| Dataset(s)                                    |                           |       |            |
| Versão dos dados                             |                           |       |            |
| População                                   |                           |       |            |
| Período                                      |                           |       |            |
| Entradas                                      |                           |       |            |
| Saídas                                       |                           |       |            |
| Modelo                                        |                           |       |            |
| Versão do modelo                             |                           |       |            |
| Procedimentos relevantes                      |                           |       |            |
| Métricas                                     |                           |       |            |
| Resultados reportados                         |                           |       |            |
| Limitações declaradas                       |                           |       |            |
| Decisões explicitamente documentadas         |                           |       |            |
| Responsabilidades explicitamente documentadas |                           |       |            |
| Evidências institucionais ou operacionais    |                           |       |            |

Situações sugeridas:

- identificada;
- parcialmente identificada;
- não identificada;
- requer esclarecimento;
- não aplicável nesta etapa.

---

## 5. Verificações cruzadas

### 5.1 Dados e modelo

| Verificação                      | Fonte 1 | Fonte 2 | Resultado | Observação |
| ---------------------------------- | ------- | ------- | --------- | ------------ |
| Dataset de treinamento             |         |         |           |              |
| Dataset de validação             |         |         |           |              |
| Dataset de teste                   |         |         |           |              |
| Versões dos datasets              |         |         |           |              |
| Número de pacientes / instâncias |         |         |           |              |
| Períodos                          |         |         |           |              |
| Separação entre conjuntos        |         |         |           |              |
| Sobreposição entre conjuntos     |         |         |           |              |
| Entradas utilizadas                |         |         |           |              |
| Versão do modelo                  |         |         |           |              |
| Configuração relevante           |         |         |           |              |
| Métricas / resultados             |         |         |           |              |

### 5.2 Outras verificações

| Verificação                   | Fontes comparadas | Resultado | Observação |
| ------------------------------- | ----------------- | --------- | ------------ |
| Tarefa de IA                    |                   |           |              |
| Contexto de Uso                 |                   |           |              |
| Trilha de Execução            |                   |           |              |
| Responsabilidades               |                   |           |              |
| Decisões documentadas          |                   |           |              |
| Versionamento / rastreabilidade |                   |           |              |

Resultados permitidos:

- Consistente;
- Informação ausente;
- Requer esclarecimento;
- Divergência confirmada;
- Não aplicável.

> Informação ausente em um artefato não constitui, por si só, inconsistência.

---

## 6. Inconsistências identificadas

| ID | Síntese | Fonte(s) | Impacto | Estado |
| -- | -------- | -------- | ------- | ------ |
|    |          |          |         |        |

As inconsistências devem ser detalhadas em:

`avaliacao_niar/registro_de_inconsistencias.md`

Não selecionar silenciosamente uma das versões conflitantes.

> A resolução de uma inconsistência não elimina seu registro histórico. O estado deve ser atualizado para refletir a forma de resolução, por exemplo: correção documental, nova evidência ou enquadramento metodológico.

---

## 7. Pendências identificadas

| ID | Questão | Tipo | Impacto | Próxima ação | Estado |
| -- | -------- | ---- | ------- | --------------- | ------ |
|    |          |      |         |                 |        |

Tipos sugeridos:

- complementação documental;
- esclarecimento;
- confirmação factual;
- verificação pelo NIAR;
- análise técnica adicional;
- decisão institucional pendente.

Uma pendência pode ser:

- impeditiva para a continuidade;
- não impeditiva e tratada em paralelo;
- resolvida;
- cancelada por reenquadramento metodológico;
- escalonada para decisão institucional.

A ausência de um artefato, por si só, não gera automaticamente uma pendência.

As pendências devem ser detalhadas em:

`documentacao_projeto/registro_de_pendencias.md`

> Somente pendências que dependam efetivamente da equipe do projeto devem ser encaminhadas à equipe.

---

## 8. Determinação de evidências adicionais

Antes de solicitar novos artefatos, o NIAR-Saúde deve verificar:

1. qual informação ou evidência é necessária;
2. qual requisito aplicável, etapa posterior ou decisão do ciclo depende dessa evidência;
3. se a evidência já está suficientemente registrada em alguma fonte existente;
4. se há uma lacuna real;
5. qual artefato ou registro seria adequado para suprir essa lacuna.

| Necessidade de evidência | Motivo | Evidência já disponível | Lacuna | Complemento necessário |
| ------------------------- | ------ | -------------------------- | ------ | ----------------------- |
|                           |        |                            |        |                         |

> A necessidade da evidência precede a escolha do artefato utilizado para registrá-la.
>
> A existência de templates como Fairness Report, Explainability Report, Technical Decision Record, RIPD ou artefatos operacionais não implica sua obrigatoriedade para todas as tarefas.

---

## 9. Verificações adicionais pelo NIAR-Saúde

Registrar verificações que ainda podem ser realizadas internamente antes de solicitar esclarecimentos à equipe.

| Verificação | Evidência necessária | Responsável | Estado |
| ------------- | ---------------------- | ------------ | ------ |
|               |                        | NIAR-Saúde  |        |

---

## 10. Itens que dependem da equipe do projeto

Registrar somente após o NIAR verificar que a questão não pode ser resolvida com as evidências disponíveis.

| ID | Questão | Evidência ou esclarecimento solicitado | Motivo | Estado |
| -- | -------- | --------------------------------------- | ------ | ------ |
|    |          |                                         |        |        |

---

## 11. Síntese da pré-avaliação

### Pontos suficientemente estabelecidos

- [ ]

### Pontos ainda em verificação

- [ ]

### Pendências abertas

- [ ]

### Divergências confirmadas

- [ ]

### Evidências adicionais necessárias

- [ ]

---

## 12. Estado para continuidade

| Questão                                              | Resultado  |
| ----------------------------------------------------- | ---------- |
| Unidade de avaliação suficientemente delimitada     | Sim / Não |
| Inventário documental concluído                     | Sim / Não |
| Verificações cruzadas concluídas                   | Sim / Não |
| Existem divergências confirmadas                     | Sim / Não |
| Existem pendências materiais                         | Sim / Não |
| Existem verificações internas ainda necessárias    | Sim / Não |
| Existem itens que precisam ser solicitados ao projeto | Sim / Não |
| Avaliação por requisito pode ser iniciada           | Sim / Não |
| Pendências abertas impedem a continuidade?           | Sim / Não |

### Justificativa

[Registrar de forma objetiva as condições para continuidade.]

> A existência de pendências não impede automaticamente o início da avaliação por requisito.
>
> O NIAR-Saúde deve registrar explicitamente se cada pendência é impeditiva ou não impeditiva e justificar seu impacto sobre a continuidade.
>
> Pendências não impeditivas podem permanecer abertas em paralelo, desde que seu impacto seja reavaliado antes da etapa em que a questão se torne material para a consolidação da dimensão, para o resultado formal da avaliação ou para eventual decisão institucional.

---

## 13. Próximos passos

- [ ] delimitar Tarefa de IA, Versão Avaliável, Contexto de Uso e Trilha de Execução;
- [ ] verificar os artefatos técnicos necessários à delimitação da unidade;
- [ ] concluir o inventário documental necessário à pré-avaliação;
- [ ] concluir as verificações cruzadas necessárias;
- [ ] registrar divergências confirmadas no `registro_de_inconsistencias.md`;
- [ ] revisar e consolidar as pendências válidas no ciclo atual;
- [ ] determinar quais evidências adicionais são efetivamente necessárias;
- [ ] relacionar as evidências adicionais necessárias aos requisitos ou etapas do ciclo que justificam sua solicitação;
- [ ] concluir as verificações que podem ser realizadas internamente pelo NIAR-Saúde;
- [ ] determinar quais questões dependem efetivamente da equipe do projeto;
- [ ] classificar as pendências abertas quanto ao impacto na continuidade;
- [ ] determinar as condições para iniciar a avaliação por requisito;
- [ ] encaminhar pendências não impeditivas em paralelo, quando aplicável;
- [ ] iniciar a avaliação por requisito;
- [ ] registrar formalmente a conclusão da pré-avaliação documental.

---

## 14. Histórico de versões

| Versão | Data       | Responsável | Alteração                                                                                                                                                                                     | Status          |
| ------- | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 0.1     | 24/07/2026 | NIAR-Saúde  | Criação do documento                                                                                                                                                                          | Em elaboração |
| 0.2     | 26/08/2026 | NIAR-Saúde  | Inclusão da distinção entre pendências impeditivas e não impeditivas, preservação histórica de inconsistências resolvidas e atualização do fluxo de continuidade da pré-avaliação | Em uso          |

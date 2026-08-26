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

> Pendências materiais relacionadas à Tarefa de IA, Versão Avaliável, Contexto de Uso ou Trilha devem ser resolvidas antes da avaliação por requisito.

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

---

## 7. Pendências identificadas

| ID | Questão | Tipo | Impacto | Próxima ação | Estado |
| -- | -------- | ---- | ------- | --------------- | ------ |
|    |          |      |         |                 |        |

Tipos sugeridos:

- informação;
- evidência;
- esclarecimento;
- inconsistência;
- delimitação;
- análise metodológica;
- decisão institucional.

As pendências devem ser detalhadas em:

`documentacao_projeto/registro_de_pendencias.md`

> Somente pendências que dependam efetivamente da equipe do projeto devem ser encaminhadas à equipe.

---

## 8. Determinação de evidências adicionais

Antes de solicitar novos artefatos, o NIAR-Saúde deve verificar:

1. qual informação ou evidência é necessária;
2. qual requisito futuro depende dessa evidência;
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

### Justificativa

[Registrar de forma objetiva as condições para continuidade.]

> Uma pendência não impede automaticamente o início da avaliação por requisito. O impacto deve ser analisado conforme sua materialidade para a delimitação da unidade ou para os requisitos afetados.

---

## 13. Próximos passos

- [ ] realizar verificações adicionais pelo NIAR-Saúde;
- [ ] solicitar esclarecimentos específicos à equipe do projeto;
- [ ] solicitar evidência adicional;
- [ ] atualizar a identificação da avaliação;
- [ ] iniciar avaliação por requisito;
- [ ] outro: __________________.

---

## 14. Histórico de versões

| Versão | Data | Responsável | Alteração            | Status          |
| ------- | ---- | ------------ | ---------------------- | --------------- |
| 0.1     |      | NIAR-Saúde  | Criação do documento | Em elaboração |

# Checklist de Justiça — FIAR-Saúde

**Preenchimento pelo NIAR-Saúde com base nos artefatos e evidências fornecidos pela equipe do projeto**

---

## Identificação

- **Tarefa de IA:**
- **Versão Avaliável:**
- **Contexto de Uso:**
- **Trilha de Execução:**
- **Avaliador(es) NIAR:**
- **Data da avaliação:**
- **Artefatos analisados:**

---

## Regra geral de aplicabilidade

A aplicabilidade deve ser determinada antes da análise das evidências.

Um requisito deve ser considerado **Não aplicável** somente quando a condição objetiva pressuposta pelo requisito não estiver presente na Tarefa de IA, na Versão Avaliável ou no Contexto de Uso avaliado.

A ausência de prática, mecanismo, análise, registro ou evidência **não constitui justificativa de não aplicabilidade**. Nesses casos, a ausência deve ser registrada como pendência ou limitação.

Quando não for possível determinar se a condição objetiva está presente, registrar **Aplicabilidade a esclarecer**, sem presumir Não aplicável.

### Situação da evidência

Para cada pergunta de avaliação, o NIAR-Saúde deve assinalar a situação da evidência:

- [ ] **Evidência suficiente**
- [ ] **Evidência parcial**
- [ ] **Evidência não encontrada**
- [ ] **Evidências inconsistentes**
- [ ] **Evidência adicional necessária**

---

# RC01 — Grupos e populações

## Requisito

**Identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.**

## Aplicabilidade

**A Tarefa, no Contexto de Uso avaliado, pode produzir efeitos ou benefícios que incidam sobre pessoas, grupos ou populações?**

- [ ] Sim
- [ ] Não
- [ ] Não é possível determinar

**Justificativa:**

---

### Regra

- **Sim** → continuar a análise do RC01.
- **Não** → registrar RC01 como **Não aplicável**, com justificativa.
- **Não é possível determinar** → registrar pendência de aplicabilidade.

## Checklist

**Orientação:** algumas respostas podem ser obtidas diretamente do Data Card, Model Card ou de outros documentos do projeto. Quando a pergunta exigir fundamentação ou interpretação específica para Justiça, essa análise deve ser registrada em fonte adequada, por exemplo no Fairness Report.

| Pergunta de avaliação                                                                                                                                                                | Análise / evidência encontrada | Situação da evidência                                                               | Fonte/artefato de evidência |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- |
| Quais grupos ou populações podem ser afetados de forma diferente pela Tarefa?                                                                                                        |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Por que esses grupos ou populações foram considerados relevantes para esta Tarefa e este Contexto de Uso?                                                                            |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| A identificação decorre do Contexto de Uso e da população pertinente à avaliação, e não apenas dos atributos disponíveis nos dados?                                           |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem grupos potencialmente relevantes que não podem ser analisados com os dados disponíveis?                                                                                      |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem grupos potencialmente sujeitos a exclusão dos benefícios da Tarefa?**Nesta etapa, apenas identifique-os; a avaliação das desigualdades de acesso é feita em RC04.** |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Há limitações ou incertezas na identificação dos grupos e populações relevantes?                                                                                                |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |

**Evidências que podem ajudar:** descrição da população, características demográficas, critérios de inclusão/exclusão, literatura pertinente, características do Contexto de Uso, documentação dos dados e conhecimento clínico ou institucional sobre a população considerada.

### Síntese da análise do RC01

- **Evidências disponíveis:**
- **Limitações / pendências:**
- **Evidência adicional a solicitar:**
- **Observações metodológicas:**

---

# RC02 — Diferenças nos efeitos

## Requisito

**Avaliar se a Tarefa de IA produz, reproduz ou agrava diferenças injustificadas nos efeitos sobre os grupos e populações identificados.**

## Aplicabilidade

**Existem grupos ou populações identificados em RC01 sobre os quais a Tarefa possa produzir efeitos no Contexto de Uso avaliado?**

- [ ] Sim
- [ ] Não
- [ ] Não é possível determinar

**Justificativa:**

---

### Regra

- **Sim** → continuar a análise do RC02.
- **Não** → registrar RC02 como **Não aplicável**, com justificativa.
- **Não é possível determinar** → registrar pendência de aplicabilidade.

> A impossibilidade de realizar determinada comparação por ausência ou insuficiência de dados **não torna RC02 não aplicável**. Deve ser registrada como limitação ou pendência da avaliação.

## Checklist

**Orientação:** métricas e resultados já existentes podem ser recuperados do Model Card ou de outros artefatos técnicos. A interpretação das diferenças entre grupos, sua justificabilidade, eventual necessidade de tratamento e riscos residuais constituem análise específica de Justiça e devem ser registradas em fonte apropriada, como o Fairness Report. Quando houver uma decisão técnica decorrente dessa análise, seu fundamento pode exigir registro de decisão.

| Pergunta de avaliação                                                                                                                              | Análise / evidência encontrada | Situação da evidência                                                               | Fonte/artefato de evidência |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- |
| O desempenho ou outros efeitos relevantes e observáveis no Contexto de Uso avaliado foram analisados para os grupos identificados em RC01?          |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Quais métricas, análises ou outros critérios foram utilizados?                                                                                    |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Foram encontradas diferenças de desempenho, erro ou outros efeitos entre os grupos?                                                                 |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Foram analisados tipos de erro relevantes, como falsos positivos e falsos negativos, quando pertinentes à Tarefa?                                   |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem diferenças nas decisões ou consequências decorrentes dos resultados ou do uso da Tarefa, quando observáveis no Contexto de Uso avaliado? |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| As diferenças encontradas foram interpretadas considerando seu significado clínico, técnico ou operacional?                                       |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Quando foram encontradas diferenças, foi analisado se elas são justificadas ou injustificadas? Com base em quê?                                   |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Alguma ação para evitar, reduzir ou tratar diferenças consideradas problemáticas foi considerada ou realizada?                                   |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Permanecem diferenças ou riscos residuais relevantes para os grupos identificados?                                                                  |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |

**Observação:** a avaliação não pressupõe uma métrica universal de fairness nem exige necessariamente comparação estatística formal para todos os grupos. O método deve ser adequado à Tarefa, aos efeitos avaliáveis e às evidências disponíveis.

**Nota:** outros efeitos podem incluir, conforme a Tarefa e o Contexto de Uso, padrões de erro, calibração, decisões, consequências clínicas, técnicas ou operacionais. Nem todos precisam ser avaliados em todos os contextos.

### Síntese da análise do RC02

- **Evidências disponíveis:**
- **Limitações / pendências:**
- **Evidência adicional a solicitar:**
- **Observações metodológicas:**

---

# RC03 — Dados, variáveis-alvo e padrões de referência

## Requisito

**Avaliar se os dados, as variáveis-alvo e os padrões de referência utilizados no desenvolvimento e na avaliação da Tarefa de IA são adequados para os grupos e populações identificados.**

## Aplicabilidade

**O desenvolvimento ou a avaliação da Tarefa utiliza dados, variáveis-alvo ou padrões de referência cuja adequação possa ser relevante para os grupos identificados em RC01?**

- [ ] Sim
- [ ] Não
- [ ] Não é possível determinar

**Justificativa:**

---

### Regra

- **Sim** → continuar a análise do RC03.
- **Não** → registrar RC03 como **Não aplicável**, com justificativa.
- **Não é possível determinar** → registrar pendência de aplicabilidade.

> Ausência de informação sobre os dados, a variável-alvo ou o padrão de referência não justifica Não aplicável. Deve ser registrada como limitação da evidência.

## Checklist

### A. Informações factuais

| Pergunta de avaliação                                                                                        | Análise / evidência encontrada | Situação da evidência                                                               | Fonte/artefato de evidência |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- |
| Os grupos identificados em RC01 estão representados nos dados utilizados no desenvolvimento e na avaliação? |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Há grupos com baixa representação, ausência de informação ou informação insuficiente?                  |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Qual é a origem dos dados e como eles foram selecionados?                                                     |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Qual ou quais variáveis-alvo são utilizadas pela Tarefa?                                                     |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Quais padrões de referência foram utilizados no desenvolvimento e na avaliação, em cada etapa pertinente?  |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem limitações conhecidas relacionadas aos dados, às variáveis-alvo ou aos padrões de referência?    |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |

### B. Análise para Justiça

| Pergunta de avaliação                                                                                       | Análise / evidência encontrada | Situação da evidência                                                               | Fonte/artefato de evidência |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- |
| A origem ou o processo de seleção dos dados pode afetar alguns dos grupos identificados de forma diferente? |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Há razões para considerar os dados inadequados para algum dos grupos identificados?                         |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| A variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?         |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| A variável-alvo pode incorporar ou refletir desigualdades preexistentes relevantes?                          |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Há razões para que algum padrão de referência seja menos adequado ou válido para determinados grupos?    |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Alguma dessas condições pode plausivelmente contribuir para diferenças nos efeitos avaliados em RC02?      |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |

**Observação:** problemas gerais de qualidade ou validade dos dados pertencem principalmente à dimensão Segurança. Em Justiça, o foco está em condições com mecanismo plausível de efeito diferenciado entre grupos ou populações.

**Orientação para análise:** a resposta pode considerar, conforme pertinente, literatura clínica ou técnica, diferenças conhecidas entre grupos, processo de definição dos rótulos, concordância entre avaliadores, validade do padrão de referência, limitações de mensuração e outros elementos que indiquem se o alvo ou a referência podem funcionar de forma diferente entre grupos. A checklist não exige um método único de análise.

### Relação entre os artefatos

- **Data Card** → composição, proveniência, seleção e limitações dos dados.
- **Model Card** → Tarefa, variável-alvo, desenvolvimento, avaliação e desempenho.
- **Fairness Report ou análise equivalente** → pode registrar as implicações desses elementos para os grupos e populações considerados, sem duplicar a factualidade já documentada.

### Síntese da análise do RC03

- **Evidências disponíveis:**
- **Limitações / pendências:**
- **Evidência adicional a solicitar:**
- **Observações metodológicas:**

---

# RC04 — Acesso e possibilidade de benefício

## Requisito

**Avaliar se a forma de disponibilização da Tarefa de IA produz, reproduz ou agrava desigualdades injustificadas entre os grupos e populações identificados quanto à possibilidade de se beneficiar de seu uso.**

## Aplicabilidade

**No Contexto de Uso avaliado, existe alguma forma de disponibilização da Tarefa pela qual pessoas, grupos ou populações possam acessar ou se beneficiar de seu uso?**

- [ ] Sim
- [ ] Não
- [ ] Não é possível determinar

**Justificativa:**

---

### Regra

- **Sim** → continuar a análise do RC04.
- **Não** → registrar RC04 como **Não aplicável**, com justificativa.
- **Não é possível determinar** → registrar pendência de aplicabilidade; não presumir Não aplicável.

> Um uso futuro pretendido que ainda não integra o Contexto de Uso avaliado não deve ser usado para tornar RC04 aplicável ao ciclo atual.

## Checklist

| Pergunta de avaliação                                                                                                                                        | Análise / evidência encontrada | Situação da evidência                                                               | Fonte/artefato de evidência |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- |
| Como a Tarefa é disponibilizada no Contexto de Uso avaliado?                                                                                                  |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem requisitos de infraestrutura, tecnologia ou recursos para acessar ou utilizar a Tarefa?                                                                |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Idioma, conectividade, localização, custo, letramento ou outras condições podem limitar a possibilidade de algum grupo acessar ou se beneficiar da Tarefa? |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Existem diferenças entre locais, serviços ou populações quanto à disponibilidade da Tarefa?                                                               |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Algum grupo identificado em RC01 possui menor possibilidade de se beneficiar da disponibilização da Tarefa?                                                  |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| As desigualdades identificadas foram analisadas quanto à sua justificabilidade?                                                                               |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Foram consideradas medidas ou alternativas para evitar, reduzir ou tratar barreiras identificadas?                                                             |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |
| Permanecem limitações ou desigualdades residuais de acesso ou possibilidade de benefício?                                                                   |                                  | [ ] Suficiente[ ] Parcial[ ] Não encontrada[ ] Inconsistente[ ] Adicional necessária |                              |

### Síntese da análise do RC04

- **Evidências disponíveis:**
- **Limitações / pendências:**
- **Evidência adicional a solicitar:**
- **Observações metodológicas:**

---

# Fechamento da checklist

## Situação dos requisitos

| Requisito | Aplicabilidade                              | Principais evidências | Principais pendências |
| --------- | ------------------------------------------- | ---------------------- | ---------------------- |
| RC01      | Aplicável / Não aplicável / A esclarecer |                        |                        |
| RC02      | Aplicável / Não aplicável / A esclarecer |                        |                        |
| RC03      | Aplicável / Não aplicável / A esclarecer |                        |                        |
| RC04      | Aplicável / Não aplicável / A esclarecer |                        |                        |

---

## Evidências ou artefatos adicionais necessários

- [ ] Nenhum
- [ ] Complementação do Data Card
- [ ] Complementação do Model Card
- [ ] Produção ou atualização do Fairness Report
- [ ] Registro de decisão
- [ ] Outra análise/documentação: ______________________

---

## Limitações conhecidas

---

## Solicitações adicionais à equipe do projeto

### Solicitação 1

- **Informação/evidência solicitada:**
- **Artefato ou análise a complementar:**
- **Responsável no projeto:**
- **Prazo:**

### Solicitação 2

- **Informação/evidência solicitada:**
- **Artefato ou análise a complementar:**
- **Responsável no projeto:**
- **Prazo:**

---

## Acompanhamento pelo NIAR

- **Responsável NIAR:**
- **Data prevista para revisão das complementações:**

---

## Observações gerais da avaliação

---

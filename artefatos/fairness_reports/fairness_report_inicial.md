# Fairness Report — FIAR-Saúde

**Preenchimento pela equipe do projeto**

Este relatório registra as análises específicas de Justiça necessárias para a avaliação FIAR-Saúde. Ele deve reutilizar, por referência, informações factuais já documentadas em Data Cards, Model Cards e outros artefatos, evitando duplicação desnecessária.

A existência deste relatório não demonstra, isoladamente, que a Tarefa de IA seja justa ou que não existam disparidades.

**Como preencher:** responda apenas ao que for pertinente à Tarefa e ao Contexto de Uso. Quando a informação já estiver no Data Card, Model Card ou outro documento, apenas indique a fonte. Quando a resposta depender de conhecimento técnico ou clínico específico, ela pode ser construída conjuntamente pela equipe.

---

## 1. Identificação

| Campo                 | Preenchimento |
| --------------------- | ------------- |
| Projeto               |               |
| Tarefa de IA          |               |
| Versão Avaliável    |               |
| Contexto de Uso       |               |
| Trilha de Execução  |               |
| Versão do relatório |               |
| Data de referência   |               |

---

## 2. Escopo da análise de Justiça

### 2.1 Escopo considerado

Descrever brevemente o que esta análise de Justiça cobre, incluindo a população pertinente, os dados e resultados considerados e o Contexto de Uso.

[Preencher]

### 2.2 Fora do escopo

Registrar grupos, populações, condições, usos ou análises que não fazem parte deste relatório.

[Preencher]

### 2.3 Limitações gerais de escopo

Registrar limitações que afetem a interpretação da análise.

[Preencher]

---

## 3. RC01 — Grupos e populações

**Requisito:** Identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.

### 3.1 Grupos considerados

| Grupo ou população | Por que este grupo pode ser afetado de forma diferente ou ter menos possibilidade de se beneficiar? | Está disponível nos dados? | Foi analisado?       | Fonte factual / referência | Limitações |
| -------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------- | --------------------------- | ------------ |
|                      |                                                                                                     | Sim / Não / Parcial         | Sim / Não / Parcial |                             |              |

Exemplos podem incluir sexo, idade, região, condição clínica ou outros grupos relevantes para a população atendida. Não é necessário incluir um grupo apenas porque essa informação existe nos dados.

### 3.2 Grupos relevantes não analisáveis

Existem grupos potencialmente relevantes que não puderam ser analisados com os dados disponíveis?

[Preencher]

### 3.3 Completude da seleção

Existe algum grupo importante para esta Tarefa que ficou de fora da análise? Por quê?

[Preencher]

### 3.4 Limitações e incertezas

Registrar incertezas na identificação ou seleção dos grupos.

[Preencher]

> A disponibilidade de um atributo nos dados não é, por si só, justificativa suficiente para sua inclusão. Da mesma forma, a indisponibilidade de um atributo potencialmente relevante deve ser registrada como limitação quando impedir a análise.

---

## 4. RC02 — Diferenças nos efeitos

**Requisito:** Avaliar se a Tarefa de IA produz, reproduz ou agrava diferenças injustificadas nos efeitos sobre os grupos e populações identificados.

### 4.1 Resultados por grupo

Registrar apenas métricas, comparações ou outros efeitos pertinentes à Tarefa e ao Contexto de Uso. Resultados já documentados em outro artefato podem ser referenciados, sem necessidade de repetição integral.

| Grupo ou comparação | Métrica ou efeito | Resultado / diferença observada | Incerteza ou limitação | Interpretação clínica, técnica ou operacional | Há uma explicação aceitável para a diferença? | Fonte |
| --------------------- | ------------------ | -------------------------------- | ------------------------ | ------------------------------------------------- | -------------------------------------------------- | ----- |
|                       |                    |                                  |                          |                                                   | Sim/Não/Ainda não sabemos                        |       |

### 4.2 Tipos de erro relevantes

Foram analisados tipos de erro relevantes para os grupos considerados, como falsos positivos, falsos negativos ou outros erros pertinentes?

[Preencher]

### 4.3 Critérios de interpretação

Como a equipe decidiu se uma diferença entre grupos é importante ou preocupante?

Podem ser considerados, conforme pertinente:

- magnitude da diferença;
- incerteza estatística;
- relevância clínica;
- relevância técnica;
- relevância operacional;
- relevância social;
- tamanho e estabilidade dos grupos;
- literatura ou referência externa pertinente;
- critério institucional ou regulatório aplicável.

[Preencher]

### 4.4 Como interpretar as diferenças encontradas

Para cada diferença considerada relevante, explicar:

- existe uma razão clínica, técnica ou operacional conhecida para essa diferença?
- essa razão é considerada aceitável no Contexto de Uso?
- a diferença pode prejudicar algum grupo?
- ainda faltam informações para chegar a uma conclusão?
  [Preencher]

### 4.5 Ações ou respostas consideradas

Registrar medidas consideradas ou realizadas em resposta a diferenças consideradas problemáticas, quando houver.

[Preencher]

### 4.6 Riscos residuais

Depois da análise e de eventuais ações, permanecem diferenças ou problemas que possam afetar algum grupo?

[Preencher]

> Diferença numérica não equivale automaticamente a injustiça. A análise deve permanecer proporcional às evidências disponíveis e ao Contexto de Uso.

---

## 5. RC03 — Dados, variáveis-alvo e padrões de referência

**Requisito:** Avaliar se os dados, as variáveis-alvo e os padrões de referência utilizados no desenvolvimento e na avaliação da Tarefa de IA são adequados para os grupos e populações identificados.

Esta seção deve registrar as **implicações para Justiça**, e não repetir a descrição factual completa dos dados já presente no Data Card ou no Model Card.

**Para facilitar o preenchimento:**

- **Dados**: informações usadas para desenvolver ou avaliar o modelo.
- **O que o modelo tenta prever ou identificar**: aquilo que aparece tecnicamente como variável-alvo ou rótulo.
- **Padrão de referência**: informação usada como referência para dizer se a resposta do modelo está correta, por exemplo diagnóstico ou avaliação de especialistas.

| Elemento               | Questão para Justiça                                                                                                                                                      | Análise | Limitação / incerteza | Fonte |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------------- | ----- |
| Dados                  | A origem ou o processo de seleção dos dados pode afetar alguns grupos de forma diferente?                                                                                 |          |                         |       |
| Dados                  | Há razões para considerar os dados inadequados para algum dos grupos identificados?                                                                                       |          |                         |       |
| Variável-alvo         | O que o modelo tenta prever ou identificar é definido de forma adequada para todos os grupos? Há algum grupo para o qual essa definição pode funcionar pior?            |          |                         |       |
| Variável-alvo         | A forma como o resultado esperado foi definido pode refletir diferenças já existentes na assistência, no diagnóstico ou nos dados?                                      |          |                         |       |
| Padrão de referência | A referência usada como “verdade” para avaliar o modelo é igualmente confiável para todos os grupos? Há algum grupo em que essa referência possa ser menos adequada? |          |                         |       |
| Relação com RC02     | Alguma característica dos dados, da definição do resultado ou da referência utilizada pode ajudar a explicar as diferenças encontradas entre os grupos?                |          |                         |       |

### Orientação

A análise pode considerar, conforme pertinente:

- cobertura e seleção dos dados;
- diferenças de medição;
- composição dos grupos;
- processo de definição das variáveis-alvo;
- processo de rotulagem;
- concordância entre avaliadores;
- validade do padrão de referência;
- literatura clínica ou técnica;
- mecanismos plausíveis de efeito diferenciado.

Não é exigido um método único de análise.

---

## 6. RC04 — Acesso e possibilidade de benefício

**Requisito:** Avaliar se a forma de disponibilização da Tarefa de IA produz, reproduz ou agrava desigualdades injustificadas entre os grupos e populações identificados quanto à possibilidade de se beneficiar de seu uso.

### 6.1 Aplicabilidade

No uso que está sendo avaliado agora, alguma pessoa, grupo ou serviço consegue utilizar ou se beneficiar desta Tarefa de IA?

- [ ] Sim
- [ ] Não
- [ ] Não é possível determinar

**Justificativa:**

[Preencher]

> Se a resposta for **Não**, não é necessário preencher as subseções 6.2 a 6.5. Um uso futuro pretendido que ainda não integra o Contexto de Uso atual não deve ser usado para tornar RC04 aplicável.

### 6.2 Forma de disponibilização

Como a Tarefa é disponibilizada no Contexto de Uso avaliado?

[Preencher]

### 6.3 Barreiras ou condições de acesso

Existem condições como infraestrutura, conectividade, localização, custo, idioma, letramento, recursos institucionais ou outras que possam afetar diferentemente os grupos identificados?

[Preencher]

### 6.4 Diferenças na possibilidade de benefício

Algum grupo possui menor possibilidade de acessar, utilizar ou se beneficiar da Tarefa?

[Preencher]

### 6.5 Medidas e riscos residuais

Foram consideradas medidas para evitar, reduzir ou tratar barreiras? Permanecem desigualdades residuais?

[Preencher]

---

## 7. Limitações e análises ainda necessárias

Registrar apenas questões que permanecem abertas e que sejam necessárias para completar a análise de Justiça.

| O que ainda não sabemos? | Por que isso é importante? | O que precisa ser feito? | Quem pode responder? | Estado |
| ------------------------- | --------------------------- | ------------------------ | -------------------- | ------ |
|                           |                             |                          |                      |        |

---

## 8. Evidências utilizadas e decisões relacionadas

### 8.1 Evidências e fontes

Referenciar os artefatos efetivamente utilizados nesta análise.

| Evidência ou fonte                          | Versão / data | Utilização nesta análise |
| -------------------------------------------- | -------------- | --------------------------- |
| Data Card                                    |                |                             |
| Model Card                                   |                |                             |
| Resultados técnicos / notebook / relatório |                |                             |
| Literatura ou referência externa            |                |                             |
| Outra fonte                                  |                |                             |

### 8.2 Decisões relacionadas

Registrar apenas decisões técnicas ou institucionais diretamente relacionadas a esta análise, quando existirem.

| ID / referência | Decisão | Relação com a análise de Justiça |
| ---------------- | -------- | ------------------------------------ |
|                  |          |                                      |

---

## 9. Síntese da equipe do projeto

### Principais achados

[Preencher]

### Principais limitações

[Preencher]

### O que ainda não conseguimos concluir

[Preencher]

### O que será feito a partir desta análise

[Preencher]

---

## 10. Histórico de versões

| Versão | Data | Responsável | Alteração             |
| ------- | ---- | ------------ | ----------------------- |
| 0.1     |      |              | Criação do relatório |

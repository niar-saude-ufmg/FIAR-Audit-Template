
# Fairness Report

## Sobre este modelo

Este modelo organiza as análises de justiça de uma Tarefa de IA. Seu uso é opcional: a existência deste documento não é, por si só, requisito para a avaliação. O que importa é se as análises pertinentes foram feitas e estão documentadas.

- **Aproveite o que já existe.** Se uma análise está no Model Card, no Data Card, em um artigo ou em outro documento, indique a seção, página ou tabela e traga apenas os resultados essenciais.
- **Adapte à tarefa.** Preencha o que for pertinente ao tipo de tarefa (classificação, predição, geração de dados sintéticos, outra).
- **Quando não puder responder um campo, use:**
  - **Não sabemos:** a equipe não conhece a informação.
  - **Não realizado:** a análise ou ação ainda não foi feita. Informe se está planejada.
  - **Ainda não definido:** a escolha ainda não foi tomada.
  - **Não se aplica:** o campo não se aplica a esta tarefa. Explique o motivo.
- **Separe resultado de interpretação.** "A sensibilidade foi menor no grupo A" é um resultado. Dizer que isso é injusto exige considerar o contexto, as limitações e as consequências (seção 5).

Este documento é preenchido pela equipe do projeto. Ele não classifica o atendimento a requisitos nem substitui decisões do NIAR-Saúde ou do Comitê Gestor.

---

## 1. Contexto da análise 

| Campo                                                          | Preenchimento |
| -------------------------------------------------------------- | ------------- |
| Projeto                                                        |               |
| Tarefa de IA e finalidade                                      |               |
| Versão avaliada                                               |               |
| Contexto considerado na análise                               |               |
| Dados utilizados na análise (conjunto, período, tamanho)     |               |
| Responsável pela análise                                     |               |
| Data da análise                                               |               |
| Documentos de referência (Model Card, Data Card, artigo etc.) |               |

---

## 2. Grupos e preocupações de justiça 

Quais grupos podem ser afetados de forma diferente pela tarefa, e por quê? A escolha deve partir da tarefa, da população e do contexto, e não apenas dos atributos disponíveis nos dados.

| Grupo considerado | Por que este grupo foi considerado | Possível prejuízo ou desigualdade investigada |
| ----------------- | ---------------------------------- | ----------------------------------------------- |
|                   |                                    |                                                 |

**Grupos ou interseções relevantes não analisados e motivo:**
(ex.: atributo não registrado nos dados; subgrupo pequeno demais para comparação)

---

## 3. Dados, rótulos e representação por grupo

Os dados permitem comparar os grupos de forma confiável? Responda o que for pertinente à tarefa.

| Campo                                                                                    | Preenchimento |
| ---------------------------------------------------------------------------------------- | ------------- |
| Quantidade e cobertura dos dados por grupo                                               |               |
| Dados ausentes e problemas conhecidos de qualidade, por grupo                            |               |
| Origem e adequação dos rótulos ou do padrão de referência, quando pertinentes       |               |
| Para dados sintéticos: cobertura da base de origem, variáveis e limitações por grupo |               |
| Limitações para a comparação entre grupos                                            |               |

---

## 4. Análises e resultados

| Campo                                                                                              | Preenchimento |
| -------------------------------------------------------------------------------------------------- | ------------- |
| Pergunta investigada (que diferença entre grupos se quer verificar)                               |               |
| Métricas utilizadas e por que são pertinentes a essa pergunta                                    |               |
| Procedimento de comparação (conjunto de dados, limiar de classificação quando houver, método) |               |
| Localização das análises existentes (documento, seção, tabela)                                |               |

**Resultados por grupo**

Informe os valores por grupo, as diferenças em relação ao grupo de comparação, os denominadores (número de casos) e a incerteza (por exemplo, intervalo de confiança). Indique quando um grupo for pequeno demais para concluir.

*Exemplo adaptável, para classificação:*

| Grupo | Casos positivos / negativos | Sensibilidade (IC 95%) | Taxa de falsos positivos (IC 95%) | Diferença em relação ao grupo de comparação |
| ----- | --------------------------- | ---------------------- | --------------------------------- | ------------------------------------------------ |
|       |                             |                        |                                   |                                                  |

*Exemplo adaptável, para dados sintéticos:*

| Grupo | Registros reais / sintéticos | Fidelidade (métrica e valor) | Utilidade no uso posterior (métrica e valor) | Diferença em relação ao grupo de comparação |
| ----- | ----------------------------- | ----------------------------- | --------------------------------------------- | ------------------------------------------------ |
|       |                               |                               |                                               |                                                  |

Se os dados sintéticos forem usados para treinar um classificador, as métricas de classificação por grupo desse uso posterior também podem ser pertinentes.

---

## 5. Interpretação, limitações e ações

| Campo                                                  | Preenchimento |
| ------------------------------------------------------ | ------------- |
| O que os resultados significam no contexto considerado |               |
| Possíveis consequências para os grupos               |               |
| O que os dados não permitem concluir                  |               |

**Ações**

| Ação | Situação                      | Responsável | Prazo, se houver | Onde está documentada |
| ------ | ------------------------------- | ------------ | ---------------- | ---------------------- |
|        | realizada / prevista / proposta |              |                  |                        |

- **Realizada:** já feita; indique onde está documentada.
- **Prevista:** decidida pela equipe, com responsável.
- **Proposta:** sugerida, sem decisão tomada.

---

## 6. Síntese em linguagem simples

Escreva para quem não é da área técnica. Use números concretos e distinga porcentagem de pontos percentuais.

| Campo                                  | Preenchimento |
| -------------------------------------- | ------------- |
| Principal achado                       |               |
| Possível consequência para os grupos |               |
| O que permanece incerto                |               |

*Exemplo fictício:* "No conjunto de teste, o modelo deixou de identificar 20 de cada 100 casos positivos no grupo A e 10 de cada 100 no grupo B, uma diferença de 10 pontos percentuais. Esse resultado descreve o teste realizado; sua consequência para o uso pretendido ainda precisa ser discutida."

Esta síntese não classifica o atendimento a requisitos nem propõe deliberação institucional.

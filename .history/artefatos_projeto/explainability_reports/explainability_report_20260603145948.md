# Explainability Report — FIAR-Saúde

**Projeto:**
**Tarefa:**
**Versão Avaliável:**
**Trilha:** ( ) Experimental ( ) Produção
**Responsável técnico:**
**Data de produção:**

---

## 1. Ferramenta e Justificativa

Descreva a ferramenta de explicabilidade utilizada e justifique sua escolha com base
nas características do modelo e no contexto da tarefa.

**Ferramenta utilizada:**

**Justificativa:**

**Escopo da análise:**

> Indique se a explicabilidade foi aplicada a todos os modelos desenvolvidos ou apenas
> a um subconjunto, e justifique formalmente qualquer exclusão.

> Ferramentas sugeridas: SHAP, DICE, Captum, LIME, entre outras.

---

## 2. Análise Local

A análise local examina a contribuição de cada atributo para previsões individuais,
permitindo identificar o comportamento do modelo em casos específicos.

### Metodologia

Descreva brevemente o método de análise local utilizado (ex: waterfall plot, force plot).

### Resultados

<!-- Insira aqui os gráficos de análise local para amostras representativas do conjunto de teste -->

![Análise local — amostra 1](imagens/local_amostra1.png)

![Análise local — amostra 2](imagens/local_amostra2.png)

**Interpretação:**

> Descreva os atributos mais impactantes identificados, o sentido de sua influência
> (positiva ou negativa) e eventuais padrões observados entre amostras.

---

## 3. Análise Global

A análise global examina o comportamento agregado do modelo sobre o conjunto de dados,
identificando os atributos de maior influência sistemática.

### Metodologia

Descreva brevemente o método de análise global utilizado (ex: summary plot, bar plot).

### Resultados

<!-- Insira aqui o gráfico de análise global -->

![Análise global — summary plot](imagens/global_summary.png)

**Interpretação:**

> Descreva os atributos de maior importância global, a direção de sua influência
> e eventuais interações relevantes identificadas.

---

## 4. Relação com a Avaliação de Justiça

Descreva se os atributos sensíveis identificados no Fairness Report (ex: raça, sexo,
região) aparecem como relevantes na análise de explicabilidade, e qual a implicação
disso para a interpretação do modelo.

**Atributos sensíveis presentes na análise de explicabilidade:** ( ) Sim ( ) Não

**Descrição:**

---

## 5. Conclusão

Sintetize os principais achados da análise de explicabilidade, destacando:

- os atributos mais influentes globalmente;
- comportamentos locais relevantes;
- implicações para o uso responsável do modelo;
- limitações da análise realizada.

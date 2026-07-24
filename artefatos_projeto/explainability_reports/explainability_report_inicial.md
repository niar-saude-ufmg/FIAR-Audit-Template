# Relatório Inicial de Explicabilidade

## Controle do documento

| Campo                 | Preenchimento                                        |
| --------------------- | ---------------------------------------------------- |
| Versão do documento  | 0.1                                                  |
| Status                | Em preenchimento pelo projeto                        |
| Projeto               | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Tarefa de IA          | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Versão Avaliável    | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Contexto de Uso       | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Trilha                | [ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde] |
| Responsável técnico | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Data de referência   | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |
| Última atualização | [INFORMAÇÃO PENDENTE — preencher pelo projeto]    |

> Este documento registra as evidências disponíveis e as análises planejadas
> para explicabilidade e interpretação da Tarefa de IA, da Versão Avaliável e
> do Contexto de Uso identificados.
>
> A existência deste relatório não demonstra, isoladamente, que a tarefa seja
> transparente, interpretável ou adequadamente compreendida por seus usuários.
>
> Importância de variável, atribuição ou saliência não deve ser interpretada
> automaticamente como causalidade.

---

## 1. Finalidade da explicabilidade

Descrever por que explicações são necessárias neste Contexto de Uso.

Possíveis finalidades, somente quando aplicáveis:

- apoiar compreensão técnica do comportamento do modelo;
- apoiar revisão por especialistas;
- apoiar identificação de erros;
- apoiar investigação de casos;
- comunicar limitações;
- apoiar contestação;
- apoiar supervisão humana;
- apoiar validação clínica;
- apoiar monitoramento;
- apoiar prestação de contas;
- apoiar pesquisa.

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

---

## 2. Estado atual da análise

Selecionar uma opção e justificar:

```text
Análise de explicabilidade não iniciada

Plano de explicabilidade elaborado

Análise parcial realizada

Análise concluída pelo projeto

Análise existente, mas ainda não fornecida

Análise fornecida e em validação

Não aplicável — justificativa obrigatória
```

### Estado

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

### Justificativa

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

Quando ainda não houver análise suficiente, este documento deve funcionar como plano de explicabilidade.

---

## 3. Escopo

### 3.1 Incluído

Registrar:

* modelo;
* saídas;
* casos;
* métodos;
* públicos;
* Contexto de Uso;
* versão;
* conjunto de dados;
* tipo de explicação.
* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 3.2 Fora do escopo

* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 3.3 Limitações de escopo

* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

---

## 4. Público-alvo

| ID      | Público                                          | Papel | Necessidade de explicação | Tipo de explicação esperado |
| ------- | ------------------------------------------------- | ----- | --------------------------- | ----------------------------- |
| PUB-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |       |                             |                               |

Possíveis públicos, quando aplicáveis:

* equipe de desenvolvimento;
* especialistas clínicos;
* operadores;
* pesquisadores;
* gestores;
* avaliadores do NIAR-Saúde;
* pacientes;
* cidadãos;
* responsáveis institucionais;
* equipes de suporte;
* reguladores.

Não assumir que o mesmo tipo de explicação atende adequadamente a todos os públicos.

---

## 5. Decisão ou processo apoiado pela explicação

Descrever:

* em que momento a explicação é apresentada;
* qual decisão ou interpretação ela deve apoiar;
* quem a utiliza;
* que ação pode resultar dela;
* quais consequências podem decorrer de interpretação incorreta.

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

---

## 6. Perguntas de explicabilidade

| ID        | Pergunta                                                                  | Público-alvo | Decisão relacionada | Prioridade |
| --------- | ------------------------------------------------------------------------- | ------------- | -------------------- | ---------- |
| EXP-Q-001 | [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |               |                      |            |

Exemplos, quando aplicáveis:

* quais elementos da entrada mais influenciaram uma saída?
* quais padrões globais o modelo utiliza?
* como o comportamento varia entre grupos?
* por que duas instâncias semelhantes receberam saídas diferentes?
* quais sinais podem indicar erro?
* em que situações o modelo é menos confiável?
* quais limitações devem ser apresentadas ao usuário?

---

## 7. Método utilizado

| Campo                    | Preenchimento                                     |
| ------------------------ | ------------------------------------------------- |
| Método                  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Biblioteca ou ferramenta | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Versão                  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Tipo de explicação     | Global / Local / Ambos                            |
| Dependência do modelo   | Agnóstico / Específico do modelo                |
| Unidade explicada        | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Saída explicada         | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Configuração           | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Fonte ou execução      | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

Exemplos de métodos, somente quando efetivamente utilizados:

* SHAP;
* LIME;
* Integrated Gradients;
* Grad-CAM;
* saliency maps;
* attention visualization;
* feature permutation;
* partial dependence;
* counterfactuals;
* protótipos;
* regras;
* análise de erros;
* modelo substituto;
* método clínico específico.

Não inventar método ou resultado.

---

## 8. Justificativa do método

Registrar:

* relação com a arquitetura;
* relação com a modalidade dos dados;
* relação com o público;
* relação com o Contexto de Uso;
* vantagens;
* limitações;
* alternativas consideradas.

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

Quando os documentos não mencionarem alternativas:

```text
[INFORMAÇÃO PENDENTE — confirmar com a equipe se houve alternativas consideradas]
```

---

## 9. Alternativas consideradas

| Alternativa                                       | Vantagens | Limitações | Motivo para adoção ou rejeição |
| ------------------------------------------------- | --------- | ------------ | ---------------------------------- |
| [INFORMAÇÃO PENDENTE — preencher pelo projeto] |           |              |                                    |

Não reconstruir alternativas retrospectivamente sem confirmação.

---

## 10. Dados e casos utilizados

| Campo                    | Preenchimento                                     |
| ------------------------ | ------------------------------------------------- |
| Dataset                  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Versão                  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Partição               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Número de casos         | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Critério de seleção   | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Classes ou saídas       | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Grupos considerados      | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Casos de erro incluídos | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Fonte ou execução      | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

### Critério de seleção dos exemplos

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

A seleção não deve se limitar apenas a exemplos de bom desempenho sem justificativa.

---

## 11. Resultados globais disponíveis

Registrar padrões gerais do comportamento do modelo, quando efetivamente analisados.

| ID      | Resultado                                         | Método | Evidência | Interpretação permitida | Limitação |
| ------- | ------------------------------------------------- | ------- | ---------- | ------------------------- | ----------- |
| GLO-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |         |            |                           |             |

Possíveis resultados globais:

* importância agregada;
* sensibilidade a atributos;
* padrões por classe;
* estabilidade;
* resposta a perturbações;
* diferenças entre grupos;
* dependências parciais;
* comportamento médio.

Não tratar associação global como mecanismo causal.

---

## 12. Resultados locais disponíveis

| ID      | Caso                                              | Saída explicada | Resultado da explicação | Evidência | Interpretação permitida |
| ------- | ------------------------------------------------- | ---------------- | ------------------------- | ---------- | ------------------------- |
| LOC-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |                  |                           |            |                           |

Registrar, quando aplicável:

* instância;
* predição;
* classe;
* score;
* elementos destacados;
* método;
* resultado;
* revisão por especialista;
* limitações.

---

## 13. Visualizações e interfaces

| ID      | Visualização ou interface                       | Público | Finalidade | Localização | Estado |
| ------- | ------------------------------------------------- | -------- | ---------- | ------------- | ------ |
| VIS-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |          |            |               |        |

Estados sugeridos:

* protótipo;
* em desenvolvimento;
* testada internamente;
* validada com usuários;
* integrada;
* não implementada.

---

## 14. Interpretação permitida

Descrever o que os resultados de explicabilidade permitem afirmar.

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

Exemplos de formulações permitidas, quando sustentadas:

* o método atribuiu maior relevância a determinados segmentos da entrada;
* o modelo apresentou padrão consistente em um conjunto de casos;
* a análise identificou sensibilidade a determinada variável;
* especialistas consideraram determinadas explicações clinicamente plausíveis.

---

## 15. Interpretação não permitida

Registrar explicitamente limites como:

* atribuição não demonstra causalidade;
* importância não demonstra necessidade;
* saliência não demonstra uso clínico correto;
* explicação local não descreve todo o comportamento do modelo;
* explicação global não explica cada instância;
* plausibilidade não demonstra fidelidade;
* confiança do modelo não equivale a explicação;
* probabilidade não equivale a justificativa;
* atenção não equivale automaticamente a importância;
* explicação não valida o diagnóstico;
* explicação não substitui supervisão.
* [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

---

## 16. Fidelidade

Registrar se foi avaliada a fidelidade da explicação ao comportamento real do modelo.

| Campo                 | Preenchimento                                     |
| --------------------- | ------------------------------------------------- |
| Avaliação realizada | Sim / Não                                        |
| Método               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Métrica              | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Resultado             | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Limitação           | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

Quando não houver avaliação:

```text
[ANÁLISE PENDENTE — fidelidade não avaliada]
```

---

## 17. Estabilidade e robustez das explicações

Registrar se explicações semelhantes são produzidas para:

* entradas semelhantes;
* pequenas perturbações;
* diferentes seeds;
* diferentes versões do modelo;
* diferentes métodos;
* diferentes subconjuntos.

| Teste                                                                     | Resultado | Evidência | Limitação |
| ------------------------------------------------------------------------- | --------- | ---------- | ----------- |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |           |            |             |

---

## 18. Validação com especialistas

| Campo                    | Preenchimento                                     |
| ------------------------ | ------------------------------------------------- |
| Especialistas envolvidos | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Perfil                   | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Número de participantes | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Procedimento             | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Critérios               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Resultado                | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Limitações             | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

Plausibilidade para especialistas não demonstra, isoladamente, fidelidade ao modelo.

---

## 19. Validação com usuários

| Campo                 | Preenchimento                                     |
| --------------------- | ------------------------------------------------- |
| Usuários envolvidos  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Contexto              | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Método               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Compreensão avaliada | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Utilidade avaliada    | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Riscos identificados  | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Resultado             | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

---

## 20. Relação com o Contexto de Uso

Descrever como a explicação será utilizada no fluxo real ou experimental.

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

Considerar:

* momento de apresentação;
* pressão de tempo;
* nível de especialização;
* possibilidade de contestação;
* registro da decisão;
* risco de automação;
* excesso de confiança;
* divergência entre usuário e modelo;
* necessidade de treinamento;
* impacto sobre fluxo de trabalho.

---

## 21. Riscos de interpretação

| ID          | Risco                                                                     | Público afetado | Consequência | Mitigação prevista |
| ----------- | ------------------------------------------------------------------------- | ---------------- | ------------- | -------------------- |
| RSK-EXP-001 | [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |                  |               |                      |

Possíveis riscos:

* falsa causalidade;
* confiança excessiva;
* confirmação de hipótese;
* cherry-picking;
* explicação persuasiva, mas infiel;
* ocultação de incerteza;
* interpretação fora do escopo;
* sobrecarga cognitiva;
* dependência indevida;
* aparência de objetividade;
* uso de explicação como justificativa posterior.

---

## 22. Incerteza

Registrar como a incerteza da predição e da própria explicação é apresentada.

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

Distinguir:

* probabilidade;
* calibração;
* confiança;
* incerteza epistemológica;
* incerteza aleatória;
* estabilidade da explicação;
* ausência de evidência.

---

## 23. Casos de erro

| ID          | Caso                                              | Tipo de erro | Explicação analisada | Conclusão | Encaminhamento |
| ----------- | ------------------------------------------------- | ------------ | ---------------------- | ---------- | -------------- |
| ERR-EXP-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |              |                        |            |                |

A análise de explicabilidade deve incluir, quando pertinente:

* falsos positivos;
* falsos negativos;
* casos limítrofes;
* casos de baixa confiança;
* casos discordantes entre modelo e especialista;
* casos de grupos relevantes;
* casos fora da distribuição.

---

## 24. Diferenças entre grupos

Registrar se as explicações foram comparadas entre grupos relevantes.

| Grupo                                                                     | Método | Resultado | Evidência | Limitação |
| ------------------------------------------------------------------------- | ------- | --------- | ---------- | ----------- |
| [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |         |           |            |             |

Não concluir ausência de diferença quando a análise não tiver sido realizada.

---

## 25. Limitações

Registrar, conforme aplicável:

* método aproximado;
* baixa fidelidade;
* instabilidade;
* alta sensibilidade a parâmetros;
* dificuldade de interpretação;
* ausência de validação por especialistas;
* ausência de validação com usuários;
* análise restrita a poucos casos;
* seleção não representativa;
* ausência de comparação entre métodos;
* falta de explicação para múltiplas classes;
* incompatibilidade com o Contexto de Uso;
* ausência de incerteza;
* risco de causalidade indevida.
* [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

---

## 26. Mitigações realizadas

| ID          | Mitigação                                       | Risco tratado | Evidência | Resultado |
| ----------- | ------------------------------------------------- | ------------- | ---------- | --------- |
| MIT-EXP-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |               |            |           |

Não registrar orientação futura como mitigação implementada.

---

## 27. Análises ainda necessárias

| ID          | Análise                                                                  | Objetivo | Dados ou casos necessários | Responsável | Prioridade | Estado |
| ----------- | ------------------------------------------------------------------------- | -------- | --------------------------- | ------------ | ---------- | ------ |
| ANA-EXP-001 | [ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos] |          |                             |              |            |        |

Possíveis análises, quando justificadas:

* explicabilidade global;
* explicabilidade local;
* análise de fidelidade;
* análise de estabilidade;
* comparação entre métodos;
* validação com especialistas;
* teste com usuários;
* análise de erros;
* análise por grupo;
* análise por classe;
* avaliação no fluxo operacional;
* avaliação de incerteza.

---

## 28. Plano de explicabilidade

Preencher quando a análise ainda não tiver sido realizada.

### 28.1 Finalidade

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### 28.2 Público

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 28.3 Perguntas

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### 28.4 Método proposto

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### 28.5 Casos

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 28.6 Critérios de avaliação

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### 28.7 Validação

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### 28.8 Responsáveis

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 28.9 Prazo

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

### 28.10 Artefatos esperados

* código;
* configuração;
* visualizações;
* relatório;
* casos;
* avaliação de fidelidade;
* avaliação de estabilidade;
* registro de validação;
* decisão técnica, quando aplicável.

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

---

## 29. Evidências e arquivos-fonte

| ID          | Evidência                                        | Versão | Localização | Responsável | Utilização |
| ----------- | ------------------------------------------------- | ------- | ------------- | ------------ | ------------ |
| EVD-EXP-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |         |               |              |              |

---

## 30. Rastreabilidade da execução

| Campo                       | Preenchimento                                     |
| --------------------------- | ------------------------------------------------- |
| Repositório                | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Commit ou tag               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Script ou notebook          | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Arquivo de configuração   | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Dataset e versão           | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Modelo e versão            | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Método e versão           | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Identificador da execução | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Ambiente                    | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Data de execução          | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

---

## 31. Relação com decisões técnicas

| ID da decisão | Título                                           | Relação com a explicabilidade |
| -------------- | ------------------------------------------------- | ------------------------------- |
| DTE-XXX        | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |                                 |

Quando uma escolha metodológica relevante ainda não estiver formalizada, registrar a necessidade de criar ou atualizar um Registro de Decisão Técnica.

---

## 32. Pendências

| ID      | Pendência                                        | Tipo | Prioridade | Responsável | Evidência esperada | Estado |
| ------- | ------------------------------------------------- | ---- | ---------- | ------------ | ------------------- | ------ |
| PEN-XXX | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |      |            |              |                     |        |

As pendências devem também ser registradas em:

```text
documentacao_projeto/registro_de_pendencias.md
```

---

## 33. Pontos para possível avaliação institucional

| ID           | Questão                                                                      | Motivo | Evidência necessária | Estado |
| ------------ | ----------------------------------------------------------------------------- | ------ | ---------------------- | ------ |
| INST-EXP-001 | [DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente] |        |                        |        |

Exemplos possíveis:

* explicação obrigatória para uso de alto impacto;
* impossibilidade de fornecer explicação adequada;
* risco de interpretação indevida;
* necessidade de restringir uso;
* necessidade de supervisão adicional;
* condicionante para piloto ou implantação.

A identificação do ponto não constitui decisão institucional.

---

## 34. Conclusão provisória

Selecionar a formulação aplicável e justificar:

```text
Há evidências iniciais de explicabilidade, mas a análise permanece parcial.

Há resultados de explicabilidade disponíveis, mas sua fidelidade ou utilidade ainda não foi validada.

Não foi identificada análise de explicabilidade suficiente; este documento funciona como plano de explicabilidade.

A análise existente não está alinhada ao público ou ao Contexto de Uso.

Não aplicável — justificativa obrigatória.
```

### Conclusão

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### Interpretação permitida

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

### Interpretação não permitida

Este relatório não permite afirmar, sem evidência adicional, que:

* o modelo é plenamente interpretável;
* a explicação é causal;
* a explicação é fiel;
* a explicação é clinicamente válida;
* usuários compreendem adequadamente a saída;
* a explicação reduz risco;
* a explicação é adequada para todos os públicos;
* o sistema está pronto para implantação.

---

## 35. Validação do relatório

### Equipe do projeto

A equipe confirma a correção factual dos métodos, resultados e limitações registrados.

| Campo            | Preenchimento |
| ---------------- | ------------- |
| Nome             |               |
| Papel            |               |
| Data             |               |
| Versão validada |               |
| Observações    |               |

### NIAR-Saúde

O NIAR-Saúde verifica a suficiência, a consistência e a rastreabilidade das evidências apresentadas.

| Campo         | Preenchimento |
| ------------- | ------------- |
| Nome          |               |
| Papel         |               |
| Data          |               |
| Observações |               |

A validação factual do relatório não constitui resultado formal de conformidade.

---

## 36. Histórico de versões

| Versão | Data | Responsável      | Alteração                     | Status                        |
| ------- | ---- | ----------------- | ------------------------------- | ----------------------------- |
| 0.1     |      | Equipe do projeto | Criação do relatório inicial | Em preenchimento pelo projeto |

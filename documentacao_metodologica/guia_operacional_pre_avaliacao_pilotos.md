# Guia Operacional de Pré-Avaliação dos Pilotos FIAR-Saúde

## 1. Objetivo

Este guia orienta a execução da pré-avaliação documental dos projetos piloto do FIAR-Saúde.

Seu objetivo é apoiar o NIAR-Saúde na organização das evidências, delimitação da unidade de avaliação, identificação de inconsistências e pendências e decisão sobre as condições para iniciar a avaliação por requisito.

Este guia não substitui os templates oficiais do processo.

---

## 2. Princípios operacionais

Durante a pré-avaliação documental:

- utilizar somente fontes verificadas no ciclo atual como evidência;
- não tratar memória, conversas anteriores ou versões históricas como evidência sem nova verificação;
- não presumir o conteúdo de um arquivo a partir de seu nome;
- não assumir que um arquivo existente no repositório constitui evidência verificada;
- não assumir que a existência de template ou diretório torna um artefato obrigatório;
- determinar primeiro qual evidência é necessária e somente depois qual artefato pode fornecê-la;
- distinguir informação ausente de divergência documental;
- não selecionar silenciosamente uma das versões quando houver informações conflitantes;
- realizar verificações internas pelo NIAR-Saúde antes de solicitar nova informação à equipe do projeto;
- registrar explicitamente se uma pendência impede ou não a continuidade do ciclo.

---

## 3. Documentos utilizados na pré-avaliação

Os principais registros utilizados nesta etapa são:

```text
documentacao_projeto/
├── formulario_entrada.md
├── identificacao_avaliacao.md
├── controle_artefatos.md
├── historico_validacao.md
└── registro_de_pendencias.md

avaliacao_niar/
├── pre_avaliacao_documental.md
└── registro_de_inconsistencias.md
````

Os artefatos técnicos do projeto devem ser analisados apenas quando necessários para responder às questões da pré-avaliação.

---

## 4. Sequência operacional

### Etapa 1 — Delimitar a unidade de avaliação

Confirmar:

* Tarefa de IA;
* Versão Avaliável;
* Contexto de Uso;
* Trilha de Execução.

Registrar a delimitação em:

```text
documentacao_projeto/identificacao_avaliacao.md
```

A avaliação por requisito não deve começar enquanto uma questão material impedir a identificação da unidade de avaliação.

---

### Etapa 2 — Inventariar os documentos e evidências disponíveis

Registrar em:

```text
documentacao_projeto/controle_artefatos.md
```

Para cada arquivo ou evidência, determinar:

* se foi efetivamente disponibilizado;
* sua versão;
* sua função declarada ou identificada;
* se foi verificado no ciclo atual;
* sua relação com a Versão Avaliável;
* se foi utilizado como evidência.

A presença de um arquivo no repositório não significa que ele tenha sido verificado ou que seja aplicável.

---

### Etapa 3 — Identificar as informações sustentadas pelas fontes

No arquivo:

```text
avaliacao_niar/pre_avaliacao_documental.md
```

registrar quais informações estão efetivamente sustentadas por cada fonte verificada.

Exemplos:

* finalidade da tarefa;
* datasets utilizados;
* função de cada dataset;
* população;
* período;
* divisão entre treino, validação e teste;
* entradas e saídas;
* versão do modelo;
* procedimentos de avaliação;
* métricas;
* resultados;
* limitações;
* responsabilidades documentadas.

Não preencher lacunas por inferência.

---

### Etapa 4 — Realizar verificações cruzadas

Comparar as fontes relevantes.

Verificar, quando aplicável:

* coerência da Tarefa de IA;
* uso dos datasets;
* versões;
* números de pacientes ou instâncias;
* períodos;
* separação entre conjuntos;
* sobreposição entre conjuntos;
* entradas e saídas;
* versão e configuração do modelo;
* métricas e resultados;
* contexto de uso;
* responsabilidades;
* decisões documentadas.

Os resultados podem ser registrados como:

* Consistente;
* Informação ausente;
* Requer esclarecimento;
* Divergência confirmada;
* Não aplicável.

Informação ausente não constitui, por si só, inconsistência.

---

## 5. Como tratar inconsistências

Uma inconsistência existe quando há uma divergência confirmada entre duas ou mais informações.

Registrar em:

```text
avaliacao_niar/registro_de_inconsistencias.md
```

A inconsistência deve preservar:

* fontes conflitantes;
* informações conflitantes;
* impacto;
* gravidade;
* estado;
* forma de resolução.

Não escolher uma versão como correta sem evidência suficiente.

Antes de solicitar esclarecimento à equipe, verificar se a questão pode ser resolvida por evidência documental adicional.

Uma inconsistência pode ser resolvida por nova evidência sem apagar seu registro histórico.

A resolução da dúvida não significa necessariamente que o documento que continha a informação incorreta já tenha sido corrigido. A correção documental pode permanecer registrada separadamente.

---

## 6. Como tratar pendências

Registrar em:

```text
documentacao_projeto/registro_de_pendencias.md
```

Uma pendência representa uma questão ainda não suficientemente resolvida.

Pode envolver:

* complementação documental;
* esclarecimento;
* confirmação factual;
* verificação pelo NIAR-Saúde;
* análise técnica adicional;
* decisão institucional.

Antes de abrir uma pendência por ausência de artefato, verificar:

1. qual informação ou evidência é realmente necessária;
2. por que ela é necessária;
3. se já existe evidência suficiente em outra fonte;
4. se há uma lacuna concreta;
5. somente então, qual artefato ou registro poderia suprir essa lacuna.

Uma inconsistência pode gerar uma pendência para seu tratamento, mas os dois registros não são equivalentes.

---

## 7. Verificação interna antes de contatar o projeto

Antes de solicitar informação ou evidência à equipe do projeto, o NIAR-Saúde deve verificar se a questão pode ser resolvida por:

* documentos já verificados;
* outras fontes disponíveis cuja análise seja justificada;
* registros administrativos;
* comparação entre artefatos;
* evidência complementar incorporada ao ciclo.

Somente após essas verificações devem ser encaminhadas perguntas específicas à equipe.

Evitar solicitações genéricas como:

```text
Enviar documentação faltante.
```

Preferir perguntas objetivas, por exemplo:

```text
Confirmar quem responde tecnicamente pela Versão Avaliável identificada neste ciclo.
```

---

## 8. Pendências impeditivas e não impeditivas

Toda pendência aberta deve ter seu impacto sobre a continuidade analisado.

### Impeditiva

A resolução é necessária para iniciar ou concluir determinada etapa.

Exemplo:

* não é possível identificar qual versão do modelo está sendo avaliada.

### Não impeditiva

A questão permanece aberta, mas não inviabiliza a etapa seguinte.

Exemplo:

* uma responsabilidade factual ainda precisa ser confirmada, mas a Tarefa de IA, a Versão Avaliável, os dados e o Contexto de Uso estão suficientemente delimitados para iniciar a avaliação técnica.

Pendências não impeditivas podem permanecer abertas em paralelo.

O registro deve indicar em qual etapa sua resolução se tornará necessária.

---

## 9. Cancelamento por reenquadramento metodológico

Uma pendência pode ser cancelada quando a revisão do NIAR-Saúde demonstrar que ela foi aberta com base em uma premissa inadequada.

Exemplos:

* considerar obrigatório um artefato apenas porque existe um template;
* presumir necessária uma análise antes de verificar a aplicabilidade do requisito;
* tratar como pendência a simples existência de um arquivo ainda não analisado.

Nesse caso:

* não apagar o ID;
* preservar a questão original;
* registrar a justificativa;
* marcar a pendência como cancelada por reenquadramento.

---

## 10. Incorporação de evidência complementar

Fontes externas ou complementares podem ser incorporadas ao ciclo quando forem necessárias para responder a uma questão concreta.

Exemplos:

* artigo científico;
* material suplementar;
* documentação experimental;
* registro administrativo verificável.

Quando incorporada, a evidência deve ser registrada em:

```text
documentacao_projeto/controle_artefatos.md
```

e sua utilização deve aparecer na pré-avaliação, pendência ou inconsistência relacionada.

A incorporação de uma fonte complementar não torna esse tipo de documento obrigatório para os demais projetos.

---

## 11. Conclusão da pré-avaliação

Antes de iniciar a avaliação por requisito, verificar se:

* a Tarefa de IA está suficientemente delimitada;
* a Versão Avaliável está identificada;
* o Contexto de Uso está explícito;
* a Trilha de Execução está definida;
* o inventário documental necessário à etapa foi concluído;
* as verificações cruzadas necessárias foram realizadas;
* as inconsistências identificadas foram registradas;
* as pendências abertas foram consolidadas;
* o impacto das pendências sobre a continuidade foi determinado;
* as verificações internas do NIAR-Saúde foram concluídas;
* as questões que dependem efetivamente da equipe do projeto foram identificadas.

A existência de pendências abertas não impede automaticamente o início da avaliação por requisito.

O NIAR-Saúde deve registrar explicitamente se existem condições para continuidade.

---

## 12. Avaliação por requisito

Quando a pré-avaliação permitir continuidade, iniciar a avaliação por requisito.

Para cada requisito:

1. determinar a aplicabilidade;
2. registrar `Aplicável` ou `Não aplicável`;
3. justificar a decisão;
4. identificar as evidências pertinentes;
5. analisar suficiência, consistência, rastreabilidade e contextualização;
6. somente então atribuir o resultado previsto pela metodologia.

A existência de um artefato não substitui a análise de aplicabilidade e suficiência das evidências.

---

## 13. Checklist operacional

Antes de encerrar a pré-avaliação:

* [ ] Tarefa de IA delimitada;
* [ ] Versão Avaliável delimitada;
* [ ] Contexto de Uso delimitado;
* [ ] Trilha de Execução definida;
* [ ] documentos necessários inventariados;
* [ ] evidências verificadas no ciclo identificadas;
* [ ] verificações cruzadas concluídas;
* [ ] inconsistências registradas;
* [ ] pendências consolidadas;
* [ ] pendências classificadas quanto ao impacto na continuidade;
* [ ] verificações internas do NIAR-Saúde concluídas;
* [ ] questões para a equipe do projeto identificadas;
* [ ] decisão sobre início da avaliação por requisito registrada.

---

## 14. Controle de versão

Ao concluir um bloco metodológico relevante, realizar commit antes de iniciar a etapa seguinte.

Exemplos de marcos:

* conclusão da delimitação da unidade de avaliação;
* conclusão da pré-avaliação documental;
* resolução de conjunto relevante de pendências ou inconsistências;
* início da avaliação por requisito.

O histórico do Git complementa, mas não substitui:

```text
historico_validacao.md
```

---

## 15. Registros relacionados

Utilizar em conjunto:

```text
documentacao_projeto/identificacao_avaliacao.md
documentacao_projeto/controle_artefatos.md
documentacao_projeto/historico_validacao.md
documentacao_projeto/registro_de_pendencias.md

avaliacao_niar/pre_avaliacao_documental.md
avaliacao_niar/registro_de_inconsistencias.md

```

Este guia deve ser utilizado como roteiro operacional. As regras e definições formais permanecem nos documentos metodológicos e templates correspondentes.




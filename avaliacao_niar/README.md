# Avaliação NIAR-Saúde

Esta pasta reúne os instrumentos e registros produzidos pelo NIAR-Saúde durante a pré-avaliação, a avaliação técnica e a consolidação de um ciclo FIAR-Saúde.

A avaliação segue a sequência metodológica:

1. pré-avaliação documental;
2. registro e tratamento de pendências e inconsistências;
3. avaliação por requisito;
4. consolidação por dimensão;
5. resultado formal da avaliação técnica.

A avaliação do NIAR-Saúde é independente da equipe responsável pelo desenvolvimento, mas pode envolver solicitações de esclarecimento, complementação documental e fornecimento de novas evidências.

A existência ou ausência de um artefato não determina automaticamente conformidade.

---

## Estrutura

### `pre_avaliacao_documental.md`

Registro da pré-avaliação documental do ciclo.

Deve registrar, quando aplicável:

- identificação ou confirmação da Tarefa de IA;
- Versão Avaliável;
- Contexto de Uso;
- Trilha de Execução;
- inventário dos artefatos disponíveis;
- verificações cruzadas;
- informações ausentes;
- ambiguidades;
- divergências confirmadas;
- pendências identificadas;
- decisão sobre a possibilidade de iniciar a avaliação requisito a requisito.

A execução desta etapa deve utilizar, em conjunto:

- a documentação metodológica vigente do FIAR-Saúde;
- `documentacao_metodologica/guia_operacional_pre_avaliacao_pilotos.md`.

### `registro_de_inconsistencias.md`

Registro apenas de divergências efetivamente confirmadas entre evidências.

Ausência de informação, dúvida interpretativa ou evidência ainda não fornecida não devem ser registradas automaticamente como inconsistência.

### `perguntas_para_entrevista_inicial.md`

Perguntas utilizadas quando esclarecimentos adicionais forem necessários.

Entrevistas são mecanismos complementares de esclarecimento e não substituem evidências formais quando estas forem aplicáveis e necessárias ao requisito analisado.

### `avaliacao_por_requisito/`

Contém os registros detalhados da avaliação individual dos requisitos das sete dimensões do FIAR-Saúde.

Cada requisito deve seguir a sequência:

**aplicabilidade → justificativa de aplicabilidade → evidências pertinentes → evidências disponíveis → mecanismos de verificação utilizados → resultado da verificação → análise de suficiência, consistência, rastreabilidade e contextualização → achado, limitações, pendências e inconsistências, quando aplicáveis → sinal de governança, quando aplicável → referências de rastreabilidade.**

A interpretação operacional dos requisitos deve utilizar:

`documentacao_metodologica/guia_requisitos_avaliacao.md`

A aplicabilidade deve ser determinada antes da análise das evidências.

A ausência de uma evidência ou artefato não constitui automaticamente pendência ou Não Conformidade.

### `avaliacao_por_dimensao/`

Contém a consolidação das avaliações dos requisitos de cada dimensão:

- Governança;
- Segurança;
- Privacidade;
- Responsabilização;
- Rastreabilidade;
- Justiça;
- Transparência.

A consolidação por dimensão:

- preserva a rastreabilidade até as avaliações individuais dos requisitos;
- considera suficiência, consistência, rastreabilidade e contextualização de forma transversal;
- não utiliza soma, média, percentual, contagem ou regra de maioria;
- não atribui nível de maturidade.

### `avaliacao_formal/`

Contém o resultado formal da avaliação técnica para a combinação:

**Tarefa de IA + Versão Avaliável + Contexto de Uso.**

O resultado consolida:

- as avaliações por requisito;
- as consolidações por dimensão;
- pendências e inconsistências materialmente relevantes;
- sinais de governança;
- necessidade de escalonamento, quando aplicável.

Os estados de resultado são:

- **Conforme**;
- **Pendente**;
- **Não Conforme**.

A existência de uma pendência registrada não determina automaticamente o resultado **Pendente**. Deve-se avaliar se a questão é material para a conclusão sobre o atendimento dos requisitos aplicáveis.

A avaliação formal não atribui maturidade ao projeto e não substitui eventual decisão institucional.

---

## Relação entre os níveis da avaliação

```text
pré-avaliação documental
        ↓
avaliação por requisito
        ↓
consolidação por dimensão
        ↓
resultado formal da avaliação técnica
        ↓
decisão institucional, quando 

```

Cada nível consolida o anterior sem substituir seus registros detalhados.
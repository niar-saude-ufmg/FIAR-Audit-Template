# Avaliação NIAR-Saúde

Esta pasta reúne os registros produzidos pelo NIAR-Saúde durante a avaliação técnica de uma Tarefa de IA.

A avaliação segue a sequência metodológica definida no FIAR-Saúde:

1. pré-avaliação documental;
2. identificação e tratamento de pendências;
3. avaliação por requisito;
4. consolidação por dimensão;
5. consolidação da avaliação técnica.

A avaliação do NIAR-Saúde é independente da equipe responsável pelo desenvolvimento, mas pode envolver solicitações de esclarecimento, complementação documental e fornecimento de novas evidências.

A existência ou ausência de um artefato não determina automaticamente conformidade.

---

## Estrutura

### `pre_avaliacao_documental.md`

Registro da pré-avaliação documental do ciclo.

Deve conter:

- confirmação da Tarefa de IA;
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

O procedimento metodológico correspondente está definido no repositório FIAR-Saúde em:

`docs/protocolo_pre_avaliacao_documental.md`

### `registro_de_inconsistencias.md`

Registro apenas de divergências efetivamente confirmadas entre evidências.

Ausência de informação, dúvida interpretativa ou evidência ainda não fornecida não devem ser registradas automaticamente como inconsistência.

### `perguntas_para_entrevista_inicial.md`

Perguntas utilizadas quando esclarecimentos adicionais forem necessários.

Entrevistas são mecanismos complementares e não substituem evidências que devam existir formalmente.

### `avaliacao_por_requisito/`

Contém os registros detalhados da avaliação de cada requisito aplicável das sete dimensões do FIAR-Saúde.

Cada requisito deve seguir a sequência:

**aplicabilidade → evidências esperadas → evidências disponíveis → mecanismo de verificação → resultado da verificação → análise transversal → achado ou pendência → sinal de governança, quando aplicável.**

### `avaliacao_por_dimensao/`

Contém a consolidação dos requisitos de cada dimensão:

- Governança;
- Segurança;
- Privacidade;
- Responsabilização;
- Rastreabilidade;
- Justiça;
- Transparência.

A consolidação da dimensão não utiliza soma, média, percentual ou contagem de requisitos.

### `avaliacao_formal/`

Contém registros formais produzidos após a análise técnica.

Esta pasta não substitui a consolidação global da avaliação e não deve duplicar registros mantidos em `consolidacao_avaliacao/`.

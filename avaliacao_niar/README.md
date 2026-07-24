# Avaliação pelo NIAR-Saúde

Esta pasta reúne os instrumentos, registros de trabalho e resultados produzidos
pelo NIAR-Saúde durante a preparação e a execução da avaliação de uma Tarefa
de IA em uma Versão Avaliável e um Contexto de Uso específicos.

A documentação metodológica oficial do FIAR-Saúde está disponível em:

<https://github.com/niar-saude-ufmg/FIAR-Saude>

Em caso de divergência entre este template e a documentação oficial vigente,
prevalece a documentação oficial do FIAR-Saúde.

---

## Finalidade da pasta

Os documentos desta pasta apoiam:

- a inspeção documental inicial;
- a verificação preliminar de suficiência;
- a análise de consistência entre artefatos;
- a verificação de rastreabilidade;
- a preparação de entrevistas;
- o registro de inconsistências;
- a avaliação das dimensões do FIAR-Saúde;
- a consolidação do resultado formal, quando aplicável.

A pasta contém documentos de uso exclusivo do NIAR-Saúde e documentos que
podem ser compartilhados com a equipe do projeto para esclarecimento factual.

A validação factual pela equipe do projeto não substitui a avaliação técnica do
NIAR-Saúde.

---

## Estrutura da pasta

```text
avaliacao_niar/
├── README.md
├── pre_avaliacao_documental.md
├── perguntas_para_entrevista_inicial.md
├── registro_de_inconsistencias.md
├── avaliacao_por_dimensao/
│   ├── README.md
│   └── template_avaliacao_dimensao.md
└── avaliacao_formal/
    ├── README.md
    └── resultado_avaliacao.md
````

---

## Instrumentos preparatórios

### `pre_avaliacao_documental.md`

Organiza a inspeção inicial dos artefatos recebidos.

Pode registrar:

* artefatos disponíveis;
* suficiência documental preliminar;
* consistência entre Data Card e Model Card;
* rastreabilidade das versões;
* responsáveis identificados;
* limitações;
* riscos;
* evidências faltantes;
* perguntas;
* próximos passos.

A pré-avaliação não atribui resultado formal de conformidade.

### `perguntas_para_entrevista_inicial.md`

Reúne perguntas específicas derivadas das lacunas, inconsistências e limitações
identificadas nos documentos.

Não deve funcionar como questionário genérico.

Perguntas cuja resposta já esteja claramente documentada não devem ser repetidas.

### `registro_de_inconsistencias.md`

Registra divergências entre:

* documentos;
* versões;
* resultados;
* descrições técnicas;
* responsáveis;
* Contextos de Uso;
* informações fornecidas em momentos distintos.

Uma inconsistência não deve ser resolvida silenciosamente.

---

## Avaliação por dimensão

A pasta `avaliacao_por_dimensao/` reúne as análises realizadas pelo NIAR-Saúde
para as sete dimensões do FIAR-Saúde:

* Justiça;
* Transparência;
* Responsabilização;
* Privacidade;
* Segurança;
* Governança;
* Rastreabilidade.

Cada análise deve indicar:

* requisito ou questão avaliada;
* evidência esperada;
* evidência apresentada;
* verificação realizada;
* resultado técnico;
* limitação;
* pendência;
* eventual sinal de governança.

A existência de um artefato não determina automaticamente que a evidência seja
suficiente.

---

## Avaliação formal

A pasta `avaliacao_formal/` reúne os documentos associados ao resultado formal
da avaliação, quando esta etapa tiver sido autorizada e executada.

A avaliação formal deve estar associada explicitamente a:

* uma Tarefa de IA;
* uma Versão Avaliável;
* um Contexto de Uso;
* uma trilha;
* uma data de referência;
* um conjunto identificado de evidências.

Os possíveis resultados formais devem seguir a documentação oficial vigente do
FIAR-Saúde.

A avaliação formal não constitui:

* certificação de que o sistema seja justo;
* certificação de segurança;
* validação clínica;
* aprovação regulatória;
* autorização automática de implantação;
* avaliação de maturidade do projeto.

A conformidade é pontual e pertence à combinação entre Tarefa de IA, Versão
Avaliável e Contexto de Uso.

A maturidade é longitudinal e pertence ao projeto.

---

## Independência da avaliação

Os documentos que contêm análise, julgamento ou conclusão do NIAR-Saúde não
devem ser alterados diretamente pela equipe do projeto.

Quando houver necessidade de validação factual:

1. o NIAR-Saúde identifica a questão;
2. a equipe do projeto apresenta resposta e fonte;
3. o NIAR-Saúde verifica a resposta;
4. a alteração é incorporada de forma rastreável, quando sustentada;
5. divergências não resolvidas permanecem registradas.

O projeto pode:

* corrigir informações factuais;
* complementar dados;
* fornecer evidências;
* esclarecer decisões técnicas;
* atualizar seus próprios artefatos.

O projeto não deve substituir silenciosamente:

* conclusões do NIAR-Saúde;
* enquadramentos metodológicos;
* registros de inconsistência;
* sinais de governança;
* resultados formais de avaliação.

---

## Marcadores

Quando necessário, utilizar:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]

[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]

[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

---

## Rastreabilidade

Toda conclusão do NIAR-Saúde deve indicar, quando aplicável:

* artefato utilizado;
* versão;
* seção;
* data;
* responsável;
* execução relacionada;
* evidência complementar;
* limitação de acesso;
* verificação realizada.

Não deve haver conclusão sem evidência correspondente.

---

## Relação com a decisão institucional

A avaliação técnica pode identificar situações que exijam tratamento fora do
escopo técnico do NIAR-Saúde, como:

* risco residual significativo;
* necessidade de aceite de risco;
* definição de condicionantes;
* restrição de uso;
* conflito institucional;
* ausência de responsável;
* decisão sobre continuidade, suspensão ou implantação.

Nesses casos, o NIAR-Saúde registra o ponto e recomenda o encaminhamento à
instância institucional competente.

O registro de avaliação técnica não substitui o Registro de Decisão Institucional.



# Artefatos do Projeto

Esta pasta reúne os artefatos técnicos, documentais e operacionais produzidos e mantidos pela equipe do projeto ao longo do ciclo FIAR-Saúde.

Os artefatos devem estar vinculados, sempre que aplicável, a:

- uma Tarefa de IA;
- uma Versão Avaliável;
- um Contexto de Uso;
- uma data de referência;
- uma pessoa ou equipe responsável;
- uma fonte técnica ou execução correspondente.

A documentação metodológica oficial do FIAR-Saúde está disponível em:

[https://github.com/niar-saude-ufmg/FIAR-Saude](https://github.com/niar-saude-ufmg/FIAR-Saude)

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

---

## 1. Finalidade da pasta

Os arquivos desta pasta constituem entradas do pipeline de evidências do FIAR-Saúde.

Eles permitem registrar, de forma rastreável:

- origem, composição e limitações dos dados;
- características, usos e limitações dos modelos;
- resultados técnicos;
- análises de justiça;
- análises de explicabilidade;
- decisões técnicas;
- aspectos de privacidade e proteção de dados;
- riscos e mitigações;
- resultados consolidados das dimensões de IAR;
- evidências operacionais, quando aplicáveis.

A existência de um arquivo, por si só, não demonstra que:

- a evidência esteja completa;
- a análise seja adequada;
- o resultado seja válido;
- o risco esteja mitigado;
- a tarefa esteja conforme;
- o sistema esteja autorizado para implantação.

O NIAR-Saúde avalia a suficiência, a consistência e a rastreabilidade dos artefatos apresentados.

---

## 2. Responsabilidade pelos artefatos

A equipe do projeto é responsável por:

- produzir os artefatos técnicos;
- assegurar a correção factual das informações;
- registrar métodos, resultados e limitações;
- manter o versionamento;
- indicar responsáveis;
- atualizar os artefatos após mudanças relevantes;
- fornecer as evidências necessárias para verificação;
- corrigir inconsistências identificadas.

O NIAR-Saúde é responsável por:

- orientar a organização das evidências;
- verificar presença, suficiência, consistência e rastreabilidade;
- identificar lacunas e inconsistências;
- solicitar complementações;
- avaliar a relação entre os artefatos e as dimensões do FIAR-Saúde;
- registrar conclusões e sinais de governança.

O NIAR-Saúde não deve ser apresentado como autor das análises técnicas realizadas pela equipe do projeto.

---

## 3. Estrutura da pasta

```text
artefatos_projeto/
├── README.md
├── data_cards/
├── model_cards/
├── fairness_reports/
├── explainability_reports/
├── decision_records/
├── consolidated_iar_report/
├── compliance/
│   └── ripd/
└── operational_artifacts/
    ├── monitoring/
    ├── incidents/
    ├── version_history/
    └── periodic_review/
```


---

## 4. Artefatos de desenvolvimento

Os artefatos de desenvolvimento podem ser aplicáveis tanto à Trilha Experimental quanto à Trilha Produção.

### `data_cards/`

Contém a documentação dos datasets utilizados pela tarefa.

Os Data Cards devem registrar, quando aplicável:

* nome e versão do dataset;
* origem;
* finalidade;
* população;
* unidade de análise;
* período;
* abrangência;
* processo de coleta;
* critérios de inclusão e exclusão;
* atributos;
* transformações;
* divisão entre treino, validação e teste;
* limitações;
* riscos;
* aspectos de privacidade;
* responsáveis;
* condições de acesso e uso.

Quando uma tarefa utiliza mais de um dataset, cada dataset relevante deve ser identificado separadamente.

### `model_cards/`

Contém a documentação dos modelos utilizados pela tarefa.

Os Model Cards devem registrar, quando aplicável:

* nome e versão do modelo;
* arquitetura;
* tarefa computacional;
* entradas e saídas;
* dados utilizados;
* procedimentos de treinamento;
* procedimentos de inferência;
* métricas;
* resultados;
* usos pretendidos;
* usos inadequados;
* limitações;
* riscos;
* responsáveis;
* código e pesos relacionados;
* condições de implantação.

Um Model Card não substitui o registro da Tarefa de IA ou do Contexto de Uso.

O mesmo modelo pode participar de mais de uma Tarefa de IA.

### `fairness_reports/`

Contém os relatórios de justiça.

Esses relatórios devem distinguir claramente:

* informações já existentes;
* grupos ou estratos avaliados;
* justificativa dos grupos;
* métricas utilizadas;
* resultados disponíveis;
* disparidades identificadas;
* mitigações realizadas;
* riscos residuais;
* limitações;
* análises ainda necessárias.

Métricas globais não devem ser usadas como conclusão sobre justiça.

A ausência de análise por grupos não permite afirmar ausência de disparidade.

Quando ainda não houver análise suficiente, o arquivo deve funcionar como plano de avaliação de justiça.

### `explainability_reports/`

Contém os relatórios de explicabilidade e interpretação.

Esses relatórios devem registrar:

* finalidade da explicabilidade;
* público-alvo;
* método utilizado;
* justificativa;
* resultados globais;
* resultados locais;
* interpretação permitida;
* limitações;
* riscos de interpretação;
* relação com o Contexto de Uso;
* análises adicionais necessárias.

Importância de variável não deve ser tratada como causalidade.

Não devem ser inventados resultados de SHAP, LIME, mapas de ativação ou outros métodos.

Quando não houver análise suficiente, o arquivo deve funcionar como plano de explicabilidade.

### `decision_records/`

Contém os Registros de Decisão Técnica, identificados preferencialmente pelo prefixo:

```text
DTE
```

Exemplo:

```text
DTE-001-caracterizacao-inicial-da-tarefa.md
```

Os registros devem documentar decisões técnicas efetivamente tomadas e sustentadas por evidências.

Exemplos:

* escolha de arquitetura;
* escolha de dataset;
* estratégia de divisão dos dados;
* função de perda;
* definição de thresholds;
* seleção de métricas;
* procedimento de pré-processamento;
* exclusão de população;
* escolha de método de explicabilidade;
* estratégia de mitigação.

Uma descrição técnica não deve ser convertida automaticamente em decisão formal quando não houver evidência de que uma escolha tenha sido deliberada.

Os Registros de Decisão Técnica não devem ser confundidos com Registros de Decisão Institucional.

Decisões institucionais, como aceite de risco, definição de condicionantes ou restrições de uso, devem ser armazenadas separadamente.

### `relatorio_consolidado_iar/`

Contém relatórios que sintetizam o estado das evidências e análises das dimensões do FIAR-Saúde.

O relatório consolidado:

* não substitui os artefatos originais;
* não deve reproduzir integralmente Data Cards ou Model Cards;
* deve indicar as fontes utilizadas;
* deve registrar evidências, lacunas, limitações e análises pendentes;
* não deve atribuir conformidade sem avaliação formal do NIAR-Saúde.

Para cada dimensão, podem ser utilizadas as classificações descritivas:

* `Evidência disponível`;
* `Evidência parcial`;
* `Evidência não identificada`;
* `Não aplicável — requer justificativa`.

Essas classificações não equivalem a resultado de conformidade.

### `compliance/ripd/`

Contém documentos relacionados à privacidade e à proteção de dados, incluindo o Relatório de Impacto à Proteção de Dados Pessoais, quando aplicável.

A existência ou necessidade de RIPD depende do tratamento de dados, das responsabilidades institucionais e da avaliação da área competente.

O projeto não deve declarar que o RIPD não se aplica sem justificativa.

---

## 5. Artefatos operacionais

A pasta `operational_artifacts/` reúne evidências relacionadas à operação ativa da tarefa.

Esses artefatos são especialmente relevantes para tarefas na Trilha Produção.

### `monitoring/`

Pode conter:

* relatórios de monitoramento;
* métricas operacionais;
* avaliação de drift;
* desempenho por período;
* desempenho por grupo;
* disponibilidade;
* alertas;
* acompanhamento de thresholds;
* registros de revisão.

### `incidents/`

Pode conter:

* registros de incidentes;
* data e contexto;
* impacto;
* causa;
* pessoas ou áreas envolvidas;
* resposta;
* ação corretiva;
* prevenção de recorrência;
* necessidade de escalonamento.

### `version_history/`

Pode conter:

* histórico de versões dos dados;
* histórico de versões dos modelos;
* histórico do código;
* mudanças de configuração;
* implantações;
* reimplantações;
* rollback;
* vínculo entre versão e avaliação.

### `periodic_review/`

Pode conter:

* revisões periódicas;
* atas;
* reavaliações;
* decisões sobre continuidade;
* atualização de riscos;
* atualização de condicionantes;
* revisão de escopo;
* revisão de políticas;
* planejamento do próximo ciclo.

Artefatos operacionais não devem ser preenchidos ficticiamente em tarefas ainda não implantadas.

Quando não se aplicarem ao estágio atual, registrar:

```text
NÃO SE APLICA NESTE ESTÁGIO — tarefa sem operação ativa.
```

---

## 6. Vinculação à Versão Avaliável

Cada artefato deve indicar, quando aplicável:

| Campo                | Conteúdo esperado                                  |
| -------------------- | --------------------------------------------------- |
| Projeto              | Nome do projeto                                     |
| Tarefa de IA         | Tarefa à qual o artefato se refere                 |
| Versão Avaliável   | Identificador da versão avaliada                   |
| Contexto de Uso      | Contexto considerado                                |
| Versão do documento | Versão do próprio artefato                        |
| Data de referência  | Data das informações                              |
| Responsável         | Pessoa ou equipe responsável                       |
| Fontes               | Dados, código, execução ou documento relacionado |
| Estado               | Rascunho, em validação, validado ou substituído  |

Quando o artefato não puder ser associado de forma suficiente à Versão Avaliável, registrar a limitação em:

```text
documentacao_projeto/registro_de_pendencias.md
```

---

## 7. Cabeçalho recomendado

Os documentos podem utilizar o seguinte cabeçalho:

```markdown
---
documento:
versao_documento:
status:
projeto:
tarefa:
versao_avaliavel:
contexto_de_uso:
elaborado_por:
responsavel_tecnico:
data_de_referencia:
ultima_atualizacao:
---
```

O uso do cabeçalho não substitui o histórico de versões.

---

## 8. Estados dos artefatos

Os artefatos podem utilizar os seguintes estados:

* `Rascunho`
* `Em preenchimento pelo projeto`
* `Minuta para validação`
* `Em revisão`
* `Validado factualmente pelo projeto`
* `Em avaliação pelo NIAR`
* `Requer atualização`
* `Substituído`
* `Arquivado`

Esses estados não equivalem a resultado de conformidade.

---

## 9. Marcadores de lacunas

Quando a informação não estiver disponível:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]
```

Quando a conclusão depender de análise não realizada:

```text
[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]
```

Quando houver divergência:

```text
[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]
```

Quando o enquadramento depender do NIAR-Saúde:

```text
[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]
```

Quando houver necessidade de deliberação institucional:

```text
[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

---

## 10. Evidências e fontes

As afirmações técnicas devem ser vinculadas, sempre que possível, a:

* dataset;
* versão;
* arquivo;
* tabela;
* figura;
* relatório;
* repositório;
* commit;
* tag;
* configuração;
* log;
* execução;
* artigo;
* decisão técnica;
* responsável que confirmou a informação.

Evitar referências vagas como:

```text
Segundo os experimentos.
```

Preferir:

```text
Resultado obtido na execução RUN-2026-001, associada ao commit abc123,
à configuração config_v1.yaml e ao dataset CODE-II v1.0.
```

---

## 11. Atualização dos artefatos

Os artefatos devem ser atualizados quando ocorrer mudança relevante em:

* modelo;
* dados;
* arquitetura;
* variáveis;
* população;
* escopo;
* Contexto de Uso;
* procedimento de treinamento;
* procedimento de inferência;
* thresholds;
* métricas;
* integração;
* responsabilidades;
* riscos;
* regulação;
* operação;
* monitoramento.

A atualização deve indicar:

* o que mudou;
* por que mudou;
* quem realizou a mudança;
* qual versão anterior foi substituída;
* quais evidências foram atualizadas;
* se a mudança pode gerar uma nova Versão Avaliável.

A definição de uma nova Versão Avaliável deve seguir a documentação oficial vigente do FIAR-Saúde.

---

## 12. Relação com a avaliação pelo NIAR-Saúde

O NIAR-Saúde pode:

* solicitar complementações;
* identificar inconsistências;
* pedir evidências adicionais;
* verificar correspondência entre documentos;
* registrar limitações;
* solicitar nova análise;
* avaliar suficiência;
* recomendar revisão;
* identificar sinais de governança.

O NIAR-Saúde não deve alterar silenciosamente resultados, métodos ou decisões técnicas do projeto.

Quando houver necessidade de correção, o projeto deve atualizar o artefato e preservar o histórico.

---

## 13. Segurança e confidencialidade

Antes de adicionar um artefato, verificar:

* autorização para armazenamento;
* presença de dados pessoais ou sensíveis;
* presença de identificadores diretos;
* informações protegidas por contrato;
* propriedade intelectual;
* credenciais;
* tokens;
* chaves;
* segredos;
* risco de exposição pelo histórico do Git.

Não armazenar no repositório:

* dados brutos sensíveis;
* credenciais;
* chaves privadas;
* segredos de infraestrutura;
* informações cuja inclusão não tenha sido autorizada.

Quando a evidência não puder ser armazenada diretamente, registrar:

* existência;
* responsável;
* localização controlada;
* forma de acesso;
* versão;
* procedimento de verificação pelo NIAR-Saúde.

---

## 14. Não objetivos

Os artefatos desta pasta não devem ser usados isoladamente para afirmar que:

* o sistema é justo;
* o sistema é seguro;
* o sistema é ético;
* o sistema é clinicamente válido;
* o sistema está conforme;
* o projeto possui determinado nível de maturidade;
* o sistema está autorizado para implantação.

Essas conclusões dependem dos processos de avaliação, governança e decisão aplicáveis.


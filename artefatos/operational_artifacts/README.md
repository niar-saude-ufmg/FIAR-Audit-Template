# Artefatos Operacionais

Esta pasta reúne evidências produzidas durante pilotos operacionais ou durante a operação ativa de uma Tarefa de IA.

Os artefatos operacionais devem estar vinculados, quando aplicável, a:

- uma Tarefa de IA;
- uma Versão Avaliável;
- um Contexto de Uso;
- uma implantação ou ambiente operacional identificado;
- um período de referência;
- uma pessoa ou equipe responsável.

A documentação metodológica oficial do FIAR-Saúde está disponível em:

[https://github.com/niar-saude-ufmg/FIAR-Saude](https://github.com/niar-saude-ufmg/FIAR-Saude)

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

Os diretórios deste conjunto fazem parte da estrutura canônica do `FIAR-Audit-Template` e representam classes de registros operacionais previstas pelo FIAR-Saúde.

A presença de um diretório, README ou template não implica que a evidência correspondente seja aplicável ou obrigatória em toda avaliação.

A aplicabilidade deve ser determinada no contexto de cada ciclo, considerando a Tarefa de IA, a Versão Avaliável, o Contexto de Uso, a Trilha de Execução e o requisito analisado.

Artefatos operacionais são particularmente relevantes para tarefas na Trilha Produção e para evidenciar recorrência, rastreabilidade e institucionalização das práticas ao longo do tempo. Um template não preenchido não constitui evidência e sua simples existência não deve gerar automaticamente uma pendência.

---

## 1. Finalidade

Os artefatos desta pasta permitem registrar evidências relacionadas a:

- desempenho em ambiente operacional;
- comportamento ao longo do tempo;
- mudanças na distribuição dos dados;
- disponibilidade e funcionamento do serviço;
- intervenções humanas;
- incidentes;
- atualizações de versão;
- revisões periódicas;
- medidas corretivas;
- necessidade de nova avaliação;
- sinais de governança identificados durante a operação.

A existência desses artefatos não demonstra, isoladamente, que:

- a operação seja segura;
- o desempenho permaneça adequado;
- os riscos estejam controlados;
- a tarefa esteja conforme;
- a implantação esteja autorizada;
- o risco residual tenha sido aceito.

---

## 2. Aplicabilidade

Os artefatos operacionais são especialmente relevantes para tarefas:

- em piloto operacional;
- integradas a sistemas institucionais;
- utilizadas por profissionais;
- capazes de influenciar decisões reais;
- submetidas a monitoramento contínuo;
- enquadradas na Trilha Produção.

Para tarefas exclusivamente experimentais ou sem operação ativa, a ausência de registros operacionais não constitui, por si só, pendência. A não aplicabilidade deve ser registrada no processo de avaliação quando relevante para o requisito analisado, sem necessidade de preencher ficticiamente os templates desta pasta.

Não criar dados fictícios de monitoramento, incidentes ou revisão apenas para preencher a estrutura.

Mesmo sem operação ativa, podem existir evidências de planejamento operacional, riscos previstos, critérios para futura implantação, gatilhos de monitoramento ou responsabilidades futuras. Esses registros devem ser produzidos quando forem aplicáveis ao estágio, ao contexto e aos requisitos analisados.

---

## 3. Estrutura

```text
operational_artifacts/
├── README.md
├── monitoring/
│   ├── README.md
│   └── monitoring_report_template.md
├── incidents/
│   ├── README.md
│   └── incident_record_template.md
├── version_history/
│   ├── README.md
│   └── version_change_record_template.md
└── periodic_review/
    ├── README.md
    └── periodic_review_template.md
```

---

## 4. `monitoring/`

Reúne evidências de acompanhamento da tarefa durante piloto ou operação.

Pode conter:

* métricas de desempenho;
* métricas por grupo;
* métricas por classe;
* volume de uso;
* disponibilidade;
* latência;
* falhas;
* abstinência;
* intervenções humanas;
* discordâncias;
* calibração;
* drift;
* mudança de prevalência;
* alertas;
* violações de limites;
* registros de revisão.

Quando aplicável, os relatórios de monitoramento devem indicar:

* período;
* versão;
* população;
* dados analisados;
* métricas;
* thresholds;
* baseline;
* limites esperados;
* responsáveis;
* eventos relevantes;
* medidas adotadas.

---

## 5. `incidents/`

Reúne registros de eventos que tenham causado ou possam causar:

* dano;
* comportamento inesperado;
* indisponibilidade;
* exposição indevida de dados;
* decisão incorreta;
* uso fora do escopo;
* falha de integração;
* falha de supervisão;
* violação de segurança;
* degradação relevante;
* descumprimento de condicionante.

Quando houver incidente registrado, o registro deve preservar, conforme aplicável:

* data e horário;
* tarefa e versão;
* ambiente;
* descrição;
* forma de detecção;
* pessoas ou grupos afetados;
* impacto;
* resposta imediata;
* investigação;
* causa identificada;
* ação corretiva;
* ação preventiva;
* responsáveis;
* necessidade de escalonamento;
* necessidade de nova avaliação.

Um incidente não deve ser apagado após seu encerramento.

---

## 6. `version_history/`

Reúne registros de mudanças relacionadas à operação da tarefa.

Podem ser registradas alterações em:

* modelo;
* pesos;
* dados;
* código;
* arquitetura;
* variáveis;
* thresholds;
* configuração;
* interface;
* integração;
* infraestrutura;
* população;
* escopo;
* Contexto de Uso;
* procedimento de supervisão;
* monitoramento;
* responsáveis.

Cada mudança registrada deve indicar, quando aplicável:

* versão anterior;
* versão nova;
* motivo;
* responsável;
* data;
* evidência;
* impacto esperado;
* testes realizados;
* aprovação técnica;
* possibilidade de nova Versão Avaliável;
* necessidade de reavaliação pelo NIAR-Saúde.

---

## 7. `periodic_review/`

Reúne revisões realizadas em intervalos definidos ou após gatilhos relevantes.

A revisão periódica pode considerar:

* desempenho;
* justiça;
* transparência;
* responsabilização;
* privacidade;
* segurança;
* governança;
* rastreabilidade;
* incidentes;
* drift;
* mudanças de contexto;
* reclamações;
* intervenções humanas;
* atualização regulatória;
* adequação dos controles;
* necessidade de continuidade, restrição ou suspensão.

A revisão periódica não substitui uma nova avaliação quando houver mudança relevante.

---

## 8. Vinculação à operação

Cada artefato operacional deve indicar, quando aplicável:

| Campo                 | Conteúdo esperado                              |
| --------------------- | ----------------------------------------------- |
| Projeto               | Nome do projeto                                 |
| Tarefa de IA          | Tarefa monitorada                               |
| Versão Avaliável    | Versão relacionada                             |
| Versão em operação | Versão efetivamente implantada                 |
| Contexto de Uso       | Contexto operacional                            |
| Ambiente              | Piloto, homologação ou produção             |
| Unidade ou sistema    | Local de operação                             |
| Período              | Intervalo coberto                               |
| Responsável          | Pessoa ou equipe                                |
| Fonte                 | Logs, sistemas, banco ou relatório             |
| Estado                | Rascunho, em revisão, validado ou substituído |

A versão implantada deve poder ser associada à versão avaliada.

Quando a associação entre a versão em operação e a Versão Avaliável for necessária para o requisito analisado e não puder ser estabelecida de forma suficiente, o NIAR-Saúde deve registrar a limitação e determinar se ela constitui pendência de rastreabilidade ou inconsistência documental confirmada.

---

## 9. Responsabilidades

A equipe responsável pela operação deve:

* produzir e preservar os registros;
* verificar a integridade dos dados;
* acompanhar métricas e limites;
* tratar alertas;
* registrar incidentes;
* comunicar mudanças;
* executar medidas corretivas;
* manter responsáveis atualizados;
* notificar o NIAR-Saúde quando aplicável.

O NIAR-Saúde pode:

* verificar, quando aplicável, a existência dos registros;
* avaliar suficiência e consistência;
* verificar associação entre versão e operação;
* analisar evidências longitudinais;
* identificar lacunas;
* identificar sinais de governança;
* recomendar revisão;
* indicar necessidade de nova avaliação;
* recomendar escalonamento institucional.

O NIAR-Saúde não substitui a equipe operacional responsável pelo sistema.

---

## 10. Fontes de evidência

Podem ser utilizadas:

* logs de aplicação;
* logs de inferência;
* painéis;
* bancos de monitoramento;
* registros de chamados;
* registros de incidentes;
* relatórios de qualidade;
* sistemas clínicos;
* registros de intervenção humana;
* atas;
* decisões técnicas;
* decisões institucionais;
* avaliações periódicas;
* auditorias de segurança.

Quando a fonte não puder ser incluída no repositório, registrar:

```text
Evidência mantida em ambiente institucional controlado.

Fonte:
Responsável:
Período:
Localização:
Forma de acesso:
Verificação realizada:
Restrições:
```

---

## 11. Dados operacionais sensíveis

Não armazenar no Git:

* dados pessoais;
* dados pessoais sensíveis;
* identificadores de pacientes;
* prontuários;
* entradas completas de sistemas clínicos;
* credenciais;
* chaves;
* tokens;
* detalhes exploráveis de vulnerabilidades;
* logs contendo dados não anonimizados;
* informações protegidas por contrato.

Os relatórios devem utilizar resultados agregados ou referências a ambientes
controlados, conforme as regras institucionais aplicáveis.

---

## 12. Alertas e limites

Esta seção aplica-se apenas quando houver métricas, thresholds ou limites operacionais definidos para a tarefa.

Quando houver limites de monitoramento, registrar:

| Campo                         | Preenchimento                                     |
| ----------------------------- | ------------------------------------------------- |
| Métrica                      | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Limite esperado               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Limite de alerta              | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Limite crítico               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Justificativa                 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Responsável pela definição | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Ação esperada               | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

Não inventar thresholds retrospectivamente.

A ausência de limite definido deve ser registrada como pendência quando relevante.

---

## 13. Gatilhos de revisão ou reavaliação

Podem constituir gatilhos:

* queda de desempenho;
* disparidade entre grupos;
* drift;
* mudança de prevalência;
* alteração de população;
* mudança de Contexto de Uso;
* novo modelo;
* retreinamento;
* alteração de threshold;
* incidente;
* falha de segurança;
* reclamação relevante;
* mudança regulatória;
* mudança institucional;
* alteração de integração;
* aumento de automação;
* redução da supervisão humana.

Quando um gatilho relevante for identificado, ele deve ser associado ao encaminhamento correspondente no processo de avaliação, monitoramento ou governança.

---

## 14. Estados dos artefatos

Podem ser utilizados:

* `Planejado`
* `Em coleta`
* `Em análise`
* `Em revisão`
* `Validado factualmente`
* `Requer ação`
* `Encerrado`
* `Substituído`
* `Arquivado`

Esses estados não equivalem a resultado formal de conformidade.

---

## 15. Pendências

Quando identificadas, pendências relacionadas aos artefatos operacionais devem ser registradas em:

```text
documentacao_projeto/registro_de_pendencias.md
```

Utilizar, quando aplicável:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]

[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]

[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

---

## 16. Relação com conformidade e maturidade

As evidências operacionais podem sustentar avaliações relativas à tarefa e à versão em operação.

Entretanto:

* a conformidade permanece vinculada à Tarefa de IA, à Versão Avaliável e ao Contexto de Uso;
* uma nova versão pode exigir nova avaliação;
* a existência de monitoramento não demonstra, isoladamente, conformidade;
* a ausência de incidentes registrados não demonstra ausência de incidentes;
* um único relatório não determina maturidade;
* a maturidade do projeto depende de evidências longitudinais e recorrentes.

---

## 17. Decisões institucionais

Questões como:

* continuidade da operação;
* suspensão;
* restrição de uso;
* aceite de risco residual;
* autorização de mudança;
* definição de condicionante;
* autorização de implantação;

devem ser registradas separadamente como decisões institucionais.

Os artefatos desta pasta podem fornecer evidências para a decisão, mas não a substituem.

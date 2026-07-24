# Perguntas para a Entrevista Inicial

## Controle do documento

| Campo                       | Preenchimento                                     |
| --------------------------- | ------------------------------------------------- |
| Versão do documento        | 0.1                                               |
| Status                      | Rascunho interno do NIAR                          |
| Elaborado por               | NIAR-Saúde                                       |
| Projeto                     | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Tarefa de IA                | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Versão Avaliável          | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Contexto de Uso             | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Data prevista da entrevista | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |
| Participantes esperados     | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |

> Este documento deve conter perguntas específicas, derivadas das lacunas e inconsistências identificadas nos artefatos recebidos.
>
> Não incluir perguntas cuja resposta já esteja claramente documentada.

---

## 1. Objetivo da entrevista

A entrevista tem como objetivo esclarecer questões que não puderam ser resolvidas por meio da inspeção documental.

A entrevista não substitui:

- atualização de Data Card;
- atualização de Model Card;
- fornecimento de evidência;
- registro de decisão técnica;
- identificação de versão;
- definição formal de responsável;
- produção de análise técnica.

Informações confirmadas oralmente devem ser incorporadas ao artefato correspondente sempre que aplicável.

---

## 2. Preparação

### Artefatos revisados antes da entrevista

| ID      | Artefato                                          | Versão | Data | Observação |
| ------- | ------------------------------------------------- | ------- | ---- | ------------ |
| ART-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |         |      |              |

### Pendências relacionadas

| ID      | Pendência                                         | Tipo | Prioridade |
| ------- | -------------------------------------------------- | ---- | ---------- |
| PEN-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |      |            |

### Inconsistências relacionadas

| ID      | Inconsistência                                                | Documentos envolvidos |
| ------- | -------------------------------------------------------------- | --------------------- |
| INC-001 | [INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos] |                       |

---

## 3. Tarefa de IA e Contexto de Uso

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-TAR-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis, somente quando aplicáveis:

- Qual é o objetivo específico da tarefa considerada neste ciclo?
- A descrição reúne mais de uma finalidade operacional?
- O mesmo modelo será utilizado para mais de uma tarefa?
- Qual é o uso atual e qual é apenas uso futuro pretendido?
- A tarefa já influencia decisões reais?
- Quais usuários recebem ou interpretam sua saída?
- Que processo ocorre depois da predição?
- Quais usos estão explicitamente fora do escopo?
- Há supervisão humana?
- O profissional pode discordar ou ignorar a saída?
- O sistema registra essa intervenção?

---

## 4. Dados

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-DAD-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Qual versão exata do dataset foi utilizada?
- Como essa versão pode ser identificada?
- Os dados usados correspondem integralmente ao Data Card?
- Houve filtros, exclusões ou transformações não documentados?
- Como foi feita a separação entre treino, validação e teste?
- Há sobreposição de pacientes ou unidades entre conjuntos?
- Como dados ausentes foram tratados?
- Quais atributos sensíveis ou proxies estão disponíveis?
- Houve atualização dos dados após a execução reportada?
- Existe registro reproduzível da preparação dos dados?

---

## 5. Modelo

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-MOD-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Qual commit produziu o modelo avaliado?
- Como os pesos são identificados?
- Qual configuração foi utilizada?
- Há diferenças entre a arquitetura documentada e a executada?
- Como os hiperparâmetros foram escolhidos?
- Qual função de perda foi utilizada?
- Como os thresholds foram definidos?
- Houve alterações após acesso aos resultados de teste?
- Há registro da execução principal?
- O modelo pode ser reconstruído a partir dos artefatos existentes?

---

## 6. Validação

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-VAL-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Qual conjunto sustenta cada resultado reportado?
- O conjunto de teste foi utilizado mais de uma vez?
- Houve ajuste após análise dos resultados de teste?
- As métricas correspondem ao Contexto de Uso?
- Existem intervalos de confiança?
- Existe avaliação por classe?
- Existe avaliação prospectiva?
- Existe validação externa institucional?
- Quais critérios determinaram que o desempenho seria aceitável?
- Quem revisou e aprovou o protocolo de validação?

---

## 7. Justiça

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-JUS-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Quais grupos foram considerados relevantes?
- Qual foi a justificativa clínica ou operacional para os grupos?
- Que métricas foram calculadas por grupo?
- A avaliação foi feita para todas as saídas ou classes relevantes?
- Foram avaliados falsos positivos e falsos negativos?
- Houve análise interseccional?
- Como atributos ausentes limitaram a avaliação?
- Existem diferenças consideradas materialmente relevantes?
- Houve mitigação?
- Quais riscos residuais permanecem?
- Quem definiu o critério de aceitabilidade?

Não transformar ausência de evidência em ausência de disparidade.

---

## 8. Transparência e explicabilidade

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-TRA-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Para quem a explicação é destinada?
- Que decisão a explicação deve apoiar?
- Qual método foi utilizado?
- Por que esse método foi escolhido?
- Há explicações globais e locais?
- As explicações foram revisadas por especialistas?
- Como são apresentadas ao usuário?
- Quais limitações interpretativas foram documentadas?
- Há risco de interpretar associação como causalidade?
- A explicação será utilizada em ambiente real?

---

## 9. Privacidade

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-PRI-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Quem é responsável pelo tratamento dos dados?
- Qual é a base legal registrada?
- Que aprovação ética cobre o uso realizado?
- O escopo atual corresponde ao escopo aprovado?
- Que técnicas de anonimização ou pseudonimização foram aplicadas?
- Quem possui acesso?
- Como o acesso é registrado?
- Quais regras de compartilhamento existem?
- Qual é a política de retenção?
- Foi avaliada a necessidade de RIPD?
- Há risco de reidentificação?

---

## 10. Segurança

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-SEG-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Onde os dados, código e pesos estão armazenados?
- Como o acesso é controlado?
- Como a integridade dos artefatos é verificada?
- Há gestão de credenciais e segredos?
- Existe backup?
- Existe plano de contingência?
- O que ocorre se o modelo ou serviço ficar indisponível?
- Há registros de incidentes?
- Foi realizada análise de ameaças?
- Há riscos específicos na integração com outros sistemas?
- Quem responderá por incidentes?

Distinguir segurança de artefatos experimentais de segurança operacional de um
sistema implantado.

---

## 11. Governança

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-GOV-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Quem aprovou o objetivo e o escopo?
- Quem pode autorizar mudanças?
- Quais condicionantes já foram definidos?
- Existe processo de revisão?
- Existe processo para escalonamento de risco?
- Quem decide sobre implantação?
- Como mudanças futuras serão comunicadas ao NIAR-Saúde?
- Há critérios para suspensão?
- Há documentação das decisões relevantes?
- Existe instância institucional responsável por casos escalonados?

---

## 12. Rastreabilidade

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-RAS-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Como dados, código, modelo e resultados estão vinculados?
- Existe identificador único da execução?
- Os resultados podem ser associados ao commit correspondente?
- Há registro de configurações e dependências?
- Há histórico de mudanças?
- Existem artefatos que foram substituídos?
- É possível reconstruir as decisões técnicas?
- Como novas versões serão identificadas?
- Quem mantém os registros?

---

## 13. Responsabilização

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-RES-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Quem responde tecnicamente pela tarefa?
- Quem responde pelos dados?
- Quem responde pelo modelo?
- Quem responde pela validação?
- Quem responderá pela implantação?
- Quem responderá pelo monitoramento?
- Quem pode aceitar ou rejeitar uma mudança?
- Os papéis estão formalmente registrados?
- Os autores dos documentos correspondem aos responsáveis atuais?

---

## 14. Mudanças futuras e versionamento

| ID        | Pergunta                                          | Motivo | Fonte da dúvida | Resposta | Evidência ou atualização necessária |
| --------- | ------------------------------------------------- | ------ | ---------------- | -------- | --------------------------------------- |
| Q-VER-001 | [INFORMAÇÃO PENDENTE — preencher pelo projeto] |        |                  |          |                                         |

Questões possíveis:

- Quais mudanças estão previstas?
- Haverá novo treinamento?
- Haverá atualização de dados?
- Haverá alteração de arquitetura?
- Haverá mudança de população?
- Haverá mudança do Contexto de Uso?
- Que alterações devem iniciar nova Versão Avaliável?
- Como mudanças menores serão registradas?
- Quem notificará o NIAR-Saúde?
- Existe calendário de revisão?

---

## 15. Confirmações orais

| ID      | Informação confirmada oralmente | Confirmada por | Data | Artefato que deve ser atualizado | Estado |
| ------- | --------------------------------- | -------------- | ---- | -------------------------------- | ------ |
| ORA-001 |                                   |                |      |                                  |        |

Utilizar:

```text
[CONFIRMAÇÃO ORAL — requer incorporação ao artefato correspondente]
```

---

## 16. Novas evidências solicitadas

| ID      | Evidência solicitada | Responsável | Prazo | Pendência relacionada | Estado |
| ------- | --------------------- | ------------ | ----- | ---------------------- | ------ |
| SOL-001 |                       |              |       |                        |        |

---

## 17. Encaminhamentos da entrevista

| ID      | Encaminhamento | Responsável | Prazo | Documento relacionado | Estado |
| ------- | -------------- | ------------ | ----- | --------------------- | ------ |
| ENC-001 |                |              |       |                       |        |

---

## 18. Síntese

### Pontos esclarecidos

* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

### Pontos parcialmente esclarecidos

* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

### Pontos não esclarecidos

* [INFORMAÇÃO PENDENTE — preencher pelo projeto]

### Novas inconsistências

* [INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]

### Próximo passo

[INFORMAÇÃO PENDENTE — preencher pelo projeto]

---

## 19. Histórico de versões

| Versão | Data | Responsável | Alteração                                    | Status                   |
| ------- | ---- | ------------ | ---------------------------------------------- | ------------------------ |
| 0.1     |      | NIAR-Saúde  | Criação do roteiro específico da entrevista | Rascunho interno do NIAR |




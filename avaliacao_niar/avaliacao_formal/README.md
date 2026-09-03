# Avaliação Formal

Esta pasta reúne os registros do resultado formal de avaliação de uma Tarefa de IA em uma Versão Avaliável e um Contexto de Uso específicos.

A avaliação formal consolida, de forma sintética e rastreável:

1. as avaliações individuais dos requisitos;
2. as consolidações por dimensão;
3. o resultado de conformidade do ciclo.

A avaliação formal somente deve ser preenchida após:

- delimitação da Tarefa de IA;
- identificação suficiente da Versão Avaliável;
- confirmação do Contexto de Uso;
- validação da Trilha de Execução;
- inventário das evidências e artefatos disponíveis e aplicáveis;
- conclusão das avaliações por requisito pertinentes;
- consolidação das dimensões avaliadas;
- registro das pendências e inconsistências relevantes.

A documentação metodológica vigente do FIAR-Saúde e do FIAR-Audit-Template deve orientar os critérios, procedimentos e resultados aplicáveis.

---

## Objeto da avaliação

O objeto da avaliação não é o modelo isolado.

A avaliação recai sobre a combinação entre:

- Tarefa de IA;
- Versão Avaliável;
- Contexto de Uso;
- artefatos e evidências associados;
- requisitos aplicáveis à Tarefa de IA, ao Contexto de Uso e à Trilha de Execução.

---

## Resultado pontual

O resultado da avaliação é pontual e não deve ser generalizado para:

- outras versões;
- outros Contextos de Uso;
- outras tarefas;
- o projeto inteiro;
- a instituição;
- futuras implantações.

O resultado formal utiliza os estados:

- **Conforme**;
- **Pendente**;
- **Não Conforme**.

A classificação deve ser fundamentada na materialidade dos achados e nas evidências verificadas.

Ela não deve resultar de:

- soma de requisitos;
- média;
- percentual;
- regra de maioria;
- mera presença ou ausência de artefatos.

A existência de uma pendência registrada não determina automaticamente o resultado **Pendente**. Deve-se verificar se a questão aberta é material para a conclusão sobre o atendimento dos requisitos aplicáveis.

---

## Conformidade e maturidade

A conformidade pertence à Tarefa de IA, à Versão Avaliável e ao Contexto de Uso avaliados.

A maturidade pertence ao projeto e é inferida longitudinalmente a partir da recorrência, continuidade e rastreabilidade das práticas ao longo do tempo.

Este diretório não deve ser usado para atribuir maturidade a partir de um único ciclo.

---

## Não objetivos

A avaliação formal não constitui, isoladamente:

- certificação de modelo;
- garantia de ausência de viés;
- garantia de segurança;
- validação clínica;
- autorização regulatória;
- autorização automática de implantação;
- aceite institucional de risco.

---

## Decisão institucional

Quando a avaliação identificar questões que exigem:

- aceite de risco;
- condicionantes;
- restrição de uso;
- decisão sobre implantação;
- decisão sobre continuidade;
- outra deliberação institucional;

o resultado técnico deve indicar a necessidade de escalonamento, sem substituir a decisão da instância competente.

Um sinal de governança ou indicação de escalonamento não constitui, por si só, decisão institucional.

O Registro de Decisão Institucional deve permanecer separado do resultado técnico.

---

## Papel deste diretório

Este diretório contém o **resultado formal da avaliação técnica do NIAR-Saúde**.

A análise detalhada que fundamenta esse resultado permanece registrada em:

- `avaliacao_niar/avaliacao_por_requisito/`;
- `avaliacao_niar/avaliacao_por_dimensao/`.

O documento formal não deve duplicar integralmente essas análises.

Seu objetivo é registrar de forma sintética e rastreável:

- o objeto avaliado;
- a síntese das dimensões avaliadas;
- o resultado de conformidade;
- os fundamentos determinantes do resultado;
- as pendências e inconsistências relevantes;
- os sinais de governança;
- recomendações técnicas;
- referências a condicionantes institucionais, quando existentes;
- eventual necessidade de escalonamento;
- gatilhos para reavaliação.

Quando houver decisão institucional, ela deve ser registrada separadamente em:

`decisao_institucional/`

---

## Template

O template para registro do resultado formal está disponível em:

[`template_resultado_avaliacao.md`](template_resultado_avaliacao.md)

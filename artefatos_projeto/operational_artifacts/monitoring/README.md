# Monitoramento Operacional

Esta pasta reúne os registros de monitoramento de uma Tarefa de IA durante piloto operacional ou operação ativa.

O monitoramento deve estar associado explicitamente a:

- uma Tarefa de IA;
- uma versão efetivamente implantada;
- uma Versão Avaliável correspondente;
- um Contexto de Uso;
- um ambiente operacional;
- um período de referência;
- responsáveis pelo acompanhamento e pela resposta.

A existência de monitoramento não demonstra, isoladamente, que a tarefa permaneça adequada, segura ou conforme.

---

## 1. Finalidade

O monitoramento operacional pode acompanhar:

- desempenho técnico;
- qualidade das entradas;
- qualidade das saídas;
- distribuição dos dados;
- prevalência;
- calibração;
- desempenho por classe;
- desempenho por grupo;
- disponibilidade;
- latência;
- falhas;
- uso fora do escopo;
- intervenções humanas;
- discordâncias;
- volume de uso;
- incidentes;
- mudanças de contexto;
- cumprimento de condicionantes;
- necessidade de revisão ou reavaliação.

---

## 2. Aplicabilidade

Para tarefas sem piloto operacional ou operação ativa, registrar:

```text
NÃO SE APLICA NESTE ESTÁGIO — tarefa sem piloto operacional ou operação ativa.
```

A ausência de operação ativa não impede a elaboração de um plano de monitoramento para uso futuro.

---

## 3. Arquivos

Utilizar o template:

```text
monitoring_report_template.md
```

Cada período de monitoramento pode gerar um novo arquivo, por exemplo:

```text
monitoring_report_2026-01.md
monitoring_report_2026-Q1.md
monitoring_report_piloto_fase_1.md
```

Evitar sobrescrever relatórios anteriores.

---

## 4. Frequência

A frequência deve ser definida de acordo com:

* risco;
* volume de uso;
* velocidade de mudança;
* impacto das decisões;
* disponibilidade dos rótulos;
* capacidade operacional;
* requisitos institucionais;
* condicionantes;
* histórico de incidentes.

Possíveis frequências:

* contínua;
* diária;
* semanal;
* mensal;
* trimestral;
* semestral;
* após número definido de casos;
* após gatilho específico.

Não utilizar frequência genérica sem justificativa.

---

## 5. Métricas

As métricas devem ser relacionadas ao Contexto de Uso.

Podem incluir:

### Desempenho

* sensibilidade;
* especificidade;
* precisão;
* valor preditivo positivo;
* valor preditivo negativo;
* F1;
* AUROC;
* AUPRC;
* calibração;
* erro absoluto;
* erro percentual;
* taxa de abstinência;
* cobertura;
* taxa de priorização.

### Operação

* volume;
* disponibilidade;
* latência;
* falhas;
* tempo de processamento;
* taxa de chamadas inválidas;
* taxa de dados ausentes;
* taxa de intervenção humana;
* taxa de discordância;
* taxa de uso fora do escopo.

### Justiça

* desempenho por grupo;
* taxas de erro por grupo;
* calibração por grupo;
* cobertura por grupo;
* acesso ou uso por grupo;
* efeitos interseccionais.

### Mudança

* drift de entrada;
* drift de saída;
* mudança de prevalência;
* mudança de população;
* mudança de equipamento;
* mudança de unidade;
* mudança temporal.

Não utilizar métricas apenas por disponibilidade técnica.

---

## 6. Baselines e limites

Cada métrica monitorada deve indicar, quando aplicável:

* baseline;
* valor esperado;
* limite de alerta;
* limite crítico;
* janela temporal;
* método de comparação;
* responsável pela definição;
* ação prevista.

A definição dos limites deve ser registrada em decisão técnica quando representar uma escolha metodológica relevante.

---

## 7. Rótulos e atraso de observação

Quando o resultado verdadeiro estiver disponível apenas posteriormente, registrar:

* fonte do rótulo;
* atraso esperado;
* processo de vinculação;
* qualidade do rótulo;
* revisão clínica;
* dados ainda sem desfecho;
* influência do atraso sobre a interpretação.

Não comparar diretamente métricas calculadas com rótulos incompletos com métricas históricas sem registrar a limitação.

---

## 8. Responsabilidades

Devem estar definidos:

| Papel                           | Responsabilidade                        |
| ------------------------------- | --------------------------------------- |
| Responsável pelo monitoramento | Produção e revisão dos resultados    |
| Responsável técnico           | Investigação de falhas e degradação |
| Responsável operacional        | Resposta no ambiente de uso             |
| Responsável pelos dados        | Qualidade e disponibilidade das fontes  |
| Responsável pela segurança    | Eventos de segurança                   |
| Responsável institucional      | Encaminhamentos institucionais          |
| Ponto focal do NIAR-Saúde      | Comunicação e reavaliação           |

Papéis não aplicáveis devem ser justificados.

---

## 9. Alertas

Todo alerta deve registrar:

* métrica;
* data;
* valor observado;
* limite violado;
* versão;
* ambiente;
* investigação;
* ação;
* responsável;
* encerramento;
* necessidade de incidente;
* necessidade de reavaliação.

Um alerta não deve ser apagado após sua resolução.

---

## 10. Relação com incidentes

Um alerta deve ser encaminhado para:

```text
../incidents/
```

quando houver ou puder haver:

* dano;
* decisão indevida;
* uso fora do escopo;
* falha relevante;
* exposição de dados;
* degradação material;
* descumprimento de condicionante;
* necessidade de suspensão;
* risco institucional relevante.

---

## 11. Privacidade

Os relatórios devem evitar dados individuais.

Utilizar, quando possível:

* agregações;
* identificadores pseudonimizados;
* contagens mínimas;
* supressão de células pequenas;
* referências a ambientes controlados.

Não armazenar logs sensíveis no Git.

---

## 12. Rastreabilidade

Cada relatório deve indicar:

* versão implantada;
* versão avaliada;
* commit;
* configuração;
* período;
* fonte dos dados;
* scripts;
* execução;
* dashboard;
* responsáveis.

Quando não houver correspondência suficiente:

```text
[INCONSISTÊNCIA IDENTIFICADA — versão monitorada não associada de forma suficiente à Versão Avaliável]
```

---

## 13. Gatilhos de reavaliação

Podem exigir reavaliação:

* queda relevante de desempenho;
* disparidade relevante;
* drift persistente;
* alteração de prevalência;
* incidente;
* mudança de população;
* mudança de escopo;
* mudança de Contexto de Uso;
* alteração de threshold;
* retreinamento;
* nova integração;
* redução da supervisão humana;
* mudança regulatória;
* descumprimento de condicionante.

O relatório deve registrar o encaminhamento, não apenas o evento.

---


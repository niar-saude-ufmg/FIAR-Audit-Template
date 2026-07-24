# Avaliação por Dimensão

Esta pasta reúne as análises técnicas realizadas pelo NIAR-Saúde para as sete dimensões do FIAR-Saúde:

- Justiça;
- Transparência;
- Responsabilização;
- Privacidade;
- Segurança;
- Governança;
- Rastreabilidade.

A avaliação deve ser realizada para uma Tarefa de IA, uma Versão Avaliável e um Contexto de Uso específicos.

A avaliação das dimensões não deve ser feita sobre o modelo isolado quando os riscos e as evidências dependem dos dados, procedimentos, usuários e contexto.

---
## Estrutura recomendada

Uma instância pode utilizar um arquivo por dimensão:

```text
avaliacao_por_dimensao/
├── README.md
├── justica.md
├── transparencia.md
├── responsabilizacao.md
├── privacidade.md
├── seguranca.md
├── governanca.md
└── rastreabilidade.md
```

O arquivo `template_avaliacao_dimensao.md` pode ser copiado e renomeado para
cada dimensão.

---

## Princípios

### Evidência antes da conclusão

Toda conclusão deve indicar a evidência utilizada.

### Contextualidade

A suficiência depende:

* da tarefa;
* da versão;
* do Contexto de Uso;
* da trilha;
* dos riscos;
* do estágio de desenvolvimento.

### Ausência de evidência

Ausência de evidência não deve ser tratada como evidência de ausência de risco, problema ou disparidade.

### Não duplicação

O arquivo de avaliação não deve copiar integralmente Data Cards, Model Cards ou relatórios técnicos.

Deve indicar:

* o que foi analisado;
* onde a evidência está;
* que verificação foi realizada;
* qual conclusão é permitida;
* que limitações permanecem.

### Não certificação

A avaliação de uma dimensão não certifica que o sistema seja justo, seguro, privado, transparente ou adequadamente governado em qualquer contexto.

---

## Classificações descritivas preparatórias

Antes de uma avaliação formal, podem ser utilizadas:

* `Evidência disponível`;
* `Evidência parcial`;
* `Evidência não identificada`;
* `Não aplicável — requer justificativa`.

Essas classificações não equivalem a resultado formal de conformidade.

---

## Sinais de governança

Uma avaliação pode identificar sinais que exijam:

* complementação;
* correção;
* análise adicional;
* monitoramento;
* restrição de escopo;
* revisão futura;
* escalonamento institucional.

O sinal de governança não deve ser confundido com decisão institucional.

---

## Artefatos relacionados

Exemplos:

* Data Card;
* Model Card;
* Fairness Report;
* Explainability Report;
* RIPD;
* registros de decisão técnica;
* logs;
* registros de execução;
* relatórios de validação;
* registros operacionais;
* documentos de governança.

A presença do arquivo, isoladamente, não demonstra suficiência.




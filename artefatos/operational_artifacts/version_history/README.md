# Histórico de Versões e Mudanças

Esta pasta reúne registros de mudanças técnicas e operacionais relacionadas à Tarefa de IA.

O objetivo é permitir reconstruir:

- o que mudou;
- por que mudou;
- quem implementou e, quando aplicável, quem autorizou;
- quais versões foram afetadas;
- quais testes foram realizados;
- quais riscos foram considerados;
- se a mudança **pode caracterizar** nova Versão Avaliável;
- se a mudança **pode exigir** nova avaliação.

---

## 1. Mudanças que podem requerer registro

Podem requerer registro alterações relevantes em:

- dados;
- fontes;
- filtros;
- população;
- variáveis;
- rótulos;
- arquitetura;
- pesos;
- treinamento;
- thresholds;
- métricas;
- código;
- dependências;
- infraestrutura;
- interface;
- integração;
- Contexto de Uso;
- supervisão humana;
- monitoramento;
- responsáveis;
- condicionantes.

---

## 2. Identificação

Quando houver mudança relevante a registrar, pode ser utilizado:

```text
version_change_record_template.md
```

Recomenda-se manter um registro individual por mudança relevante, por exemplo:

```text
MUD-001-atualizacao-thresholds.md
MUD-002-retreinamento-modelo.md
MUD-003-alteracao-fonte-dados.md
```

---

## 3. Mudanças relevantes

Podem constituir mudança relevante:

* retreinamento;
* nova arquitetura;
* novas variáveis;
* nova população;
* novo objetivo;
* novo Contexto de Uso;
* nova integração;
* alteração material de threshold;
* novo fluxo decisório;
* redução de supervisão;
* mudança de distribuição;
* incidente;
* alteração regulatória;
* modificação de condicionante.

Quando houver dúvida sobre se a alteração caracteriza uma mudança relevante para fins de avaliação, o enquadramento deve ser validado pelo NIAR-Saúde.

---

## 4. Versionamento semântico

O projeto pode utilizar sua própria política de versionamento, mas deve documentá-la.

Exemplo:

* major: mudança relevante de comportamento ou escopo;
* minor: melhoria compatível;
* patch: correção sem alteração de finalidade.

O número da versão, sozinho, não determina se há nova Versão Avaliável.

---

## 5. Relação com decisão técnica

Uma mudança pode implementar uma decisão técnica.

Nesse caso, indicar, quando aplicável e disponível:

* ID da decisão;
* versão;
* commit;
* evidência;
* testes;
* responsável.

---

## 6. Relação com operação

Nenhuma mudança deve ser tratada como implantada apenas porque foi incorporada ao código.

Registrar separadamente:

* desenvolvimento;
* teste;
* homologação;
* piloto;
* produção;
* rollback.

---

## 7. Preservação

Não apagar registros de versões substituídas.

Para tarefas em operação ativa, o histórico deve permitir identificar, quando aplicável, qual versão esteve em operação em cada período relevante.

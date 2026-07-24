# Histórico de Versões e Mudanças

Esta pasta reúne registros de mudanças técnicas e operacionais relacionadas à Tarefa de IA.

O objetivo é permitir reconstruir:

- o que mudou;
- por que mudou;
- quem autorizou e implementou;
- quais versões foram afetadas;
- quais testes foram realizados;
- quais riscos foram considerados;
- se a mudança exige nova Versão Avaliável;
- se a mudança exige nova avaliação.

---

## 1. Mudanças que devem ser registradas

Registrar alterações em:

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

Utilizar:

```text
version_change_record_template.md
```

Criar um arquivo por mudança:

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

A classificação deve ser validada pelo NIAR-Saúde quando houver dúvida.

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

Nesse caso, indicar:

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

O histórico deve permitir identificar qual versão estava em operação em cada período.


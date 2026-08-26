# Decisões Institucionais

Esta pasta reúne os registros de decisões que ultrapassam o escopo estritamente técnico da equipe do projeto e da avaliação realizada pelo NIAR-Saúde.

Essas decisões podem envolver:

- aceite de risco residual;
- definição de condicionantes;
- autorização ou restrição de piloto;
- autorização ou restrição de implantação;
- continuidade, suspensão ou encerramento;
- definição de responsabilidades institucionais;
- tratamento de conflitos entre objetivos;
- aceitação de limitações relevantes;
- escalonamento de incidentes;
- resposta a mudanças regulatórias ou institucionais.

Os registros desta pasta devem estar associados a uma Tarefa de IA, a uma Versão Avaliável e a um Contexto de Uso específicos, sempre que aplicável.

---

## 1. Distinção entre avaliação técnica e decisão institucional

A equipe do projeto produz:

- artefatos técnicos;
- análises;
- evidências;
- registros de decisão técnica;
- propostas de mitigação;
- informações sobre riscos e limitações.

O NIAR-Saúde:

- verifica suficiência;
- verifica consistência;
- verifica rastreabilidade;
- realiza avaliação técnica;
- identifica lacunas;
- registra sinais de governança;
- recomenda encaminhamentos;
- indica questões que exigem deliberação institucional.

A instância institucional competente:

- delibera sobre questões escalonadas;
- define condicionantes;
- decide sobre aceite de risco;
- determina restrições;
- decide sobre continuidade, suspensão, piloto ou implantação;
- atribui responsabilidades institucionais.

Uma recomendação técnica do NIAR-Saúde não deve ser registrada como decisão institucional.

---

## 2. Estrutura

```text
decisao_institucional/
├── README.md
├── registro_decisao_institucional_template.md
└── registro_de_condicionantes.md
```

Cada decisão institucional efetivamente formalizada deve ser registrada em arquivo próprio, com identificador rastreável.

Exemplo:

```text
DIN-001-autorizacao-piloto-condicionado.md
DIN-002-restricao-de-populacao.md
DIN-003-aceite-de-risco-residual.md
```

Não reutilizar identificadores.

---

## 3. Instância competente

A instância responsável deve ser identificada conforme a estrutura institucional vigente.

No contexto do NIAR-Saúde, questões institucionais podem ser encaminhadas ao
Comitê Gestor ou a outra instância competente, conforme:

* natureza da decisão;
* competência formal;
* nível de risco;
* responsabilidade sobre o projeto;
* estrutura institucional;
* regulação aplicável.

Não presumir que toda decisão institucional seja tomada pelo Comitê Gestor.

Quando aplicável, o registro deve indicar explicitamente a instância que deliberou e a competência institucional correspondente.

---

## 4. Situações que podem exigir decisão institucional

Podem exigir deliberação:

* risco residual relevante;
* disparidade material;
* insuficiência de evidência considerada relevante para uma decisão institucional;
* impossibilidade de mitigação imediata;
* limitação relevante de privacidade;
* limitação relevante de segurança;
* uso fora do escopo inicialmente aprovado;
* expansão de população;
* mudança de Contexto de Uso;
* implantação de nova versão;
* incidente relevante;
* ausência de responsável;
* conflito entre desempenho e risco;
* necessidade de restrição;
* necessidade de supervisão adicional;
* continuidade de piloto;
* autorização de operação.

A existência de uma dessas situações não significa automaticamente que o risco seja inaceitável.

---

## 5. Fontes da decisão

A decisão pode considerar:

* avaliação do NIAR-Saúde;
* relatórios por dimensão;
* Data Cards;
* Model Cards;
* relatórios de justiça;
* relatórios de explicabilidade;
* RIPD;
* documentos de segurança;
* registros de incidentes;
* registros de monitoramento;
* registros de decisão técnica;
* pareceres jurídicos;
* pareceres éticos;
* pareceres clínicos;
* condicionantes anteriores;
* manifestação da equipe do projeto.

As fontes utilizadas devem ser identificadas, quando aplicável, por versão, data e localização ou referência de rastreabilidade.

---

## 6. Condicionantes

Uma decisão pode estabelecer condicionantes, como:

* completar determinada análise;
* limitar a população;
* limitar o período;
* limitar o ambiente;
* exigir supervisão humana;
* impedir uso automático;
* exigir monitoramento;
* definir limite operacional;
* atualizar RIPD;
* atualizar Data Card ou Model Card;
* produzir evidência adicional;
* reavaliar após prazo;
* suspender em caso de incidente;
* comunicar mudança ao NIAR-Saúde;
* realizar nova avaliação antes de expansão.

As condicionantes devem ser específicas, verificáveis, atribuídas e acompanhadas.

---

## 7. Decisão e conformidade

Uma decisão institucional:

* não substitui a avaliação técnica;
* não transforma evidência insuficiente em evidência suficiente;
* não elimina limitações;
* não altera silenciosamente o resultado técnico;
* não certifica que a tarefa seja justa, segura, ética ou clinicamente válida.

Da mesma forma, um resultado técnico favorável não constitui automaticamente autorização institucional.

---

## 8. Aceite de risco

Quando houver aceite de risco residual, registrar:

* risco;
* evidência;
* probabilidade ou condição;
* impacto;
* mitigação existente;
* limitação;
* responsável pelo aceite;
* duração;
* condições;
* gatilhos de revisão;
* população e contexto cobertos.

O aceite deve ser explícito.

Não inferir aceite de risco a partir de ausência de objeção ou continuidade informal do projeto.

---

## 9. Validade

Toda decisão institucional formalizada deve indicar, quando aplicável:

* data;
* versão;
* escopo;
* validade;
* condições de revisão;
* gatilhos de reavaliação;
* versões cobertas;
* Contextos de Uso cobertos.

Uma decisão não deve ser generalizada para versões ou contextos não identificados.

---

## 10. Preservação e rastreabilidade

Decisões substituídas não devem ser apagadas.

Registrar:

* decisão anterior;
* decisão nova;
* motivo da alteração;
* data;
* instância;
* evidências novas;
* condicionantes alteradas.

---

## 11. Confidencialidade

Quando a decisão contiver informação restrita:

* manter o documento em ambiente controlado;
* registrar no repositório apenas metadados;
* indicar responsável;
* indicar localização;
* indicar forma de acesso;
* preservar versão e data.

Não armazenar no Git:

* dados pessoais;
* pareceres jurídicos restritos;
* informações sensíveis de segurança;
* assinaturas não destinadas à publicação;
* informações institucionais protegidas.

---

## 12. Relação com os demais diretórios

As evidências técnicas permanecem em:

```text
artefatos_projeto/
```

A avaliação do NIAR-Saúde permanece em:

```text
avaliacao_niar/
```

As pendências permanecem consolidadas em:

```text
documentacao_projeto/registro_de_pendencias.md
```

As decisões institucionais permanecem em:

```text
decisao_institucional/
```

Não duplicar integralmente os documentos de origem.

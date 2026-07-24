# Resultado Consolidado do Ciclo FIAR-Saúde

Esta pasta reúne os documentos consolidados produzidos ao final de um ciclo FIAR-Saúde para uma combinação específica de:

- Tarefa de IA;
- Versão Avaliável;
- Contexto de Uso;
- trilha;
- conjunto de evidências;
- data de referência.

O diretório mantém temporariamente o nome `auditoria_final/` por compatibilidade com a automação existente.

O nome do diretório não significa que todos os documentos nele contidos sejam decisões institucionais ou que todo ciclo resulte em aprovação, certificação ou autorização de uso.

A documentação metodológica oficial do FIAR-Saúde está disponível em:

<https://github.com/niar-saude-ufmg/FIAR-Saude>

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

---

## 1. Finalidade

Esta pasta deve reunir referências ou versões consolidadas dos resultados produzidos nas diferentes etapas do ciclo, incluindo, quando aplicável:

- identificação final do objeto avaliado;
- síntese das evidências consideradas;
- resultado da avaliação técnica realizada pelo NIAR-Saúde;
- pendências remanescentes;
- limitações;
- sinais de governança;
- recomendações técnicas;
- condicionantes estabelecidas por decisão institucional;
- registros de decisões institucionais relacionadas;
- indicação de gatilhos de revisão ou nova avaliação.

O conteúdo deve preservar a distinção entre:

1. artefatos técnicos produzidos pelo projeto;
2. avaliação realizada pelo NIAR-Saúde;
3. decisões tomadas pela instância institucional competente.

---

## 2. Estrutura recomendada

```text
auditoria_final/
├── README.md
├── sintese_do_ciclo.md
├── referencias_da_avaliacao.md
└── indice_de_decisoes_e_condicionantes.md
````

Os arquivos consolidados devem referenciar os documentos de origem, evitando duplicação integral.

Não é obrigatório criar todos os arquivos antes da conclusão das etapas correspondentes.

---

## 3. Objeto do resultado

Todo documento desta pasta deve identificar explicitamente:

| Campo                   | Conteúdo esperado                         |
| ----------------------- | ------------------------------------------ |
| Projeto                 | Projeto ao qual pertence o ciclo           |
| Tarefa de IA            | Unidade avaliada                           |
| Versão Avaliável      | Versão específica considerada            |
| Contexto de Uso         | Contexto considerado na avaliação        |
| Trilha                  | Trilha Experimental ou Trilha Produção   |
| Data de referência     | Data-limite das evidências                |
| Artefatos considerados  | Lista versionada das fontes                |
| Avaliação relacionada | Documento de avaliação do NIAR-Saúde    |
| Decisões relacionadas  | Registros institucionais, quando existirem |

O resultado não deve ser generalizado para outras versões, tarefas, populações
ou Contextos de Uso.

---

## 4. Documentos de origem

### Artefatos do projeto

Permanecem em:

```text
artefatos_projeto/
```

Incluem, quando aplicáveis:

* Data Cards;
* Model Cards;
* relatórios de justiça;
* relatórios de explicabilidade;
* registros de decisão técnica;
* documentos de privacidade;
* registros operacionais;
* relatório consolidado de IAR produzido pelo projeto.

### Avaliação do NIAR-Saúde

Permanece em:

```text
avaliacao_niar/
```

Inclui, quando aplicáveis:

* pré-avaliação documental;
* registro de inconsistências;
* avaliação por dimensão;
* resultado formal da avaliação técnica;
* sinais de governança;
* recomendações e encaminhamentos.

### Decisões institucionais

Permanecem em:

```text
decisao_institucional/
```

Incluem, quando existirem:

* autorização ou restrição de piloto;
* condicionantes;
* aceite de risco residual;
* decisão sobre continuidade;
* restrição de escopo;
* suspensão;
* decisão sobre implantação.

Esta pasta não deve transformar automaticamente recomendações técnicas em
decisões institucionais.

---

## 5. Responsabilidades

### Equipe do projeto

É responsável pela correção factual e técnica dos artefatos que produziu.

### NIAR-Saúde

É responsável por:

* verificar suficiência;
* verificar consistência;
* verificar rastreabilidade;
* registrar a avaliação técnica;
* identificar limitações;
* registrar sinais de governança;
* indicar encaminhamentos.

### Instância institucional competente

É responsável pelas deliberações que ultrapassam o escopo técnico, como:

* aceite de risco;
* estabelecimento de condicionantes;
* autorização ou restrição de uso;
* continuidade;
* suspensão;
* implantação.

A consolidação final não deve apagar ou confundir essas responsabilidades.

---

## 6. Resultado da avaliação técnica

Quando houver resultado formal, ele deve ser referenciado a partir de:

```text
avaliacao_niar/avaliacao_formal/resultado_avaliacao.md
```

O resultado deve estar limitado à Tarefa de IA, à Versão Avaliável e ao Contexto
de Uso identificados.

O resultado técnico não constitui, isoladamente:

* certificação de que a tarefa seja justa;
* certificação de segurança;
* validação clínica;
* aprovação regulatória;
* aceite institucional de risco;
* autorização automática de implantação.

---

## 7. Decisão institucional

Quando houver deliberação institucional, o documento correspondente deve ser
referenciado a partir de:

```text
decisao_institucional/
```

A decisão deve indicar:

* instância responsável;
* competência;
* escopo;
* versões cobertas;
* Contexto de Uso;
* justificativa;
* condicionantes;
* restrições;
* validade;
* gatilhos de revisão;
* riscos residuais explicitamente aceitos, quando aplicável.

Na ausência de decisão institucional, registrar:

```text
Nenhuma decisão institucional vinculada a este ciclo na data de referência.
```

Essa formulação não deve ser interpretada como autorização tácita.

---

## 8. Condicionantes

As condicionantes devem permanecer registradas em:

```text
decisao_institucional/registro_de_condicionantes.md
```

Nesta pasta, deve ser incluída apenas uma síntese ou índice contendo:

* ID;
* decisão de origem;
* condicionante;
* responsável;
* prazo;
* estado;
* localização da evidência.

Não reproduzir ou modificar silenciosamente a formulação da decisão original.

---

## 9. Pendências e limitações

Pendências abertas não devem desaparecer da consolidação final.

Referenciar:

```text
documentacao_projeto/registro_de_pendencias.md
```

A síntese deve distinguir:

* pendências resolvidas;
* pendências abertas;
* pendências críticas;
* análises não realizadas;
* evidências indisponíveis;
* inconsistências mantidas;
* limitações aceitas apenas para continuidade documental;
* questões aguardando decisão institucional.

O encerramento de um ciclo não significa que todas as pendências tenham sido
resolvidas.

---

## 10. Maturidade

Este diretório não atribui automaticamente maturidade ao projeto.

A maturidade:

* pertence ao projeto;
* é longitudinal;
* depende da recorrência, estabilidade e institucionalização das práticas;
* deve considerar evidências acumuladas ao longo de diferentes versões e ciclos;
* não pode ser inferida apenas a partir de um único resultado de conformidade.

Quando houver uma análise de maturidade, ela deve indicar:

* período considerado;
* ciclos examinados;
* evidências longitudinais;
* justificativa;
* limitações;
* nível atribuído conforme a documentação vigente.

Não utilizar a expressão “maturidade do sistema” como equivalente à maturidade
do projeto.

---

## 11. Relação com conformidade

A conformidade é pontual e vinculada à combinação entre:

* Tarefa de IA;
* Versão Avaliável;
* Contexto de Uso.

Uma decisão institucional de continuidade não altera silenciosamente o resultado
da avaliação técnica.

Da mesma forma, um resultado técnico favorável não substitui autorização
institucional quando essa autorização for necessária.

---

## 12. Gatilhos de revisão

O resultado consolidado deve registrar gatilhos aplicáveis, como:

* retreinamento;
* alteração de arquitetura;
* mudança dos dados;
* mudança de variáveis;
* mudança de população;
* mudança de escopo;
* mudança do Contexto de Uso;
* alteração de thresholds;
* nova integração;
* incidente;
* drift;
* mudança regulatória;
* mudança institucional;
* descumprimento de condicionante.

A ocorrência de um gatilho pode exigir atualização documental, avaliação parcial
ou abertura de novo ciclo.

---

## 13. Preservação e versionamento

Os documentos consolidados devem indicar:

* versão;
* data;
* responsáveis;
* fontes;
* alterações;
* documento substituído;
* estado.

Versões anteriores não devem ser apagadas quando forem necessárias para
reconstruir o histórico do ciclo.

Estados possíveis:

* `Rascunho`
* `Em consolidação`
* `Para confirmação factual`
* `Consolidado pelo NIAR-Saúde`
* `Aguardando decisão institucional`
* `Vinculado a decisão institucional`
* `Substituído`
* `Arquivado`

Esses estados não equivalem a resultado de conformidade.

---

## 14. Confidencialidade

Antes de incluir documentos consolidados no repositório, verificar:

* presença de dados pessoais;
* dados pessoais sensíveis;
* informações clínicas individuais;
* pareceres restritos;
* informações de segurança;
* propriedade intelectual;
* assinaturas;
* informações institucionais confidenciais.

Quando o documento precisar permanecer em ambiente controlado, registrar apenas:

```text
Documento consolidado mantido em ambiente institucional controlado.

Título:
Versão:
Data:
Responsável:
Localização:
Procedimento de acesso:
Classificação:
```

---

## 15. Relação com o PDF

O módulo de geração do PDF pode utilizar esta pasta como uma das fontes da consolidação.

A geração automática:

* não cria novas evidências;
* não produz novas decisões;
* não resolve pendências;
* não transforma rascunhos em documentos validados;
* não altera o resultado técnico;
* não constitui assinatura ou aprovação institucional.

O PDF deve reproduzir apenas documentos e estados efetivamente registrados no repositório.

---

## 16. Conteúdo mínimo para fechamento documental

Antes de consolidar o ciclo, verificar se estão identificados:

* Tarefa de IA;
* Versão Avaliável;
* Contexto de Uso;
* trilha;
* data de referência;
* artefatos considerados;
* resultado ou estado da avaliação;
* limitações;
* inconsistências relevantes;
* pendências remanescentes;
* responsáveis;
* decisões institucionais, quando existentes;
* condicionantes, quando existentes;
* gatilhos de revisão.

A presença desses elementos permite o fechamento documental do ciclo, mas não significa aprovação, certificação ou autorização de implantação.


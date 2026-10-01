# Guia de Requisitos para Avaliação

Este documento organiza operacionalmente os requisitos do FIAR-Saúde já consolidados no processo atual de revisão metodológica.

As dimensões ainda em revisão permanecem identificadas neste documento, mas sem requisitos operacionais até sua estabilização. Nesta versão, apenas a dimensão **Justiça** está operacionalizada.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas.

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a **Tarefa de IA**, a **Versão Avaliável**, o **Contexto de Uso** e a **Trilha de Execução**.

Um requisito deve ser considerado **Não aplicável** somente quando a condição objetiva pressuposta por sua formulação não estiver presente no objeto avaliado. A ausência de prática, mecanismo, capacidade, procedimento, registro ou evidência que o próprio requisito busca avaliar não constitui justificativa de não aplicabilidade e deve ser refletida posteriormente na análise e no resultado do requisito. Quando a presença da condição objetiva ainda não puder ser determinada, a aplicabilidade não deve ser presumida como Não aplicável.

As orientações deste guia apoiam o preenchimento dos instrumentos de avaliação do NIAR-Saúde. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

Nas dimensões já consolidadas na revisão metodológica atual, as formulações dos requisitos devem ser reproduzidas sem alteração. As explicações, exemplos e cautelas deste guia têm função operacional e não criam requisitos adicionais.

---

## Status das dimensões

| Dimensão           | Status nesta versão                     |
| ------------------- | ---------------------------------------- |
| Governança         | Em revisão metodológica                |
| Segurança          | Em revisão metodológica                |
| Privacidade         | Em revisão metodológica                |
| Responsabilização | Em revisão metodológica                |
| Rastreabilidade     | Em revisão metodológica                |
| Justiça            | **Operacionalizada nesta versão** |
| Transparência      | Em revisão metodológica                |

---

## Governança

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

## Segurança

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

## Privacidade

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

## Responsabilização

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

## Rastreabilidade

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

# Justiça

A dimensão de Justiça avalia se a Tarefa de IA pode produzir, reproduzir ou agravar diferenças injustificadas entre grupos e populações relevantes, considerando tanto os efeitos da Tarefa quanto a adequação dos dados, variáveis-alvo, padrões de referência e formas de disponibilização.

A análise não deve presumir que toda diferença observada represente automaticamente injustiça ou discriminação. Também não deve limitar a seleção de grupos aos atributos disponíveis nos dados.

Nesta versão do guia, a dimensão está organizada nos quatro requisitos estabilizados na revisão metodológica atual: **RC01 a RC04**.

## Orientação transversal para Justiça

A avaliação de Justiça deve distinguir:

- **informação factual já documentada**, que pode ser recuperada de Data Card, Model Card, documentação do projeto, resultados experimentais ou outras fontes;
- **análise específica de Justiça**, que pode exigir interpretação, fundamentação ou julgamento adicional pela equipe do projeto;
- **decisão metodológica do NIAR-Saúde**, que não deve ser transferida ao projeto como se fosse ausência de evidência;
- **decisão técnica ou institucional**, quando um achado exigir escolha, tratamento, aceitação de risco, restrição ou outro encaminhamento.

O **Fairness Report** é uma possível fonte para consolidar análises específicas de Justiça. Ele não deve duplicar desnecessariamente fatos já documentados em Data Cards, Model Cards ou outros artefatos. Quando a informação factual já existir, o Fairness Report pode referenciá-la e acrescentar apenas a análise necessária para Justiça.

A ausência de um Fairness Report, isoladamente, não demonstra insuficiência. A questão é se as evidências necessárias para responder ao requisito estão disponíveis em fontes adequadas.

---

## RC01 — Grupos e populações

### Requisito

**Identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.**

### O que o requisito busca verificar

Verificar se os grupos e populações relevantes para a análise de Justiça foram identificados de forma fundamentada a partir da Tarefa de IA, da população pertinente e do Contexto de Uso avaliado.

O requisito não busca simplesmente listar atributos existentes nos dados. A seleção deve ser justificada pela possibilidade de efeitos diferenciados, exclusão de benefícios, limitações de representação, características clínicas, sociais, territoriais, institucionais ou outras condições relevantes para a Tarefa e o Contexto.

### Aspectos a considerar na aplicabilidade

- RC01 é aplicável quando a Tarefa, no Contexto de Uso avaliado, pode produzir efeitos ou benefícios que incidam sobre pessoas, grupos ou populações.
- A ausência de dados sobre determinado grupo relevante não torna o requisito não aplicável.
- A ausência de análise prévia de grupos não torna o requisito não aplicável.
- Grupos relevantes podem ser demográficos, territoriais, clínicos, institucionais ou definidos por outra característica pertinente à Tarefa.
- Populações explicitamente fora do escopo validado devem ser registradas como delimitação ou limitação de escopo, e não automaticamente como grupo para comparação de Justiça.
- O uso futuro pretendido não deve ser utilizado para definir grupos do Contexto de Uso atual quando ainda não fizer parte da unidade avaliada.

### Exemplos de evidências pertinentes

- descrição da população relevante;
- Data Card;
- Model Card;
- Formulário de Entrada;
- Identificação da Avaliação;
- critérios de inclusão e exclusão;
- resultados estratificados já existentes;
- documentação de limitações de cobertura ou representatividade;
- literatura clínica, técnica ou institucional pertinente;
- conhecimento clínico ou institucional documentado;
- Fairness Report ou análise equivalente.

Esses exemplos não constituem lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

### Mecanismos de verificação possíveis

- verificação documental;
- consistência cruzada entre população, Contexto de Uso e grupos selecionados;
- verificação de que os grupos não foram escolhidos apenas por disponibilidade de atributos;
- verificação de grupos relevantes que não podem ser analisados com os dados disponíveis;
- análise da fundamentação utilizada para selecionar os grupos;
- verificação de limitações ou incertezas sobre a completude da seleção.

### Observações metodológicas

- A disponibilidade de um atributo nos dados não constitui, por si só, justificativa para tratá-lo como grupo relevante para Justiça.
- Informações factuais sobre os grupos podem estar disponíveis no Data Card, Model Card ou outros documentos.
- Quando a relevância dos grupos ou a completude de sua seleção não estiver explicitamente fundamentada, essa análise deve ser produzida pela equipe do projeto, por exemplo no Fairness Report.
- A ausência de raça/etnia ou de outro atributo potencialmente relevante deve ser registrada como limitação quando impedir a análise; não deve ser preenchida por inferência.
- Identificar um grupo potencialmente sujeito à exclusão de benefícios em RC01 não equivale a analisar desigualdades de acesso. Essa análise pertence a RC04 quando aplicável.
- Não utilizar afirmações sobre implantação ou benefício futuro como evidência do Contexto de Uso atual.

---

## RC02 — Diferenças nos efeitos

### Requisito

**Avaliar se a Tarefa de IA produz, reproduz ou agrava diferenças injustificadas nos efeitos sobre os grupos e populações identificados.**

### O que o requisito busca verificar

Verificar se os efeitos relevantes e observáveis da Tarefa foram examinados entre os grupos identificados em RC01 e, quando diferenças forem encontradas, se elas foram interpretadas de forma contextualizada.

A análise não pressupõe uma métrica universal de fairness nem exige necessariamente comparação estatística formal para todos os grupos.

### Aspectos a considerar na aplicabilidade

- RC02 é aplicável quando existem grupos identificados em RC01 sobre os quais a Tarefa possa produzir efeitos no Contexto de Uso avaliado.
- A impossibilidade de realizar determinada comparação por ausência ou insuficiência de dados não torna o requisito não aplicável.
- Os efeitos relevantes dependem da Tarefa e do Contexto de Uso.
- Em contexto experimental, podem ser observáveis principalmente diferenças de desempenho, erro, calibração ou outros resultados técnicos.
- Em contexto operacional, podem também ser pertinentes diferenças em decisões, consequências ou resultados decorrentes do uso.
- O uso futuro pretendido não deve ser usado como substituto de efeitos não observáveis no contexto atual.

### Exemplos de evidências pertinentes

- resultados estratificados;
- métricas por grupo;
- análise de erros;
- Model Card;
- resultados experimentais;
- Fairness Report;
- análise de calibração, quando pertinente;
- documentação de decisões ou consequências observáveis, quando aplicável;
- Registro de Decisão, quando houver decisão sobre tratamento ou aceitação de diferenças.

### Mecanismos de verificação possíveis

- revisão de métricas e resultados por grupo;
- comparação de desempenho;
- análise de falsos positivos e falsos negativos, quando pertinente;
- análise de calibração, quando pertinente;
- interpretação clínica, técnica ou operacional das diferenças;
- análise da magnitude, estabilidade e relevância prática;
- verificação dos critérios utilizados para considerar uma diferença justificada, injustificada ou inconclusiva;
- verificação de medidas de tratamento ou mitigação, quando houver;
- análise de riscos residuais.

### Observações metodológicas

- Algumas respostas podem ser obtidas diretamente de resultados já documentados em Model Card ou outros artefatos.
- A interpretação das diferenças entre grupos, sua justificabilidade, necessidade de tratamento e riscos residuais constitui análise específica de Justiça e deve ser registrada em fonte apropriada, como o Fairness Report.
- **Outros efeitos relevantes** devem ser entendidos como efeitos observáveis e pertinentes à Tarefa e ao Contexto de Uso. Conforme o caso, podem incluir desempenho, padrões de erro, calibração, decisões, consequências clínicas, técnicas ou operacionais.
- Nem todos esses efeitos precisam ser avaliados em todos os contextos.
- Diferença numérica não equivale automaticamente a injustiça.
- Ausência de significância estatística não torna automaticamente uma diferença irrelevante.
- A decisão de que uma diferença é aceitável, problemática ou sujeita a tratamento deve explicitar o critério utilizado.
- Não exigir uma métrica específica de fairness sem relação demonstrada com a Tarefa e com o efeito que precisa ser avaliado.

---

## RC03 — Dados, variáveis-alvo e padrões de referência

### Requisito

**Avaliar se os dados, as variáveis-alvo e os padrões de referência utilizados no desenvolvimento e na avaliação da Tarefa de IA são adequados para os grupos e populações identificados.**

### O que o requisito busca verificar

Verificar se características dos dados, das variáveis-alvo e dos padrões de referência podem produzir ou contribuir para diferenças relevantes entre os grupos identificados em RC01.

RC03 não substitui a avaliação geral de qualidade de dados. Em Justiça, o foco é verificar se existe mecanismo plausível de efeito diferenciado entre grupos.

### Aspectos a considerar na aplicabilidade

- RC03 é aplicável quando o desenvolvimento ou a avaliação da Tarefa utiliza dados, variáveis-alvo ou padrões de referência cuja adequação possa ser relevante para os grupos identificados em RC01.
- Ausência de informação sobre dados, target ou referência não justifica não aplicabilidade.
- A análise deve distinguir informações factuais sobre os dados e a tarefa da análise específica de suas implicações para Justiça.
- A adequação pode variar entre grupos mesmo quando o dado, target ou padrão de referência seja aceitável de forma geral.
- Não é necessário presumir que toda limitação dos dados seja uma questão de Justiça; deve existir relação plausível com efeitos diferenciados entre grupos.

### Informações factuais que podem ser necessárias

- representação dos grupos nos dados de desenvolvimento e avaliação;
- grupos com baixa representação ou informação ausente;
- origem e processo de seleção dos dados;
- variável ou variáveis-alvo;
- padrões de referência utilizados em cada etapa;
- processo de rotulagem, adjudicação ou definição de referência;
- limitações conhecidas relacionadas aos dados, targets ou referências.

### Exemplos de evidências pertinentes

- Data Card;
- Model Card;
- documentação de rotulagem;
- documentação de adjudicação;
- estatísticas de composição;
- critérios de inclusão e exclusão;
- documentação de seleção dos dados;
- literatura clínica ou técnica pertinente;
- Fairness Report;
- documentação de concordância entre avaliadores;
- análises adicionais específicas quando necessárias.

### Mecanismos de verificação possíveis

- revisão de composição e cobertura dos grupos;
- análise da origem e do processo de seleção dos dados;
- análise de possíveis diferenças de medição;
- avaliação da adequação da variável-alvo entre grupos;
- avaliação de possíveis desigualdades preexistentes incorporadas pelo target;
- avaliação da adequação ou validade do padrão de referência entre grupos;
- análise da relação plausível entre essas condições e diferenças observadas em RC02;
- revisão metodológica;
- consistência cruzada entre Data Card, Model Card e análise de Justiça.

### Orientação para análise

A resposta pode considerar, conforme pertinente:

- literatura clínica ou técnica;
- diferenças conhecidas entre grupos;
- processo de definição das variáveis-alvo;
- processo de rotulagem;
- concordância entre avaliadores;
- validade do padrão de referência;
- limitações de mensuração;
- cobertura e seleção dos dados;
- mecanismos plausíveis pelos quais uma dessas condições poderia produzir efeitos diferenciados.

A checklist não exige um método único de análise.

### Observações metodológicas

- **Data Card** tende a fornecer composição, proveniência, seleção e limitações dos dados.
- **Model Card** tende a fornecer informações sobre Tarefa, variável-alvo, desenvolvimento, avaliação e desempenho.
- **Fairness Report** deve acrescentar as implicações desses elementos para os grupos considerados, sem repetir desnecessariamente a factualidade já documentada.
- Problemas gerais de qualidade ou validade dos dados pertencem principalmente à dimensão Segurança quando não houver mecanismo plausível de efeito diferenciado entre grupos.
- A pergunta “a variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?” exige fundamentação técnica ou clínica; não deve ser respondida apenas pela existência formal de uma variável-alvo.
- Da mesma forma, a adequação do padrão de referência deve considerar se existem razões para sua validade ou confiabilidade variar entre grupos.
- Ausência de análise específica deve ser registrada como ausência ou insuficiência de evidência, e não como conclusão automática de inadequação.

---

## RC04 — Acesso e possibilidade de benefício

### Requisito

**Avaliar se a forma de disponibilização da Tarefa de IA produz, reproduz ou agrava desigualdades injustificadas entre os grupos e populações identificados quanto à possibilidade de se beneficiar de seu uso.**

### O que o requisito busca verificar

Verificar se a forma concreta pela qual a Tarefa é disponibilizada no Contexto de Uso avaliado cria ou agrava diferenças entre grupos quanto à possibilidade de acessar, utilizar ou se beneficiar da Tarefa.

O requisito trata de desigualdades associadas à disponibilização da Tarefa, e não de diferenças de desempenho já analisadas em RC02.

### Aspectos a considerar na aplicabilidade

- RC04 é aplicável quando, no Contexto de Uso avaliado, existe alguma forma de disponibilização da Tarefa pela qual pessoas, grupos ou populações possam acessar ou se beneficiar de seu uso.
- Se não existe disponibilização da Tarefa no Contexto atual, RC04 pode ser considerado Não aplicável, com justificativa.
- Uso futuro pretendido que ainda não integra o Contexto de Uso não deve ser usado para tornar RC04 aplicável.
- Ausência de análise de acesso não justifica Não aplicável quando a Tarefa já está efetivamente disponibilizada.
- A forma de disponibilização pode envolver infraestrutura, conectividade, localização, idioma, custo, recursos institucionais, letramento, capacidade operacional ou outras condições pertinentes.

### Exemplos de evidências pertinentes

- documentação operacional;
- Model Card;
- descrição do Contexto de Uso;
- fluxos de disponibilização;
- documentação de infraestrutura necessária;
- documentação de usuários ou serviços;
- Fairness Report;
- materiais de uso;
- registros de acesso ou utilização;
- documentação institucional pertinente.

### Mecanismos de verificação possíveis

- verificação da forma concreta de disponibilização;
- identificação de requisitos de acesso ou uso;
- análise de barreiras entre grupos, serviços ou localidades;
- comparação da possibilidade de benefício entre os grupos de RC01;
- análise da justificabilidade de desigualdades de acesso;
- análise de medidas consideradas para reduzir barreiras;
- análise de limitações ou desigualdades residuais.

### Observações metodológicas

- Identificar em RC01 um grupo potencialmente sujeito à exclusão de benefícios não torna RC04 automaticamente aplicável.
- A condição objetiva de RC04 é a existência de disponibilização da Tarefa no Contexto de Uso avaliado.
- Não utilizar benefícios hipotéticos de uma futura implantação para preencher RC04 em uma avaliação exclusivamente experimental.
- Quando RC04 for Não aplicável, suas perguntas substantivas não precisam ser preenchidas como se houvesse ausência de evidência; deve-se registrar a justificativa de não aplicabilidade.
- Se o Contexto de Uso mudar para incluir disponibilização ou uso assistencial, a aplicabilidade de RC04 deve ser reavaliada.

---

## Transparência

> **Status:** requisitos em revisão metodológica.
>
> Esta dimensão ainda não foi consolidada no processo atual de revisão dos requisitos do FIAR-Saúde. Os requisitos e orientações operacionais serão inseridos após sua estabilização.

---

# Uso do guia durante a avaliação

Para cada requisito aplicável:

1. utilizar este guia para compreender o objetivo, os aspectos de aplicabilidade, as evidências pertinentes e os mecanismos de verificação possíveis;
2. determinar **Aplicável** ou **Não aplicável** antes da análise das evidências;
3. registrar a justificativa da decisão de aplicabilidade;
4. identificar o que precisa ser demonstrado;
5. localizar as fontes ou artefatos que fornecem as evidências necessárias;
6. distinguir informação factual já documentada de análise específica ainda necessária;
7. registrar somente evidências efetivamente verificadas no ciclo;
8. analisar suficiência, consistência, rastreabilidade, pertinência, atualidade e contextualização;
9. registrar limitações, pendências e inconsistências somente quando sustentadas pelas evidências;
10. não transformar ausência de artefato específico em resultado automático;
11. não solicitar novamente ao projeto informação já disponível em artefatos adequados;
12. quando a análise específica depender da equipe do projeto, solicitar somente o complemento necessário;
13. quando a questão corresponder a decisão metodológica do NIAR-Saúde, registrá-la internamente e não transferi-la ao projeto como pendência factual.

A avaliação é realizada para a combinação **Tarefa de IA + Versão Avaliável + Contexto de Uso**, considerando também a **Trilha de Execução**.

---

# Referências documentais

## Documentação normativa do FIAR-Saúde

A documentação normativa vigente do FIAR-Saúde permanece como referência superior deste guia.

As referências específicas de cada dimensão deverão ser atualizadas à medida que os respectivos requisitos forem estabilizados no processo atual de revisão metodológica.

Para Justiça, a formulação dos quatro requisitos utilizada nesta versão corresponde ao conjunto estabilizado na revisão metodológica atual da dimensão.

## Documentação operacional relacionada

- `documentacao_metodologica/guia_operacional_pre_avaliacao_pilotos.md`
- instrumentos de avaliação por requisito do NIAR-Saúde;
- checklist operacional de Justiça;
- templates de artefatos do projeto, quando pertinentes.

---

# Controle de atualização

Este arquivo deve acompanhar o estado da revisão metodológica do FIAR-Saúde.

Quando uma dimensão for estabilizada:

1. inserir seus requisitos na seção correspondente;
2. reproduzir as formulações sem alteração;
3. incluir orientação operacional de aplicabilidade, evidências e verificação;
4. revisar sobreposições com dimensões já consolidadas;
5. atualizar o status da dimensão no início deste documento;
6. evitar manter requisitos locais ou versões anteriores que possam ser confundidos com a versão vigente;
7. registrar a alteração no controle de versão do FIAR-Audit-Template.

Quando um requisito for criado, alterado, removido ou renumerado, a mudança deve ser refletida neste guia antes de seu uso em novos ciclos de avaliação.

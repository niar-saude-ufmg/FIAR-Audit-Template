# Guia de Requisitos para Avaliação

Este documento organiza operacionalmente os requisitos do FIAR-Saúde já consolidados no processo atual de revisão metodológica.

As dimensões ainda em revisão permanecem identificadas neste documento, mas sem requisitos operacionais até sua estabilização. Nesta versão, apenas a dimensão **Justiça** está operacionalizada.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas.

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a **Tarefa de IA**, a **Versão Avaliável**, o **Contexto de Uso** e a **Trilha de Execução**.

Um requisito deve ser considerado **Não aplicável** somente quando a condição objetiva pressuposta por sua formulação não estiver presente no objeto avaliado. A ausência de prática, mecanismo, capacidade, procedimento, registro ou evidência que o próprio requisito busca avaliar não constitui justificativa de não aplicabilidade e deve ser refletida posteriormente na análise e no resultado do requisito. Quando a presença da condição objetiva ainda não puder ser determinada, a aplicabilidade não deve ser presumida como Não aplicável.

As orientações deste guia apoiam o preenchimento de `ciclos/Cxx/avaliacao.md`. O fluxo, os resultados possíveis e as regras de pendência estão em `documentacao_metodologica/guia_fluxo.md`. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

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

A identificação dos grupos pode se apoiar no Contexto de Uso, na literatura, na documentação dos dados e no conhecimento clínico ou institucional. Não depende de uma análise prévia de desempenho. Quando relevante para o contexto, considere também combinações de características, como raça/cor e sexo. Os grupos relevantes devem ser identificados mesmo quando os dados disponíveis não permitirem analisá-los.

### Aspectos a considerar na aplicabilidade

- RC01 é aplicável quando a Tarefa, no Contexto de Uso avaliado, pode produzir efeitos ou benefícios que incidam sobre pessoas, grupos ou populações.
- A ausência de dados sobre determinado grupo relevante não torna o requisito não aplicável.
- A ausência de análise prévia de grupos não torna o requisito não aplicável.
- Grupos relevantes podem ser demográficos, territoriais, clínicos, institucionais ou definidos por outra característica pertinente à Tarefa.
- Populações explicitamente fora do escopo validado devem ser registradas como delimitação ou limitação de escopo, e não automaticamente como grupo para comparação de Justiça.
- O uso futuro pretendido não deve ser utilizado para definir grupos do Contexto de Uso atual quando ainda não fizer parte da unidade avaliada.

### Pergunta de aplicabilidade

**A Tarefa, no Contexto de Uso avaliado, pode produzir efeitos ou benefícios que incidam sobre pessoas, grupos ou populações?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

### Roteiro de perguntas

Roteiro de apoio à análise. Não é checklist: responder só o pertinente.

- Quais grupos ou populações podem ser afetados de forma diferente pela Tarefa?
- Por que esses grupos ou populações foram considerados relevantes para esta Tarefa e este Contexto de Uso?
- A identificação decorre do Contexto de Uso e da população pertinente à avaliação, e não apenas dos atributos disponíveis nos dados?
- Existem grupos potencialmente relevantes que não podem ser analisados com os dados disponíveis?
- Existem grupos potencialmente sujeitos a exclusão dos benefícios da Tarefa? (Apenas identificar; a análise de acesso é feita em RC04.)
- Há limitações ou incertezas na identificação dos grupos e populações relevantes?

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

### Pergunta de aplicabilidade

**Existem grupos ou populações identificados em RC01 sobre os quais a Tarefa possa produzir efeitos no Contexto de Uso avaliado?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

A impossibilidade de realizar determinada comparação por ausência ou insuficiência de dados não torna RC02 não aplicável; o resultado é Inconclusivo.

### Roteiro de perguntas

Roteiro de apoio à análise. Não é checklist: responder só o pertinente.

- Para os grupos identificados em RC01, foram analisados o desempenho da Tarefa ou outros efeitos relevantes observáveis no Contexto de Uso avaliado?
- Quais métricas, análises ou outros critérios foram utilizados?
- Foram encontradas diferenças de desempenho, erro ou outros efeitos entre os grupos?
- Foram analisados tipos de erro relevantes, como falsos positivos e falsos negativos, quando pertinentes à Tarefa?
- Existem diferenças nas decisões ou consequências decorrentes dos resultados ou do uso da Tarefa, quando observáveis no Contexto de Uso avaliado?
- As diferenças encontradas foram interpretadas considerando seu significado clínico, técnico ou operacional?
- Quando foram encontradas diferenças, foi analisado se elas são justificadas ou injustificadas? Com base em quê?
- Quais ações para evitar, reduzir ou tratar diferenças consideradas problemáticas foram consideradas? Quais chegaram a ser realizadas, se houver?
- Considerando as ações realizadas, se houver, permanecem diferenças ou riscos relevantes para os grupos identificados?

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

**Variável-alvo** é o resultado que o sistema procura prever. **Padrão de referência** é a informação ou o procedimento usado para estabelecer o resultado considerado correto no desenvolvimento ou na avaliação do sistema. Exemplos incluem diagnóstico confirmado por especialista, resultado de exame ou desfecho registrado, quando utilizados com essa finalidade. Não se refere à métrica nem à meta de desempenho do modelo.

### Aspectos a considerar na aplicabilidade

- RC03 é aplicável quando o desenvolvimento ou a avaliação da Tarefa utiliza dados, variáveis-alvo ou padrões de referência cuja adequação possa ser relevante para os grupos identificados em RC01.
- Ausência de informação sobre dados, target ou referência não justifica não aplicabilidade.
- A análise deve distinguir informações factuais sobre os dados e a tarefa da análise específica de suas implicações para Justiça.
- A adequação pode variar entre grupos mesmo quando o dado, target ou padrão de referência seja aceitável de forma geral.
- Não é necessário presumir que toda limitação dos dados seja uma questão de Justiça; deve existir relação plausível com efeitos diferenciados entre grupos.

### Informações factuais que podem ser necessárias

- representação dos grupos nos dados de desenvolvimento e avaliação;
- grupos com poucos registros ou com informações ausentes ou insuficientes para sua análise;
- origem e processo de seleção dos dados;
- variável ou variáveis-alvo;
- padrões de referência utilizados em cada etapa;
- processo de rotulagem, adjudicação ou definição de referência;
- limitações conhecidas relacionadas aos dados, targets ou referências.

### Pergunta de aplicabilidade

**O desenvolvimento ou a avaliação da Tarefa utiliza dados, variáveis-alvo ou padrões de referência cuja adequação possa ser relevante para os grupos identificados em RC01?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

Ausência de informação sobre os dados, a variável-alvo ou o padrão de referência não justifica Não aplicável.

### Roteiro de perguntas

Roteiro de apoio à análise. Não é checklist: responder só o pertinente. As informações factuais estão na seção anterior; aqui ficam as perguntas de análise para Justiça.

- A origem ou o processo de seleção dos dados pode afetar alguns dos grupos identificados de forma diferente?
- Há razões para considerar os dados inadequados para algum dos grupos identificados?
- A variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?
- A variável-alvo pode incorporar ou refletir desigualdades preexistentes relevantes?
- Há razões para que algum padrão de referência seja menos adequado ou válido para determinados grupos?
- Alguma das limitações ou inadequações identificadas nos dados, nas variáveis-alvo ou nos padrões de referência pode contribuir para diferenças nos efeitos avaliados em RC02?

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

A avaliação não exige um método único de análise.

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

Considere quem pode utilizar a Tarefa, onde e por quais meios, além das condições que podem limitar seus benefícios para as populações afetadas.

### Aspectos a considerar na aplicabilidade

- RC04 é aplicável quando, no Contexto de Uso avaliado, existe alguma forma de disponibilização da Tarefa pela qual pessoas, grupos ou populações possam acessar ou se beneficiar de seu uso.
- Se não existe disponibilização da Tarefa no Contexto atual, RC04 pode ser considerado Não aplicável, com justificativa.
- Uso futuro pretendido que ainda não integra o Contexto de Uso não deve ser usado para tornar RC04 aplicável.
- Ausência de análise de acesso não justifica Não aplicável quando a Tarefa já está efetivamente disponibilizada.
- A forma de disponibilização pode envolver infraestrutura, conectividade, localização, idioma, custo, recursos institucionais, letramento, capacidade operacional ou outras condições pertinentes.

### Pergunta de aplicabilidade

**No Contexto de Uso avaliado, existe alguma forma de disponibilização da Tarefa pela qual pessoas, grupos ou populações possam acessar ou se beneficiar de seu uso?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

Um uso futuro pretendido que ainda não integra o Contexto de Uso avaliado não torna RC04 aplicável ao ciclo atual.

### Roteiro de perguntas

Roteiro de apoio à análise. Não é checklist: responder só o pertinente.

- Como a Tarefa é disponibilizada aos usuários e serviços no Contexto de Uso avaliado: onde, por quais meios e para quem?
- Existem requisitos de infraestrutura, tecnologia ou recursos para acessar ou utilizar a Tarefa?
- Idioma, conectividade, localização, custo, letramento ou outras condições podem limitar a possibilidade de algum grupo acessar ou se beneficiar da Tarefa? Considere tanto as condições dos pacientes quanto as dos profissionais e serviços que utilizam o sistema.
- Existem diferenças entre locais, serviços ou populações quanto à oferta da Tarefa, isto é, onde ou para quem ela está disponível?
- Algum grupo identificado em RC01 possui menor possibilidade de se beneficiar da disponibilização da Tarefa?
- Foi analisado se as desigualdades de acesso ou de possibilidade de benefício identificadas são justificadas ou injustificadas?
- Foram consideradas medidas ou alternativas para evitar, reduzir ou tratar as barreiras de acesso ou de possibilidade de benefício identificadas?
- Considerando as medidas adotadas, se houver, permanecem limitações ou desigualdades de acesso ou de possibilidade de benefício?

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
- análise da justificabilidade de desigualdades de acesso ou de possibilidade de benefício;
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

Para cada requisito, no bloco correspondente de `ciclos/Cxx/avaliacao.md`:

1. responder à pergunta de aplicabilidade, com justificativa, consultando as informações factuais das fontes e antes de julgar o atendimento;
2. identificar o que precisa ser demonstrado;
3. localizar as evidências nas fontes registradas na identificação do ciclo;
4. distinguir informação factual já documentada de análise específica ainda necessária;
5. usar o roteiro de perguntas como apoio, sem tratá-lo como checklist;
6. analisar suficiência, consistência, rastreabilidade e pertinência;
7. atribuir o resultado (Atendido, Não atendido, Inconclusivo com motivo, ou Não aplicável).

Ausência de artefato não é resultado. Não solicitar novamente informação já disponível. Decisão metodológica do NIAR é registrada, não vira pendência. As regras de pendência estão no guia do fluxo.

A avaliação é realizada para a combinação **Tarefa de IA + Versão Avaliável + Contexto de Uso**, considerando também a **Trilha de Execução**.

---

# Referências documentais

## Documentação normativa do FIAR-Saúde

A documentação normativa vigente do FIAR-Saúde permanece como referência superior deste guia.

As referências específicas de cada dimensão deverão ser atualizadas à medida que os respectivos requisitos forem estabilizados no processo atual de revisão metodológica.

Para Justiça, a formulação dos quatro requisitos utilizada nesta versão corresponde ao conjunto estabilizado na revisão metodológica atual da dimensão.

## Documentação operacional relacionada

- `documentacao_metodologica/guia_fluxo.md`
- `ciclos/Cxx/avaliacao.md`
- `documentacao_metodologica/apoio_roteiro_entrevista.md` (material de apoio)
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

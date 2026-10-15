# Guia de Avaliação do FIAR-Saúde

Este documento organiza operacionalmente os requisitos do FIAR-Saúde já consolidados no processo atual de revisão metodológica.

As dimensões ainda em revisão permanecem identificadas neste documento, mas sem requisitos operacionais até sua estabilização. Nesta versão, apenas a dimensão **Justiça** está operacionalizada.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas.

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a **Tarefa de IA**, a **Versão Avaliável**, o **Contexto de Uso** e a **Trilha de Execução**.

Um requisito deve ser considerado **Não aplicável** somente quando a condição objetiva pressuposta por sua formulação não estiver presente no objeto avaliado. A ausência de prática, mecanismo, capacidade, procedimento, registro ou evidência que o próprio requisito busca avaliar não constitui justificativa de não aplicabilidade e deve ser refletida posteriormente na análise e no resultado do requisito. Quando a presença da condição objetiva ainda não puder ser determinada, a aplicabilidade não deve ser presumida como Não aplicável.

As orientações deste guia apoiam o preenchimento de `ciclos/Cxx/identificacao.md` e `ciclos/Cxx/avaliacao.md`. A primeira parte, **Fluxo do ciclo**, trata das etapas, dos resultados possíveis e das regras de pendência. A segunda, **Dimensões e requisitos**, trata de cada requisito. As regras normativas do ciclo estão em `docs/ciclo_avaliacao.md` do FIAR-Saude. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

Nas dimensões já consolidadas na revisão metodológica atual, as formulações dos requisitos devem ser reproduzidas sem alteração. As explicações, exemplos e cautelas deste guia têm função operacional e não criam requisitos adicionais.

---

# Fluxo do ciclo

## Papéis

- **Equipe do projeto:** produz e mantém os artefatos e responde às perguntas do NIAR.
- **NIAR-Saúde**: delimita o ciclo, avalia os requisitos, recomenda e prepara o relatório ao Comitê. Não edita artefatos da equipe.
- **Comitê Gestor**: valida os relatórios e delibera sobre riscos e questões encaminhadas, inclusive condicionantes e restrições de uso. Pode pedir esclarecimentos ou revisão ao NIAR-Saúde, sem refazer a análise técnica. A aceitação de risco não altera os resultados dos requisitos.
- O FIAR-Saúde não é certificação.

## Conceitos

- **Projeto**: iniciativa responsável por uma ou mais Tarefas de IA; guarda o histórico dos ciclos.
- **Tarefa de IA**: modelo, dados e procedimentos orientados a um objetivo clínico ou operacional. Nova tarefa quando mudam objetivo, tipo de resultado ou escopo essencial.
- **Versão Avaliável:** estado da tarefa avaliado no ciclo. Falta de identificador exato não impede automaticamente a avaliação, desde que as evidências possam ser relacionadas à tarefa, ao estado avaliado e ao contexto.
- **Contexto de Uso**: condições em que a tarefa é desenvolvida, avaliada ou usada. Por padrão, o ciclo considera o contexto atual; um uso pretendido pode ser avaliado antes de sua implementação, se explicitamente delimitado e justificado. O uso pretendido que não for objeto do ciclo é registrado separadamente.
- **Unidade de avaliação**: Tarefa + Versão Avaliável + Contexto de Uso.
- **Ciclo:** uma avaliação de uma unidade, da delimitação ao fechamento.
- **Trilha**: Experimental ou Produção; orienta a aplicabilidade dos requisitos e a natureza das evidências.
- **Evidência**: informação que responde ao requisito. Fonte: onde ela está (artefato ou comunicação).
- **Maturidade:** a definir em revisão posterior.

## Etapas do ciclo

1. **Entrada**: formulário do projeto (entrada/), aberto na entrada e atualizado quando houver mudanças relevantes, com um bloco por Tarefa de IA apresentada.
2. **Delimitação:** ciclos/Cxx/identificacao.md. Termina com "pronto para avaliar". Só bloqueia se não for possível identificar a tarefa ou relacionar as evidências a ela.
3. **Avaliação**: ciclos/Cxx/avaliacao.md, um bloco por requisito. RC01 antes dos demais.
4. **Rodadas com a equipe**: uma mensagem por rodada, com as pendências destinadas à equipe. Recomendações podem seguir na mesma mensagem, em parte separada e identificadas como não obrigatórias. A equipe responde pelo canal que preferir; a resposta é guardada em comunicacoes/ e citada na avaliação. Não se exige atualizar um artefato só para transcrever uma resposta; pode ser necessário quando o requisito exigir documentação atualizada ou comunicação a um público.
5. **Fechamento**: resultado de cada requisito e síntese. Se houver gatilho, segue o relatório ao Comitê.

## Resultados por requisito

- **Atendido**: a evidência verificada sustenta o atendimento.
- **Não atendido**: a evidência verificada mostra que o requisito não é cumprido.
- **Inconclusivo:** a evidência disponível não permite concluir. Registrar o motivo (ex.: evidência incompleta, não localizada, aguardando resposta, aplicabilidade não determinada).
- **Não aplicável:** a condição pressuposta pelo requisito não existe na unidade, com justificativa.

Atendimento parcial ou prática apenas planejada não levam automaticamente a Inconclusivo: com evidência suficiente de não atendimento, o resultado é Não atendido.

Ausência de artefato não é resultado. A pergunta é sempre se há evidência para o requisito.

## Pendências

- Existe só ligada à delimitação (D-xx) ou a um requisito (RCxx-Px).
- Serve para delimitar a avaliação, determinar a aplicabilidade ou concluir a análise.
- Antes de abrir: (1) é necessária? (2) já está em alguma fonte? (3) já foi respondida? Só abrir se (1) for sim e as demais forem não.
- **Destinatário**: Equipe (vai na rodada) ou NIAR (verificação interna ou decisão metodológica ainda não tomada).
- Bloqueia só o que está ligado a ela.
- **Estados**: aberta, respondida, encerrada, cancelada (com motivo). Resposta recebida é analisada e não encerra a pendência automaticamente. Só o NIAR encerra, citando a fonte.
- Pendência aberta só torna o requisito Inconclusivo quando impede a conclusão. Com evidência suficiente de não atendimento, registra-se Não atendido. Inconclusivo pode existir sem pendência.

## Inconsistências

Contradição confirmada, dentro de uma fonte ou entre fontes, sobre o mesmo fato, versão e contexto. Informação ausente não é inconsistência. Registrar na identificação (DI-xx) ou no bloco do requisito afetado (RCxx-Ix); gera pendência quando precisar de esclarecimento, com destinatário conforme quem pode resolvê-la.

## Decisões metodológicas e informações não confirmadas

- Decisão metodológica já tomada: registrada no documento que afeta, com justificativa.
- Informação factual: registrada com a fonte. Não se pede nova confirmação à equipe só para repetir o que a fonte já diz.
- Inferência ainda não sustentada: marcada como hipótese do NIAR, com base e limitação. Não substitui fato demonstrado.
- Responsabilidade técnica: não é deduzida. Sem documentação suficiente, fica como não confirmada. Só se pergunta à equipe quando for necessário à delimitação ou a um requisito.

## Encaminhamentos

- Recomendação do NIAR: sugestão à equipe, não obrigatória, não altera resultados.
- Questão para o Comitê: aceite de risco, restrição de uso, responsabilidades ou conflitos que ultrapassam a avaliação técnica.
- Condicionantes só são definidas pelo Comitê (decisoes/).

## Relatório ao Comitê Gestor

Um por projeto (relatorios/RCG-xxx.md), enviado quando houver:

1. primeira avaliação concluída;
2. resultado que muda de categoria, ou risco novo ou agravado, mesmo sem mudança de categoria;
3. mudança de contexto para uso real ou entrada na Trilha Produção;
4. questão para o Comitê;
5. revisão periódica, se definida.

Ciclos que não alteram resultados entram no relatório seguinte. A aceitação de riscos vale para a versão e o contexto avaliados.

## Mudanças relevantes

Quatro tratamentos: só registrar; reavaliar os requisitos afetados; abrir novo ciclo (nova versão ou novo contexto); delimitar nova tarefa. A escolha e o motivo ficam na identificação do novo ciclo ou no commit.

## Histórico

O Git guarda o histórico. Commits citam IDs (D-xx, RCxx-Px, RCG-xxx, DCG-xxx) quando pertinente.

## Material de apoio

documentacao_metodologica/apoio_roteiro_entrevista.md: exemplos de perguntas. Não é checklist; perguntar só o que vier de uma pendência.

---

# Dimensões e requisitos

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

Quando as fontes ou a equipe confirmarem que a identificação ou a avaliação pedida por um requisito não foi feita, há evidência suficiente de não atendimento, e o resultado é Não atendido. Enquanto isso não estiver confirmado, a ausência de análise é registrada como ausência ou insuficiência de evidência (Inconclusivo, com pendência quando necessária). Em nenhum dos casos se conclui, só por isso, que os dados, os efeitos ou o acesso sejam inadequados. Uma fundamentação técnica ou clínica pode constituir avaliação, pois a análise não exige método único.

A identificação de diferença injustificada ou de condição relevante não é suficiente para considerar RC02, RC03 ou RC04 atendido. Deve existir decisão justificada sobre o tratamento do achado, que pode ser técnico, processual ou institucional, envolver restrição de uso ou, quando pertinente, a decisão de não utilizar a Tarefa. (Derivação: 06_Requisitos_Candidatos, TRANSVERSAL-JUS; 07_Sintese_Corpus_Justica, Tratamento dos achados.)

---

## RC01 — Grupos e populações

### Requisito

**Identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.**
**Em palavras simples:** quem pode ser prejudicado pela IA ou ficar sem o benefício dela? E por que esses grupos?

### O que o requisito busca verificar

Verificar se os grupos e populações relevantes para a análise de Justiça foram identificados de forma fundamentada a partir da Tarefa de IA, da população pertinente e do Contexto de Uso avaliado.

O requisito não busca simplesmente listar atributos existentes nos dados. A seleção deve ser justificada pela possibilidade de efeitos diferenciados, exclusão de benefícios, limitações de representação, características clínicas, sociais, territoriais, institucionais ou outras condições relevantes para a Tarefa e o Contexto.

A identificação dos grupos pode **se apoiar no Contexto de Uso, na literatura, na documentação dos dados e no conhecimento clínico ou institucional**. Não depende de uma análise prévia de desempenho. Quando relevante para o contexto, considere também combinações de características, como raça/cor e sexo. Os grupos relevantes devem ser identificados mesmo quando os dados disponíveis não permitirem analisá-los.

### Aspectos a considerar na aplicabilidade

- RC01 é aplicável quando a Tarefa, no Contexto de Uso avaliado, pode produzir efeitos ou benefícios que incidam sobre pessoas, grupos ou populações.
- A ausência de dados sobre determinado grupo relevante não torna o requisito não aplicável.
- A ausência de análise prévia de grupos não torna o requisito não aplicável.
- Grupos relevantes podem ser demográficos, territoriais, clínicos, institucionais ou definidos por outra característica pertinente à Tarefa.
- Populações explicitamente fora do escopo validado devem ser registradas como delimitação ou limitação de escopo, e não automaticamente como grupo para comparação de Justiça.
- O uso futuro pretendido não deve ser utilizado para definir grupos do Contexto de Uso atual quando ainda não fizer parte da unidade avaliada.

### Pergunta de aplicabilidade

**Do jeito que é usada hoje (Contexto de Uso avaliado), a Tarefa pode afetar ou beneficiar pessoas, grupos ou populações?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

### Checklist do avaliador

Para cada item, marque na tabela Checklist de `ciclos/Cxx/avaliacao.md`: **Respondido**, quando as fontes respondem (indique a fonte); **Não localizado**, quando as fontes não respondem (se houver hipótese do NIAR, descreva-a, mas ela não conta como resposta); ou **Não pertinente**, quando o item não se aplica a esta Tarefa (explique por quê). Os itens ajudam a verificar o requisito: não são requisitos e não valem pontos. O resultado é do requisito, não de cada item. Um item Não localizado não vira pendência por si só. Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa.

- **RC01.1** Quais grupos ou populações a Tarefa pode afetar de forma diferente?
- **RC01.2** Por que esses grupos importam para esta Tarefa e este Contexto de Uso?
- **RC01.3** Os grupos foram escolhidos pensando em onde e para quem a Tarefa é usada, e não só porque a informação existe nos dados?
- **RC01.4** Há grupos importantes que os dados não permitem analisar?
- **RC01.5** Há grupos que podem ficar sem o benefício da Tarefa? (Só identificar aqui; o acesso é analisado em RC04.)
- **RC01.6** Há dúvidas ou limites na escolha dos grupos?

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

### Checklist do avaliador

Percorrer todos os itens e registrar a situação de cada um na tabela Checklist de `ciclos/Cxx/avaliacao.md`: Respondido (com a fonte), Não localizado ou Não pertinente (com o motivo). Os itens orientam a verificação: não são requisitos, não recebem pontuação, e um item Não localizado não gera pendência automaticamente; aplicam-se as regras de pendência. O resultado é atribuído ao requisito, não aos itens. Se o requisito for Não aplicável, a tabela não é preenchida; registra-se só a justificativa de não aplicabilidade. Respondido vale quando as fontes respondem ao item; hipótese do NIAR não conta como Respondido: registrar Não localizado e descrever a hipótese.

- **RC02.1** Para os grupos identificados em RC01, foram analisados o desempenho da Tarefa ou outros efeitos relevantes observáveis no Contexto de Uso avaliado?
- **RC02.2** Quais métricas, análises ou outros critérios foram utilizados?
- **RC02.3** Foram encontradas diferenças de desempenho, erro ou outros efeitos entre os grupos?
- **RC02.4** Foram analisados tipos de erro relevantes, como falsos positivos e falsos negativos, quando pertinentes à Tarefa?
- **RC02.5** Existem diferenças nas decisões ou consequências decorrentes dos resultados ou do uso da Tarefa, quando observáveis no Contexto de Uso avaliado?
- **RC02.6** As diferenças encontradas foram interpretadas considerando seu significado clínico, técnico ou operacional?
- **RC02.7** Quando foram encontradas diferenças, foi analisado se elas são justificadas ou injustificadas? Com base em quê?
- **RC02.8** Foram consideradas ações para evitar, reduzir ou tratar diferenças consideradas problemáticas? Se sim, quais? Quais chegaram a ser realizadas, se houver?
- **RC02.9** Considerando as ações realizadas, se houver, permanecem diferenças ou riscos relevantes para os grupos identificados?

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

**Variável-alvo** é o resultado que a Tarefa procura prever. **Padrão de referência** é a informação ou o procedimento usado para estabelecer o resultado considerado correto no desenvolvimento ou na avaliação da Tarefa. Exemplos incluem diagnóstico confirmado por especialista, resultado de exame ou desfecho registrado, quando utilizados com essa finalidade. Não se refere à métrica nem à meta de desempenho do modelo.

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

### Checklist do avaliador

Percorrer todos os itens e registrar a situação de cada um na tabela Checklist de `ciclos/Cxx/avaliacao.md`: Respondido (com a fonte), Não localizado ou Não pertinente (com o motivo). Os itens orientam a verificação: não são requisitos, não recebem pontuação, e um item Não localizado não gera pendência automaticamente; aplicam-se as regras de pendência. O resultado é atribuído ao requisito, não aos itens. Se o requisito for Não aplicável, a tabela não é preenchida; registra-se só a justificativa de não aplicabilidade. Respondido vale quando as fontes respondem ao item; hipótese do NIAR não conta como Respondido: registrar Não localizado e descrever a hipótese. As informações factuais estão na seção anterior; o primeiro item registra onde foram localizadas.

- **RC03.1** As informações factuais de RC03 listadas no guia foram localizadas? Indicar as fontes.
- **RC03.2** A origem ou o processo de seleção dos dados pode afetar alguns dos grupos identificados de forma diferente?
- **RC03.3** Há razões para considerar os dados inadequados para algum dos grupos identificados?
- **RC03.4** A variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?
- **RC03.5** A variável-alvo pode incorporar ou refletir desigualdades preexistentes relevantes?
- **RC03.6** Há razões para que algum padrão de referência seja menos adequado ou válido para determinados grupos?
- **RC03.7** Alguma das limitações ou inadequações identificadas nos dados, nas variáveis-alvo ou nos padrões de referência pode contribuir para diferenças nos efeitos avaliados em RC02?
- **RC03.8** Quando foram identificadas limitações ou inadequações relevantes para algum grupo, há decisão justificada sobre seu tratamento?

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
- Quando utilizado, o **Fairness Report** deve acrescentar as implicações desses elementos para os grupos considerados, sem repetir desnecessariamente a factualidade já documentada.
- Problemas gerais de qualidade ou validade dos dados pertencem principalmente à dimensão Segurança quando não houver mecanismo plausível de efeito diferenciado entre grupos.
- A pergunta “a variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?” exige fundamentação técnica ou clínica; não deve ser respondida apenas pela existência formal de uma variável-alvo.
- Da mesma forma, a adequação do padrão de referência deve considerar se existem razões para sua validade ou confiabilidade variar entre grupos.
- Ausência de análise específica não leva à conclusão automática de inadequação dos dados, da variável-alvo ou do padrão de referência. O resultado do requisito nesse caso segue a Orientação transversal para Justiça.

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

### Checklist do avaliador

Percorrer todos os itens e registrar a situação de cada um na tabela Checklist de `ciclos/Cxx/avaliacao.md`: Respondido (com a fonte), Não localizado ou Não pertinente (com o motivo). Os itens orientam a verificação: não são requisitos, não recebem pontuação, e um item Não localizado não gera pendência automaticamente; aplicam-se as regras de pendência. O resultado é atribuído ao requisito, não aos itens. Se o requisito for Não aplicável, a tabela não é preenchida; registra-se só a justificativa de não aplicabilidade. Respondido vale quando as fontes respondem ao item; hipótese do NIAR não conta como Respondido: registrar Não localizado e descrever a hipótese.

- **RC04.1** Como a Tarefa é disponibilizada aos usuários e serviços no Contexto de Uso avaliado: onde, por quais meios e para quem?
- **RC04.2** Existem requisitos de infraestrutura, tecnologia ou recursos para acessar ou utilizar a Tarefa?
- **RC04.3** Idioma, conectividade, localização, custo, letramento ou outras condições podem limitar a possibilidade de algum grupo acessar ou se beneficiar da Tarefa? Considere tanto as condições dos pacientes quanto as dos profissionais e serviços que utilizam a Tarefa.
- **RC04.4** Existem diferenças entre locais, serviços ou populações quanto à oferta da Tarefa, isto é, onde ou para quem ela está disponível?
- **RC04.5** Algum grupo identificado em RC01 possui menor possibilidade de se beneficiar da disponibilização da Tarefa?
- **RC04.6** Foi analisado se as desigualdades de acesso ou de possibilidade de benefício identificadas são justificadas ou injustificadas?
- **RC04.7** Foram consideradas medidas ou alternativas para evitar, reduzir ou tratar as barreiras de acesso ou de possibilidade de benefício identificadas?
- **RC04.8** Considerando as medidas adotadas, se houver, permanecem limitações ou desigualdades de acesso ou de possibilidade de benefício?

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
5. percorrer o checklist do requisito e registrar a situação de cada item na tabela Checklist de `avaliacao.md`;
6. analisar suficiência, consistência, rastreabilidade e pertinência;
7. atribuir o resultado (Atendido, Não atendido, Inconclusivo com motivo, ou Não aplicável).

Ausência de artefato não é resultado. Não solicitar novamente informação já disponível. Decisão metodológica do NIAR é registrada, não vira pendência. As regras de pendência estão na seção Pendências, em Fluxo do ciclo.

A avaliação é realizada para a combinação **Tarefa de IA + Versão Avaliável + Contexto de Uso**, considerando também a **Trilha de Execução**.

---

# Referências documentais

## Documentação normativa do FIAR-Saúde

A documentação normativa vigente do FIAR-Saúde permanece como referência superior deste guia.

As referências específicas de cada dimensão deverão ser atualizadas à medida que os respectivos requisitos forem estabilizados no processo atual de revisão metodológica.

Para Justiça, a formulação dos quatro requisitos utilizada nesta versão corresponde ao conjunto estabilizado na revisão metodológica atual da dimensão.

A fundamentação de **RC01–RC04** está registrada em [`docs/mapeamento_referencias.md`](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/mapeamento_referencias.md) do FIAR-Saude, com as fontes principais por requisito e a distinção entre fundamentação substantiva, apoio técnico-operacional e literatura científica. Os IDs das fontes e a cadeia de derivação remetem à planilha de reconstrução de Justiça ([`docs/fontes/derivacao_requisitos_justica.xlsm`](https://github.com/niar-saude-ufmg/FIAR-Saude/blob/main/docs/fontes/derivacao_requisitos_justica.xlsm), no FIAR-Saude), especialmente às abas `04_Extracoes`, `06_Requisitos_Candidatos` e `07_Sintese_Corpus_Justica`. As fontes apoiam a fundamentação dos requisitos; não tornam métricas, métodos ou artefatos específicos obrigatórios.

## Documentação operacional relacionada

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

Ao alterar o checklist de um requisito, atualizar também a tabela Checklist correspondente em `ciclos/C01/avaliacao.md`.

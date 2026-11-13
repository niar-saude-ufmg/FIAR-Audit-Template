# Guia de Avaliação do FIAR-Saúde

Este documento organiza operacionalmente os requisitos do FIAR-Saúde já consolidados no processo atual de revisão metodológica.

As dimensões ainda em revisão permanecem identificadas neste documento, mas sem requisitos operacionais até sua estabilização. Nesta versão, apenas a dimensão **Justiça** está operacionalizada.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas. A exceção são os relatórios de dimensão definidos como obrigatórios na documentação de cada dimensão; em Justiça, o Fairness Report (ver Orientação transversal para Justiça).

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a **Tarefa de IA**, a **Versão Avaliável**, o **Contexto de Uso** e a **Trilha de Execução**.

Um requisito deve ser considerado **Não aplicável** somente quando a condição objetiva pressuposta por sua formulação não estiver presente no objeto avaliado. A ausência de prática, mecanismo, capacidade, procedimento, registro ou evidência que o próprio requisito busca avaliar não constitui justificativa de não aplicabilidade e deve ser refletida posteriormente na análise e no resultado do requisito. Quando a presença da condição objetiva ainda não puder ser determinada, a aplicabilidade não deve ser presumida como Não aplicável.

As orientações deste guia apoiam o preenchimento de `ciclos/Cxx/identificacao.md` e `ciclos/Cxx/avaliacao.md` e a verificação dos relatórios de dimensão. A primeira parte, **Fluxo do ciclo**, trata das etapas, dos resultados possíveis e das regras de pendência, lacuna e inconsistência. A segunda, **Dimensões e requisitos**, trata de cada requisito. As regras normativas do ciclo estão em `docs/ciclo_avaliacao.md` do FIAR-Saude. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

Nas dimensões já consolidadas na revisão metodológica atual, as formulações dos requisitos devem ser reproduzidas sem alteração. As explicações, exemplos e cautelas deste guia têm função operacional e não criam requisitos adicionais.

---

# Fluxo do ciclo

## Papéis

- **Equipe do projeto:** produz e mantém os artefatos, confere, completa e assina os relatórios de dimensão e responde às lacunas e perguntas do NIAR.
- **NIAR-Saúde**: delimita o ciclo, verifica os relatórios de dimensão com as demais evidências, aponta lacunas, avalia os requisitos, recomenda e prepara o relatório ao Comitê. Não edita artefatos da equipe.
- **Comitê Gestor**: valida os relatórios de avaliação do NIAR-Saúde e delibera sobre riscos e questões encaminhadas, inclusive condicionantes e restrições de uso. Pode pedir esclarecimentos ou revisão ao NIAR-Saúde, sem refazer a análise técnica. A aceitação de risco não altera os resultados dos requisitos. Lê a síntese da equipe de cada relatório de dimensão, apresentada no relatório do NIAR-Saúde.
- **Agentes**: o agente da sala segura pré-preenche os relatórios de dimensão; sem ele, o NIAR, ou um agente a seu serviço pode pré-preencher um rascunho (ver Etapas do ciclo). Outro agente pode rascunhar a verificação para o NIAR. Quem produz e quem verifica são agentes separados. Todo texto de agente é validado pela equipe ou pelo NIAR.
- O FIAR-Saúde não é certificação.

## Conceitos

- **Projeto**: iniciativa responsável por uma ou mais Tarefas de IA; guarda o histórico dos ciclos.
- **Tarefa de IA**: modelo, dados e procedimentos orientados a um objetivo clínico, assistencial, operacional ou de pesquisa. Nova tarefa quando mudam objetivo, tipo de resultado ou escopo essencial. Modelo é um componente cujos parâmetros são ajustados ou aprendidos a partir de dados (por exemplo, aprendizado de máquina ou modelo estatístico, como o pareamento probabilístico de registros). Procedimento só com regras fixas definidas por pessoas não é Tarefa de IA; quando gera dados usados por uma Tarefa de IA, é examinado na avaliação dela (RC03).
- **Versão Avaliável:** estado da tarefa avaliado no ciclo. Falta de identificador exato não impede automaticamente a avaliação, desde que as evidências possam ser relacionadas à tarefa, ao estado avaliado e ao contexto.
- **Contexto de Uso**: condições em que a tarefa é desenvolvida, avaliada ou usada. Por padrão, o ciclo considera o contexto atual; um uso pretendido pode ser avaliado antes de sua implementação, se explicitamente delimitado e justificado. O uso pretendido que não for objeto do ciclo é registrado separadamente.
- **Unidade de avaliação**: Tarefa + Versão Avaliável + Contexto de Uso.
- **Ciclo:** uma avaliação de uma unidade, da delimitação ao fechamento.
- **Trilha**: Experimental ou Produção; orienta a aplicabilidade dos requisitos e a natureza das evidências.
- **Evidência**: informação que responde ao requisito. Fonte: onde ela está (artefato ou comunicação).
- **Relatório de dimensão**: artefato da equipe com sua posição formal e assinada sobre os requisitos de uma dimensão. Cada dimensão define se ele é obrigatório e qual é o modelo; em Justiça, é o Fairness Report (modelo em `artefatos/fairness_reports/fairness_report.md` do FIAR-Audit-Template; no repositório do projeto, o relatório fica em `artefatos/fairness_reports/`). Tarefa, Versão, Contexto e Trilha são os da identificação. Cada nova versão lista as lacunas a que responde.
- **Lacuna**: ponto do relatório de dimensão que impede concluir um requisito (ver Lacunas).
- **Maturidade:** a definir em revisão posterior.

## Etapas do ciclo

1. **Entrada**: formulário do projeto (entrada/), aberto na entrada e atualizado quando houver mudanças relevantes, com um bloco por Tarefa de IA apresentada.
2. **Delimitação:** ciclos/Cxx/identificacao.md. Termina com "pronto para avaliar", que libera o relatório de dimensão e a avaliação. Só bloqueia se não for possível identificar a tarefa ou relacionar as evidências a ela.
3. **Relatório de dimensão**: nas dimensões com relatório obrigatório, o agente da sala segura pré-preenche o relatório com a execução, o Model Card e o Data Card. Sem execução na sala segura, os fatos vêm de publicações ou relatórios técnicos, indicados como fonte. Sem agente da sala segura, o NIAR, ou um agente a seu serviço, pode pré-preencher o relatório como rascunho, a partir do Model Card, do Data Card, de publicações e das comunicações registradas em comunicacoes/; esse agente não é o que verifica o relatório. Em cada campo, o agente marca a origem e a versão e aponta as divergências entre as fontes. Fatos tirados de comunicações entram com a fonte (arquivo e data). Campos de julgamento pré-preenchidos a partir do Model Card ou de comunicações da equipe vêm marcados "a confirmar". A equipe confere, confirma ou corrige, completa os julgamentos e assina. O relatório só passa a ser posição da equipe quando ela o assina. Tarefa, Versão, Contexto e Trilha são iguais aos da identificação.
4. **Avaliação**: ciclos/Cxx/avaliacao.md, um bloco por requisito. RC01 antes dos demais. O NIAR verifica cada campo do relatório de dimensão com as evidências e aponta lacunas. O avaliacao.md aponta para os campos do relatório e não reescreve os fatos.
5. **Rodadas com a equipe**: uma mensagem por rodada, com as lacunas e as pendências destinadas à equipe, a versão do relatório de dimensão verificada e o prazo. A mensagem cita o commit ou a versão dos arquivos a conferir. Recomendações podem seguir na mesma mensagem, em parte separada e identificadas como não obrigatórias. A equipe responde às lacunas em nova versão do relatório de dimensão e às pendências pelo canal que preferir; a resposta é guardada em comunicacoes/ e citada na avaliação. O NIAR reavalia os requisitos afetados. Não se exige atualizar um artefato só para transcrever uma resposta; pode ser necessário quando o requisito exigir documentação atualizada ou comunicação a um público.
6. **Fechamento**: resultado de cada requisito, pendências e lacunas remanescentes e síntese. Se houver gatilho, segue o relatório ao Comitê.

## Resultados por requisito

- **Atendido**: a evidência verificada sustenta o atendimento.
- **Não atendido**: a evidência verificada mostra que o requisito não é cumprido.
- **Inconclusivo:** a evidência disponível não permite concluir. Registrar o motivo (ex.: evidência incompleta, não localizada, aguardando resposta, aplicabilidade não determinada, relatório de dimensão não entregue).
- **Não aplicável:** a condição pressuposta pelo requisito não existe na unidade, com justificativa.

Atendimento parcial ou prática apenas planejada não levam automaticamente a Inconclusivo: com evidência suficiente de não atendimento, o resultado é Não atendido.

Ausência de artefato não é resultado. A pergunta é sempre se há evidência para o requisito.

Se um relatório de dimensão obrigatório não for entregue no prazo, os requisitos da dimensão ficam Inconclusivos, com o motivo "relatório de dimensão não entregue", salvo evidência suficiente de não atendimento.

## Pendências

- Existe só ligada à delimitação (D-xx) ou a um requisito (RCxx-Px).
- Serve para delimitar a avaliação, determinar a aplicabilidade ou concluir a análise.
- Antes de abrir: (1) é necessária? (2) já está em alguma fonte? (3) já foi respondida? Só abrir se (1) for sim e as demais forem não.
- Se a fonte responde em parte, a questão cita o que já está documentado e pergunta só o que falta.
- **Destinatário**: Equipe (vai na rodada) ou NIAR (verificação interna ou decisão metodológica ainda não tomada). Nas dimensões com relatório, pergunta à equipe sobre o conteúdo de um requisito é lacuna, não pendência. A pendência de requisito fica para verificação interna do NIAR e para pedidos que não cabem no relatório, como o acesso a uma fonte. A pendência de delimitação (D-xx) não muda.
- Bloqueia só o que está ligado a ela.
- **Estados**: aberta, respondida, encerrada, cancelada (com motivo). Resposta recebida é analisada e não encerra a pendência automaticamente. Só o NIAR encerra, citando a fonte.
- Pendência aberta só torna o requisito Inconclusivo quando impede a conclusão. Com evidência suficiente de não atendimento, registra-se Não atendido. Inconclusivo pode existir sem pendência.

## Lacunas

- Ponto do relatório de dimensão que impede concluir um requisito: campo vazio, campo que não responde ao item, falta de fonte, julgamento sem fundamento ou sem autor, divergência com outra evidência ou campo que segue marcado "a confirmar" na versão assinada.
- **Quem aponta**: o NIAR, ao verificar o relatório. Um agente pode rascunhar, desde que não seja o que preencheu o relatório. O NIAR valida.
- **ID**: RCxx-Ly, numerado por requisito dentro do ciclo (ex.: RC02-L1). Fora do ciclo, cite junto com o ciclo (ex.: C01 RC02-L1).
- **Onde fica**: na tabela Lacunas do bloco do requisito em `ciclos/Cxx/avaliacao.md`. O pedido à equipe fica em comunicacoes/ e traz as lacunas, a versão do relatório verificada e o prazo.
- **Prazo**: definido pelo NIAR no pedido de cada rodada.
- **Resposta**: nova versão do relatório de dimensão, que lista as lacunas a que responde.
- **Estados**: aberta, respondida, encerrada, cancelada (com motivo). A lacuna fica respondida quando chega a nova versão. Só o NIAR encerra, citando a versão e o campo do relatório.
- Antes de abrir: (1) é necessária para concluir o requisito? (2) a resposta já está no relatório ou em outra fonte? (3) já foi apontada? Só abrir se (1) for sim e as demais forem não. Item Não localizado não vira lacuna por si só.
- Lacuna aberta só torna o requisito Inconclusivo quando impede a conclusão. Com evidência suficiente de não atendimento, registra-se Não atendido. Vencido o prazo, o NIAR conclui com o que houver. Lacuna aberta no fechamento entra nas lacunas remanescentes.
- Nas dimensões com relatório, pergunta à equipe sobre o conteúdo de um requisito é lacuna. A pendência de requisito fica para verificação interna do NIAR e para pedidos que não cabem no relatório, como o acesso a uma fonte. A pendência de delimitação (D-xx) não muda.
- Pendência de aplicabilidade não é lacuna: a aplicabilidade é decidida pelo NIAR, mesmo quando depende de informação da equipe.


## Inconsistências

Contradição confirmada, dentro de uma fonte ou entre fontes, sobre o mesmo fato, versão e contexto. Informação ausente não é inconsistência. Registrar na identificação (DI-xx) ou no bloco do requisito afetado (RCxx-Ix); gera pendência quando precisar de esclarecimento, com destinatário conforme quem pode resolvê-la. Inconsistência entre um relatório de dimensão e outra fonte gera lacuna.

Estados: aberta; resolvida (com a fonte que a resolve); cancelada (com motivo, ex.: a revisão mostrou que não se tratava do mesmo fato, versão ou contexto). Inconsistência aberta no fechamento entra nas limitações.

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

Ciclos que não alteram resultados entram no relatório seguinte. A aceitação de riscos vale para a versão e o contexto avaliados. O relatório inclui a síntese da equipe de cada relatório de dimensão, identificada como posição da equipe e separada da análise do NIAR.

## Mudanças relevantes

Quatro tratamentos: só registrar; reavaliar os requisitos afetados; abrir novo ciclo (nova versão ou novo contexto); delimitar nova tarefa. A escolha e o motivo ficam na identificação do novo ciclo ou no commit. Mudança listada na síntese de um relatório de dimensão como motivo de nova versão exige nova versão desse relatório.

## Histórico

O Git guarda o histórico. Commits citam IDs (D-xx, RCxx-Px, RCxx-Ly, DI-xx, RCxx-Ix, RCG-xxx, DCG-xxx) quando pertinente.

## Material de apoio

documentacao_metodologica/apoio_roteiro_entrevista.md: exemplos de perguntas. Não é checklist; perguntar só o que vier de uma pendência ou de uma lacuna.

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

O **Fairness Report** é o relatório de dimensão de Justiça. É obrigatório nesta dimensão, nas Trilhas Experimental e Produção, e é a posição formal da equipe. O modelo está em `artefatos/fairness_reports/fairness_report.md`. Os campos [A] resumem a informação factual, com fonte e versão: execução na sala segura, Data Card, Model Card ou outro documento. Sem execução na sala segura, os fatos vêm de publicações ou relatórios técnicos, indicados como fonte. Os campos [J] trazem a análise específica de Justiça e são assinados pela equipe. Cada campo indica o item do checklist a que responde (RCxx.y).

O avaliador lê o campo que responde a cada item e o confere com as evidências. O avaliacao.md aponta para o campo e não reescreve os fatos. Os estados do relatório são da equipe: Analisável Sim/Não; justificada, injustificada ou sem conclusão; considerada, realizada ou descartada; OBRIGATÓRIO/CONDICIONAL. O resultado do requisito e a situação do item são do NIAR e ficam só no avaliacao.md.

Quando as fontes ou o Fairness Report confirmarem que a identificação ou a avaliação pedida por um requisito não foi feita, há evidência suficiente de não atendimento, e o resultado é Não atendido. Enquanto isso não estiver confirmado, a ausência de análise é registrada como ausência ou insuficiência de evidência (Inconclusivo, com lacuna quando necessária). Em nenhum dos casos se conclui, só por isso, que os dados, os efeitos ou o acesso sejam inadequados. Uma fundamentação técnica ou clínica pode constituir avaliação, pois a análise não exige método único.

A identificação de diferença injustificada ou de condição relevante não é suficiente para considerar RC02, RC03 ou RC04 atendido. Deve existir decisão justificada sobre o tratamento do achado, que pode ser técnico, processual ou institucional, envolver restrição de uso ou, quando pertinente, a decisão de não utilizar a Tarefa. Uma diferença ou barreira classificada como sem conclusão também exige decisão sobre o que fazer, por exemplo nova análise ou monitoramento. (Derivação: 06_Requisitos_Candidatos, TRANSVERSAL-JUS; 07_Sintese_Corpus_Justica, Tratamento dos achados.)

---

## RC01 — Grupos e populações

### Requisito

**Identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.**
**Em palavras simples:** quais grupos podem ser prejudicados pela Tarefa ou ficar sem seus benefícios, e por quê?

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

**No uso atual (Contexto de Uso avaliado), a Tarefa pode afetar ou beneficiar pessoas, grupos ou populações?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

### Checklist do avaliador

Para cada item, marque na tabela Checklist de `ciclos/Cxx/avaliacao.md`: **Respondido**, quando o campo do Fairness Report indicado pelo código do item responde e as evidências o sustentam (indique o campo e a fonte); **Não localizado**, quando o campo está vazio ou não responde (se houver hipótese do NIAR, descreva-a, mas ela não conta como resposta); ou **Não pertinente**, quando o item não se aplica a esta Tarefa (explique por quê). Os itens ajudam a verificar o requisito: não são requisitos e não valem pontos. O resultado é do requisito, não de cada item. Um item Não localizado não vira lacuna nem pendência por si só. Divergência entre o relatório e outra fonte é inconsistência (RCxx-Ix). Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa.

- **RC01.1** Quais grupos ou populações a Tarefa pode afetar de forma diferente?
- **RC01.2** Por que esses grupos são relevantes para esta Tarefa e este Contexto de Uso?
- **RC01.3** Os grupos foram escolhidos com base no Contexto de Uso e na população atendida, e não apenas porque a informação existe nos dados?
- **RC01.4** Há grupos relevantes que os dados disponíveis não permitem analisar?
- **RC01.5** Há grupos que podem ficar sem os benefícios da Tarefa? (Apenas identificar; o acesso é analisado em RC04.)
- **RC01.6** Há limitações ou incertezas na escolha dos grupos?

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
- Fairness Report (Seção 1).

Esses exemplos não constituem lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto. O Fairness Report é a exceção: é obrigatório em Justiça.

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
- Quando a relevância dos grupos ou a completude de sua seleção não estiver explicitamente fundamentada, essa análise é registrada pela equipe no Fairness Report (1.1 e 1.2).
- A ausência de raça/etnia ou de outro atributo potencialmente relevante deve ser registrada como limitação quando impedir a análise; não deve ser preenchida por inferência.
- Identificar um grupo potencialmente sujeito à exclusão de benefícios em RC01 não equivale a analisar desigualdades de acesso. Essa análise pertence a RC04 quando aplicável.
- Não utilizar afirmações sobre implantação ou benefício futuro como evidência do Contexto de Uso atual.

---

## RC02 — Diferenças nos efeitos

### Requisito

**Avaliar se a Tarefa de IA produz, reproduz ou agrava diferenças injustificadas nos efeitos sobre os grupos e populações identificados.**

**Em palavras simples:** a Tarefa tem desempenho ou efeitos piores para algum grupo de RC01? Se tem, há justificativa?

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

**No uso atual (Contexto de Uso avaliado), a Tarefa pode ter efeitos sobre algum grupo identificado em RC01?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

A impossibilidade de realizar determinada comparação por ausência ou insuficiência de dados não torna RC02 não aplicável; o resultado é Inconclusivo.

### Checklist do avaliador

Para cada item, marque na tabela Checklist de `ciclos/Cxx/avaliacao.md`: **Respondido**, quando o campo do Fairness Report indicado pelo código do item responde e as evidências o sustentam (indique o campo e a fonte); **Não localizado**, quando o campo está vazio ou não responde (se houver hipótese do NIAR, descreva-a, mas ela não conta como resposta); ou **Não pertinente**, quando o item não se aplica a esta Tarefa (explique por quê). Os itens ajudam a verificar o requisito: não são requisitos e não valem pontos. O resultado é do requisito, não de cada item. Um item Não localizado não vira lacuna nem pendência por si só. Divergência entre o relatório e outra fonte é inconsistência (RCxx-Ix). Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa.

- **RC02.1** Foram analisados o desempenho ou os efeitos da Tarefa para cada grupo de RC01?
- **RC02.2** Quais métricas, análises ou critérios foram utilizados?
- **RC02.3** Foram encontradas diferenças entre os grupos (no desempenho, nos erros ou em outros efeitos)?
- **RC02.4** Foram analisados os tipos de erro que importam para esta Tarefa (por exemplo, falsos positivos e falsos negativos)?
- **RC02.5** Quando a Tarefa já influencia decisões, há diferenças entre os grupos nessas decisões ou em suas consequências?
- **RC02.6** Foi analisado o significado prático das diferenças (clínico, técnico ou operacional)?
- **RC02.7** As diferenças foram consideradas justificadas ou não? Com base em qual critério?
- **RC02.8** Para as diferenças consideradas problemáticas, foram previstas ações para evitá-las, reduzi-las ou tratá-las? Quais? Alguma foi realizada?
- **RC02.9** Após as ações realizadas, se houver, permanecem diferenças ou riscos relevantes para os grupos?

### Exemplos de evidências pertinentes

- resultados estratificados;
- métricas por grupo;
- análise de erros;
- Model Card;
- resultados experimentais;
- Fairness Report (Seção 2);
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
- verificação dos critérios utilizados para considerar uma diferença justificada, injustificada ou sem conclusão;
- verificação de medidas de tratamento ou mitigação, quando houver;
- análise de riscos residuais.

### Observações metodológicas

- Algumas respostas podem ser obtidas diretamente de resultados já documentados em Model Card ou outros artefatos.
- A interpretação das diferenças entre grupos, sua justificabilidade, necessidade de tratamento e riscos residuais constitui análise específica de Justiça e é registrada pela equipe no Fairness Report (2.4 a 2.6).
- **Outros efeitos relevantes** devem ser entendidos como efeitos observáveis e pertinentes à Tarefa e ao Contexto de Uso. Conforme o caso, podem incluir desempenho, padrões de erro, calibração, decisões, consequências clínicas, técnicas ou operacionais.
- Nem todos esses efeitos precisam ser avaliados em todos os contextos.
- Diferença numérica não equivale automaticamente a injustiça.
- Ausência de significância estatística não torna automaticamente uma diferença irrelevante.
- A classificação de uma diferença como justificada, injustificada ou sem conclusão, e a decisão sobre seu tratamento, devem explicitar o critério utilizado.
- Não exigir uma métrica específica de fairness sem relação demonstrada com a Tarefa e com o efeito que precisa ser avaliado.

---

## RC03 — Dados, variáveis-alvo e padrões de referência

### Requisito

**Avaliar se os dados, as variáveis-alvo e os padrões de referência utilizados no desenvolvimento e na avaliação da Tarefa de IA são adequados para os grupos e populações identificados.**

**Em palavras simples:** os dados de treino e de teste, o que a Tarefa procura prever e o que serve como resposta correta são adequados para todos os grupos de RC01?

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

**Para desenvolver ou avaliar a Tarefa, foram usados dados, variáveis-alvo ou padrões de referência que podem servir melhor para uns grupos de RC01 do que para outros?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

Ausência de informação sobre os dados, a variável-alvo ou o padrão de referência não justifica Não aplicável.

### Checklist do avaliador

Para cada item, marque na tabela Checklist de `ciclos/Cxx/avaliacao.md`: **Respondido**, quando o campo do Fairness Report indicado pelo código do item responde e as evidências o sustentam (indique o campo e a fonte); **Não localizado**, quando o campo está vazio ou não responde (se houver hipótese do NIAR, descreva-a, mas ela não conta como resposta); ou **Não pertinente**, quando o item não se aplica a esta Tarefa (explique por quê). Os itens ajudam a verificar o requisito: não são requisitos e não valem pontos. O resultado é do requisito, não de cada item. Um item Não localizado não vira lacuna nem pendência por si só. Divergência entre o relatório e outra fonte é inconsistência (RCxx-Ix). Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa. As informações factuais estão na seção anterior; o primeiro item registra onde foram localizadas.

- **RC03.1** As informações factuais de RC03 listadas no guia foram encontradas? Indique as fontes.
- **RC03.2** A origem dos dados, ou a forma como foram selecionados, pode afetar algum grupo de RC01 de forma diferente?
- **RC03.3** Há motivos para considerar os dados inadequados para algum grupo de RC01?
- **RC03.4** A variável-alvo (o que a Tarefa procura prever) mede adequadamente o fenômeno de interesse para todos os grupos?
- **RC03.5** A variável-alvo pode refletir desigualdades já existentes (por exemplo, diferenças de acesso a serviços de saúde)?
- **RC03.6** O padrão de referência (o que serve como resposta correta) pode ser menos confiável para algum grupo?
- **RC03.7** Algum problema encontrado nos dados, na variável-alvo ou no padrão de referência pode causar ou aumentar diferenças nos efeitos analisados em RC02?
- **RC03.8** Para os problemas identificados em algum grupo, há decisão justificada sobre seu tratamento?

### Exemplos de evidências pertinentes

- Data Card;
- Model Card;
- documentação de rotulagem;
- documentação de adjudicação;
- estatísticas de composição;
- critérios de inclusão e exclusão;
- documentação de seleção dos dados;
- literatura clínica ou técnica pertinente;
- Fairness Report (Seção 3);
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
- O **Fairness Report** resume os fatos em 3.1, com fonte e versão, e acrescenta em 3.2 as implicações desses elementos para os grupos considerados.
- Problemas gerais de qualidade ou validade dos dados pertencem principalmente à dimensão Segurança quando não houver mecanismo plausível de efeito diferenciado entre grupos.
- A pergunta “a variável-alvo mede ou representa adequadamente o fenômeno de interesse para os diferentes grupos?” exige fundamentação técnica ou clínica; não deve ser respondida apenas pela existência formal de uma variável-alvo.
- Da mesma forma, a adequação do padrão de referência deve considerar se existem razões para sua validade ou confiabilidade variar entre grupos.
- Ausência de análise específica não leva à conclusão automática de inadequação dos dados, da variável-alvo ou do padrão de referência. O resultado do requisito nesse caso segue a Orientação transversal para Justiça.

---

## RC04 — Acesso e possibilidade de benefício

### Requisito

**Avaliar se a forma de disponibilização da Tarefa de IA produz, reproduz ou agrava desigualdades injustificadas entre os grupos e populações identificados quanto à possibilidade de se beneficiar de seu uso.**

**Em palavras simples:** a forma como a Tarefa é disponibilizada permite que todos os grupos de RC01 a utilizem e se beneficiem dela? Quando não permite, há justificativa?

### O que o requisito busca verificar

Verificar se a forma concreta pela qual a Tarefa é disponibilizada no Contexto de Uso avaliado cria ou agrava diferenças entre grupos quanto à possibilidade de acessar, utilizar ou se beneficiar da Tarefa.

O requisito trata de desigualdades associadas à disponibilização da Tarefa, e não de diferenças de desempenho já analisadas em RC02.

Considere quem pode utilizar a Tarefa, onde e por quais meios, além das condições que podem limitar seus benefícios para as populações afetadas.

### Aspectos a considerar na aplicabilidade

- RC04 é aplicável quando, no Contexto de Uso avaliado, existe alguma forma de disponibilização da Tarefa pela qual pessoas, grupos ou populações possam acessar ou se beneficiar de seu uso.
- Se não existe disponibilização da Tarefa no Contexto atual, RC04 pode ser considerado Não aplicável, com justificativa.
- Uso futuro pretendido que ainda não integra o Contexto de Uso não deve ser usado para tornar RC04 aplicável.
- A equipe registra na Seção 4 do Fairness Report (CONDICIONAL) se a Tarefa não está disponível no uso atual e por quê. O NIAR confirma ou não; o registro da equipe não define a aplicabilidade.
- Ausência de análise de acesso não justifica Não aplicável quando a Tarefa já está efetivamente disponibilizada.
- A forma de disponibilização pode envolver infraestrutura, conectividade, localização, idioma, custo, recursos institucionais, letramento, capacidade operacional ou outras condições pertinentes.

### Pergunta de aplicabilidade

**No uso atual (Contexto de Uso avaliado), a Tarefa já está disponível de alguma forma que permita a pessoas, grupos ou populações utilizá-la ou se beneficiar dela?**

Se não for possível determinar, registrar pendência de aplicabilidade e resultado Inconclusivo, com o motivo "aplicabilidade não determinada". Não presumir Não aplicável.

Um uso futuro pretendido que ainda não integra o Contexto de Uso avaliado não torna RC04 aplicável ao ciclo atual.

### Checklist do avaliador

Para cada item, marque na tabela Checklist de `ciclos/Cxx/avaliacao.md`: **Respondido**, quando o campo do Fairness Report indicado pelo código do item responde e as evidências o sustentam (indique o campo e a fonte); **Não localizado**, quando o campo está vazio ou não responde (se houver hipótese do NIAR, descreva-a, mas ela não conta como resposta); ou **Não pertinente**, quando o item não se aplica a esta Tarefa (explique por quê). Os itens ajudam a verificar o requisito: não são requisitos e não valem pontos. O resultado é do requisito, não de cada item. Um item Não localizado não vira lacuna nem pendência por si só. Divergência entre o relatório e outra fonte é inconsistência (RCxx-Ix). Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa.

- **RC04.1** Como a Tarefa é disponibilizada hoje aos usuários e serviços: onde, por quais meios e para quem?
- **RC04.2** O uso da Tarefa exige alguma infraestrutura, tecnologia ou recurso?
- **RC04.3** Idioma, conexão, localização, custo, letramento ou outras condições podem dificultar que algum grupo utilize a Tarefa ou se beneficie dela? Considere pacientes, profissionais e serviços.
- **RC04.4** A Tarefa está disponível em alguns locais, serviços ou populações e em outros não?
- **RC04.5** Pela forma como a Tarefa é disponibilizada, algum grupo de RC01 tem menos possibilidade de se beneficiar dela?
- **RC04.6** Foi analisado se as diferenças de acesso ou de benefício são justificadas ou não?
- **RC04.7** Foram previstas medidas ou alternativas para evitar, reduzir ou tratar essas barreiras de acesso ou de benefício?
- **RC04.8** Após as medidas adotadas, se houver, permanecem limitações ou diferenças de acesso ou de benefício?

### Exemplos de evidências pertinentes

- documentação operacional;
- Model Card;
- descrição do Contexto de Uso;
- fluxos de disponibilização;
- documentação de infraestrutura necessária;
- documentação de usuários ou serviços;
- Fairness Report (Seção 4);
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
3. ler os campos do relatório de dimensão, quando houver, que respondem ao requisito e conferi-los com as evidências nas fontes registradas na identificação do ciclo;
4. distinguir informação factual já documentada de análise específica ainda necessária;
5. percorrer o checklist do requisito e registrar a situação de cada item na tabela Checklist de `avaliacao.md`;
6. analisar suficiência, consistência, rastreabilidade e pertinência;
7. registrar as lacunas necessárias, conforme a seção Lacunas;
8. atribuir o resultado (Atendido, Não atendido, Inconclusivo com motivo, ou Não aplicável).

Ausência de artefato não é resultado. Não solicitar novamente informação já disponível. Decisão metodológica do NIAR é registrada, não vira pendência. As regras de pendência e de lacuna estão nas seções Pendências e Lacunas, em Fluxo do ciclo.

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
- modelo do Fairness Report: `artefatos/fairness_reports/fairness_report.md` (a versão .docx para Word é gerada a partir dele)
- `documentacao_metodologica/apoio_roteiro_entrevista.md` (material de apoio)
- templates de artefatos do projeto, quando pertinentes.

---

# Controle de atualização

Este arquivo deve acompanhar o estado da revisão metodológica do FIAR-Saúde.

**Vigência.** As mudanças da nova ordem do ciclo (relatórios de dimensão, Fairness Report obrigatório, lacunas, estados de inconsistência) valem para todos os ciclos a partir desta versão do guia, inclusive os que estão em andamento. Um ciclo em andamento recomeça a avaliação: a identificação é conferida e mantida, se continuar válida; a equipe entrega o relatório de dimensão; o avaliacao.md é refeito no modelo novo. A avaliação anterior (avaliacao.md) não é usada como fonte e fica só no histórico do Git. As comunicações com a equipe registradas em comunicacoes/ continuam valendo como fonte e podem apoiar o pré-preenchimento do relatório de dimensão. A decisão e o motivo ficam registrados no commit do projeto.

Quando uma dimensão for estabilizada:

1. inserir seus requisitos na seção correspondente;
2. reproduzir as formulações sem alteração;
3. incluir orientação operacional de aplicabilidade, evidências e verificação;
4. revisar sobreposições com dimensões já consolidadas;
5. atualizar o status da dimensão no início deste documento;
6. evitar manter requisitos locais ou versões anteriores que possam ser confundidos com a versão vigente;
7. registrar a alteração no controle de versão do FIAR-Audit-Template.

Quando um requisito for criado, alterado, removido ou renumerado, a mudança deve ser refletida neste guia antes de seu uso em novos ciclos de avaliação.

Ao alterar o checklist de um requisito, atualizar também a tabela Checklist correspondente em `ciclos/C01/avaliacao.md` e os códigos RCxx.y do modelo do Fairness Report.

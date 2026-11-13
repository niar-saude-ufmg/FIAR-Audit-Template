# Prompts de apoio à avaliação

Uso opcional, com assistente de IA. O resultado é rascunho: o avaliador do NIAR revisa e responde por ele. Quem pré-preenche o relatório de dimensão (Prompt 1b) e quem verifica (Prompt 2) são agentes separados: use sessões diferentes.
As referências do FIAR são lidas online, nos repositórios públicos, na versão indicada pela tag. O repositório do projeto é privado e é lido localmente: abra o assistente de IA na pasta dele. No início de cada sessão, cole a mensagem de contexto abaixo e, depois, o prompt da etapa.


## Contexto (colar no início do chat)

```text
Referências do FIAR-Saúde (repositórios públicos, versão [tag]):

- Guia de avaliação (fluxo e requisitos): https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Audit-Template/[tag]/documentacao_metodologica/guia_requisitos_avaliacao.md
- Modelos do ciclo: https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Audit-Template/[tag]/ciclos/C01/identificacao.md e https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Audit-Template/[tag]/ciclos/C01/avaliacao.md
- Modelo do Fairness Report e guia de preenchimento: artefatos/fairness_reports/FairnessReport_FIAR_Template.docx e FairnessReport_FIAR_Guia.docx do FIAR-Audit-Template
- Modelo de relatório ao Comitê: https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Audit-Template/[tag]/relatorios/RCG-001.md
- Regras do ciclo: https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Saude/[tag]/docs/ciclo_avaliacao.md
- Requisitos de Justiça: https://raw.githubusercontent.com/niar-saude-ufmg/FIAR-Saude/[tag]/docs/avaliacao/justica.md

Use essas versões, lidas online. Se não conseguir abrir algum link, avise e pare; não use outra versão. Não use cópias locais desses documentos, mesmo que existam nesta máquina, nem o PDF. Ao registrar o guia de requisitos usado, informe a tag.

O repositório do projeto [nome] é a pasta local aberta no Assistente de IA. Antes de começar, informe a branch e o commit dele. Use só as fontes dele e as referências acima. Arquivos sem commit só contam como fonte se o avaliador confirmar. O histórico do Git serve para verificar versões. Ignore .history/ e arquivos de sistema. O relatório de dimensão da equipe, quando houver, está em artefatos/ (Fairness Report em artefatos/fairness_reports/); informe a versão usada. Em ciclo que recomeçou, o avaliacao.md anterior não é fonte; as comunicações em comunicacoes/ continuam valendo.

Altere só o arquivo indicado no prompt da etapa. Não altere artefatos da equipe, não faça commit e não rode comandos que mudem o Git. O CLAUDE.md do projeto também vale.
```


## Prompt 0. Preparação do repositório

Uso: uma vez, em repositórios criados antes do fluxo atual. Cole antes a mensagem de contexto, com o Claude Code aberto na pasta do repositório do projeto.

```text
Compare o repositório do projeto com a estrutura atual do FIAR-Audit-Template e aponte:

- o que criar ou mover (entrada/, comunicacoes/, ciclos/Cxx/, relatorios/, decisoes/);
- as fontes disponíveis: formulário, artefatos da equipe e comunicações;
- os registros do fluxo anterior (pré-avaliação, pendências, controle de artefatos, decisão institucional, avaliações por dimensão ou requisito).

Registros do fluxo anterior servem só de referência. Uma informação que contenham só vale como evidência se estiver em uma fonte verificável. Pendências antigas não são reabertas automaticamente. Nesta etapa, não preencha a identificação, não avalie requisitos e não altere os artefatos da equipe.

Se o repositório já estiver na estrutura atual, informe isso e pare. Não revise a identificação nem a avaliação existentes; para isso, use o Prompt 3.
```

## Prompt 1. Delimitação

```text
Preencha ciclos/Cxx/identificacao.md seguindo a parte "Fluxo do ciclo" de guia_requisitos_avaliacao.md.

- Use só as fontes fornecidas neste ciclo. Registre cada uma na seção 2 (F-01, F-02...) e cite o ID em cada informação.
- Registre como fonte só o que for pertinente à tarefa, à versão e ao contexto. Fontes de ciclos anteriores valem se continuarem pertinentes e atuais. Registros não verificados servem só como pistas.
- Por padrão, o Contexto de Uso é o atual. Avalie um uso pretendido só se a delimitação o incluir explicitamente; registre à parte o uso pretendido que não for objeto do ciclo.
- Inferência sem sustentação suficiente deve ser marcada como hipótese do NIAR, com base e limitação.
- Não deduza responsabilidades técnicas. Se não estiverem documentadas, registre como não confirmadas.
- Falta de identificador exato da versão vai em "Limitações de identificação"; não é pendência.
- Abra pendência D-xx só se ela impedir identificar a Tarefa de IA ou relacionar as evidências a ela.
- Campo vazio não é pendência.
- Inconsistência (DI-xx) só com contradição confirmada, dentro de uma fonte ou entre fontes, sobre o mesmo fato, versão e contexto.
- Termine com a decisão (pronto para avaliar: Sim ou Não) e a justificativa. "Sim" libera o relatório de dimensão e a avaliação.
```

## Prompt 1b. Pré-preenchimento do relatório de dimensão sem sala segura

Uso: quando não houver execução na sala segura. O NIAR pré-preenche o relatório como rascunho para a equipe. Use uma sessão só para isto; a verificação (Prompt 2) é feita em outra sessão.

```text
Pré-preencha o relatório de dimensão de [dimensão] do projeto, no modelo [para Justiça: FairnessReport_FIAR_Template.docx, com o guia FairnessReport_FIAR_Guia.docx], seguindo a etapa 3 de "Etapas do ciclo" de guia_requisitos_avaliacao.md. Não houve execução na sala segura.

- Tarefa de IA, Versão Avaliável, Contexto de Uso e Trilha: copie de ciclos/Cxx/identificacao.md.
- Use só estas fontes, registradas na identificação: Model Card, Data Card, publicações e comunicações em comunicacoes/. Não use o avaliacao.md de ciclos anteriores nem registros do fluxo anterior.
- Em cada campo, registre a fonte e a versão. Para comunicações, cite o arquivo e a data.
- Fato é o que existe ou aconteceu: números, métricas, fontes dos dados, onde e como a Tarefa é usada. Fatos entram resumidos nos campos [A], com fonte. Não copie trechos longos.
- Posição da equipe é julgamento, critério, decisão ou intenção (por exemplo, "não há critério de aceitabilidade", "a concordância não foi estratificada"). Posições tiradas de comunicações ou do Model Card entram nos campos [J] com [a confirmar] no início. Não as transforme em fato nem em decisão da equipe.
- Não escreva julgamentos seus nos campos [J]. Se nenhuma fonte trouxer a posição da equipe, deixe o campo vazio.
- Divergência entre fontes: registre no campo "Divergências entre fontes" da Seção 0, com as duas fontes. Não escolha uma delas.
- Seção 0, Execução na sala segura: escreva que não houve e indique as fontes dos resultados.
- Entregue o texto de cada campo na ordem do modelo, com o nome do campo, para o avaliador colar no .docx.
- Seção 4: registre os fatos sobre a disponibilização. Se as fontes indicarem que a Tarefa não está disponível no uso atual, registre isso com fonte, marcado [a confirmar]. A declaração é da equipe.
- Seção 5: pode rascunhar os resumos, todos marcados [a confirmar]. Deixe as assinaturas em branco.
- Não atribua resultado a requisito, não use Atendido, Não atendido, Inconclusivo ou Não aplicável e não aponte lacunas. Isso é da verificação.
- Ao final, liste para o avaliador: campos [A] sem fonte, campos [J] vazios, campos [a confirmar] e divergências registradas.
- O resultado é rascunho para a equipe conferir, completar e assinar. Só depois de assinado ele é posição da equipe.
- Versão do relatório (Seção 0): 0.1.0. Entregue o rascunho ao avaliador para ser anexado ao pedido à equipe, em comunicacoes/anexos/. Não grave em artefatos/fairness_reports/: o relatório só entra lá como 1.0.0, depois de assinado pela equipe.

```

## Prompt 2. Avaliação de um requisito

```text
Preencha o bloco do requisito [RCxx] em ciclos/Cxx/avaliacao.md seguindo guia_requisitos_avaliacao.md. Avalie RC01 antes dos demais requisitos. O relatório de dimensão assinado pela equipe, versão [x], é o ponto de partida. Use uma sessão diferente da que pré-preencheu o relatório.

- Responda primeiro à pergunta de aplicabilidade, com justificativa, usando as informações factuais das fontes. Se não for possível determinar, abra pendência de aplicabilidade e marque Inconclusivo com o motivo "aplicabilidade não determinada". Pendência de aplicabilidade não é lacuna. Em RC04, registre o que a equipe declarou na Seção 4 do Fairness Report e confirme ou não, com justificativa.
- Para cada item do checklist, leia o campo do relatório indicado pelo código RCxx.y e confira com as evidências. Respondido: o campo responde e a evidência o sustenta (cite o campo e a fonte). Não localizado: campo vazio ou que não responde. Não pertinente: com motivo. O resultado é do requisito, não dos itens. Se o requisito for Não aplicável, não preencha a tabela; registre só a justificativa.
- Hipótese do NIAR não conta como Respondido: use Não localizado e descreva a hipótese.
- Aponte o campo do relatório e o ID da fonte. Não reescreva os fatos do relatório.
- Separe informação factual de análise específica de Justiça.
- Divergência entre o relatório e outra fonte: registre inconsistência (RCxx-Ix), com estado.
- Abra lacuna (RCxx-Ly) só se for necessária para concluir o requisito, se a resposta não estiver no relatório nem em outra fonte e se ainda não tiver sido apontada. Indique o campo do relatório e o que falta. Item Não localizado não vira lacuna por si só.
- Pendência de requisito (RCxx-Px) só para verificação interna do NIAR, decisão metodológica ainda não tomada ou pedido que não cabe no relatório.
- Resultado: Atendido, Não atendido, Inconclusivo (com motivo) ou Não aplicável. Atendimento parcial ou prática apenas planejada não levam automaticamente a Inconclusivo: com evidência suficiente de não atendimento, o resultado é Não atendido, mesmo com lacuna aberta.
- Os estados do relatório (justificada, injustificada, sem conclusão; considerada, realizada, descartada) são da equipe. Não os altere e não os use como resultado.
- Ausência de artefato não é resultado. Sem relatório de dimensão entregue no prazo, o resultado é Inconclusivo com o motivo "relatório de dimensão não entregue", salvo evidência suficiente de não atendimento.
- Encaminhamento: recomendação do NIAR é não obrigatória e não altera o resultado; condicionantes cabem só ao Comitê.
- Atualize a linha do requisito na Síntese do ciclo.
- Não escreva no relatório de dimensão nem nos demais artefatos da equipe.
```

## Prompt 2b. Pedido de lacunas à equipe

Uso: ao fim de cada rodada de avaliação. O resultado é rascunho; o avaliador revisa antes de enviar.

```text
Prepare o pedido da rodada [n] a partir das lacunas abertas e das pendências destinadas à Equipe em ciclos/Cxx/avaliacao.md.

- Cite a versão do relatório de dimensão verificada e o commit dos arquivos.
- Para cada lacuna: ID (RCxx-Ly), campo do relatório e o que falta. Escreva em linguagem simples. Não antecipe resultados.
- Pendências para a Equipe vão em parte separada, com o ID (RCxx-Px ou D-xx).
- Indique o prazo [data]. Peça que a nova versão do relatório liste, na Seção 6 (histórico), as lacunas a que responde.
- Recomendações do NIAR vão em parte separada, identificadas como não obrigatórias.
- Entregue como rascunho de comunicação para o avaliador revisar antes do envio.
```

## Prompt 3. Revisão do ciclo

```text
Revise identificacao.md e avaliacao.md do ciclo e aponte apenas:

- pendências sem vínculo com a delimitação ou com um requisito;
- pendências que pedem informação já disponível ou já respondida em comunicacoes/;
- decisões metodológicas já tomadas registradas como pendência;
- pendências enviadas à Equipe que dependem de verificação ou decisão do NIAR;
- pendências encerradas sem fonte;
- requisitos marcados Inconclusivo quando a evidência já mostra não atendimento;
- requisitos marcados Não aplicável por ausência de prática, mecanismo ou evidência;
- inconsistências sem duas fontes conflitantes;
- resultados sem evidência citada;
- itens do checklist marcados Respondido sem fonte, ou Não pertinente sem motivo;
- itens marcados Respondido cujo conteúdo seja só hipótese do NIAR;
- itens marcados Respondido sem o campo do relatório de dimensão que os responde;
- fatos do relatório reescritos no avaliacao.md em vez de apontados pelo campo;
- estados do relatório (justificada, injustificada, sem conclusão; considerada, realizada, descartada) usados como resultado, ou resultado atribuído à equipe;
- lacunas sem campo do relatório ou sem descrição do que falta;
- lacunas encerradas sem a versão e o campo do relatório que as responderam;
- perguntas à equipe sobre o conteúdo de um requisito abertas como pendência, e não como lacuna;
- campos marcados [a confirmar] na versão assinada do relatório, ou fatos do relatório sem fonte e versão;
- inconsistências sem estado (aberta, resolvida ou cancelada);
- uso do avaliacao.md de um ciclo recomeçado como fonte;
- Síntese diferente dos blocos (resultado, motivo, itens não localizados ou lacunas abertas);
- na identificação: hipótese registrada como fato, responsabilidade técnica deduzida ou fonte não pertinente à unidade.

Não crie pendências novas nem altere resultados; liste os problemas para o avaliador decidir.
```

## Prompt 4. Relatório ao Comitê Gestor

```text
Preencha relatorios/RCG-xxx.md a partir das sínteses dos ciclos indicados.

- Linguagem simples, para quem não é da área técnica.
- Indique o motivo do envio, conforme os gatilhos do guia, e os ciclos e unidades abrangidos.
- Na cobertura, diga explicitamente quais dimensões não foram avaliadas.
- Um risco para cada requisito Não atendido ou Inconclusivo: o risco, quem pode ser afetado, o requisito de origem e, se Inconclusivo, o que não se sabe. Indique as lacunas abertas relacionadas.
- Não classifique gravidade e não diga se o risco é aceitável; isso cabe ao Comitê.
- Recomendações do NIAR são não obrigatórias.
- Apresente a síntese da equipe de cada relatório de dimensão (no Fairness Report, a Seção 5) em parte separada, identificada como posição da equipe. Não a reescreva nem a misture com a análise do NIAR.
- Na decisão solicitada, deixe claro que a aceitação vale para a versão e o contexto avaliados.
```

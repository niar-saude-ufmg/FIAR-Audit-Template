# Guia do fluxo FIAR-Saúde

## Papéis

- Equipe do projeto: produz e mantém os artefatos e responde às perguntas do NIAR.
- NIAR-Saúde: delimita o ciclo, avalia os requisitos, recomenda e prepara o relatório ao Comitê. Não edita artefatos da equipe.
- Comitê Gestor: valida os relatórios e delibera sobre riscos e questões encaminhadas, inclusive condicionantes e restrições de uso. Pode pedir esclarecimentos ou revisão ao NIAR-Saúde, sem refazer a análise técnica. A aceitação de risco não altera os resultados dos requisitos.
- O FIAR-Saúde não é certificação.

## Conceitos

- Projeto: iniciativa responsável por uma ou mais Tarefas de IA; guarda o histórico dos ciclos.
- Tarefa de IA: modelo, dados e procedimentos orientados a um objetivo clínico ou operacional. Nova tarefa quando mudam objetivo, tipo de resultado ou escopo essencial.
- Versão Avaliável: estado da tarefa avaliado no ciclo. Falta de identificador exato não impede automaticamente a avaliação, desde que as evidências possam ser relacionadas à tarefa, ao estado avaliado e ao contexto.
- Contexto de Uso: condições em que a tarefa é desenvolvida, avaliada ou usada. Por padrão, o ciclo considera o contexto atual; um uso pretendido pode ser avaliado antes de sua implementação, se explicitamente delimitado e justificado. O uso pretendido que não for objeto do ciclo é registrado separadamente.
- Unidade de avaliação: Tarefa + Versão Avaliável + Contexto de Uso.
- Ciclo: uma avaliação de uma unidade, da delimitação ao fechamento.
- Trilha: Experimental ou Produção; orienta a aplicabilidade dos requisitos e a natureza das evidências.
- Evidência: informação que responde ao requisito. Fonte: onde ela está (artefato ou comunicação).
- Maturidade: a definir em revisão posterior.

## Etapas do ciclo

1. **Entrada**: formulário do projeto (entrada/), aberto na entrada e atualizado quando houver mudanças relevantes, com um bloco por Tarefa de IA apresentada.
2. **Delimitação:** ciclos/Cxx/identificacao.md. Termina com "pronto para avaliar". Só bloqueia se não for possível identificar a tarefa ou relacionar as evidências a ela.
3. **Avaliação**: ciclos/Cxx/avaliacao.md, um bloco por requisito. RC01 antes dos demais.
4. **Rodadas com a equipe**: uma mensagem por rodada, com as pendências destinadas à equipe. Recomendações podem seguir na mesma mensagem, em parte separada e identificadas como não obrigatórias. A equipe responde pelo canal que preferir; a resposta é guardada em comunicacoes/ e citada na avaliação. Não se exige atualizar um artefato só para transcrever uma resposta; pode ser necessário quando o requisito exigir documentação atualizada ou comunicação a um público.
5. **Fechamento**: resultado de cada requisito e síntese. Se houver gatilho, segue o relatório ao Comitê.

## Resultados por requisito

- Atendido: a evidência verificada sustenta o atendimento.
- Não atendido: a evidência verificada mostra que o requisito não é cumprido.
- Inconclusivo: a evidência disponível não permite concluir. Registrar o motivo (ex.: evidência incompleta, não localizada, aguardando resposta, aplicabilidade não determinada).

Atendimento parcial ou prática apenas planejada não levam automaticamente a Inconclusivo: com evidência suficiente de não atendimento, o resultado é Não atendido.

- Não aplicável: a condição pressuposta pelo requisito não existe na unidade, com justificativa.

Ausência de artefato não é resultado. A pergunta é sempre se há evidência para o requisito.

## Pendências

- Existe só ligada à delimitação (D-xx) ou a um requisito (RCxx-Px).
- Serve para delimitar a avaliação, determinar a aplicabilidade ou concluir a análise.
- Antes de abrir: (1) é necessária? (2) já está em alguma fonte? (3) já foi respondida? Só abrir se (1) for sim e as demais forem não.
- Destinatário: Equipe (vai na rodada) ou NIAR (verificação interna ou decisão metodológica ainda não tomada).
- Bloqueia só o que está ligado a ela.
- Estados: aberta, respondida, encerrada, cancelada (com motivo). Resposta recebida é analisada e não encerra a pendência automaticamente. Só o NIAR encerra, citando a fonte.
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

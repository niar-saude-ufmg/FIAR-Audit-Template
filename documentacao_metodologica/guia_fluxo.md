# Guia do fluxo FIAR-Saúde

## Papéis

- Equipe do projeto: produz e mantém os artefatos e responde às perguntas do NIAR.
- NIAR-Saúde: delimita o ciclo, avalia os requisitos, recomenda e prepara o relatório ao Comitê. Não edita artefatos da equipe.
- Comitê Gestor: valida os relatórios e delibera sobre riscos e questões encaminhadas, inclusive condicionantes e restrições de uso. Pode pedir esclarecimentos ou revisão ao NIAR-Saúde, sem refazer a análise técnica. A aceitação de risco não altera os resultados dos requisitos.
- O FIAR-Saúde não é certificação.

## Conceitos

- Projeto: iniciativa responsável por uma ou mais Tarefas de IA; guarda o histórico dos ciclos.
- Tarefa de IA: modelo, dados e procedimentos orientados a um objetivo clínico ou operacional. Nova tarefa quando mudam objetivo, tipo de resultado ou escopo essencial.
- Versão Avaliável: estado da tarefa avaliado no ciclo, identificado pelos elementos disponíveis. Falta de identificador exato é limitação, não impedimento.
- Contexto de Uso: condições do uso atual (finalidade, usuários, população, ambiente). O uso pretendido é registrado e, quando se concretizar, gera reavaliação.
- Unidade de avaliação: Tarefa + Versão Avaliável + Contexto de Uso.
- Ciclo: uma avaliação de uma unidade, da delimitação ao fechamento.
- Trilha: Experimental ou Produção; influencia só a aplicabilidade dos requisitos.
- Evidência: informação que responde ao requisito. Fonte: onde ela está (artefato ou comunicação).
- Maturidade: a definir em revisão posterior.

## Etapas do ciclo

1. Entrada: formulário, uma vez por projeto (entrada/).
2. Delimitação: ciclos/Cxx/identificacao.md. Termina com "pronto para avaliar". Só bloqueia se não for possível identificar a tarefa.
3. Avaliação: ciclos/Cxx/avaliacao.md, um bloco por requisito. RC01 antes dos demais.
4. Rodadas com a equipe: uma mensagem por rodada, só com pendências destinadas à equipe. A equipe responde pelo canal que preferir; a resposta é guardada em comunicacoes/ e citada na avaliação. Atualizar o artefato é recomendação, não condição.
5. Fechamento: resultado de cada requisito e síntese. Se houver gatilho, segue o relatório ao Comitê.

## Resultados por requisito

- Atendido: a evidência verificada sustenta o atendimento.
- Não atendido: a evidência verificada mostra que o requisito não é cumprido.
- Inconclusivo: falta evidência suficiente. Motivo: parcial, planejado ou não localizado.
- Não aplicável: a condição pressuposta pelo requisito não existe na unidade, com justificativa.

Ausência de artefato não é resultado. A pergunta é sempre se há evidência para o requisito.

## Pendências

- Existe só ligada à delimitação (D-xx) ou a um requisito (RCxx-Px).
- Antes de abrir: (1) é necessária? (2) já está em alguma fonte? (3) já foi respondida? (4) é decisão do NIAR? Só abrir se (1) for sim e as demais forem não. Decisão do NIAR é registrada, não vira pendência.
- Destinatário: Equipe (vai na rodada) ou NIAR (verificação interna).
- Bloqueia só o que está ligado a ela.
- Estados: aberta, respondida, encerrada, cancelada (com motivo). Só o NIAR encerra, citando a fonte.
- Requisito com pendência aberta fica Inconclusivo. Inconclusivo pode existir sem pendência.

## Inconsistências

Divergência confirmada entre fontes sobre o mesmo fato, versão e contexto. Informação ausente não é inconsistência. Registrar no bloco do requisito afetado (RCxx-Ix); gera pendência se precisar de resposta da equipe.

## Atribuições do NIAR

Quando o NIAR deduzir algo sem confirmação da equipe, registra "atribuído pelo NIAR" e a base da dedução.

## Encaminhamentos

- Recomendação do NIAR: sugestão à equipe, não obrigatória, não altera resultados.
- Questão para o Comitê: aceite de risco, restrição de uso, responsabilidades ou conflitos que ultrapassam a avaliação técnica.
- Condicionantes só são definidas pelo Comitê (decisoes/).

## Relatório ao Comitê Gestor

Um por projeto (relatorios/RCG-xxx.md), enviado quando houver:

1. primeira avaliação concluída;
2. resultado que muda de categoria;
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
EOF

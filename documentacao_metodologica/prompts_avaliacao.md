# Prompts de apoio à avaliação

Uso opcional, com assistente de IA. O resultado é rascunho: o avaliador do NIAR revisa e responde por ele.
Antes de qualquer prompt, forneça ao assistente: guia_fluxo.md, guia_requisitos_avaliacao.md e os arquivos do ciclo.

## Prompt 1. Delimitação

Preencha ciclos/Cxx/identificacao.md seguindo guia_fluxo.md.

- Use só as fontes fornecidas neste ciclo. Registre cada uma na seção 5 (F-01, F-02...) e cite o ID em cada informação.
- Contexto de Uso é o uso atual. Registre o uso pretendido à parte.
- Inferência sem sustentação suficiente deve ser marcada como hipótese do NIAR, com base e limitação.
- Não deduza responsabilidades técnicas. Se não estiverem documentadas, registre como não confirmadas.
- Falta de identificador exato da versão vai em "Limitações de identificação"; não é pendência.
- Abra pendência D-xx só se ela impedir identificar a Tarefa de IA.
- Campo vazio não é pendência.
- Termine com a decisão "pronto para avaliar" e a justificativa.

## Prompt 2. Avaliação de um requisito

Preencha o bloco do requisito [RCxx] em ciclos/Cxx/avaliacao.md seguindo guia_requisitos_avaliacao.md.

- Responda primeiro à pergunta de aplicabilidade, com justificativa. Se não for possível determinar, abra pendência e marque Inconclusivo.
- Use o roteiro de perguntas como apoio, não como checklist.
- Cite as evidências pelo ID da fonte e pela seção.
- Separe informação factual de análise específica de Justiça.
- Resultado: Atendido, Não atendido, Inconclusivo (parcial, planejado ou não localizado) ou Não aplicável.
- Ausência de artefato não é resultado.
- Antes de abrir uma pendência, verifique: é necessária para este requisito? já está em alguma fonte? já foi respondida? é decisão do NIAR? Só abra se a primeira for sim e as demais forem não. Indique o destinatário (Equipe ou NIAR).
- Inconsistência só com divergência confirmada sobre o mesmo fato, versão e contexto.
- Não escreva nos artefatos da equipe.

## Prompt 3. Revisão do ciclo

Revise identificacao.md e avaliacao.md do ciclo e aponte apenas:

- pendências sem vínculo com a delimitação ou com um requisito;
- pendências que pedem informação já disponível ou já respondida em comunicacoes/;
- decisões do NIAR registradas como pendência;
- inconsistências sem duas fontes conflitantes;
- resultados sem evidência citada;
- inferências não marcadas como hipótese do NIAR e responsabilidades técnicas deduzidas sem fonte.

Não crie pendências novas nem altere resultados; liste os problemas para o avaliador decidir.

## Prompt 4. Relatório ao Comitê Gestor

Preencha relatorios/RCG-xxx.md a partir das sínteses dos ciclos indicados.

- Linguagem simples, para quem não é da área técnica.
- Na cobertura, diga explicitamente quais dimensões não foram avaliadas.
- Um risco para cada requisito Não atendido ou Inconclusivo: o risco, quem pode ser afetado, o requisito de origem e, se Inconclusivo, o que não se sabe.
- Não classifique gravidade e não diga se o risco é aceitável; isso cabe ao Comitê.
- Recomendações do NIAR são não obrigatórias.
- Na decisão solicitada, deixe claro que a aceitação vale para a versão e o contexto avaliados.

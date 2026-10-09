# Prompts de apoio à avaliação

Uso opcional, com assistente de IA. O resultado é rascunho: o avaliador do NIAR revisa e responde por ele.
Antes de qualquer prompt, forneça ao assistente: guia_fluxo.md, guia_requisitos_avaliacao.md e os arquivos do ciclo.

## Prompt 0. Preparação do repositório

Uso: uma vez, em repositórios criados antes do fluxo atual. Forneça o repositório do projeto (por exemplo, em ZIP) e o guia_fluxo.md.

```text
Compare o repositório do projeto com a estrutura atual do FIAR-Audit-Template e aponte:

- o que criar ou mover (entrada/, comunicacoes/, ciclos/Cxx/, relatorios/, decisoes/);
- as fontes disponíveis: formulário, artefatos da equipe e comunicações;
- os registros do fluxo anterior (pré-avaliação, pendências, controle de artefatos, decisão institucional, avaliações por dimensão ou requisito).

Registros do fluxo anterior servem só de referência. Uma informação que contenham só vale como evidência se estiver em uma fonte verificável. Pendências antigas não são reabertas automaticamente. Nesta etapa, não preencha a identificação, não avalie requisitos e não altere os artefatos da equipe.
```

## Prompt 1. Delimitação

```text
Preencha ciclos/Cxx/identificacao.md seguindo guia_fluxo.md.

- Use só as fontes fornecidas neste ciclo. Registre cada uma na seção 2 (F-01, F-02...) e cite o ID em cada informação.
- Por padrão, o Contexto de Uso é o atual. Avalie um uso pretendido só se a delimitação o incluir explicitamente; registre à parte o uso pretendido que não for objeto do ciclo.
- Inferência sem sustentação suficiente deve ser marcada como hipótese do NIAR, com base e limitação.
- Não deduza responsabilidades técnicas. Se não estiverem documentadas, registre como não confirmadas.
- Falta de identificador exato da versão vai em "Limitações de identificação"; não é pendência.
- Abra pendência D-xx só se ela impedir identificar a Tarefa de IA ou relacionar as evidências a ela.
- Campo vazio não é pendência.
- Termine com a decisão "pronto para avaliar" e a justificativa.
```

## Prompt 2. Avaliação de um requisito

```text
Preencha o bloco do requisito [RCxx] em ciclos/Cxx/avaliacao.md seguindo guia_requisitos_avaliacao.md.

- Responda primeiro à pergunta de aplicabilidade, com justificativa, usando as informações factuais das fontes. Se não for possível determinar, abra pendência e marque Inconclusivo com o motivo "aplicabilidade não determinada".
- Use o roteiro de perguntas como apoio, não como checklist.
- Cite as evidências pelo ID da fonte e pela seção.
- Separe informação factual de análise específica de Justiça.
- Resultado: Atendido, Não atendido, Inconclusivo (com motivo) ou Não aplicável. Atendimento parcial ou prática apenas planejada não levam automaticamente a Inconclusivo: com evidência suficiente de não atendimento, o resultado é Não atendido.
- Ausência de artefato não é resultado.
- Antes de abrir uma pendência, verifique: é necessária para este requisito? já está em alguma fonte? já foi respondida? Só abra se a primeira for sim e as demais forem não. Indique o destinatário (Equipe, ou NIAR para verificação interna ou decisão metodológica ainda não tomada).
- Inconsistência só com contradição confirmada, dentro de uma fonte ou entre fontes, sobre o mesmo fato, versão e contexto.
- Não escreva nos artefatos da equipe.
```

## Prompt 3. Revisão do ciclo

```text
Revise identificacao.md e avaliacao.md do ciclo e aponte apenas:

- pendências sem vínculo com a delimitação ou com um requisito;
- pendências que pedem informação já disponível ou já respondida em comunicacoes/;
- decisões metodológicas já tomadas registradas como pendência;
- requisitos marcados Inconclusivo quando a evidência já mostra não atendimento;
- inconsistências sem duas fontes conflitantes;
- resultados sem evidência citada;
- inferências não marcadas como hipótese do NIAR e responsabilidades técnicas deduzidas sem fonte.

Não crie pendências novas nem altere resultados; liste os problemas para o avaliador decidir.
```

## Prompt 4. Relatório ao Comitê Gestor

```text
Preencha relatorios/RCG-xxx.md a partir das sínteses dos ciclos indicados.

- Linguagem simples, para quem não é da área técnica.
- Na cobertura, diga explicitamente quais dimensões não foram avaliadas.
- Um risco para cada requisito Não atendido ou Inconclusivo: o risco, quem pode ser afetado, o requisito de origem e, se Inconclusivo, o que não se sabe.
- Não classifique gravidade e não diga se o risco é aceitável; isso cabe ao Comitê.
- Recomendações do NIAR são não obrigatórias.
- Na decisão solicitada, deixe claro que a aceitação vale para a versão e o contexto avaliados.
```

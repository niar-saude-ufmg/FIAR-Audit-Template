# Guia de Requisitos para Avaliação

Este documento organiza operacionalmente os requisitos vigentes do FIAR-Saúde para apoiar sua aplicação nos ciclos de avaliação conduzidos pelo NIAR-Saúde.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas.

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a Tarefa de IA, a Versão Avaliável, o Contexto de Uso e a Trilha de Execução.

As orientações deste guia apoiam o preenchimento do template de avaliação de requisito. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

As formulações dos requisitos reproduzem a documentação canônica vigente do FIAR-Saúde. As explicações, exemplos e cautelas deste guia têm função operacional e não criam requisitos adicionais.


## Fontes normativas e natureza das orientações

Os requisitos reproduzidos neste guia têm como fonte normativa a documentação vigente do FIAR-Saúde.

Fontes principais:

- `FIAR-Saude/docs/dimensoes_avaliacao.md`
- `FIAR-Saude/docs/avaliacao/governanca.md`
- `FIAR-Saude/docs/avaliacao/privacidade.md`
- `FIAR-Saude/docs/avaliacao/justica.md`

As formulações identificadas como **Requisito** são reproduzidas da documentação canônica do FIAR-Saúde.

As seções **O que o requisito busca verificar**, **Aspectos a considerar na aplicabilidade**, **Exemplos de evidências pertinentes**, **Mecanismos de verificação possíveis** e **Observações metodológicas** constituem orientação operacional do FIAR-Audit-Template. Elas auxiliam a aplicação dos requisitos, mas não criam requisitos adicionais nem substituem a documentação normativa.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

---

## Governança

A dimensão de Governança avalia as estruturas, processos, responsabilidades, condições de uso, supervisão, acompanhamento e formas de resposta associadas à Tarefa de IA. Os requisitos canônicos vigentes são GOV-01 a GOV-10.

### GOV-01

**Requisito:**  
As estruturas, papéis e competências institucionais relevantes para a tarefa estão identificados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-01

**O que o requisito busca verificar:**  
Verificar se estão suficientemente identificadas as estruturas institucionais e os papéis relevantes para a Tarefa de IA no escopo da avaliação, incluindo as responsabilidades necessárias para compreender quem desenvolve, responde tecnicamente, acompanha, avalia, supervisiona ou toma decisões relacionadas à tarefa, quando esses papéis forem pertinentes ao contexto analisado.

O requisito busca assegurar que responsabilidades relevantes não permaneçam implícitas ou sejam inferidas apenas a partir de autoria, participação técnica ou vínculo institucional.

**Aspectos a considerar na aplicabilidade:**
- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde, inclusive na Trilha Experimental.
- A extensão dos papéis a identificar depende da Tarefa de IA, da Versão Avaliável, do Contexto de Uso, da Trilha de Execução e das estruturas efetivamente envolvidas.
- Tarefas em produção podem exigir papéis adicionais relacionados à operação, supervisão, monitoramento, incidentes ou decisão institucional.
- Não devem ser exigidos papéis que não sejam pertinentes ao estágio e ao escopo da tarefa.

**Exemplos de evidências pertinentes:**
- registros de identificação do projeto e da avaliação;
- registros institucionais ou administrativos que identifiquem responsáveis e atribuições;
- documentação de papéis e responsabilidades;
- registros de designação de responsáveis técnicos ou institucionais;
- documentação de estruturas de supervisão ou governança, quando aplicável;
- registros de decisões que permitam identificar a competência decisória;
- confirmações factuais específicas quando a responsabilidade não puder ser estabelecida documentalmente;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência cruzada entre documentos e registros;
- verificação de rastreabilidade das atribuições à tarefa e à Versão Avaliável;
- verificação institucional ou administrativa;
- confirmação factual quando a evidência disponível for insuficiente;

**Observações metodológicas:**
- Autoria de artigo, código, modelo, Data Card, Model Card ou outro artefato não estabelece automaticamente responsabilidade institucional ou técnica.
- Participação no desenvolvimento não equivale automaticamente à competência para decidir, supervisionar ou aceitar riscos.
- A existência de um template de papéis e responsabilidades não torna seu preenchimento obrigatório se outras evidências forem suficientes e rastreáveis.
- Uma responsabilidade não confirmada deve ser tratada como insuficiência de evidência ou pendência factual, e não como inconsistência, salvo quando houver fontes efetivamente incompatíveis.
- Os papéis avaliados devem estar vinculados ao escopo concreto da Tarefa de IA e não apenas ao projeto de forma genérica.

---

### GOV-02

**Requisito:**  
Existem processos definidos para decisões técnicas, operacionais ou institucionais relevantes à tarefa?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-02

**O que o requisito busca verificar:**  
Verificar se decisões relevantes para a tarefa são tomadas por meio de processos identificáveis e rastreáveis, com clareza sobre quem decide, em que situações, com base em quais informações e como a decisão é registrada quando necessário.

O requisito não exige um fluxo burocrático único, mas busca evitar que decisões relevantes permaneçam informais, sem atribuição de competência ou sem possibilidade de reconstrução posterior.

**Aspectos a considerar na aplicabilidade:**
- O grau de formalização esperado depende do estágio da tarefa e da natureza das decisões.
- Na Trilha Experimental, decisões metodológicas relevantes podem exigir registro sem que exista um processo operacional de produção.
- Na Trilha Produção, decisões operacionais, mudanças, incidentes, restrições de uso e escalonamentos podem requerer processos adicionais.
- Somente decisões materialmente relevantes para a tarefa e seu contexto devem ser consideradas.

**Exemplos de evidências pertinentes:**
- fluxos ou procedimentos de decisão;
- Registros de Decisão Técnica;
- atas, pareceres ou decisões institucionais;
- registros de aprovação de mudanças;
- documentação de escalonamento;
- histórico de decisões associado a versões da tarefa;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- rastreabilidade entre decisão, responsável e evidência utilizada;
- consistência cruzada entre registros técnicos e institucionais;
- verificação institucional quando a competência decisória precisar ser confirmada;

**Observações metodológicas:**
- A ausência de um artefato denominado Registro de Decisão Técnica não implica, por si só, descumprimento; deve-se verificar se as decisões relevantes estão suficientemente documentadas em fonte equivalente.
- Não confundir o processo decisório do projeto com o processo de avaliação conduzido pelo NIAR-Saúde.
- Decisões triviais ou de rotina não precisam receber o mesmo nível de formalização que decisões capazes de alterar risco, escopo, uso ou comportamento da tarefa.
- Uma decisão deve ser analisada juntamente com seu contexto, evidências e versão correspondente.

---

### GOV-03

**Requisito:**  
A finalidade, as condições e os limites de uso da tarefa estão definidos?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-03

**O que o requisito busca verificar:**  
Verificar se está claro para que a tarefa foi desenvolvida ou avaliada, em quais condições seu uso é considerado e quais usos, populações, ambientes ou situações estão fora do escopo avaliado ou não são recomendados.

O requisito delimita o objeto de governança e reduz o risco de extrapolar resultados obtidos em um contexto para usos não avaliados.

**Aspectos a considerar na aplicabilidade:**
- Aplicável a todas as tarefas, mas o nível de detalhamento depende do estágio e do Contexto de Uso.
- Uso atual e uso pretendido devem ser distinguidos quando não forem equivalentes.
- Tarefas experimentais podem ter finalidade limitada a pesquisa, desenvolvimento ou validação.
- Tarefas em produção devem explicitar condições operacionais, usuários, população, ambiente e eventuais restrições relevantes.

**Exemplos de evidências pertinentes:**
- Formulário de Entrada;
- Identificação da Avaliação;
- Model Card ou documentação equivalente;
- protocolos de uso;
- documentação institucional sobre escopo ou autorização;
- registros de condicionantes e restrições;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência cruzada entre finalidade, contexto, dados e documentação do modelo;
- contextualização;
- rastreabilidade de restrições e decisões;

**Observações metodológicas:**
- Descrever uma possibilidade futura não equivale a definir o Contexto de Uso atual.
- O bom desempenho em determinada avaliação não autoriza inferir adequação para usos fora do escopo documentado.
- Limitações técnicas e limites institucionais de uso devem ser distinguidos quando necessário.
- Mudança substantiva de finalidade ou Contexto de Uso pode exigir nova delimitação da tarefa ou reavaliação.

---

### GOV-04

**Requisito:**  
A necessidade e a forma de supervisão humana foram determinadas de acordo com a natureza da tarefa e o Contexto de Uso?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-04

**O que o requisito busca verificar:**  
Verificar se o projeto determinou, de maneira contextualizada, se a tarefa requer supervisão humana e, quando requer, qual é a finalidade dessa supervisão e como ela se relaciona ao uso da saída da IA.

O requisito não presume que toda Tarefa de IA exija o mesmo tipo de supervisão nem que a simples presença de uma pessoa no fluxo seja suficiente.

**Aspectos a considerar na aplicabilidade:**
- A aplicabilidade da supervisão depende do tipo de tarefa, do grau de autonomia, das consequências dos resultados e do contexto de uso.
- Em tarefas exclusivamente experimentais, pode não existir ainda um fluxo de supervisão operacional, mas o uso pretendido pode exigir que essa necessidade seja considerada.
- Em produção, devem ser considerados os pontos concretos em que revisão, intervenção ou decisão humana são necessárias.
- A supervisão deve ser proporcional ao risco e à função da saída da IA.

**Exemplos de evidências pertinentes:**
- Model Card;
- descrição do fluxo operacional;
- procedimentos de revisão humana;
- documentação de interfaces e informações fornecidas ao usuário;
- políticas ou instruções de uso;
- decisões institucionais sobre supervisão;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- contextualização;
- verificação documental;
- consistência entre uso declarado e supervisão prevista;
- análise do fluxo de decisão;

**Observações metodológicas:**
- Supervisão humana não deve ser presumida como mecanismo eficaz apenas porque existe formalmente.
- Distinguir supervisão da execução técnica do projeto e da avaliação pelo NIAR-Saúde.
- A forma de supervisão deve permitir compreender a função real do humano no fluxo.
- Se a tarefa não produz ou apoia decisões que demandem supervisão, a justificativa de não aplicabilidade deve ser registrada.

---

### GOV-05

**Requisito:**  
Quando aplicável, os responsáveis pela supervisão possuem informações e mecanismos adequados para intervir ou revisar o uso da tarefa?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-05

**O que o requisito busca verificar:**  
Verificar se a supervisão humana definida no requisito anterior é operacionalmente viável: os responsáveis precisam dispor das informações, competências e possibilidades de ação necessárias para revisar, questionar, interromper ou substituir a saída ou o uso da tarefa, conforme o contexto.

O foco não é apenas a existência nominal de um supervisor, mas a capacidade efetiva de exercer a supervisão prevista.

**Aspectos a considerar na aplicabilidade:**
- Aplicável somente quando houver supervisão humana pertinente ao uso da tarefa.
- A análise depende da função atribuída ao supervisor e das decisões que ele pode tomar.
- Em tarefas ainda não operacionais, pode ser prematuro exigir interfaces ou procedimentos completos; deve-se avaliar o estágio real.
- Em produção, mecanismos efetivos de intervenção e revisão tendem a ser materialmente relevantes.

**Exemplos de evidências pertinentes:**
- procedimentos de supervisão;
- interfaces ou materiais de uso;
- documentação das informações apresentadas ao supervisor;
- protocolos de exceção ou revisão;
- registros de treinamento ou orientação, quando pertinentes;
- registros operacionais que demonstrem possibilidade de intervenção;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão documental;
- análise contextual;
- inspeção do fluxo operacional;
- entrevista ou confirmação factual, quando necessária;
- análise de evidências operacionais, quando disponíveis;

**Observações metodológicas:**
- Não concluir que há supervisão efetiva apenas porque o sistema é descrito como 'human-in-the-loop'.
- A adequação das informações deve ser julgada em relação à decisão que o supervisor precisa tomar.
- Evitar exigir mecanismos de intervenção inexistentes em tarefas puramente experimentais quando o uso operacional ainda não ocorre.
- Limitações humanas, de tempo, informação ou autoridade podem ser relevantes para a análise.

---

### GOV-06

**Requisito:**  
Riscos, limitações ou achados relevantes possuem processo definido de tratamento ou escalonamento?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-06

**O que o requisito busca verificar:**  
Verificar se riscos, limitações ou achados com relevância para a tarefa não permanecem apenas registrados, mas possuem uma forma definida de tratamento, acompanhamento ou escalonamento compatível com sua natureza.

O requisito conecta a produção de evidência à governança: identificar um problema é diferente de possuir um processo para decidir o que fazer a respeito.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando houver riscos, limitações ou achados que demandem tratamento ou decisão.
- O tipo de resposta pode variar entre correção técnica, investigação, monitoramento, restrição de uso, registro de risco residual ou escalonamento institucional.
- Na Trilha Experimental, o tratamento pode ocorrer dentro do ciclo de desenvolvimento.
- Na Trilha Produção, podem ser necessários fluxos de resposta, prazos, responsáveis e escalonamento operacional ou institucional.

**Exemplos de evidências pertinentes:**
- registros de risco;
- Fairness/Explainability Reports ou outros relatórios com achados relevantes;
- Registros de Decisão Técnica;
- planos de mitigação;
- fluxos de escalonamento;
- registros de acompanhamento;
- decisões institucionais ou condicionantes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- rastreabilidade entre achado, decisão e ação;
- verificação documental;
- consistência cruzada;
- verificação institucional quando houver escalonamento;

**Observações metodológicas:**
- Nem todo risco exige mitigação técnica; a resposta deve ser contextualizada e fundamentada.
- Registrar uma limitação não demonstra, sozinho, que ela foi tratada.
- Não abrir automaticamente uma nova pendência se o risco já estiver adequadamente tratado em outro registro.
- Escalonamento institucional é necessário apenas quando a questão excede a competência decisória ordinária do projeto ou do NIAR, conforme a arquitetura vigente.

---

### GOV-07

**Requisito:**  
Condicionantes, restrições ou decisões institucionais estão documentados e associados à tarefa quando aplicáveis?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-07

**O que o requisito busca verificar:**  
Verificar se condicionantes, restrições de uso e decisões institucionais relevantes são preservadas de forma rastreável e vinculadas à tarefa, à versão e ao contexto a que se referem.

O requisito busca evitar que decisões institucionais se desvinculem do objeto avaliado ou se percam ao longo de mudanças de versão e uso.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando houver condicionantes, restrições ou decisões institucionais relacionadas à tarefa.
- Nem toda avaliação exige uma decisão institucional adicional.
- A ausência de deliberação formal não deve ser tratada como lacuna quando nenhuma questão exigiu escalonamento.
- Em produção, decisões sobre autorização, restrição, suspensão ou risco residual podem ser especialmente relevantes.

**Exemplos de evidências pertinentes:**
- atas ou registros institucionais;
- pareceres;
- condicionantes de uso;
- registros de aceite de risco quando aplicável;
- documentação de escalonamento;
- histórico da avaliação;
- registros vinculados à versão;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação institucional;
- rastreabilidade;
- consistência entre decisão e estado da tarefa;
- verificação documental;

**Observações metodológicas:**
- Não presumir que toda decisão técnica constitui decisão institucional.
- Uma decisão institucional deve ser atribuída à instância competente e não à autoria de um documento.
- Condicionantes devem permanecer vinculados ao escopo para o qual foram definidos.
- Decisões históricas não devem ser aplicadas automaticamente a novas versões ou contextos sem verificar sua validade.

---

### GOV-08

**Requisito:**  
Existem mecanismos adequados de monitoramento, revisão e atualização para o estágio da tarefa?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-08

**O que o requisito busca verificar:**  
Verificar se a tarefa possui mecanismos de acompanhamento proporcionais ao seu estágio, capazes de apoiar revisão de desempenho, riscos, limitações, dados, modelo ou condições de uso quando pertinente.

O requisito não impõe monitoramento contínuo uniforme a todas as tarefas; exige adequação ao estágio e à Trilha de Execução.

**Aspectos a considerar na aplicabilidade:**
- Na Trilha Experimental, podem ser suficientes mecanismos associados aos ciclos previstos de desenvolvimento e avaliação.
- Na Trilha Produção, normalmente são relevantes monitoramento operacional, revisão periódica e atualização de evidências.
- O que deve ser acompanhado depende dos riscos e propriedades relevantes da tarefa.
- Mecanismos inexistentes ou ainda não exigíveis no estágio atual não devem ser tratados como não conformidade sem análise de aplicabilidade.

**Exemplos de evidências pertinentes:**
- planos de monitoramento;
- registros de revisão;
- histórico de atualizações;
- relatórios de desempenho ou risco;
- registros de drift ou mudanças de dados;
- procedimentos de revisão periódica;
- evidências operacionais;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- análise de evidências operacionais;
- contextualização;
- verificação documental;
- rastreabilidade longitudinal;

**Observações metodológicas:**
- Não confundir monitoramento de desempenho com monitoramento integral de governança.
- A existência de dashboards ou métricas não demonstra, por si só, que existe processo de revisão e resposta.
- A frequência e o escopo devem ser proporcionais à tarefa e ao risco.
- Para tarefas experimentais, evitar importar requisitos operacionais próprios de produção.

---

### GOV-09

**Requisito:**  
Existem critérios ou gatilhos para reavaliação quando mudanças relevantes ocorrerem?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-09

**O que o requisito busca verificar:**  
Verificar se o projeto consegue reconhecer mudanças capazes de alterar materialmente a avaliação da tarefa e se existem critérios para decidir quando uma nova avaliação, integral ou parcial, deve ser iniciada.

O requisito sustenta a governança longitudinal e evita que mudanças relevantes sejam tratadas como simples manutenção sem reconsideração das evidências afetadas.

**Aspectos a considerar na aplicabilidade:**
- Aplicável em qualquer tarefa sujeita a evolução, embora a formalização esperada varie por trilha.
- Podem ser relevantes mudanças no modelo, dados, procedimentos, população, finalidade, integração ou Contexto de Uso.
- Nem toda alteração técnica constitui nova Versão Avaliável.
- Em produção, incidentes, drift ou mudanças operacionais podem funcionar como gatilhos adicionais.

**Exemplos de evidências pertinentes:**
- política ou registro de gestão de mudanças;
- histórico de versões;
- Registros de Decisão Técnica;
- critérios documentados de reavaliação;
- registros de incidentes;
- documentação de alterações de dados, modelo ou contexto;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- rastreabilidade longitudinal;
- consistência entre mudança e decisão de reavaliar;
- revisão de histórico de versões;

**Observações metodológicas:**
- Não assumir que toda nova versão de software ou correção menor exige avaliação completa.
- A relação entre mudança e dimensões potencialmente afetadas deve ser explicitada.
- Mudança de finalidade ou Contexto de Uso pode ser mais relevante que uma alteração de arquitetura interna.
- Enquanto critérios institucionais de gatilho não estiverem formalizados, o avaliador deve evitar inventar thresholds próprios.

---

### GOV-10

**Requisito:**  
Para tarefas em produção, existem mecanismos para restringir, suspender, corrigir ou descontinuar o uso quando necessário?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/governanca.md` — GOV-10

**O que o requisito busca verificar:**  
Verificar se tarefas em operação possuem mecanismos de resposta capazes de reduzir ou interromper sua utilização quando riscos, incidentes, falhas ou mudanças tornarem o uso inadequado.

O requisito trata da capacidade operacional de agir, e não apenas de reconhecer um problema.

**Aspectos a considerar na aplicabilidade:**
- Específico da Trilha Produção.
- Deve considerar a forma real de integração da tarefa ao sistema e as consequências de interrupção ou restrição.
- Os mecanismos podem variar entre rollback, desativação, restrição de funcionalidades, fallback manual, suspensão temporária ou descontinuação.
- A aplicabilidade e a robustez esperada dependem da criticidade e do Contexto de Uso.

**Exemplos de evidências pertinentes:**
- procedimentos operacionais;
- planos de contingência;
- mecanismos de rollback ou desativação;
- registros de incidentes e ações corretivas;
- decisões institucionais;
- procedimentos de continuidade e fallback;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- análise de evidências operacionais;
- verificação institucional;
- revisão documental;
- testes ou demonstração de mecanismos, quando aplicável;

**Observações metodológicas:**
- Não aplicável a tarefas que não estejam em produção.
- A simples possibilidade técnica de desligar um componente não demonstra que existe um processo governado de restrição ou suspensão.
- Devem ser considerados responsáveis, condições de acionamento e consequências operacionais.
- O FIAR-Saúde avalia a evidência do mecanismo e de sua governança; não substitui validações técnicas especializadas de continuidade ou segurança.

---

## Segurança

**Fonte normativa da dimensão:**  
`FIAR-Saude/docs/dimensoes_avaliacao.md`

A dimensão de Segurança é uma das sete dimensões canônicas do FIAR-Saúde. Na documentação vigente consultada, o arquivo detalhado de avaliação de Segurança ainda não foi criado. Portanto, este guia **não cria identificadores ou requisitos operacionais de Segurança**.

Até a publicação dos requisitos canônicos, a avaliação deve usar apenas os aspectos orientadores já definidos pelo FIAR-Saúde — como registros de incidentes, controle de acesso a dados e ambientes, mecanismos de resposta a falhas e mecanismos de proteção, hardening ou isolamento quando aplicáveis — sem convertê-los em requisitos numerados não oficiais.

Quando a especificação canônica de Segurança for publicada, esta seção deverá ser atualizada preservando os identificadores, formulações e mecanismos oficiais.

---

## Privacidade

A dimensão de Privacidade avalia como os dados utilizados pela Tarefa de IA são obtidos, tratados, protegidos e governados, considerando sua natureza, finalidade e Contexto de Uso. Os requisitos canônicos vigentes são PRI-01 a PRI-10.

### PRI-01

**Requisito:**  
A origem, a natureza e a finalidade dos dados utilizados na tarefa estão documentadas?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-01

**O que o requisito busca verificar:**  
Verificar se é possível compreender de onde vêm os dados, que tipo de informação contêm e para que são utilizados na Tarefa de IA, de modo a sustentar a análise de privacidade e a coerência com o Contexto de Uso.

**Aspectos a considerar na aplicabilidade:**
- Aplicável a todas as tarefas que utilizam dados.
- A profundidade depende da natureza, sensibilidade, proveniência e condições de acesso.
- Dados públicos, agregados ou anonimizados continuam exigindo documentação suficiente de origem e finalidade.

**Exemplos de evidências pertinentes:**
- Data Card ou documentação equivalente;
- Formulário de Entrada;
- documentação de acesso ou proveniência;
- descrição das fontes e do tratamento;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência cruzada;
- rastreabilidade da fonte e finalidade;

**Observações metodológicas:**
- Não inferir natureza ou sensibilidade apenas pelo nome do dataset.
- Distinguir finalidade original de coleta da finalidade de uso na tarefa quando relevante.
- A existência do Data Card não garante suficiência; o conteúdo precisa sustentar a conclusão.

---

### PRI-02

**Requisito:**  
Está identificado se a tarefa trata dados pessoais, sensíveis, anonimizados, pseudonimizados ou agregados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-02

**O que o requisito busca verificar:**  
Verificar se a natureza dos dados quanto à possibilidade de identificação e sensibilidade está explicitamente caracterizada, permitindo avaliar controles e riscos pertinentes.

**Aspectos a considerar na aplicabilidade:**
- Aplicabilidade depende dos dados efetivamente tratados.
- A classificação pode variar entre etapas do pipeline.
- Dados pseudonimizados não devem ser tratados automaticamente como anônimos.
- Dados agregados podem manter riscos residuais dependendo da granularidade.

**Exemplos de evidências pertinentes:**
- Data Card;
- documentação técnica do pipeline;
- esquema de dados;
- documentação de anonimização/pseudonimização/agregação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- análise de suficiência;
- revisão metodológica quando necessário;

**Observações metodológicas:**
- Não presumir anonimização apenas porque identificadores diretos foram removidos.
- Registrar incerteza quando a evidência não permite caracterizar adequadamente o dado.
- A avaliação FIAR não substitui determinação jurídica formal da natureza do dado.

---

### PRI-03

**Requisito:**  
O tratamento dos dados é consistente com a finalidade e o Contexto de Uso declarados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-03

**O que o requisito busca verificar:**  
Verificar se coleta, seleção, transformação, acesso e uso dos dados permanecem coerentes com a finalidade declarada da tarefa e com o contexto efetivamente avaliado.

**Aspectos a considerar na aplicabilidade:**
- Aplicável sempre que dados sejam tratados.
- Considerar diferenças entre uso atual e uso pretendido.
- Mudanças de finalidade, população ou integração podem exigir nova análise.
- Restrições éticas, contratuais ou institucionais devem ser consideradas quando pertinentes.

**Exemplos de evidências pertinentes:**
- Data Card;
- Model Card;
- aprovação ética quando aplicável;
- documentação institucional;
- termos ou condições de acesso;
- Identificação da Avaliação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- consistência cruzada;
- contextualização;
- verificação institucional;

**Observações metodológicas:**
- A presença de uma aprovação ética não demonstra automaticamente coerência de todo o tratamento.
- Comparar escopo, período, população, fontes e finalidade entre registros.
- Não atribuir não conformidade jurídica; registrar inconsistências e riscos no escopo do FIAR.

---

### PRI-04

**Requisito:**  
Restrições de acesso, uso, compartilhamento, armazenamento e retenção estão documentadas quando aplicáveis?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-04

**O que o requisito busca verificar:**  
Verificar se as condições que limitam quem pode acessar, utilizar, compartilhar, armazenar ou manter os dados estão identificadas e rastreáveis quando relevantes para a tarefa.

**Aspectos a considerar na aplicabilidade:**
- Aplicabilidade varia conforme natureza e governança dos dados.
- Dados restritos ou sensíveis tendem a exigir maior formalização.
- Dados públicos podem não demandar os mesmos controles, mas condições específicas ainda podem existir.
- Em produção, mudanças de acesso podem exigir acompanhamento operacional.

**Exemplos de evidências pertinentes:**
- políticas de acesso;
- termos de uso ou compartilhamento;
- registros de autorização;
- Data Card;
- políticas de retenção/descarte;
- documentação de armazenamento;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- rastreabilidade;
- consistência com práticas declaradas;

**Observações metodológicas:**
- Não confundir ausência de restrição com ausência de documentação quando a natureza do dado exige clareza.
- Evitar exigir o mesmo conjunto de controles para dados públicos e dados sensíveis.
- Se a política existir apenas em nível institucional, verificar se ela é aplicável à tarefa concreta.

---

### PRI-05

**Requisito:**  
As medidas de proteção adotadas são compatíveis com a natureza dos dados e os riscos identificados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-05

**O que o requisito busca verificar:**  
Verificar se as salvaguardas técnicas, organizacionais e institucionais adotadas são proporcionais aos dados tratados e aos riscos relevantes identificados.

**Aspectos a considerar na aplicabilidade:**
- A aplicabilidade e intensidade dos controles dependem da sensibilidade, granularidade, acesso, ambiente e finalidade.
- Nenhuma técnica específica é universalmente obrigatória.
- Medidas podem incluir anonimização, pseudonimização, minimização, controle de acesso, criptografia, segregação ou armazenamento seguro.

**Exemplos de evidências pertinentes:**
- documentação de anonimização/pseudonimização;
- controles de acesso;
- documentação de segurança dos dados;
- políticas institucionais;
- Data Card;
- registros de revisão de permissões;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão documental;
- revisão metodológica;
- contextualização;
- verificação técnica quando aplicável;

**Observações metodológicas:**
- A presença de uma medida não demonstra adequação por si só.
- Avaliar o risco que a medida pretende tratar e suas limitações.
- Não transformar preferências técnicas do avaliador em requisitos universais.
- O FIAR não certifica conformidade jurídica nem segurança absoluta.

---

### PRI-06

**Requisito:**  
As limitações das medidas de proteção estão documentadas, quando relevantes?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-06

**O que o requisito busca verificar:**  
Verificar se o projeto reconhece limitações, riscos residuais ou condições sob as quais as medidas de proteção podem não ser suficientes.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando as medidas possuem limitações materialmente relevantes.
- A necessidade de detalhamento cresce com sensibilidade e impacto potencial.
- Pode ser não aplicável quando não houver limitação relevante identificável no escopo, desde que justificado.

**Exemplos de evidências pertinentes:**
- Data Card;
- documentação técnica;
- Registro de Decisão Técnica;
- análise de riscos;
- documentação de anonimização ou controle de acesso;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência entre medida e limitação declarada;
- revisão metodológica;

**Observações metodológicas:**
- Não presumir que uma técnica como anonimização elimina todo risco.
- Limitações podem ser técnicas, procedimentais ou institucionais.
- Ausência de seção intitulada 'limitações' não implica ausência de evidência se a informação estiver adequadamente registrada em outra fonte.

---

### PRI-07

**Requisito:**  
Aprovações éticas, registros institucionais ou outras condições aplicáveis são coerentes com o tratamento realizado?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-07

**O que o requisito busca verificar:**  
Verificar se aprovações, termos, autorizações e condições institucionais aplicáveis correspondem ao escopo real do tratamento de dados associado à tarefa.

**Aspectos a considerar na aplicabilidade:**
- Aplicável apenas quando esses registros ou condições forem pertinentes ao projeto e ao tratamento.
- Aprovação ética não deve ser exigida universalmente apenas por se tratar de saúde.
- Comparar população, finalidade, fontes, período e procedimentos quando esses elementos forem relevantes.
- Mudanças substanciais podem exigir revisão pelas instâncias competentes.

**Exemplos de evidências pertinentes:**
- parecer ou aprovação ética;
- termos institucionais;
- Data Card;
- descrição da tarefa;
- documentação de acesso;
- autorizações ou acordos aplicáveis;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação institucional;
- consistência cruzada;
- rastreabilidade;

**Observações metodológicas:**
- O NIAR verifica coerência documental; não substitui CEP, DPO, jurídico ou outra instância competente.
- Menção a um número de aprovação não equivale à verificação do documento quando o requisito depender do conteúdo.
- Ausência do documento deve primeiro ser analisada quanto à aplicabilidade e necessidade.

---

### PRI-08

**Requisito:**  
Quando aplicável, a necessidade de RIPD ou de consulta à instância institucional responsável por proteção de dados foi considerada?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-08

**O que o requisito busca verificar:**  
Verificar se, nos contextos em que a natureza do tratamento ou as regras institucionais tornam a questão relevante, foi considerada a necessidade de RIPD ou consulta à instância responsável por proteção de dados.

**Aspectos a considerar na aplicabilidade:**
- Não é universalmente aplicável.
- A decisão formal sobre RIPD pode pertencer ao controlador ou à instância institucional competente.
- A avaliação deve considerar natureza dos dados, riscos, tipo de tratamento e orientação institucional disponível.

**Exemplos de evidências pertinentes:**
- RIPD quando existente;
- registro de consulta ao DPO/Encarregado;
- decisão ou orientação institucional;
- documentação de riscos de privacidade;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação institucional;
- verificação documental;

**Observações metodológicas:**
- Não transformar o RIPD em artefato obrigatório para todas as tarefas.
- O NIAR não deve substituir a competência institucional do controlador, DPO ou jurídico.
- Uma decisão documentada de não elaborar RIPD pode constituir evidência pertinente quando emitida pela instância competente.

---

### PRI-09

**Requisito:**  
Riscos residuais ou limitações de privacidade relevantes estão registrados e associados a decisões ou medidas de tratamento?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-09

**O que o requisito busca verificar:**  
Verificar se riscos que permanecem após as medidas de proteção e limitações relevantes estão documentados e conectados às decisões, condicionantes, monitoramentos ou outras respostas adotadas.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando houver risco residual ou limitação relevante.
- A resposta pode ser técnica, organizacional, institucional ou de restrição de uso.
- O nível de formalização depende do risco e da trilha.

**Exemplos de evidências pertinentes:**
- Registro de Decisão Técnica;
- documentação de riscos;
- condicionantes;
- planos de tratamento;
- registros de consulta institucional;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- rastreabilidade entre risco e decisão;
- verificação documental;
- consistência cruzada;

**Observações metodológicas:**
- Registrar um risco não é o mesmo que tratá-lo.
- Nem todo risco residual exige eliminação; pode haver decisão fundamentada de aceitar, monitorar ou restringir.
- Aceite institucional de risco deve ser atribuído à instância competente.

---

### PRI-10

**Requisito:**  
Para tarefas em produção, mudanças relevantes no tratamento dos dados, incidentes ou alterações de acesso são acompanhados e documentados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/privacidade.md` — PRI-10

**O que o requisito busca verificar:**  
Verificar se, durante a operação, mudanças materialmente relevantes no tratamento, incidentes de privacidade ou alterações de acesso geram registros e acompanhamento apropriados.

**Aspectos a considerar na aplicabilidade:**
- Específico da Trilha Produção.
- A profundidade depende da natureza dos dados e do impacto potencial.
- Mudanças menores sem efeito no tratamento podem não exigir novo ciclo completo.
- Incidentes podem acionar outros requisitos e dimensões.

**Exemplos de evidências pertinentes:**
- registros de incidentes;
- histórico de versões;
- monitoramento;
- logs ou registros de acesso;
- registros de mudança;
- decisões corretivas;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- análise de evidências operacionais;
- rastreabilidade longitudinal;
- consistência entre evento e resposta;

**Observações metodológicas:**
- Não aplicável a tarefas sem operação ativa.
- Distinguir evento administrativo sem impacto de mudança relevante no tratamento.
- A existência de logs não basta; deve ser possível relacionar eventos relevantes a análise e resposta quando necessário.

---

## Responsabilização

**Fonte normativa da dimensão:**  
`FIAR-Saude/docs/dimensoes_avaliacao.md`

A dimensão de Responsabilização é uma das sete dimensões canônicas do FIAR-Saúde. Na documentação vigente consultada, o arquivo detalhado de avaliação de Responsabilização ainda não foi criado. Portanto, este guia **não cria identificadores ou requisitos operacionais de Responsabilização**.

Até a publicação dos requisitos canônicos, devem ser tratados apenas como aspectos orientadores os elementos já indicados pelo FIAR-Saúde, como registros nominais de decisão, registros de aceite de risco e condicionantes quando aplicáveis, atribuição clara de responsabilidades por etapa do ciclo de vida e rastreabilidade de aprovações institucionais.

Esses aspectos não devem ser convertidos em uma lista local de requisitos numerados antes de sua consolidação no FIAR-Saúde.

---

## Rastreabilidade

**Fonte normativa da dimensão:**  
`FIAR-Saude/docs/dimensoes_avaliacao.md`

A dimensão de Rastreabilidade é uma das sete dimensões canônicas do FIAR-Saúde. Na documentação vigente consultada, o arquivo detalhado de avaliação de Rastreabilidade ainda não foi criado. Portanto, este guia **não cria identificadores ou requisitos operacionais de Rastreabilidade**.

Até a publicação dos requisitos canônicos, devem ser tratados como aspectos orientadores o versionamento de dados e modelos, o histórico de decisões técnicas, os registros de execução e logs e a disponibilidade de artefatos técnicos ao longo do tempo.

A análise concreta desses aspectos pode apoiar outros requisitos já vigentes, mas não deve produzir requisitos locais que concorram com a documentação canônica.

---

## Justiça

A dimensão de Justiça examina evidências de possíveis disparidades relevantes entre grupos, populações, territórios ou unidades pertinentes ao Contexto de Uso, sem presumir que toda diferença observada represente automaticamente injustiça ou discriminação. Os requisitos canônicos vigentes são JUS-01 a JUS-09.

### JUS-01

**Requisito:**  
Os grupos, populações, territórios ou unidades relevantes para o contexto de uso foram identificados e justificados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-01

**O que o requisito busca verificar:**  
Verificar se os recortes relevantes para analisar possíveis disparidades foram escolhidos com base na tarefa e no Contexto de Uso, e não apenas porque determinados atributos estavam disponíveis nos dados.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando diferenças entre grupos, populações, territórios ou unidades possam ser relevantes para impacto ou desempenho.
- A seleção deve considerar população afetada, finalidade, desigualdades conhecidas, dados e consequências dos erros.
- Nem todas as categorias demográficas são aplicáveis a toda tarefa.

**Exemplos de evidências pertinentes:**
- Contexto de Uso;
- Formulário de Entrada;
- Data Card;
- Model Card;
- justificativa de seleção de grupos;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência cruzada;
- contextualização;

**Observações metodológicas:**
- Disponibilidade de atributo não é justificativa suficiente.
- Ausência de dado para grupo relevante deve ser registrada como limitação, não preenchida por inferência.
- Grupos relevantes podem ser territoriais, institucionais ou clínicos, e não apenas demográficos.

---

### JUS-02

**Requisito:**  
Existem limitações de cobertura, representação ou qualidade dos dados relevantes para esses grupos?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-02

**O que o requisito busca verificar:**  
Verificar se foram identificadas limitações dos dados capazes de afetar de forma desigual os grupos relevantes, incluindo sub-representação, cobertura, completude, qualidade ou diferenças de medição.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando os dados permitirem ou exigirem análise de representação/qualidade por grupos relevantes.
- A impossibilidade de avaliar por ausência de informação pode ser uma limitação material.
- O nível de análise depende da tarefa e das consequências potenciais.

**Exemplos de evidências pertinentes:**
- Data Card;
- análises descritivas;
- documentação de preparação dos dados;
- estatísticas de cobertura;
- registros de exclusão;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão documental;
- revisão metodológica;
- consistência cruzada;

**Observações metodológicas:**
- Não inferir representatividade apenas pelo tamanho total do dataset.
- Distinguir representação numérica de adequação substantiva ao contexto.
- Limitações identificadas não significam automaticamente que o sistema seja injusto.

---

### JUS-03

**Requisito:**  
O desempenho ou impacto foi avaliado entre grupos relevantes quando aplicável?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-03

**O que o requisito busca verificar:**  
Verificar se diferenças relevantes de desempenho ou impacto foram examinadas entre os grupos identificados quando esse tipo de análise é pertinente à tarefa.

**Aspectos a considerar na aplicabilidade:**
- Nem toda tarefa permite a mesma análise de grupos.
- A aplicabilidade depende de disponibilidade de dados, função da tarefa e consequências dos resultados.
- Métricas devem ser adequadas ao tipo de problema e podem incluir desempenho, erro ou outro impacto pertinente.

**Exemplos de evidências pertinentes:**
- Fairness Report ou equivalente;
- métricas estratificadas;
- resultados experimentais;
- Model Card;
- análises por subgrupo;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão metodológica;
- revisão de métricas e resultados;
- reprodução ou testes quando aplicável;

**Observações metodológicas:**
- Métrica global não substitui análise por grupo quando esta for materialmente relevante.
- A ausência de análise deve ser interpretada à luz da aplicabilidade e da disponibilidade dos dados.
- Diferença numérica observada ainda precisa ser contextualizada.

---

### JUS-04

**Requisito:**  
As métricas e métodos utilizados são adequados à tarefa e aos grupos avaliados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-04

**O que o requisito busca verificar:**  
Verificar se as escolhas de métricas, comparações, agregações e métodos de análise de disparidade são tecnicamente adequadas ao tipo de tarefa, tamanho dos grupos e finalidade da avaliação.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando houver análise quantitativa ou metodológica de justiça.
- Métricas devem ser selecionadas conforme classificação, regressão, previsão ou outra tarefa.
- Tamanho e estabilidade dos grupos podem afetar a interpretação.
- A ausência de uma métrica padronizada universal deve ser tratada por justificativa metodológica.

**Exemplos de evidências pertinentes:**
- Fairness Report;
- protocolo experimental;
- Model Card;
- documentação de métricas;
- código ou resultados, quando necessários e disponíveis;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão metodológica;
- revisão de métricas;
- análise de suficiência e estabilidade;

**Observações metodológicas:**
- Não impor uma única definição de fairness a todas as tarefas.
- Evitar interpretar diferenças pequenas sem considerar incerteza, tamanho de amostra e relevância prática.
- Métrica tecnicamente correta pode ser inadequada ao objetivo decisório se não capturar o dano relevante.

---

### JUS-05

**Requisito:**  
Disparidades identificadas foram adequadamente interpretadas no contexto de uso?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-05

**O que o requisito busca verificar:**  
Verificar se diferenças observadas foram interpretadas considerando magnitude, estabilidade, composição dos grupos, consequências potenciais e contexto, evitando conclusões automáticas de injustiça ou irrelevância.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando houver disparidades identificadas.
- A interpretação depende da função da tarefa e de quem pode ser afetado.
- Pode exigir conhecimento contextual ou institucional além da métrica.

**Exemplos de evidências pertinentes:**
- Fairness Report;
- documentação de limitações;
- análises contextuais;
- Model Card;
- registros de discussão técnica ou institucional;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- contextualização;
- consistência entre evidências;
- revisão de resultados;

**Observações metodológicas:**
- Disparidade não equivale automaticamente a discriminação ou injustiça.
- Ausência de significância estatística não torna automaticamente uma diferença irrelevante.
- Consequências potenciais e contexto de uso devem participar da interpretação.

---

### JUS-06

**Requisito:**  
Quando necessário, possíveis causas das disparidades foram investigadas?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-06

**O que o requisito busca verificar:**  
Verificar se, diante de disparidades materialmente relevantes, o projeto investigou fatores plausíveis relacionados aos dados, medição, seleção, modelagem, contexto ou mudanças de distribuição.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando a magnitude ou relevância do achado justificar investigação adicional.
- Nem toda diferença exige investigação causal completa.
- A capacidade de investigar depende das evidências e do desenho disponível.

**Exemplos de evidências pertinentes:**
- análises adicionais;
- documentação dos dados;
- registros técnicos;
- comparações de cobertura/qualidade;
- experimentos de sensibilidade ou ablação quando adequados;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- revisão metodológica;
- consistência cruzada;
- análise exploratória adicional quando aplicável;

**Observações metodológicas:**
- Hipótese sobre causa não deve ser apresentada como causalidade demonstrada.
- Estruturas sociais ou epidemiológicas podem contribuir para disparidades sem que o modelo seja a única causa.
- Quando a origem não puder ser estabelecida, a limitação deve permanecer explícita.

---

### JUS-07

**Requisito:**  
Medidas de mitigação, monitoramento, restrição ou outra resposta foram consideradas quando os achados justificaram ação?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-07

**O que o requisito busca verificar:**  
Verificar se achados relevantes resultaram em consideração explícita de respostas proporcionais, que podem incluir investigação, mudança de dados ou modelo, monitoramento, restrição de uso ou decisão institucional.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando os achados justificarem alguma ação.
- A ação adequada depende da causa provável, da magnitude, do Contexto de Uso e dos trade-offs.
- Mitigação técnica não é a única resposta possível.
- Em produção, monitoramento ou condicionantes podem ser especialmente relevantes.

**Exemplos de evidências pertinentes:**
- Registro de Decisão Técnica;
- Fairness Report;
- planos de mitigação;
- condicionantes;
- registros de monitoramento;
- decisões de restrição ou aceite de risco;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- rastreabilidade entre achado e decisão;
- revisão de efeitos da mitigação;

**Observações metodológicas:**
- Ausência de mitigação técnica não implica automaticamente inadequação.
- A decisão de não mitigar deve ser fundamentada quando o achado for relevante.
- Medidas podem introduzir trade-offs que precisam ser avaliados e documentados.

---

### JUS-08

**Requisito:**  
Riscos residuais, limitações e trade-offs relevantes foram documentados?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-08

**O que o requisito busca verificar:**  
Verificar se limitações persistentes, riscos residuais e efeitos colaterais das escolhas de mitigação ou operação estão registrados e vinculados às decisões correspondentes.

**Aspectos a considerar na aplicabilidade:**
- Aplicável quando existirem riscos residuais, limitações ou trade-offs materialmente relevantes.
- A profundidade depende do impacto potencial e da resposta adotada.
- Pode incluir trade-offs entre grupos, desempenho global e redução de disparidade.

**Exemplos de evidências pertinentes:**
- Registro de Decisão Técnica;
- Model Card;
- Fairness Report;
- relatório de avaliação;
- condicionantes ou decisões institucionais;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- verificação documental;
- consistência;
- rastreabilidade entre limitação, decisão e uso;

**Observações metodológicas:**
- Não apagar risco residual após uma mitigação parcial.
- Trade-offs devem ser descritos de forma compatível com as métricas efetivamente observadas.
- Aceite de risco é uma decisão institucional quando assim definido pela governança, não conclusão do avaliador isolado.

---

### JUS-09

**Requisito:**  
Para tarefas em produção, disparidades relevantes são acompanhadas longitudinalmente quando necessário?

**Fonte normativa:**  
`FIAR-Saude/docs/avaliacao/justica.md` — JUS-09

**O que o requisito busca verificar:**  
Verificar se disparidades materialmente relevantes continuam sendo acompanhadas após implantação, permitindo identificar persistência, agravamento, melhora ou surgimento de novos padrões ao longo de versões e mudanças de contexto.

**Aspectos a considerar na aplicabilidade:**
- Específico da Trilha Produção.
- Aplicável quando a análise anterior indicar grupos ou disparidades relevantes para acompanhamento.
- A frequência e as métricas devem ser proporcionais ao risco e ao ritmo de mudança da tarefa.

**Exemplos de evidências pertinentes:**
- relatórios de monitoramento;
- histórico de versões;
- métricas por grupo ao longo do tempo;
- registros de drift;
- decisões decorrentes de mudanças;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**
- análise de evidências operacionais;
- rastreabilidade longitudinal;
- comparação entre versões;

**Observações metodológicas:**
- Não aplicável à Trilha Experimental sem operação ativa.
- Monitorar somente a métrica global pode ser insuficiente quando o risco relevante é distributivo.
- Mudanças na composição dos grupos ou nos dados podem alterar a interpretação longitudinal.

---

## Transparência

**Fonte normativa da dimensão:**  
`FIAR-Saude/docs/dimensoes_avaliacao.md`

A dimensão de Transparência é uma das sete dimensões canônicas do FIAR-Saúde. Na documentação vigente consultada, o arquivo detalhado de avaliação de Transparência ainda não foi criado. Portanto, este guia **não cria identificadores ou requisitos operacionais de Transparência**.

Até a publicação dos requisitos canônicos, devem ser tratados como aspectos orientadores os relatórios de explicabilidade local e global, justificativas e documentação sobre resultados ou decisões apoiadas pelo sistema quando aplicável, mecanismos de interpretação do modelo e comunicação de limitações a públicos não técnicos.

Esses aspectos podem orientar a preparação de evidências, mas não devem ser convertidos em requisitos numerados não oficiais.

---

## Uso do guia durante a avaliação

Para cada requisito canônico aplicável:

1. utilizar este guia para compreender o objetivo, os aspectos de aplicabilidade, as evidências pertinentes e os mecanismos de verificação possíveis;
2. registrar a aplicação concreta no `template_avaliacao_requisito.md`;
3. determinar `Aplicável` ou `Não aplicável` antes da análise das evidências;
4. registrar somente evidências efetivamente verificadas no ciclo;
5. registrar somente mecanismos de verificação efetivamente utilizados;
6. analisar suficiência, consistência, rastreabilidade e contextualização;
7. registrar achados, limitações, pendências, inconsistências e eventual sinal de governança conforme sustentado pelas evidências;
8. não transformar ausência de artefato, evidência ainda não recebida ou estado administrativo em resultado automático de conformidade.

A conformidade é consolidada para a combinação **Tarefa de IA + Versão Avaliável + Contexto de Uso**. A maturidade é inferida separadamente, de forma longitudinal, no nível do projeto.

---


## Referências

### Documentação normativa do FIAR-Saúde

- FIAR-Saúde. `docs/dimensoes_avaliacao.md`.
- FIAR-Saúde. `docs/avaliacao/governanca.md`.
- FIAR-Saúde. `docs/avaliacao/privacidade.md`.
- FIAR-Saúde. `docs/avaliacao/justica.md`.

### Documentação operacional relacionada do FIAR-Audit-Template

- `documentacao_metodologica/guia_operacional_pre_avaliacao_pilotos.md`
- `avaliacao_niar/avaliacao_por_dimensao/template_avaliacao_requisito.md`

> Este guia deve referenciar prioritariamente a documentação canônica do FIAR-Saúde. Referências externas, como normas, legislação ou literatura científica, devem ser incorporadas somente quando a documentação normativa do FIAR-Saúde estabelecer explicitamente esse vínculo ou quando forem necessárias para fundamentar uma orientação metodológica específica.

---

## Controle de atualização normativa

Este arquivo deve acompanhar a documentação vigente do FIAR-Saúde.

Quando um requisito canônico for criado, alterado, removido ou renumerado no FIAR-Saúde:

- atualizar sua formulação neste guia;
- revisar as orientações operacionais correspondentes;
- preservar a distinção entre requisito canônico e orientação operacional;
- evitar manter requisitos locais obsoletos;
- registrar a alteração no controle de versão do FIAR-Audit-Template.

Em caso de conflito, prevalece a documentação vigente do FIAR-Saúde.

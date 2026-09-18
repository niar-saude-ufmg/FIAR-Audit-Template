# Guia de Requisitos para Avaliação

Este documento organiza operacionalmente os requisitos vigentes do FIAR-Saúde para apoiar sua aplicação nos ciclos de avaliação conduzidos pelo NIAR-Saúde.

Este guia não substitui a documentação normativa do FIAR-Saúde.

Em caso de divergência, prevalece a documentação vigente do FIAR-Saúde.

A inclusão de um tipo de evidência neste guia não implica que determinado artefato seja obrigatório para todas as tarefas.

A aplicabilidade deve ser determinada individualmente para cada requisito, considerando a Tarefa de IA, a Versão Avaliável, o Contexto de Uso e a Trilha de Execução.

Um requisito deve ser considerado Não aplicável somente quando a condição objetiva pressuposta por sua formulação não estiver presente no objeto avaliado. A ausência de prática, mecanismo, capacidade, procedimento, registro ou evidência que o próprio requisito busca avaliar não constitui justificativa de não aplicabilidade e deve ser refletida posteriormente na análise e no resultado do requisito. Quando a presença da condição objetiva ainda não puder ser determinada, a aplicabilidade não deve ser presumida como Não aplicável.

As orientações deste guia apoiam o preenchimento do template de avaliação de requisito. O guia apresenta possibilidades de interpretação, evidências e verificação; a avaliação concreta deve registrar somente aquilo que for aplicável e efetivamente verificado no ciclo correspondente.

As formulações dos requisitos reproduzem a documentação canônica vigente do FIAR-Saúde. As explicações, exemplos e cautelas deste guia têm função operacional e não criam requisitos adicionais.

## Fontes normativas e natureza das orientações

Os requisitos reproduzidos neste guia têm como fonte normativa a documentação vigente do FIAR-Saúde.

Fontes principais:

- `FIAR-Saude/docs/dimensoes_avaliacao.md`
- `FIAR-Saude/docs/avaliacao/governanca.md`
- `FIAR-Saude/docs/avaliacao/seguranca.md`
- `FIAR-Saude/docs/avaliacao/privacidade.md`
- `FIAR-Saude/docs/avaliacao/responsabilizacao.md`
- `FIAR-Saude/docs/avaliacao/rastreabilidade.md`
- `FIAR-Saude/docs/avaliacao/justica.md`
- `FIAR-Saude/docs/avaliacao/transparencia.md`

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
- GOV-01 verifica a existência e a identificação dos papéis e competências institucionais necessários à governança da tarefa. A atribuição de responsabilidade por decisões, ações ou resultados concretos é analisada em RES-01.

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
- GOV-02 verifica se existe processo identificável para as categorias de decisão relevantes à tarefa.
- A associação de uma decisão concreta ao responsável e ao seu fundamento é analisada em RES-02.
- A capacidade de reconstruir a relação entre evidência, achado, decisão e ação é analisada em RAS-04.

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

- O requisito é aplicável quando, pela natureza da tarefa, pelo grau de autonomia, pelas consequências de seus resultados ou pelo Contexto de Uso, for pertinente determinar a necessidade de supervisão humana. A inexistência de supervisão atualmente definida ou implementada não constitui justificativa de não aplicabilidade.
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

- Aplicável quando, conforme a análise de GOV-04, a supervisão humana for pertinente ao uso da tarefa. A inexistência de responsáveis, informações ou mecanismos de intervenção não torna o requisito não aplicável.
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

- Aplicável quando as características da tarefa, de seu Contexto de Uso ou os achados do ciclo indicarem riscos, limitações ou questões materialmente relevantes que demandem tratamento ou decisão. A ausência de processo de tratamento ou escalonamento não constitui justificativa de não aplicabilidade.
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

- Aplicável quando existirem condicionantes, restrições ou decisões institucionais pertinentes à tarefa, independentemente de estarem adequadamente documentados. A ausência de registro não demonstra, por si só, a ausência dessa condição.
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
- A natureza e a intensidade dos mecanismos esperados devem ser proporcionais ao estágio da tarefa e à Trilha de Execução. A inexistência de mecanismos de monitoramento, revisão ou atualização que sejam pertinentes ao estágio da tarefa deve ser tratada no resultado da avaliação, e não como justificativa de não aplicabilidade.

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

- Aplicável quando a tarefa, seus dados, modelo, procedimentos, finalidade, integração ou Contexto de Uso forem passíveis de mudanças relevantes para a avaliação. A inexistência de critérios ou gatilhos previamente definidos não demonstra que a tarefa não esteja sujeita a evolução.
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

A dimensão de Segurança avalia se a Tarefa de IA e seus componentes relevantes estão protegidos, de forma proporcional ao contexto e aos riscos identificados, contra falhas, uso indevido, acesso ou alteração não autorizados, comprometimento e outras condições capazes de afetar sua integridade, disponibilidade, funcionamento esperado ou confiabilidade.

Os requisitos canônicos vigentes são SEG-01 a SEG-06.

A aplicação desta dimensão deve permanecer vinculada à Tarefa de IA, à Versão Avaliável, ao Contexto de Uso, à Trilha de Execução e aos riscos efetivamente pertinentes. A análise não constitui auditoria geral da infraestrutura de tecnologia da informação da organização.

A dimensão deve ser distinguida de:

- **Privacidade**, que avalia o tratamento e a proteção de dados pessoais ou sensíveis;
- **Governança**, que avalia estruturas, competências, processos decisórios, supervisão, tratamento e escalonamento;
- **Rastreabilidade**, que avalia se versões, eventos, mudanças e registros relevantes podem ser reconstruídos;
- **Transparência**, que avalia se informações relevantes sobre a tarefa, seus riscos, limitações e condições estão adequadamente documentadas ou comunicadas;
- **Responsabilização**, que avalia quem responde por decisões, ações e consequências e se existem elementos suficientes para prestação de contas.

Uma mesma evidência pode contribuir para mais de uma dimensão, mas deve responder à pergunta específica do requisito em análise.

Mecanismos como pentest, red teaming, hardening, isolamento, testes adversariais, monitoramento contínuo, logs operacionais ou rollback não devem ser presumidos como universais. Sua necessidade deve decorrer do risco que precisa ser tratado.

---

### SEG-01

**Requisito:**
Os ativos, componentes, ambientes e riscos de segurança relevantes para a Tarefa de IA estão identificados e documentados de forma compatível com seu Contexto de Uso e sua Trilha de Execução?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-01

**O que o requisito busca verificar:**
Verificar se existe delimitação suficiente do que precisa ser protegido e dos riscos de segurança materialmente relevantes para a Tarefa de IA no escopo do ciclo.

O requisito combina a identificação dos ativos e componentes relevantes com a identificação dos riscos associados a eles. Seu objetivo não é produzir um inventário completo da infraestrutura institucional, mas estabelecer uma base suficiente para compreender quais componentes da tarefa podem ser afetados por acesso indevido, alteração, comprometimento, indisponibilidade, falhas ou outros eventos relevantes.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde, inclusive na Trilha Experimental.
- A extensão dos ativos e ambientes considerados depende da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da Trilha de Execução.
- Podem ser pertinentes dados, modelos, código, configurações, pipelines, dependências, interfaces, serviços externos, credenciais e ambientes de desenvolvimento, avaliação ou produção.
- Não é necessário inventariar componentes sem relação material com a tarefa.
- O risco deve ser específico o suficiente para estabelecer o que pode ser afetado e por qual tipo de evento ou condição.
- Riscos específicos de IA somente devem ser considerados quando a arquitetura ou o Contexto de Uso os tornarem materialmente plausíveis.
- Uma tarefa experimental pode possuir riscos de Segurança mesmo sem integração a um sistema em produção.
- A passagem para produção pode introduzir novos ativos, interfaces, dependências e riscos que não existiam no ciclo experimental.

**Exemplos de evidências pertinentes:**

- documentação técnica da tarefa;
- Model Card ou documentação equivalente;
- diagramas ou descrições de arquitetura;
- documentação dos ambientes utilizados;
- inventário ou descrição dos componentes materialmente relevantes;
- documentação de dependências;
- registros ou análises de riscos de segurança;
- documentação de interfaces e serviços utilizados;
- registros técnicos que permitam compreender os ativos e riscos considerados;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- análise de suficiência;
- contextualização;
- consistência cruzada entre documentação da tarefa, arquitetura e riscos;
- revisão técnica específica quando necessária.

**Observações metodológicas:**

- Não transformar o requisito em inventário geral de infraestrutura de TI.
- Um ativo deve entrar no escopo quando sua perda, alteração, acesso indevido, indisponibilidade ou comprometimento puder afetar materialmente a tarefa ou seus resultados relevantes.
- Não exigir categorias genéricas de ameaça sem relação demonstrável com a arquitetura ou o Contexto de Uso.
- Não presumir riscos como poisoning, model extraction, adversarial examples, prompt injection ou jailbreak apenas porque se trata de IA.
- Quando um risco materialmente pertinente não puder ser caracterizado por ausência de informação factual sobre a arquitetura ou ambiente, pode ser necessária uma pendência factual específica.
- Ausência de documentação de um risco não constitui automaticamente inconsistência. Inconsistência exige conflito efetivo entre fontes ou informações que deveriam ser compatíveis.
- A identificação e o escalonamento institucional do risco não devem ser avaliados aqui como processo de Governança; SEG-01 verifica a caracterização do risco de Segurança.

---

### SEG-02

**Requisito:**
Existem mecanismos proporcionais para restringir e controlar o acesso aos dados, modelos, artefatos e ambientes relevantes para a tarefa?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-02

**O que o requisito busca verificar:**
Verificar se existem controles compatíveis com os riscos identificados para limitar o acesso aos componentes relevantes da tarefa às pessoas, sistemas ou funções que efetivamente necessitam desse acesso.

O requisito abrange o acesso a ativos da Tarefa de IA de forma mais ampla e não se limita aos dados pessoais ou sensíveis.

**Aspectos a considerar na aplicabilidade:**

- O nível de controle esperado depende dos ativos, das funções envolvidas, dos ambientes utilizados e das consequências de acesso indevido.
- Controles distintos podem ser adequados para desenvolvimento, avaliação e produção.
- Dados, modelos, código, configurações, credenciais, interfaces e ambientes podem demandar controles diferentes.
- Na Trilha Experimental, ainda podem existir restrições relevantes de acesso a dados, modelos ou ambientes.
- Na Trilha Produção, podem ser necessários controles adicionais relacionados ao acesso operacional.
- A existência de dados pessoais ou sensíveis também pode tornar a mesma evidência pertinente à dimensão de Privacidade.
- Nenhuma tecnologia específica de autenticação ou autorização deve ser presumida como obrigatória.

**Exemplos de evidências pertinentes:**

- documentação de autenticação e autorização;
- registros ou matrizes de permissões;
- políticas de controle de acesso aplicáveis à tarefa;
- documentação de segregação de funções;
- documentação de gestão e proteção de credenciais;
- configurações de acesso aos ambientes pertinentes;
- registros de revisão de permissões;
- evidências de restrição de interfaces ou serviços;
- documentação institucional aplicável aos ativos considerados;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- revisão técnica quando necessária;
- contextualização;
- consistência entre permissões declaradas e funções;
- inspeção ou demonstração de controles específicos, quando pertinente e viável.

**Observações metodológicas:**

- Não confundir controle de acesso de Segurança com toda a avaliação de Privacidade. Em Segurança, a pergunta é se o ativo relevante da tarefa está adequadamente protegido contra acesso indevido.
- Autenticação multifator, princípio de menor privilégio, segregação ou outros controles são mecanismos possíveis, não exigências universais.
- A existência de uma política institucional geral não demonstra automaticamente que o controle está aplicado à tarefa concreta.
- A ausência de logs de acesso não implica automaticamente descumprimento de SEG-02; primeiro deve ser determinado se esses logs são necessários para demonstrar o controle ou outro requisito.
- Não inferir permissões a partir de autoria de repositórios, documentos ou participação no projeto.
- Se a documentação declarar controles incompatíveis com a configuração efetivamente demonstrada, pode existir inconsistência.
- Questões sobre quem possui competência institucional para autorizar determinado acesso pertencem principalmente a Governança ou Responsabilização, conforme o caso.

---

### SEG-03

**Requisito:**
Existem mecanismos proporcionais para proteger a integridade da tarefa e de seus componentes relevantes contra alteração, comprometimento ou uso indevido?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-03

**O que o requisito busca verificar:**
Verificar se os componentes relevantes da tarefa possuem mecanismos adequados ao risco para reduzir a possibilidade de alteração não autorizada, corrupção, comprometimento ou utilização de forma capaz de afetar o funcionamento ou os resultados da Tarefa de IA.

O requisito trata da proteção da integridade. Ele não exige, por si só, que todo histórico de mudanças seja reconstruível; essa questão pertence principalmente à Rastreabilidade.

**Aspectos a considerar na aplicabilidade:**

- Os componentes materialmente relevantes devem ser determinados a partir de SEG-01.
- Podem ser pertinentes modelos, pesos, código, configurações, pipelines, dependências, artefatos técnicos e resultados.
- O nível de proteção depende das consequências possíveis de uma alteração ou comprometimento.
- Na Trilha Experimental, podem ser suficientes mecanismos diferentes dos necessários em operação ativa.
- Na Trilha Produção, a proteção contra alterações não autorizadas de componentes implantados pode adquirir maior relevância.
- Riscos de supply chain, dependências comprometidas ou manipulação adversarial devem ser considerados somente quando pertinentes.
- Mecanismos de verificação de integridade podem ser manuais, procedimentais ou automatizados, conforme o contexto.

**Exemplos de evidências pertinentes:**

- documentação de controle de alterações;
- controles de integridade de modelos, código ou artefatos;
- documentação de configurações relevantes;
- mecanismos de validação antes de uso ou implantação;
- registros de proteção ou gestão de dependências;
- evidências de segregação de permissões de alteração;
- testes técnicos direcionados ao risco identificado, quando pertinentes;
- registros técnicos equivalentes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- revisão documental;
- revisão técnica;
- análise de suficiência;
- consistência entre risco identificado e controle adotado;
- inspeção ou teste técnico específico, quando necessário e proporcional.

**Observações metodológicas:**

- Versionamento pode fornecer evidência útil, mas versionamento por si só não demonstra proteção contra alteração indevida.
- Não avaliar neste requisito a reconstrução completa do histórico de versões; isso pertence à Rastreabilidade.
- Não exigir assinatura, hashing, attestation ou tecnologia equivalente como mecanismo universal.
- Não exigir testes adversariais quando o risco correspondente não for materialmente pertinente.
- A ausência de um artefato denominado “relatório de segurança” não constitui ausência de evidência se o controle estiver demonstrado em fontes adequadas.
- Quando houver alegação de proteção sem evidência suficiente de implementação ou aplicação à Versão Avaliável, registrar insuficiência de evidência antes de concluir sobre conformidade.

---

### SEG-04

**Requisito:**
Quando a disponibilidade ou a continuidade forem relevantes ao Contexto de Uso, existem mecanismos proporcionais para lidar com falhas, indisponibilidade e recuperação da tarefa ou de seus componentes relevantes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-04

**O que o requisito busca verificar:**
Verificar se, quando falha ou indisponibilidade puder produzir consequência material para o Contexto de Uso, existem mecanismos proporcionais para lidar com interrupção, perda de componentes ou necessidade de recuperação.

O requisito é explicitamente condicionado à relevância da disponibilidade e da continuidade para a tarefa avaliada.

**Aspectos a considerar na aplicabilidade:**

- A aplicabilidade deve ser determinada antes da análise dos mecanismos existentes.
- Tarefas exclusivamente experimentais podem ter baixa dependência de disponibilidade contínua, mas isso não deve ser presumido sem considerar o contexto.
- Tarefas em produção tendem a tornar disponibilidade e continuidade mais relevantes, especialmente quando integradas a fluxos assistenciais ou operacionais.
- Deve-se considerar a consequência plausível da indisponibilidade, e não simplesmente a existência de infraestrutura.
- Backup, redundância, fallback, contingência e rollback são mecanismos possíveis, não requisitos universais.
- Recuperabilidade de artefatos experimentais pode ser demonstrada de forma diferente da continuidade de um serviço operacional.
- O mecanismo adequado depende do componente que falha e da função desempenhada pela tarefa.

**Exemplos de evidências pertinentes:**

- documentação de recuperação;
- procedimentos de contingência;
- mecanismos ou registros de backup;
- documentação de redundância, quando aplicável;
- procedimentos de restauração;
- mecanismos de fallback;
- documentação de rollback, quando pertinente;
- procedimentos diante de indisponibilidade;
- testes ou registros de recuperação, quando necessários;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- contextualização;
- revisão técnica;
- demonstração ou teste de recuperação, quando necessário e viável;
- consistência entre consequência da falha e mecanismo de tratamento.

**Observações metodológicas:**

- Não considerar SEG-04 automaticamente aplicável apenas porque existe um sistema computacional.
- Não transformar backup, redundância ou rollback em exigências universais.
- Um mecanismo de backup pode proteger dados ou artefatos sem garantir continuidade operacional; verificar o que ele efetivamente demonstra.
- GOV-10 pode tratar da capacidade governada de restringir, suspender ou descontinuar uma tarefa em produção; SEG-04 trata dos mecanismos de Segurança relacionados a falha, indisponibilidade e recuperação.
- A existência de um plano não demonstra, por si só, que o mecanismo técnico necessário exista.
- Quando a não aplicabilidade decorrer da ausência de dependência material de disponibilidade, registrar essa justificativa com base no Contexto de Uso.

---

### SEG-05

**Requisito:**
Os controles de segurança aplicáveis ao ambiente de desenvolvimento, avaliação ou execução são compatíveis com os riscos relevantes da tarefa?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-05

**O que o requisito busca verificar:**
Verificar se características dos ambientes efetivamente utilizados pela Tarefa de IA possuem controles proporcionais aos riscos materialmente relevantes para a tarefa.

O requisito não transforma o FIAR-Saúde em auditoria geral da infraestrutura institucional. Devem ser analisados apenas os controles do ambiente cuja ausência, falha ou configuração inadequada possa afetar materialmente a Segurança da Tarefa de IA no escopo avaliado.

**Aspectos a considerar na aplicabilidade:**

- Identificar primeiro quais ambientes participam efetivamente do desenvolvimento, avaliação ou execução da Versão Avaliável.
- Avaliar somente controles relacionados aos riscos pertinentes identificados para esses ambientes.
- Ambientes experimentais e ambientes de produção podem exigir níveis diferentes de proteção.
- O fato de a tarefa utilizar infraestrutura compartilhada não torna toda essa infraestrutura objeto da avaliação.
- Podem ser pertinentes dependências, serviços externos, armazenamento, credenciais, interfaces, segmentação ou configurações.
- Hardening, isolamento, segregação de ambientes ou segmentação de rede somente devem ser exigidos quando houver relação demonstrável com o risco.
- Controles institucionais gerais podem ser utilizados como evidência quando sua aplicação à tarefa estiver demonstrada.
- Dependências externas devem ser consideradas apenas na medida em que sejam materialmente relevantes à Segurança da tarefa.

**Exemplos de evidências pertinentes:**

- documentação dos ambientes utilizados;
- diagramas ou descrições técnicas pertinentes;
- configurações de segurança relevantes;
- documentação de segregação entre ambientes;
- documentação de dependências e serviços utilizados;
- controles de credenciais;
- evidências de isolamento, quando necessário;
- documentação de armazenamento;
- registros técnicos de configuração;
- políticas institucionais acompanhadas de evidência de aplicabilidade à tarefa;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- revisão documental;
- revisão técnica direcionada;
- contextualização;
- análise de suficiência;
- inspeção ou demonstração de configuração específica, quando necessária;
- consistência entre risco do ambiente e controle adotado.

**Observações metodológicas:**

- Não auditar indiscriminadamente rede, servidores, sistema operacional, políticas corporativas ou demais componentes da infraestrutura.
- A pergunta operacional deve permanecer: “este aspecto do ambiente é materialmente relevante para um risco da Tarefa de IA?”
- Hardening não é requisito em si; pode ser mecanismo para responder a um risco específico.
- Isolamento também não é universal. Sala segura, sandbox, containerização ou segregação física/lógica devem ser consideradas apenas quando pertinentes.
- Não exigir certificação de segurança da infraestrutura como substituto da análise do requisito.
- Uma certificação ou política institucional pode constituir evidência, mas deve ser verificada quanto à cobertura do ambiente efetivamente utilizado pela tarefa.
- Não utilizar SEG-05 para avaliar quem decide sobre controles ou quem aceita risco residual; essas questões pertencem principalmente a Governança e Responsabilização.
- Se não houver informação factual suficiente para saber em qual ambiente a Versão Avaliável foi executada, pode ser necessária complementação factual antes da conclusão da análise.

---

### SEG-06

**Requisito:**
Para tarefas em produção, ou quando os riscos de segurança pertinentes à tarefa e ao seu Contexto de Uso justificarem, existem mecanismos proporcionais para detectar, registrar e responder a eventos ou incidentes de segurança relevantes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/seguranca.md` — SEG-06

**O que o requisito busca verificar:**
Verificar se, quando o estágio da tarefa ou os riscos de segurança pertinentes à tarefa e ao seu Contexto de Uso  exigirem capacidade de acompanhamento de eventos de Segurança, existem mecanismos proporcionais para detectar ocorrências relevantes, preservar registros suficientes e realizar resposta técnica adequada.

O requisito não torna monitoramento contínuo ou gestão formal de incidentes obrigatórios para toda tarefa. Sua aplicabilidade e profundidade dependem da Trilha de Execução e do risco.

**Aspectos a considerar na aplicabilidade:**

- Em tarefas na Trilha Produção, o requisito tende a ser aplicável porque há operação ativa, mas seu nível de formalização continua dependente dos riscos concretos.
- Em tarefas experimentais, o requisito pode ser aplicável quando riscos específicos justifiquem detecção, registro e resposta mesmo sem operação ativa.
- A referência aos riscos de segurança pertinentes à tarefa e ao seu Contexto de Uso impede interpretar SEG-06 como requisito exclusivamente de produção.
- Devem ser definidos quais eventos são materialmente relevantes para a tarefa antes de determinar mecanismo de monitoramento.
- Monitoramento contínuo não é universal; monitoramento periódico, registros de execução ou mecanismos reativos podem ser suficientes em determinados contextos.
- Logs operacionais são uma possível fonte de evidência, não requisito em si.
- A necessidade de alerta, contenção, recuperação ou revisão depende do tipo de evento e de suas consequências.
- Riscos específicos de IA devem ser incluídos somente quando materialmente relevantes à arquitetura ou à interface da tarefa.

**Exemplos de evidências pertinentes:**

- mecanismos ou registros de monitoramento pertinentes;
- registros estruturados de incidentes;
- logs técnicos ou operacionais, quando necessários;
- mecanismos de alerta;
- procedimentos técnicos de resposta;
- documentação de contenção ou recuperação;
- ações corretivas;
- registros de revisão após incidentes;
- resultados de simulações ou testes direcionados, quando pertinentes;
- documentação equivalente de detecção e resposta;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- análise de evidências operacionais;
- verificação documental;
- revisão técnica;
- contextualização;
- rastreabilidade entre evento e resposta quando houver incidente;
- inspeção ou demonstração de mecanismos de detecção ou resposta, quando necessária e viável.

**Observações metodológicas:**

- A inexistência de incidentes registrados não demonstra que o requisito está atendido nem que está descumprido; deve-se avaliar o mecanismo aplicável.
- Não exigir sistema dedicado de SIEM, SOC, monitoramento 24/7 ou ferramenta específica salvo quando o risco concreto exigir capacidade equivalente.
- Não exigir red teaming, pentest ou teste adversarial simplesmente para satisfazer SEG-06.
- Quando um incidente existe, distinguir:
  - **Segurança:** mecanismos de detecção e resposta;
  - **Rastreabilidade:** capacidade de reconstruir evento, versão e registros;
  - **Responsabilização:** quem responde pelas ações e decisões decorrentes;
  - **Governança:** processo de tratamento, escalonamento e eventual decisão institucional;
  - **Transparência:** comunicação de informações relevantes aos públicos pertinentes, quando aplicável.
- A definição de quem deve ser comunicado ou qual instância decide sobre continuidade da tarefa não deve ser criada dentro de SEG-06.
- Se um registro menciona um incidente sem informação suficiente para caracterizá-lo, isso pode representar insuficiência de evidência ou pendência factual.
- Se duas fontes descrevem de forma incompatível o mesmo incidente, período ou resposta, pode existir inconsistência, desde que o conflito esteja efetivamente demonstrado.
- Ausência de um artefato denominado “Incident Report” não implica Não Conformidade quando os elementos necessários estiverem preservados por outras fontes adequadas.

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

- Aplicável quando a natureza dos dados, sua governança ou as condições de tratamento implicarem restrições pertinentes de acesso, uso, compartilhamento, armazenamento ou retenção. A ausência de documentação dessas restrições não constitui justificativa de não aplicabilidade.
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
- Em Privacidade, controles de acesso são analisados quanto às condições de tratamento e proteção dos dados. Em SEG-02, são analisados quanto à proteção dos ativos relevantes da Tarefa de IA contra acesso indevido.

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
- Quando a medida analisada também constituir controle de Segurança, distinguir a proteção dos dados tratada em Privacidade da proteção mais ampla dos ativos da tarefa tratada em SEG-02.

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
- Pode ser não aplicável quando, consideradas a natureza das medidas de proteção e as condições do tratamento, não houver limitação materialmente relevante no escopo. A ausência de análise ou de documentação de limitações não demonstra sua inexistência.

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

- Aplicável quando a natureza do tratamento, o contexto institucional ou as regras aplicáveis tornarem pertinentes aprovações éticas, registros institucionais ou outras condições. A inexistência ou indisponibilidade do registro correspondente não constitui justificativa de não aplicabilidade.
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
Quando a natureza do tratamento dos dados, os riscos de privacidade ou as regras institucionais aplicáveis tornarem a questão pertinente, a necessidade de RIPD ou de consulta à instância institucional responsável por proteção de dados foi considerada?

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

- Aplicável quando, consideradas a natureza dos dados, as medidas de proteção e as condições do tratamento, existirem riscos residuais ou limitações materialmente relevantes. A ausência de seu registro não demonstra que esses riscos ou limitações não existam.
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

A dimensão de Responsabilização avalia se responsabilidades por decisões, ações e consequências relevantes associadas à Tarefa de IA estão atribuídas de forma clara e verificável, permitindo identificar quem responde por elas e preservar base suficiente para prestação de contas.

Os requisitos canônicos vigentes são RES-01 a RES-06.

A aplicação desta dimensão deve distinguir a atribuição de responsabilidade da definição das estruturas e competências institucionais. A dimensão de Governança avalia, entre outros aspectos, quais estruturas, papéis, processos decisórios, mecanismos de supervisão e formas de escalonamento devem existir. A Responsabilização avalia quem responde por decisões, ações e consequências concretas produzidas nesses processos.

Também deve ser distinguida da Rastreabilidade. A existência de registros que permitam reconstruir decisões, mudanças ou relações entre evidências não demonstra, por si só, que esteja claro quem responde pelas decisões ou ações reconstruídas. Uma mesma evidência pode apoiar ambas as dimensões, mas deve responder a perguntas distintas em cada análise.

---

### RES-01

**Requisito:**
As responsabilidades por decisões, ações e resultados relevantes associados à tarefa estão atribuídas de forma clara e identificável?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-01

**O que o requisito busca verificar:**
Verificar se é possível identificar, para as decisões, ações e resultados materialmente relevantes no escopo avaliado, quem responde por eles de forma suficientemente clara.

A responsabilidade pode estar atribuída a uma pessoa, papel, função, equipe, unidade organizacional ou instância institucional, conforme a natureza da atividade. O requisito não exige atribuição nominal a uma pessoa física em todos os casos, mas exige que a atribuição seja específica o suficiente para evitar responsabilidade implícita, ambígua ou diluída.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde, inclusive na Trilha Experimental.
- As responsabilidades pertinentes dependem da Tarefa de IA, da Versão Avaliável, do Contexto de Uso, da Trilha de Execução e das atividades efetivamente realizadas.
- Nem toda participação no projeto constitui uma responsabilidade relevante para este requisito.
- Na Trilha Experimental, podem ser particularmente relevantes responsabilidades por decisões técnicas, produção ou manutenção de evidências, validações e resultados experimentais.
- Na Trilha Produção, podem existir responsabilidades adicionais associadas à operação, monitoramento, resposta a eventos e acompanhamento de ações.
- A análise deve considerar responsabilidades concretas associadas ao escopo da tarefa, e não apenas descrições genéricas de cargos ou da estrutura do projeto.

**Exemplos de evidências pertinentes:**

- documentação de papéis e responsabilidades;
- Identificação da Avaliação;
- registros institucionais ou administrativos de designação;
- termos de responsabilidade ou atribuição funcional;
- Registros de Decisão Técnica;
- registros de decisões institucionais;
- planos, registros ou documentos que atribuam ações a responsáveis;
- confirmações factuais específicas quando a responsabilidade necessária não puder ser estabelecida documentalmente;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada entre fontes;
- verificação institucional ou administrativa;
- rastreabilidade entre responsabilidade e objeto correspondente;
- confirmação factual quando a evidência documental for insuficiente;

**Observações metodológicas:**

- Não inferir responsabilidade a partir de autoria de artigo, código, Model Card, Data Card, relatório técnico ou outro artefato.
- Participação no desenvolvimento não implica automaticamente responsabilidade técnica, institucional ou decisória.
- A autoria de um documento demonstra, no máximo, participação em sua produção, salvo quando houver evidência adicional que estabeleça a responsabilidade correspondente.
- Quando a responsabilidade necessária não estiver explicitamente documentada, primeiro registrar a insuficiência da evidência. Se a informação depender de confirmação pelo projeto ou pela instituição, pode ser aberta uma pendência factual específica.
- Ausência de evidência não é inconsistência. Uma inconsistência somente existe quando duas ou mais fontes que deveriam ser compatíveis atribuem responsabilidades de maneira efetivamente divergente.
- Não duplicar GOV-01: Governança verifica estruturas, papéis e competências institucionais; RES-01 verifica atribuição de responsabilidade por decisões, ações ou resultados concretos.

---

### RES-02

**Requisito:**
Decisões relevantes podem ser associadas ao responsável que as tomou ou aprovou e à justificativa ou fundamento correspondente?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-02

**O que o requisito busca verificar:**
Verificar se decisões materialmente relevantes podem ser relacionadas a quem as tomou ou aprovou e se existe base suficiente para compreender o fundamento ou a justificativa registrada para a decisão.

O requisito operacionaliza o vínculo entre decisão, responsável e prestação de contas. Seu foco não é verificar se o processo decisório institucional foi corretamente desenhado nem decidir se o responsável possuía competência formal para tomar a decisão; esses aspectos pertencem principalmente à Governança.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando existam decisões relevantes para a Tarefa de IA ou para o ciclo avaliado.
- O grau de formalização esperado deve ser proporcional à materialidade da decisão.
- Decisões rotineiras ou de baixo impacto não precisam receber o mesmo nível de registro que decisões capazes de afetar dados, modelo, resultados, riscos, limitações, escopo ou condições de uso.
- Deve-se distinguir quem elaborou uma recomendação, quem tomou a decisão e quem a aprovou quando esses papéis forem distintos.
- Decisões técnicas e decisões institucionais podem utilizar mecanismos de registro diferentes.
- A justificativa pode estar distribuída entre diferentes fontes, desde que sua relação com a decisão seja reconstruível.

**Exemplos de evidências pertinentes:**

- Registro de Decisão Técnica;
- Registro de Decisão Institucional;
- atas;
- pareceres;
- registros de aprovação;
- documentação de escolha de modelo, dados, parâmetros ou estratégia;
- relatórios técnicos que registrem decisão e justificativa;
- histórico de mudanças associado à decisão;
- registros eletrônicos ou administrativos equivalentes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- rastreabilidade entre decisão, responsável e fundamento;
- consistência cruzada;
- verificação de autoria ou aprovação quando pertinente;
- confirmação factual específica quando a atribuição da decisão permanecer não demonstrada;

**Observações metodológicas:**

- Não confundir autoria do documento que registra uma decisão com autoria da própria decisão.
- Não exigir um artefato denominado `Registro de Decisão Técnica` quando fonte equivalente preservar decisão, responsável e fundamento.
- A qualidade substantiva ou adequação da decisão pode ser analisada em outros requisitos; RES-02 verifica principalmente sua atribuição e possibilidade de prestação de contas.
- Se diferentes fontes atribuírem a mesma decisão a responsáveis incompatíveis, deve-se verificar primeiro se realmente descrevem a mesma decisão e o mesmo estágio antes de registrar inconsistência.
- Não duplicar GOV-02: Governança verifica se existe um processo de decisão adequado; RES-02 verifica se uma decisão concreta pode ser associada ao responsável e ao seu fundamento.
- Não duplicar Rastreabilidade: a reconstrução da existência e sequência da decisão pode sustentar a análise, mas o elemento distintivo aqui é a atribuição de responsabilidade.

---

### RES-03

**Requisito:**
Quando responsabilidades são compartilhadas, delegadas ou transferidas, permanecem claros os limites de responsabilidade entre as partes envolvidas?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-03

**O que o requisito busca verificar:**
Verificar se a participação de múltiplas pessoas, equipes, unidades ou instituições não torna ambígua a atribuição de responsabilidade por decisões ou ações relevantes.

O requisito busca identificar se, mesmo quando a execução é compartilhada, delegada ou transferida, é possível compreender quais responsabilidades permanecem com cada parte e quais foram efetivamente delegadas ou assumidas por outra.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando houver responsabilidades distribuídas entre mais de uma pessoa, equipe, unidade ou instituição.
- Pode ser pouco relevante em tarefas pequenas nas quais uma única estrutura concentra de forma explícita as responsabilidades pertinentes.
- Devem ser considerados limites entre responsabilidade técnica, execução, aprovação, acompanhamento e responsabilidade institucional quando essas distinções forem materialmente relevantes.
- Delegação de uma atividade não deve ser interpretada automaticamente como transferência da responsabilidade final.
- Mudanças de equipe, responsáveis ou instituições ao longo do ciclo podem tornar este requisito especialmente relevante.
- A granularidade deve ser proporcional ao risco de ambiguidade ou diluição da responsabilidade.

**Exemplos de evidências pertinentes:**

- documentação de papéis e responsabilidades;
- registros de designação ou delegação;
- acordos entre equipes ou instituições;
- registros administrativos;
- atas ou decisões que distribuam responsabilidades;
- planos de ação com responsáveis distintos;
- histórico de alterações de responsabilidade;
- termos de colaboração ou operação, quando pertinentes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada entre atribuições;
- análise dos limites de responsabilidade;
- confirmação factual quando as fronteiras entre responsabilidades não estiverem claras;
- verificação institucional quando pertinente;

**Observações metodológicas:**

- Evitar expressões genéricas como “responsabilidade da equipe” quando a análise exigir saber qual equipe, função ou instância responde pelo elemento concreto.
- Não assumir que colaboração implica responsabilidade igual de todos os participantes.
- Não inferir transferência de responsabilidade a partir da simples execução de uma atividade por outra pessoa ou equipe.
- Se uma responsabilidade mudou ao longo do tempo, verificar qual atribuição correspondia ao período ou à Versão Avaliável relevante.
- Divergências entre fontes sobre limites de responsabilidade podem configurar inconsistência quando se referirem inequivocamente ao mesmo objeto e período.
- Não utilizar RES-03 para redesenhar a estrutura de competências da organização; essa análise pertence à Governança.

---

### RES-04

**Requisito:**
Ações ou encaminhamentos decorrentes de decisões relevantes possuem responsável identificável por sua execução ou acompanhamento?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-04

**O que o requisito busca verificar:**
Verificar se, uma vez estabelecida uma ação ou encaminhamento relevante, é possível identificar quem responde por executá-lo ou acompanhar sua realização.

O requisito busca evitar que decisões produzam ações sem responsável atribuível, especialmente quando envolvem correção, complementação, mitigação, revisão ou acompanhamento.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando decisões relevantes gerarem ações ou encaminhamentos.
- Nem toda decisão produz necessariamente uma ação posterior.
- A materialidade da ação determina o nível de formalização esperado.
- Podem ser relevantes ações técnicas, documentais, de monitoramento, mitigação, complementação de evidência ou atendimento de condicionantes.
- Deve-se distinguir, quando pertinente, quem executa a ação de quem acompanha ou responde por sua conclusão.
- Na Trilha Produção, ações decorrentes de incidentes, monitoramento ou alterações operacionais podem exigir maior clareza de acompanhamento.

**Exemplos de evidências pertinentes:**

- planos de ação;
- registros de encaminhamentos;
- Registro de Decisão Técnica;
- registro de pendências;
- condicionantes;
- registros de acompanhamento;
- tickets ou sistemas institucionais equivalentes;
- atas;
- registros de correção ou mitigação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- rastreabilidade entre decisão, ação e responsável;
- verificação documental;
- consistência cruzada;
- verificação de acompanhamento;
- confirmação factual específica quando a atribuição da ação não puder ser estabelecida;

**Observações metodológicas:**

- Não confundir a existência de uma recomendação com a atribuição de responsabilidade por executá-la.
- Não criar uma obrigação de ação onde o requisito ou a decisão correspondente não a estabeleça.
- O registro de uma ação pendente não constitui, por si só, falha de Responsabilização se o responsável estiver adequadamente identificado; o estado da execução deve ser tratado separadamente conforme o requisito pertinente.
- Pendências produzidas pelo próprio NIAR-Saúde possuem sua própria lógica operacional; não devem ser usadas automaticamente como evidência de que o projeto possui mecanismo interno de responsabilização.
- Não duplicar GOV-06 ou GOV-07: Governança verifica processo de tratamento, escalonamento e condicionantes; RES-04 verifica quem responde pela ação ou encaminhamento concreto que decorreu desse processo.
- A Rastreabilidade pode permitir reconstruir a sequência `achado → decisão → ação`; Responsabilização acrescenta a identificação de quem responde pela ação.

---

### RES-05

**Requisito:**
Existem registros suficientes para que os responsáveis possam prestar contas sobre decisões e ações relevantes sob sua responsabilidade?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-05

**O que o requisito busca verificar:**
Verificar se existem registros suficientes para que uma decisão ou ação relevante possa ser explicada e sustentada posteriormente pelo responsável correspondente.

A prestação de contas pressupõe mais do que saber o nome ou papel do responsável: deve existir base verificável suficiente para compreender o que foi decidido ou realizado, em qual contexto, com qual fundamento e, quando pertinente, quais encaminhamentos decorreram dessa atuação.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às decisões e ações materialmente relevantes para o escopo avaliado.
- O nível de documentação esperado deve ser proporcional à relevância da decisão ou ação.
- Nem toda prestação de contas exige um relatório específico ou documento único.
- Os registros podem estar distribuídos em diferentes fontes, desde que possam ser relacionados de forma suficiente.
- Decisões históricas podem exigir preservação dos registros necessários à sua interpretação.
- Na Trilha Produção, a recorrência de decisões e ações operacionais pode exigir mecanismos mais sistemáticos de preservação de registros.

**Exemplos de evidências pertinentes:**

- Registros de Decisão Técnica;
- Registros de Decisão Institucional;
- atas e pareceres;
- justificativas técnicas;
- documentação das evidências consideradas na decisão;
- registros de ações;
- histórico de mudanças;
- relatórios de acompanhamento;
- registros administrativos ou sistemas equivalentes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- análise de suficiência;
- rastreabilidade entre responsável, decisão, fundamento e ação;
- consistência cruzada;
- revisão do histórico correspondente;

**Observações metodológicas:**

- A existência de muitos documentos não demonstra automaticamente prestação de contas; os registros precisam permitir reconstruir de forma inteligível a atuação do responsável.
- Não exigir que toda decisão possua um relatório independente.
- Não confundir transparência pública com prestação de contas. A informação pode ser suficiente para accountability sem necessariamente ser destinada a divulgação externa.
- RES-05 não exige reavaliar a adequação substantiva de cada decisão; verifica se existe base suficiente para que ela possa ser explicada e examinada.
- A falta de registro necessário à prestação de contas constitui ausência ou insuficiência de evidência. Somente registrar inconsistência quando existirem registros incompatíveis.
- Rastreabilidade é condição frequentemente necessária para este requisito, mas não suficiente: localizar registros não demonstra, por si só, que estejam vinculados ao responsável adequado.

---

### RES-06

**Requisito:**
Quando decisões ou ações produzem consequências relevantes, é possível associá-las aos responsáveis e aos registros necessários para sua prestação de contas?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/responsabilizacao.md` — RES-06

**O que o requisito busca verificar:**
Verificar se consequências materialmente relevantes associadas a decisões ou ações podem, quando necessário, ser relacionadas às decisões ou ações correspondentes, aos responsáveis pertinentes e aos registros que sustentam sua prestação de contas.

O requisito completa a cadeia de responsabilização ao permitir analisar não apenas quem decidiu ou agiu, mas também se existe base para compreender a relação entre essa atuação e consequências relevantes observadas.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando existirem consequências relevantes associáveis a decisões ou ações no escopo da tarefa.
- Nem toda variação de resultado ou evento deve ser tratada como consequência relevante para este requisito.
- A materialidade depende da Tarefa de IA, do Contexto de Uso e do tipo de decisão ou ação considerada.
- Podem ser relevantes consequências sobre desempenho, riscos, limitações, grupos afetados, condições de uso ou operação.
- Na Trilha Experimental, consequências podem estar relacionadas a resultados experimentais, limitações identificadas ou alterações subsequentes.
- Na Trilha Produção, podem envolver incidentes, efeitos operacionais, ações corretivas ou mudanças nas condições de uso.
- A existência de uma consequência não demonstra automaticamente causalidade, culpa ou inadequação do responsável.

**Exemplos de evidências pertinentes:**

- registros de resultados;
- relatórios técnicos;
- registros de incidentes;
- registros de monitoramento;
- Registros de Decisão Técnica;
- decisões institucionais;
- ações corretivas;
- registros de mudanças;
- documentação de limitações ou impactos;
- relatórios de acompanhamento;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- rastreabilidade entre consequência, decisão ou ação e responsável;
- consistência cruzada entre registros;
- análise temporal;
- verificação documental;
- contextualização;
- revisão de evidências operacionais, quando aplicável;

**Observações metodológicas:**

- Não inferir causalidade apenas porque uma consequência ocorreu depois de determinada decisão.
- Não interpretar a associação entre responsável e consequência como atribuição automática de culpa, negligência ou responsabilidade jurídica.
- O FIAR-Saúde avalia mecanismos de responsabilização no escopo metodológico; não substitui processos jurídicos, regulatórios, disciplinares ou profissionais.
- A análise substantiva da consequência pode pertencer a Justiça, Segurança, Privacidade ou outra dimensão. RES-06 verifica se sua relação com decisões, ações e responsáveis pode ser estabelecida para fins de prestação de contas.
- Se a cadeia `decisão/ação → consequência` puder ser reconstruída, mas o responsável não puder ser identificado, há lacuna de Responsabilização, não necessariamente de Rastreabilidade.
- Se o responsável estiver identificado, mas não for possível reconstruir qual decisão ou ação está associada à consequência, pode haver também uma lacuna de Rastreabilidade.
- Evitar transformar correlação temporal, autoria técnica ou participação no projeto em atribuição de responsabilidade.

---

## Rastreabilidade

A dimensão de Rastreabilidade avalia se os estados relevantes da Tarefa de IA, suas evidências, mudanças e relações entre componentes podem ser reconstruídos de forma verificável ao longo do ciclo de vida.

Os requisitos canônicos vigentes são RAS-01 a RAS-07.

A aplicação desta dimensão deve distinguir a rastreabilidade das práticas, componentes e registros da própria Tarefa de IA da rastreabilidade produzida pelo NIAR-Saúde durante o processo de avaliação. Esta última constitui uma propriedade transversal do processo avaliativo e não substitui a análise dos requisitos da dimensão.

O nível de detalhamento esperado deve ser proporcional à Tarefa de IA, à Versão Avaliável, ao Contexto de Uso e à Trilha de Execução. A dimensão não pressupõe, como regra geral, rastreamento individual de cada entrada até cada saída, ferramentas específicas de linhagem, logs automatizados ou reprodução integral do ambiente computacional.

---

### RAS-01

**Requisito:**
A Tarefa de IA e os componentes ou versões relevantes ao estado avaliado podem ser identificados de forma inequívoca?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-01

**O que o requisito busca verificar:**
Verificar se o estado concreto da Tarefa de IA considerado no ciclo pode ser identificado sem ambiguidade e relacionado aos componentes cuja versão ou configuração seja relevante para interpretar corretamente as evidências utilizadas na avaliação.

O requisito busca evitar que documentos, resultados ou análises sejam atribuídos genericamente ao projeto ou ao sistema sem ser possível determinar a qual estado da tarefa eles efetivamente correspondem.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde, inclusive na Trilha Experimental.
- A Versão Avaliável deve constituir a referência principal do ciclo, mas outros identificadores podem ser necessários para distinguir dados, modelo, procedimentos ou componentes relevantes.
- Nem todo componente técnico precisa possuir versionamento próprio; devem ser considerados aqueles necessários para caracterizar de forma inequívoca o estado avaliado.
- Nem toda alteração técnica produz uma nova Versão Avaliável.
- O nível de granularidade necessário depende da possibilidade de uma alteração modificar evidências, resultados ou conclusões relevantes para o ciclo.
- Na Trilha Produção, pode também ser necessário distinguir versões implantadas ou utilizadas em períodos diferentes.

**Exemplos de evidências pertinentes:**

- Identificação da Avaliação;
- Model Card ou documentação equivalente;
- Data Card ou documentação equivalente;
- documentação técnica da tarefa;
- identificadores de versão de modelos, dados, código ou configurações relevantes;
- registros de experimentos;
- registros de implantação, quando aplicáveis;
- sistemas ou históricos de versionamento;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada entre artefatos;
- comparação de identificadores de versão;
- verificação de versionamento;
- rastreabilidade entre a Versão Avaliável e os componentes relevantes;

**Observações metodológicas:**

- Não presumir que o nome de um modelo ou arquivo identifica, por si só, uma versão de forma inequívoca.
- O requisito não exige que todos os componentes técnicos sejam versionados com o mesmo mecanismo.
- A ausência de Git, hash, identificador automatizado ou ferramenta específica de versionamento não implica automaticamente falha.
- Deve-se verificar se os registros existentes permitem distinguir o estado efetivamente avaliado de outros estados da tarefa.
- Diferenças entre identificadores em documentos distintos somente devem ser tratadas como inconsistência quando houver evidência suficiente de que deveriam se referir ao mesmo estado.

---

### RAS-02

**Requisito:**
A origem, versão, data ou período e relação das evidências com a unidade de avaliação podem ser identificadas?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-02

**O que o requisito busca verificar:**
Verificar se as evidências utilizadas para sustentar a avaliação podem ser relacionadas à combinação de Tarefa de IA, Versão Avaliável e Contexto de Uso considerada no ciclo.

O requisito busca evitar que documentos ou resultados sejam utilizados apenas porque estão disponíveis no repositório ou pertencem ao projeto, sem que seja possível estabelecer sua origem, seu período, sua versão ou sua pertinência ao objeto efetivamente avaliado.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às evidências materialmente relevantes para a avaliação.
- Nem toda fonte precisa conter todos os metadados no próprio documento, desde que sua origem e relação com a unidade de avaliação possam ser reconstruídas por registros complementares.
- O nível de identificação necessário depende da natureza da evidência.
- Evidências históricas podem ser utilizadas quando sua validade para o estado atual da tarefa estiver demonstrada.
- Evidências produzidas para outra versão, população, período ou Contexto de Uso não devem ser automaticamente transferidas para o ciclo atual.
- Na Trilha Produção, a dimensão temporal pode ser particularmente relevante para evidências de monitoramento ou operação.

**Exemplos de evidências pertinentes:**

- Controle de Artefatos;
- histórico de validação;
- Identificação da Avaliação;
- artefatos com versão ou data;
- registros de experimentos;
- relatórios técnicos identificados por período;
- histórico de alterações;
- registros de monitoramento;
- registros de implantação;
- referências documentais que permitam relacionar a evidência à unidade de avaliação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada;
- verificação de metadados e identificadores;
- rastreabilidade entre evidência e unidade de avaliação;
- comparação de datas, períodos e versões;
- verificação de pertinência ao Contexto de Uso;

**Observações metodológicas:**

- A presença de um arquivo no repositório do projeto não demonstra automaticamente sua pertinência ao ciclo.
- Data de criação ou modificação do arquivo não deve ser confundida automaticamente com o período ao qual a evidência se refere.
- Evidência sem identificação suficiente deve ser tratada como possível insuficiência de evidência, e não automaticamente como não conformidade.
- Uma mesma evidência pode sustentar diferentes requisitos ou dimensões, desde que sua relação com cada análise seja demonstrável.
- A rastreabilidade aqui avaliada pertence à evidência produzida ou mantida no contexto da tarefa; o NIAR-Saúde deve, adicionalmente, preservar a rastreabilidade de como utilizou essa evidência em sua avaliação.

---

### RAS-03

**Requisito:**
Mudanças relevantes na tarefa ou em seus componentes estão registradas de forma que sua evolução possa ser reconstruída?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-03

**O que o requisito busca verificar:**
Verificar se alterações materialmente relevantes na Tarefa de IA ou em seus componentes permanecem registradas em nível suficiente para compreender como o estado atual foi alcançado e quais elementos foram modificados ao longo do tempo.

O requisito não busca exigir registro exaustivo de cada alteração realizada durante o desenvolvimento, mas assegurar que mudanças capazes de afetar evidências, resultados, riscos ou conclusões anteriores possam ser identificadas e reconstruídas.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando a tarefa ou seus componentes tenham passado por mudanças relevantes para o escopo avaliado.
- Podem ser consideradas mudanças em dados, preparação dos dados, modelo, arquitetura, parâmetros, treinamento, validação, métricas, thresholds, software, dependências, interfaces ou Contexto de Uso.
- A relevância da mudança deve ser julgada em relação aos requisitos e evidências potencialmente afetados.
- Nem toda alteração técnica exige nova Versão Avaliável.
- Na Trilha Experimental, o histórico pode estar concentrado na evolução metodológica e experimental.
- Na Trilha Produção, mudanças implantadas e sua sequência temporal podem exigir rastreabilidade adicional.

**Exemplos de evidências pertinentes:**

- histórico de versões;
- changelog;
- registros de alterações;
- commits ou releases;
- Registros de Decisão Técnica;
- documentação técnica comparativa;
- registros de experimentos;
- atualização de Model Card ou Data Card;
- registros de mudança de configuração;
- registros de implantação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- comparação entre versões;
- análise de histórico;
- verificação documental;
- consistência cruzada;
- rastreabilidade longitudinal;
- associação entre mudança e evidências afetadas;

**Observações metodológicas:**

- Não exigir registro de alterações irrelevantes apenas porque são tecnicamente detectáveis.
- O avaliador deve considerar impacto potencial sobre o objeto avaliado, e não apenas tamanho aparente da alteração.
- A ausência de um changelog formal não implica falha quando o histórico puder ser reconstruído por fontes equivalentes.
- Registro de uma mudança não demonstra, por si só, que seus impactos foram adequadamente avaliados; essa análise pode pertencer a outros requisitos.
- Quando documentos descrevem mudanças diferentes para o mesmo período ou versão, verificar primeiro se se referem efetivamente ao mesmo objeto antes de registrar inconsistência.

---

### RAS-04

**Requisito:**
Evidências, achados, decisões e ações relacionadas podem ser vinculados quando essa relação for necessária para reconstruir o ciclo avaliado?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-04

**O que o requisito busca verificar:**
Verificar se, quando necessário para compreender determinado aspecto do ciclo, é possível reconstruir a relação entre uma evidência ou achado relevante, a decisão decorrente e eventual ação tomada.

O requisito avalia a existência dessa cadeia de associação. Ele não determina se a decisão foi adequada, quem deveria tê-la tomado ou se a ação adotada foi suficiente, aspectos que podem pertencer a Governança, Responsabilização ou outras dimensões.

**Aspectos a considerar na aplicabilidade:**

- A aplicabilidade decorre da necessidade de reconstruir relações entre evidências, achados, decisões e ações relevantes para o ciclo avaliado. A inexistência ou insuficiência dos vínculos necessários deve aparecer no resultado da avaliação e não constitui justificativa de não aplicabilidade.
- Nem toda evidência produz necessariamente uma decisão ou ação.
- Nem toda decisão exige uma cadeia formal complexa de registros.
- O grau de formalização esperado depende da relevância do achado e de suas possíveis consequências.
- Decisões técnicas, metodológicas e institucionais devem ser distinguidas quando necessário.
- Na Trilha Produção, incidentes, mudanças, restrições ou ações corretivas podem tornar essa rastreabilidade especialmente relevante.

**Exemplos de evidências pertinentes:**

- Registros de Decisão Técnica;
- relatórios técnicos contendo achados;
- Fairness Reports ou Explainability Reports;
- registros de riscos ou limitações;
- registro de pendências;
- registro de inconsistências;
- atas ou decisões institucionais;
- registros de ações corretivas;
- histórico de mudanças;
- condicionantes;
- documentação de reavaliação;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- rastreamento entre registros;
- consistência cruzada;
- verificação documental;
- associação entre achado, decisão e ação;
- verificação de referências ou identificadores comuns;
- análise temporal da sequência de registros;

**Observações metodológicas:**

- O requisito não exige que toda evidência resulte em uma decisão formal.
- Não avaliar neste requisito a correção substantiva da decisão; verificar se a relação pode ser reconstruída.
- A identificação do responsável por determinada decisão pertence principalmente à dimensão de Responsabilização ou Governança, embora o nome do responsável possa compor a evidência de rastreabilidade.
- Não criar artificialmente uma cadeia `evidência → decisão → ação` quando o contexto não a exige.
- A ausência de um Registro de Decisão Técnica específico não implica falha se a associação estiver adequadamente preservada em outra fonte.
- Registros produzidos pelo próprio NIAR-Saúde durante a avaliação não devem ser confundidos com evidências de que o projeto já mantinha essa rastreabilidade.

---

### RAS-05

**Requisito:**
Quando necessário à avaliação, é possível reconstruir a relação entre dados, modelo, procedimentos e resultados relevantes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-05

**O que o requisito busca verificar:**

Verificar se existe informação suficiente para relacionar os principais elementos técnicos que deram origem a um resultado ou evidência relevante para a avaliação.

Conforme a tarefa, isso pode incluir identificar quais dados, versão do modelo, procedimentos de preparação, configuração, parâmetros, método de avaliação e métricas estão associados ao resultado analisado.

O requisito busca garantir reconstrução suficiente para interpretação e verificação da evidência, e não impor reprodução integral do experimento ou linhagem individual de cada registro.

**Aspectos a considerar na aplicabilidade:**

- A necessidade de reconstruir a relação entre dados, modelo, procedimentos e resultados deve ser determinada a partir da Tarefa de IA, da Versão Avaliável e do objetivo da avaliação. A ausência dos registros ou vínculos necessários não torna o requisito não aplicável.
- A profundidade necessária depende do resultado que precisa ser interpretado ou verificado.
- Nem todo requisito exige reconstrução completa de toda a cadeia técnica.
- A necessidade pode ser maior quando diferentes versões de dados, modelos ou configurações produzem resultados distintos.
- Em tarefas experimentais, registros de treinamento, validação e testes podem constituir a principal fonte.
- Em produção, também podem ser relevantes configurações e versões efetivamente implantadas.
- Rastreamento individual entre cada registro de entrada e saída somente deve ser exigido quando necessário ao requisito, ao contexto técnico ou a obrigação externa aplicável.
- Reexecução integral de análises não constitui exigência automática deste requisito.

**Exemplos de evidências pertinentes:**

- Data Card ou documentação equivalente;
- Model Card ou documentação equivalente;
- documentação de pipelines;
- registros de experimentos;
- scripts ou notebooks, quando pertinentes;
- documentação de preparação dos dados;
- identificadores de datasets;
- parâmetros ou configurações relevantes;
- documentação de treinamento e validação;
- relatórios de resultados e métricas;
- registros de execução;
- documentação metodológica;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- revisão documental;
- revisão metodológica;
- consistência cruzada;
- rastreabilidade técnica;
- comparação entre registros experimentais e resultados reportados;
- verificação de identificadores, versões e configurações;
- teste técnico específico, somente quando necessário e viável;

**Observações metodológicas:**

- Não transformar reprodutibilidade ou reexecução integral em requisito universal de Rastreabilidade.
- Código-fonte, pesos do modelo ou acesso direto aos dados não são necessariamente exigidos se a relação relevante puder ser demonstrada de outra forma.
- A presença de um pipeline automatizado não demonstra, por si só, que a cadeia está suficientemente documentada.
- A análise deve se concentrar nos componentes necessários para compreender os resultados utilizados na avaliação.
- Se um resultado não puder ser associado inequivocamente aos dados, modelo ou procedimento que o produziu, deve-se registrar a limitação concreta sem presumir qual configuração foi utilizada.

---

### RAS-06

**Requisito:**
Substituições, correções ou atualizações relevantes preservam histórico suficiente para distinguir estados anteriores e atuais da tarefa e das evidências?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-06

**O que o requisito busca verificar:**
Verificar se atualizações de artefatos, dados, modelos ou registros não eliminam informações necessárias para compreender qual era o estado anterior, qual passou a ser o estado vigente e quais elementos materialmente relevantes foram alterados.

O requisito busca impedir que a simples substituição de documentos ou componentes apague o histórico necessário para interpretar avaliações, evidências ou decisões anteriores.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando tenham ocorrido substituições, correções ou atualizações materialmente relevantes.
- Correções puramente editoriais podem não exigir preservação detalhada quando não alterarem informação utilizada na avaliação.
- Correções que modifiquem métricas, limitações, dados, versões, responsabilidades ou outras informações utilizadas no ciclo podem exigir preservação de histórico.
- O grau de retenção deve ser proporcional à necessidade de reconstruir estados relevantes.
- Não se exige manutenção indefinida de toda versão intermediária produzida durante o desenvolvimento.
- Em ciclos sucessivos, deve ser possível distinguir evidência válida para cada estado ou Versão Avaliável.

**Exemplos de evidências pertinentes:**

- histórico de versões;
- Controle de Artefatos;
- histórico de validação;
- changelog;
- registros de substituição;
- commits ou releases;
- versões anteriores de documentos relevantes;
- registros de correção;
- documentação de mudanças;
- registros de aprovação ou validação de atualização;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- comparação entre versões;
- verificação de histórico;
- análise de registros de substituição;
- consistência cruzada;
- rastreabilidade temporal;
- análise da relação entre versão anterior e versão atual;

**Observações metodológicas:**

- Não exigir retenção indiscriminada de arquivos intermediários sem relevância para a avaliação.
- O importante é preservar informação suficiente para distinguir estados materialmente diferentes.
- A versão mais recente de um artefato não deve apagar silenciosamente uma informação relevante utilizada em avaliação anterior.
- Quando uma correção resolver uma inconsistência, o histórico da correção pode ser necessário para preservar a rastreabilidade do ciclo.
- O Controle de Artefatos possui função administrativa; sua existência ajuda na reconstrução do histórico, mas não substitui evidência técnica sobre o conteúdo da mudança.

---

### RAS-07

**Requisito:**
Para tarefas em produção, eventos operacionais relevantes podem ser associados à versão da tarefa e ao período correspondentes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/rastreabilidade.md` — RAS-07

**O que o requisito busca verificar:**
Verificar se, durante a operação, eventos materialmente relevantes podem ser relacionados ao estado da tarefa que estava efetivamente em uso e ao período em que ocorreram.

Isso permite reconstruir, quando necessário, qual versão estava implantada diante de um incidente, alteração, monitoramento, ação corretiva, rollback ou outro evento operacional relevante.

**Aspectos a considerar na aplicabilidade:**

- O requisito é direcionado à Trilha Produção.
- Para tarefas exclusivamente na Trilha Experimental, sua não aplicabilidade pode decorrer diretamente da ausência de operação ativa, desde que devidamente justificada.
- Nem todo evento operacional precisa ser registrado com o mesmo nível de detalhamento.
- Devem ser considerados eventos capazes de afetar interpretação de resultados, riscos, operação, disponibilidade, segurança, desempenho ou decisões de acompanhamento.
- A frequência e granularidade dos registros dependem da Tarefa de IA e do Contexto de Uso.
- A mudança para Trilha Produção pode tornar este requisito aplicável mesmo que não tenha sido aplicável em ciclos anteriores.

**Exemplos de evidências pertinentes:**

- registros de implantação;
- histórico de versões em produção;
- registros de monitoramento;
- registros de incidentes;
- logs operacionais pertinentes;
- registros de rollback;
- registros de suspensão ou reativação;
- histórico de configuração;
- registros de atualização;
- relatórios de operação ou manutenção;
- documentação de reavaliações;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- análise de evidências operacionais;
- rastreabilidade longitudinal;
- verificação de versão implantada;
- correlação temporal entre eventos e versões;
- consistência cruzada entre monitoramento, incidentes e registros de implantação;
- revisão documental ou técnica de logs pertinentes;

**Observações metodológicas:**

- Não aplicar automaticamente este requisito a tarefas sem operação ativa.
- A existência de logs não demonstra, por si só, que eventos podem ser associados à versão correta da tarefa.
- O requisito não exige registro de todo evento técnico de baixa relevância.
- Registros operacionais podem também sustentar requisitos de Segurança ou Governança; seu uso transversal não torna os requisitos equivalentes.
- A análise deve verificar associação entre evento, período e versão, e não julgar neste requisito se o incidente foi adequadamente tratado.
- A inexistência de determinado tipo de log não implica automaticamente Não Conformidade quando a rastreabilidade necessária for demonstrada por mecanismo equivalente.

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

- Aplicável quando cobertura, representação ou qualidade dos dados em relação aos grupos relevantes puderem afetar materialmente a tarefa ou seu Contexto de Uso. A indisponibilidade de informações necessárias para realizar essa análise constitui uma limitação da avaliação, e não justificativa de não aplicabilidade.
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
- A aplicabilidade depende da função da tarefa, dos grupos relevantes, das consequências dos resultados e da pertinência de comparar desempenho ou impacto entre esses grupos. A indisponibilidade de dados necessários pode limitar ou impedir a análise, mas não determina, por si só, a não aplicabilidade.
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

- Aplicável quando uma análise quantitativa ou metodológica de Justiça for pertinente à tarefa e aos grupos avaliados, independentemente de essa análise já ter sido realizada. A ausência da análise não constitui justificativa de não aplicabilidade.
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

- Aplicável quando a análise de Justiça estabelecer disparidades cuja interpretação contextual seja pertinente. A ausência de disparidade identificada somente sustenta a não aplicabilidade quando houver base suficiente para concluir que a condição não está presente; ausência ou insuficiência da análise anterior não deve ser tratada como ausência de disparidade.
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

- Aplicável quando uma disparidade ou achado estabelecido na análise anterior possuir magnitude ou relevância que justifique investigação adicional. A ausência de investigação não constitui justificativa de não aplicabilidade; quando a materialidade do achado ainda não puder ser determinada, a não aplicabilidade não deve ser presumida.
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

- Aplicável quando a natureza, magnitude ou consequências dos achados de Justiça justificarem considerar alguma resposta. A ausência de mitigação, monitoramento, restrição ou outra resposta não constitui justificativa de não aplicabilidade.
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

- Aplicável quando a análise de Justiça indicar riscos residuais, limitações ou trade-offs materialmente relevantes. A ausência de documentação desses elementos não demonstra sua inexistência e deve ser tratada no resultado da avaliação.
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

A dimensão de Transparência avalia se informações relevantes sobre a Tarefa de IA estão documentadas, disponíveis ou comunicadas em nível e forma adequados aos públicos pertinentes, permitindo compreender sua finalidade, características, capacidades, limitações, condições de uso, resultados e incertezas.

Os requisitos canônicos vigentes são TRA-01 a TRA-06.

A aplicação desta dimensão deve distinguir Transparência de outras dimensões relacionadas:

- **Rastreabilidade** verifica se versões, evidências, mudanças e relações relevantes podem ser reconstruídas ao longo do ciclo de vida;
- **Responsabilização** verifica quem responde por decisões, ações e consequências e se existem elementos suficientes para prestação de contas;
- **Governança** verifica estruturas, competências, processos de decisão, supervisão, condições de uso e mecanismos de escalonamento;
- **Justiça** verifica diferenças relevantes de desempenho, impacto ou tratamento entre grupos ou contextos pertinentes.

Uma mesma evidência pode contribuir para diferentes dimensões, mas deve ser analisada de acordo com a pergunta específica do requisito.

Explicabilidade constitui um possível componente da Transparência quando necessária à compreensão da tarefa ou de determinado aspecto de seu comportamento. Ela não deve ser presumida como requisito uniforme para todas as tarefas, modelos ou públicos.

A avaliação também não deve presumir que toda informação deva ser pública. O público pertinente, o nível de detalhamento, a linguagem, o canal e eventuais restrições de acesso ou divulgação dependem da Tarefa de IA, da Versão Avaliável, do Contexto de Uso, da Trilha de Execução e da finalidade da informação.

---

### TRA-01

**Requisito:**
As informações necessárias para compreender a finalidade, o escopo, o Contexto de Uso e as condições relevantes de uso da tarefa estão documentadas e disponíveis aos públicos pertinentes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-01

**O que o requisito busca verificar:**
Verificar se existe informação suficiente para que os públicos pertinentes compreendam o que a Tarefa de IA pretende realizar, em qual escopo ela foi desenvolvida ou avaliada, em quais condições seus resultados devem ser interpretados e quais usos ou situações estão dentro ou fora do contexto considerado.

O requisito não busca redefinir a finalidade, o Contexto de Uso ou os limites da tarefa. Esses elementos são delimitados ou definidos em outras etapas e dimensões. Em Transparência, a questão é se as informações necessárias para compreendê-los estão adequadamente documentadas e disponíveis para quem delas necessita.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde.
- O conteúdo necessário depende da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da Trilha de Execução.
- Uso atual e uso apenas pretendido devem ser distinguidos quando não forem equivalentes.
- Na Trilha Experimental, pode ser necessário deixar explícito que a tarefa se encontra em pesquisa, desenvolvimento, experimentação ou validação e que não existe integração ativa a um fluxo operacional.
- Na Trilha Produção, podem ser relevantes informações adicionais sobre usuários, ambiente, condições operacionais e restrições concretas de uso.
- Públicos técnicos, institucionais, profissionais ou externos podem necessitar de níveis distintos de informação.
- Nem toda informação pertinente precisa estar concentrada em um único documento.

**Exemplos de evidências pertinentes:**

- Formulário de Entrada;
- Identificação da Avaliação;
- Model Card ou documentação equivalente;
- documentação técnica;
- protocolos ou instruções de uso;
- documentação institucional;
- materiais destinados a usuários ou profissionais;
- descrição de usos previstos, usos não avaliados ou restrições de uso;
- materiais externos ou públicos, quando aplicáveis;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao público e ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada entre fontes;
- contextualização;
- análise de suficiência da informação;
- comparação entre uso declarado, Contexto de Uso e materiais disponibilizados aos públicos pertinentes;

**Observações metodológicas:**

- Não confundir definição do Contexto de Uso com comunicação do Contexto de Uso. A primeira pertence à delimitação da avaliação e pode envolver Governança; TRA-01 verifica se essa informação está adequadamente disponível.
- Uma descrição geral do projeto não é necessariamente suficiente para compreender a Tarefa de IA específica avaliada.
- Não presumir que informação disponível para a equipe de desenvolvimento esteja automaticamente disponível para todos os demais públicos pertinentes.
- Não exigir divulgação pública quando o Contexto de Uso não a tornar pertinente.
- Ausência de um Model Card não implica descumprimento se as informações necessárias estiverem adequadamente registradas em outras fontes.
- Se diferentes materiais apresentam finalidades ou condições de uso incompatíveis para a mesma tarefa e versão, a divergência pode exigir registro de inconsistência; simples ausência de detalhe constitui inicialmente insuficiência de evidência.

---

### TRA-02

**Requisito:**
Os dados, o modelo, os procedimentos e as características técnicas relevantes estão documentados em nível suficiente para compreensão e revisão pelos públicos técnicos ou institucionais pertinentes?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-02

**O que o requisito busca verificar:**
Verificar se os públicos que necessitam compreender ou revisar tecnicamente a tarefa dispõem de informação suficiente sobre seus principais elementos técnicos.

O requisito não exige exposição irrestrita de todos os detalhes internos do sistema. Busca verificar se aquilo que é materialmente necessário para compreender as evidências, métodos, resultados e limitações da tarefa está documentado em nível adequado à finalidade da revisão.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas que necessitam de compreensão ou revisão técnica no ciclo.
- A profundidade esperada varia conforme a complexidade da tarefa e o tipo de avaliação.
- Podem ser relevantes informações sobre dados, preparação, arquitetura ou classe do modelo, procedimentos de treinamento, validação e teste, métricas e configurações materialmente relevantes.
- Modelos simples e tarefas complexas podem exigir níveis diferentes de documentação.
- Informação necessária para avaliadores pode ser mais detalhada do que aquela necessária para usuários finais.
- Restrições relacionadas a privacidade, segurança, confidencialidade, propriedade intelectual ou acesso institucional devem ser consideradas.
- A necessidade de informação técnica não implica automaticamente acesso a dados brutos, código-fonte, pesos do modelo ou ambientes protegidos.

**Exemplos de evidências pertinentes:**

- Data Card ou documentação equivalente;
- Model Card ou documentação equivalente;
- artigos ou relatórios técnicos;
- documentação de pipelines;
- documentação metodológica;
- registros de treinamento, validação ou teste;
- esquemas de dados;
- documentação de métricas e procedimentos experimentais;
- registros técnicos equivalentes;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- revisão técnica;
- análise de suficiência;
- consistência cruzada entre documentação dos dados, modelo e resultados;
- contextualização da informação ao público técnico ou institucional;

**Observações metodológicas:**

- Não transformar acesso ao código-fonte, aos dados ou aos pesos do modelo em exigência universal.
- A existência de Data Card e Model Card não demonstra, por si só, que a documentação técnica seja suficiente.
- Deve-se avaliar o conteúdo efetivamente necessário para compreender as evidências relevantes ao ciclo.
- Não utilizar TRA-02 para avaliar se versões e mudanças podem ser reconstruídas; essa é uma questão de Rastreabilidade.
- Não utilizar TRA-02 para avaliar se a escolha técnica foi adequada; a análise substantiva pode pertencer a outros requisitos.
- Informação tecnicamente detalhada, mas desconectada da Tarefa de IA e da Versão Avaliável, pode não ser pertinente à avaliação.

---

### TRA-03

**Requisito:**
As capacidades, limitações, pressupostos, condições de uso e incertezas relevantes da tarefa estão documentados de forma clara?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-03

**O que o requisito busca verificar:**
Verificar se a documentação permite distinguir aquilo que a tarefa demonstrou ser capaz de realizar daquilo que permanece limitado, incerto, não avaliado ou fora de seu escopo.

O requisito busca reduzir interpretações excessivas ou inadequadas dos resultados, especialmente quando limitações, pressupostos ou incertezas são relevantes para compreender o comportamento da tarefa.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável às tarefas avaliadas pelo FIAR-Saúde.
- O conteúdo relevante depende do tipo de tarefa, dos dados, do modelo, da população e do Contexto de Uso.
- Devem ser consideradas limitações já identificadas nas fontes disponíveis, sem criar limitações hipotéticas não demonstradas.
- Podem ser pertinentes limitações relacionadas a dados, generalização, desempenho, população, ambiente, procedimento experimental ou condições operacionais.
- Incerteza deve ser considerada quando materialmente relevante para interpretação dos resultados.
- Na Trilha Experimental, pode ser especialmente importante distinguir capacidade demonstrada experimentalmente de capacidade ainda não validada em uso real.
- Na Trilha Produção, limitações conhecidas do uso real ou de monitoramento podem também ser relevantes.

**Exemplos de evidências pertinentes:**

- Model Card ou documentação equivalente;
- Data Card ou documentação equivalente;
- artigos e relatórios técnicos;
- documentação de limitações;
- resultados de validação;
- análise de erros;
- Fairness Report, quando fornecer limitações pertinentes;
- documentação de incerteza;
- registros de riscos ou restrições de uso;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- verificação documental;
- consistência cruzada entre capacidades declaradas e resultados disponíveis;
- análise de suficiência;
- contextualização;
- revisão metodológica quando necessária;

**Observações metodológicas:**

- Não inferir ausência de limitações porque nenhum documento possui seção intitulada “Limitações”.
- Não exigir que toda incerteza possível seja quantificada; determinar primeiro quais formas de incerteza são materialmente relevantes para a tarefa e seus resultados.
- Alegações sobre capacidade devem permanecer proporcionais às evidências disponíveis.
- Limitações identificadas em Justiça, Privacidade, Segurança ou outras dimensões podem exigir comunicação em Transparência quando forem relevantes para a compreensão da tarefa, mas TRA-03 não reavalia substantivamente esses achados.
- Não confundir limitação técnica com restrição institucional de uso; ambas podem precisar ser comunicadas, mas possuem naturezas diferentes.
- A omissão de uma limitação conhecida e materialmente relevante pode ser mais importante que a ausência de detalhes secundários.

---

### TRA-04

**Requisito:**
Os resultados relevantes da tarefa estão apresentados com informação suficiente sobre as condições em que foram obtidos, seu significado e seus limites de interpretação?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-04

**O que o requisito busca verificar:**
Verificar se resultados e métricas relevantes não são apresentados de forma isolada ou descontextualizada, mas acompanhados das informações necessárias para compreender o que representam, em quais condições foram produzidos e até onde podem ser interpretados.

O requisito não determina quais métricas devem ser utilizadas nem se o desempenho é adequado. Ele verifica a transparência da apresentação e interpretação dos resultados.

**Aspectos a considerar na aplicabilidade:**

- Aplicável quando resultados técnicos, experimentais ou operacionais forem utilizados para caracterizar a tarefa.
- A informação necessária depende do tipo de resultado e da finalidade de sua comunicação.
- Podem ser relevantes população ou conjunto de avaliação, período, procedimento experimental, métricas, baseline, variabilidade, intervalos ou outras informações de incerteza.
- Resultados globais podem exigir contextualização quando existirem resultados desagregados ou análises específicas relevantes para sua interpretação.
- A exigência de produzir determinada estratificação não decorre de TRA-04; quando pertinente, essa obrigação pertence principalmente à dimensão de Justiça.
- Na Trilha Experimental, deve-se evitar apresentar resultados experimentais como evidência de desempenho operacional não avaliado.
- Na Trilha Produção, evidências de desempenho real podem precisar ser distinguidas de resultados de validação prévia.

**Exemplos de evidências pertinentes:**

- relatórios de avaliação;
- resultados experimentais;
- Model Card;
- artigos técnicos;
- documentação de métricas;
- tabelas e figuras de resultados;
- resultados estratificados disponíveis;
- análises de erro;
- relatórios de monitoramento, quando aplicáveis;

Esses exemplos não constituem uma lista obrigatória de artefatos. Evidências equivalentes podem ser utilizadas quando forem suficientes, consistentes, rastreáveis e adequadas ao contexto.

**Mecanismos de verificação possíveis:**

- revisão documental;
- revisão metodológica;
- análise de suficiência;
- consistência cruzada entre métricas e descrições;
- contextualização dos resultados;
- comparação entre resultados globais e análises específicas disponíveis quando pertinente;

**Observações metodológicas:**

- A presença de uma métrica não demonstra transparência suficiente sobre o comportamento da tarefa.
- Não avaliar neste requisito se o valor da métrica é aceitável para o uso; isso pode depender de Governança, Segurança, Justiça ou análise técnica específica.
- Não exigir análises de grupos apenas para satisfazer Transparência. Justiça determina quando análises de grupos são necessárias; Transparência verifica se resultados relevantes disponíveis são apresentados adequadamente.
- Não extrapolar resultados de uma população, período ou ambiente para outro sem evidência.
- Quando diferentes fontes apresentam valores incompatíveis da mesma métrica para a mesma configuração, verificar versão, dataset e procedimento antes de classificar a situação como inconsistência.
- Resultados publicados em artigo não devem ser automaticamente atribuídos à Versão Avaliável sem verificar sua correspondência.

---

### TRA-05

**Requisito:**
Quando mecanismos de explicabilidade forem necessários, sua finalidade, método, resultados e limitações estão documentados e apresentados de forma adequada à tarefa e ao público pertinente?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-05

**O que o requisito busca verificar:**
Verificar, primeiro, se mecanismos específicos de explicabilidade são necessários para a tarefa, o Contexto de Uso e o público considerado e, quando forem necessários, se seu uso está adequadamente documentado e contextualizado.

Quando aplicável, a análise deve permitir compreender por que determinado mecanismo foi utilizado, que questão pretende responder, como foi aplicado, quais resultados produziu e quais limitações possui.

**Aspectos a considerar na aplicabilidade:**

- A necessidade de mecanismos de explicabilidade deve ser determinada em razão da natureza da tarefa, da função de suas saídas, dos públicos pertinentes e do Contexto de Uso, independentemente da existência de método, relatório ou prática de explicabilidade já implementados.
- A aplicabilidade não deve ser presumida apenas porque a tarefa utiliza um modelo de IA.
- A necessidade depende do tipo de modelo, da tarefa, do Contexto de Uso, do papel da saída, das decisões que ela pode apoiar e do público que necessita da explicação.
- Modelos intrinsecamente interpretáveis podem exigir tratamento diferente de modelos para os quais métodos adicionais são necessários.
- Explicações globais e locais respondem a perguntas diferentes e não são intercambiáveis.
- Nem todo público necessita do mesmo tipo de explicação.
- Na Trilha Experimental, explicabilidade pode ser necessária para análise técnica ou compreensão de comportamento mesmo sem uso operacional.
- Em produção, explicações podem também ser relevantes para usuários, supervisores ou processos específicos, conforme o Contexto de Uso.

**Exemplos de evidências pertinentes:**

- Explainability Report ou documentação equivalente;
- Model Card;
- análise de importância de variáveis;
- análise de sensibilidade;
- métodos de atribuição;
- explicações globais;
- explicações locais;
- visualizações;
- documentação metodológica;
- registros das limitações dos métodos utilizados;
- estudos ou testes internos de explicabilidade;

Esses exemplos não constituem uma lista obrigatória de artefatos. A existência de um `Explainability Report` não é exigência universal e evidências equivalentes podem ser utilizadas quando adequadas.

**Mecanismos de verificação possíveis:**

- revisão metodológica;
- contextualização;
- análise de suficiência;
- verificação documental;
- consistência entre finalidade declarada e método escolhido;
- análise das limitações do mecanismo de explicabilidade;
- revisão técnica específica quando necessária;

**Observações metodológicas:**

- Não confundir Transparência com Explicabilidade.
- Não presumir que métodos como SHAP, LIME, feature importance ou saliency são obrigatórios ou adequados para toda tarefa.
- A presença de um gráfico ou método pós-hoc não demonstra, por si só, explicabilidade adequada.
- Uma explicação deve ser avaliada em relação à pergunta que pretende responder e ao público para o qual é relevante.
- Não interpretar a saída de um método de explicabilidade como explicação causal sem base metodológica para isso.
- As limitações conhecidas do método utilizado fazem parte da informação necessária para interpretar a explicação.
- A não aplicação de mecanismo específico de explicabilidade não constitui automaticamente uma lacuna; primeiro deve ser estabelecida sua necessidade.
- Quando a necessidade de explicabilidade depender de uma decisão metodológica do NIAR-Saúde, essa decisão deve ser registrada como tal e não transferida automaticamente ao projeto como ausência de evidência.
- O requisito não exige que o avaliador reproduza tecnicamente toda análise de explicabilidade; o mecanismo de verificação utilizado deve ser proporcional ao que precisa ser demonstrado.

---

### TRA-06

**Requisito:**
As informações relevantes são disponibilizadas ou comunicadas em nível, forma e canal adequados aos diferentes públicos pertinentes, considerando eventuais restrições aplicáveis de acesso ou divulgação?

**Fonte normativa:**
`FIAR-Saude/docs/avaliacao/transparencia.md` — TRA-06

**O que o requisito busca verificar:**
Verificar se a transparência é adaptada aos públicos que efetivamente necessitam da informação.

O requisito considera que transparência técnica, transparência institucional, informação para profissionais ou usuários e eventual comunicação externa possuem finalidades diferentes. Portanto, não basta que a informação exista: quando sua comunicação for necessária, ela deve ser disponibilizada em nível, linguagem, forma e canal compatíveis com o público pertinente e com as condições aplicáveis de acesso.

**Aspectos a considerar na aplicabilidade:**

- O requisito é aplicável considerando os públicos efetivamente pertinentes à Tarefa de IA e ao Contexto de Uso.
- Nem toda tarefa possui os mesmos públicos.
- Na Trilha Experimental sem operação ativa, podem não existir ainda usuários finais ou profissionais utilizando resultados da tarefa.
- Avaliadores e equipes técnicas podem necessitar de documentação detalhada.
- Instâncias institucionais podem necessitar de síntese adequada para decisão e supervisão.
- Profissionais ou usuários podem necessitar principalmente de informação sobre finalidade, capacidades, limitações, condições de uso, incertezas e interpretação das saídas.
- Comunicação externa ou pública somente deve ser considerada quando pertinente ao contexto.
- Restrições aplicáveis de privacidade, segurança, confidencialidade, propriedade intelectual, contratos ou proteção de informações institucionais podem limitar acesso ou divulgação.
- Uma restrição a determinado público não elimina necessariamente a necessidade de disponibilizar informação suficiente a outro público autorizado.

**Exemplos de evidências pertinentes:**

- documentação técnica para desenvolvedores ou avaliadores;
- documentação institucional;
- materiais de uso;
- manuais;
- interfaces;
- alertas, mensagens ou informações exibidas aos usuários;
- materiais destinados a profissionais de saúde;
- protocolos ou instruções operacionais;
- relatórios ou sínteses destinados a instâncias de governança;
- materiais externos ou públicos, quando aplicáveis;
- registros das condições de acesso a documentação restrita;

Esses exemplos não constituem uma lista obrigatória de artefatos. A evidência adequada depende do público e da informação cuja comunicação precisa ser demonstrada.

**Mecanismos de verificação possíveis:**

- verificação documental;
- contextualização por público;
- análise da adequação da linguagem e do nível de detalhe;
- análise do canal de comunicação;
- consistência entre materiais destinados a públicos diferentes;
- inspeção de interfaces ou materiais de uso quando pertinente;
- confirmação factual sobre disponibilização da informação quando não puder ser estabelecida documentalmente;

**Observações metodológicas:**

- Não presumir que toda informação deve ser pública.
- Não avaliar todos os públicos possíveis; identificar aqueles efetivamente pertinentes à tarefa e ao Contexto de Uso.
- Informação tecnicamente correta pode ser insuficiente se apresentada em nível inadequado ao público que precisa utilizá-la.
- Da mesma forma, simplificação para determinado público não deve eliminar informações materialmente necessárias à interpretação adequada.
- Não exigir materiais destinados a usuários finais para uma tarefa exclusivamente experimental que ainda não possua esse tipo de usuário.
- Não transformar restrições de acesso em falha automática de Transparência; verificar se o público que necessita da informação consegue obtê-la de forma adequada.
- O NIAR-Saúde não deve determinar neste requisito a validade jurídica de restrições contratuais, de propriedade intelectual ou de confidencialidade. Quando necessário, a questão deve ser encaminhada à instância competente.
- Não duplicar Governança: TRA-06 verifica comunicação da informação, não o desenho dos processos institucionais de decisão ou supervisão.
- Não duplicar Responsabilização: identificar quem deve responder por uma decisão é questão de RES; comunicar ao público pertinente informações sobre a tarefa é questão de TRA.
- Não duplicar Rastreabilidade: o fato de um material estar associado à versão correta é relevante à análise da evidência, mas TRA-06 pergunta se a informação adequada chegou ou está disponível ao público pertinente.
- Não duplicar Justiça: quando uma análise de justiça identifica disparidade ou limitação relevante, TRA-06 pode avaliar sua comunicação aos públicos pertinentes, mas não decide quais grupos devem ser analisados nem se a disparidade exige mitigação.

---

## Uso do guia durante a avaliação

Para cada requisito canônico aplicável:

1. utilizar este guia para compreender o objetivo, os aspectos de aplicabilidade, as evidências pertinentes e os mecanismos de verificação possíveis;
2. registrar a aplicação concreta no `template_avaliacao_requisito.md`;
3. determinar `Aplicável` ou `Não aplicável` antes da análise das evidências;
4. registrar somente evidências efetivamente verificadas no ciclo;
5. registrar somente mecanismos de verificação efetivamente utilizados;
6. analisar suficiência, consistência, rastreabilidade, pertinência, atualidade e contextualização;
7. registrar achados, limitações, pendências, inconsistências e eventual sinal de governança conforme sustentado pelas evidências;
8. não transformar ausência de artefato, evidência ainda não recebida ou estado administrativo em resultado automático de conformidade.

A conformidade é consolidada para a combinação **Tarefa de IA + Versão Avaliável + Contexto de Uso**. A maturidade é inferida separadamente, de forma longitudinal, no nível do projeto.

---

## Referências

### Documentação normativa do FIAR-Saúde

- FIAR-Saúde. `docs/dimensoes_avaliacao.md`.
- FIAR-Saúde. `docs/avaliacao/governanca.md`.
- FIAR-Saúde. `docs/avaliacao/seguranca.md.`
- FIAR-Saúde. `docs/avaliacao/privacidade.md`.
- FIAR-Saúde. `docs/avaliacao/responsabilizacao.md`.
- FIAR-Saúde. `docs/avaliacao/rastreabilidade.md`.
- FIAR-Saúde. `docs/avaliacao/justica.md`.
- FIAR-Saúde. `docs/avaliacao/transparencia.md`.

### Documentação operacional relacionada do FIAR-Audit-Template

- `documentacao_metodologica/guia_operacional_pre_avaliacao_pilotos.md`
- `avaliacao_niar/avaliacao_por_requisito/template_avaliacao_requisito.md`

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

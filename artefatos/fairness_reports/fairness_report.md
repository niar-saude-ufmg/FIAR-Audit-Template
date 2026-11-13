# Fairness Report

Fairness Report · Posição da equipe sobre a Justiça da Tarefa de IA · FIAR / CIIA UFMG

**Tarefa de IA:**

## Como preencher

> O Fairness Report é o relatório de dimensão de Justiça do FIAR-Saúde. É obrigatório nas Trilhas Experimental e Produção. É a posição formal da equipe. O NIAR-Saúde o verifica com as demais evidências. O Comitê Gestor lê a Seção 5 no relatório do NIAR-Saúde. Os fatos são resumidos aqui, com fonte e versão.
>
> O relatório responde aos quatro requisitos de Justiça do FIAR-Saúde:
>
> 1. RC01 Grupos e populações: identificar, de forma fundamentada, os grupos e populações que podem ser afetados de forma desigual pela Tarefa de IA ou excluídos de seus benefícios.
> 2. RC02 Diferenças nos efeitos: avaliar se a Tarefa de IA produz, reproduz ou agrava diferenças injustificadas nos efeitos sobre esses grupos.
> 3. RC03 Dados, variáveis-alvo e padrões de referência: avaliar se são adequados para esses grupos.
> 4. RC04 Acesso e possibilidade de benefício: avaliar se a forma de disponibilização produz, reproduz ou agrava desigualdades injustificadas na possibilidade de se beneficiar do uso.
>
> **Pré-preenchimento.** O agente da sala segura pré-preenche o relatório a partir da execução, do Model Card e do Data Card. Sem agente da sala segura, o NIAR-Saúde, ou um agente a seu serviço, pré-preenche um rascunho a partir do Model Card, do Data Card, de publicações e das comunicações com a equipe. Quem pré-preenche não é quem verifica o relatório.
>
> **[A]** = fato. Campo pré-preenchido. Em cada campo, quem pré-preenche registra a origem e a versão em "Fonte e versão"; para comunicações, o arquivo e a data. As divergências entre fontes vão para a tabela "Divergências entre fontes" (Seção 0). A equipe confere.
>
> **[J]** = julgamento da equipe: por que um grupo importa, se uma diferença é justificada, se a variável-alvo é válida. Os campos [J] são assinados na Seção 5. Se quem pré-preenche tirar uma posição da equipe do Model Card ou de uma comunicação, o campo começa com **[a confirmar]**. A equipe confirma ou corrige e retira a marca. Uma posição dita por e-mail só vale como posição formal depois de confirmada aqui e assinada.
>
> **Versões.** O rascunho pré-preenchido tem versão 0.1.0 e vai anexado ao pedido à equipe. Depois de assinado, o relatório entra em artefatos/fairness_reports/ do repositório do projeto como 1.0.0. Respostas a lacunas apontadas pelo NIAR-Saúde geram novas versões, que listam na Seção 0 as lacunas a que respondem.
>
> Os códigos RCxx.y indicam o item do checklist de Justiça do FIAR-Saúde a que o campo responde. O resultado de cada requisito é do NIAR-Saúde e não consta deste relatório.
>
> Use os mesmos nomes de grupos do Data Card e do Model Card (ex.: categorias de raça/cor do IBGE, faixas etárias fixas). Sem isso, quem pré-preenche e quem verifica não conseguem cruzar os documentos.
>
> Na versão assinada, remova os blocos de instrução (as linhas que começam com ">"). Mantenha [A], [J], "Fonte e versão" e os códigos RCxx.y: eles orientam a verificação pelo NIAR-Saúde. Nenhum campo pode seguir marcado [a confirmar] na versão assinada. O Anexo A e o Checklist de entrega são material de apoio e podem ser removidos.
>
> Os exemplos usam o caso do Preditor de Risco de Reinternação Hospitalar (PRRH-v1), treinado com AIHs do SUS-MG de 2018 a 2023. Os números são ilustrativos. Exemplos marcados "(proposta)" aguardam revisão.

---

## Seção 0. Identificação da tarefa e do relatório

> Identifica a tarefa avaliada, as versões de modelo e dados a que os resultados se referem e a origem dos resultados. Sem isso, o relatório não pode ser verificado nem comparado entre versões.

**Tarefa de IA**

> Copie de ciclos/Cxx/identificacao.md. No FIAR, Tarefa de IA é modelo, dados e procedimentos orientados a um objetivo.
> Ex.: Predição do risco de reinternação em 30 dias após a alta, em adultos.

Preenchimento:

**Versão Avaliável**

> Copie de ciclos/Cxx/identificacao.md.
> Ex.: PRRH-v1 (modelo 1.0.0, base SIH-MG v2.1).

Preenchimento:

**Contexto de Uso**

> Copie de ciclos/Cxx/identificacao.md. A unidade avaliada é Tarefa + Versão Avaliável + Contexto de Uso. Usos pretendidos fora do ciclo não entram nesta avaliação.
> Ex.: apoio à alta por enfermeiros em 5 hospitais da rede.

Preenchimento:

**Trilha**

> Experimental ou Produção, como em ciclos/Cxx/identificacao.md.

Preenchimento:

**Versão do relatório**

> Siga versionamento semântico (MAJOR.MINOR.PATCH). Rascunho pré-preenchido: 0.1.0. Primeira versão assinada: 1.0.0. Depois: MAJOR para nova versão do modelo ou dos dados; MINOR para novas análises, novos grupos ou respostas a lacunas; PATCH para correções de texto.
> Ex.: 1.0.0

Preenchimento:

**Model Card e Data Card**

> Nome, versão e link dos cards a que este relatório se refere. O relatório vale para essas versões: se o modelo for retreinado, o relatório precisa de nova versão.
> Ex.: Model Card PRRH-v1 1.0.0 · Data Card Internações SUS-MG 2018 a 2023 v2.1

Preenchimento:

**Projeto**

> Projeto ao qual a Tarefa de IA está vinculada.

Preenchimento:

**Responsáveis pelo relatório**

> Nome, papel, afiliação e contato.

Preenchimento:

**Execução na sala segura** · [A]

> Data, versão do código (commit ou tag) e versão dos dados da execução que gerou os resultados. Se não houve execução na sala segura, escreva isso e indique a fonte dos resultados (artigo, relatório técnico, tabela).
> Ex.: Execução de 14/10/2026 · commit a3f9c21 · base SIH-MG v2.1

Preenchimento:

**Data de elaboração**

> DD/MM/AAAA

Preenchimento:

**Lacunas a que esta versão responde**

> IDs das lacunas (RCxx-Ly) apontadas pelo NIAR-Saúde no pedido, e a data do pedido. No rascunho e na primeira versão assinada, escreva "não se aplica".
> Ex.: Pedido de 20/11/2026: RC02-L1, RC03-L2.

Preenchimento:

**Divergências entre fontes** · [A]

> Quem pré-preenche registra aqui cada divergência entre a execução, o Model Card, o Data Card, publicações ou comunicações. Não escolhe uma das fontes. A equipe diz como resolveu. Se não houver, declare.

| Campo do relatório | Fonte 1 (e versão) | Fonte 2 (e versão) | Divergência | Como a equipe resolveu |
| ------------------- | ------------------- | ------------------- | ------------ | ---------------------- |
|                     |                     |                     |              |                        |

---

## Seção 1. Grupos e populações

> Define para quem a justiça será avaliada (RC01). É a base de todo o relatório: as Seções 2 a 4 só avaliam os grupos listados aqui.

### 1.1 Grupos e populações considerados · OBRIGATÓRIO

**Tabela de grupos** · [J · RC01.1 a RC01.3]

> Uma linha por grupo que pode ser afetado de forma diferente, com os nomes usados no Data Card e no Model Card.
> Colunas: Grupo (nome padronizado); Definição operacional (variável e categorias); Origem da identificação (contexto de uso, literatura ou dados); Justificativa e fonte (por que pode ser afetado de forma diferente, com a fonte); Analisável? (Sim ou Não; se Não, ver 1.2).
> Não se limite às colunas da base. Um grupo relevante para o contexto entra mesmo sem dados e vai para "Grupos não analisáveis".
> Para fundamentar a escolha, use as recomendações 1.2c e 2.2a do STANDING Together: identificar grupos em risco por fatores estruturais e sociais, a partir de literatura, especialistas do domínio, experiência vivida e análise de dados.
> Ex.: Pessoas com poucas consultas registradas · menos de 2 consultas nos 12 meses anteriores · literatura · o histórico de uso é preditor, e quem usa menos o serviço por barreira de acesso pode ter o risco subestimado (Obermeyer et al., 2019) · Sim.

| Grupo | Definição operacional | Origem da identificação | Justificativa e fonte | Analisável? |
| ----- | ----------------------- | ------------------------- | --------------------- | ------------ |
|       |                         |                           |                       |              |
|       |                         |                           |                       |              |
|       |                         |                           |                       |              |

**Escolha além dos dados** · [J · RC01.3]

> Diga se a escolha dos grupos foi além dos atributos que existem nos dados. Cite os grupos incluídos a partir do contexto de uso ou da literatura.
> Ex. (proposta): Sim. "Pessoas com poucas consultas" e "pessoas em situação de rua" vieram da literatura e do contexto de uso, não de colunas da base.

Preenchimento:

### 1.2 Grupos não analisáveis e exclusões · OBRIGATÓRIO

**Grupos não analisáveis** · [A + J · RC01.4]

> Grupos relevantes que não podem ser analisados e o motivo: variável inexistente, valores ausentes acima do limite ou n abaixo do mínimo. Se não houver, declare.
> Ex.: Raça/cor: 35% de valores ausentes · População indígena: n = 48 no conjunto de avaliação (mínimo: 100) · Pessoas em situação de rua: não registrado.

Preenchimento:
Fonte e versão:

**Grupos sujeitos a exclusão dos benefícios** · [J · RC01.5]

> Grupos que podem ficar sem acesso aos benefícios da tarefa e o mecanismo da exclusão. Pense em quem não chega a ser avaliado pela tarefa, não em quem é avaliado com erro. Esses grupos são retomados na Seção 4.
> Ex.: Pacientes de hospitais que não usam o painel de risco; pacientes atendidos majoritariamente na rede privada.

Preenchimento:

**Limitações na escolha dos grupos** · [J · RC01.6]

> Incertezas sobre a completude da escolha (grupos relevantes que podem ter ficado de fora) e sobre como os grupos foram definidos ou registrados.
> Ex.: Raça/cor é anotada pelo profissional na internação e nem sempre é autodeclarada.
> Ex. (proposta): Não houve consulta a representantes de pacientes; grupos definidos por deficiência podem ter ficado de fora.

Preenchimento:

> Atenção: os grupos da Seção 1 são a base das Seções 2 a 4. Todo grupo listado deve aparecer nos resultados ou constar como não analisável.

---

## Seção 2. Efeitos sobre os grupos

> Mostra se a tarefa funciona e afeta os grupos de forma diferente (RC02), registra se as diferenças são justificadas e o que foi feito a respeito.

### 2.1 Métricas e critérios · OBRIGATÓRIO

**Métricas e justificativa** · [J · RC02.2]

> Métricas usadas e por quê, considerando a decisão apoiada pela tarefa. Em uso assistivo (indicar pacientes para um benefício), o erro mais grave é deixar alguém de fora: priorize sensibilidade e taxa de falsos negativos. Em uso punitivo ou custoso, priorize falsos positivos. Inclua calibração quando o escore ordena pacientes. Ferramenta sugerida: árvore de fairness do Aequitas.
> Ex.: Sensibilidade e taxa de falsos negativos por grupo, porque deixar de indicar um paciente de alto risco significa ficar sem acompanhamento; calibração por grupo, porque o escore ordena a lista de prioridade.

Preenchimento:

**Grupo de referência** · [J · RC02.2]

> Grupo usado como base de comparação e motivo da escolha. Defina ANTES de ver os resultados.
> Ex.: faixa de 40 a 59 anos (maior grupo).

Preenchimento:

**Limiar de disparidade** · [J · RC02.2]

> Critério definido ANTES da análise para considerar uma diferença relevante.
> Ex.: razão entre 0,8 e 1,25 em relação ao grupo de referência (regra dos 80%).

Preenchimento:

**Ponto de corte operacional** · [A]

> Limiar de decisão efetivamente usado no contexto de uso, com a fonte (Model Card, seção e versão).

Preenchimento:
Fonte e versão:

**Ferramentas** · [A]

> Bibliotecas e versões usadas no cálculo.
> Ex.: Fairlearn (MetricFrame) · Aequitas.

Preenchimento:

### 2.2 Resultados por grupo · OBRIGATÓRIO

**Desempenho por grupo** · [A · RC02.1]

> Desempenho no conjunto de avaliação, com intervalo de confiança de 95%. A primeira linha traz o resultado geral. Confira se todos os grupos da Seção 1 aparecem ou constam como não analisáveis e se há n e intervalo de confiança.
> Ex.: 80+ anos · n = 1.240 · sensibilidade 0,64 (IC 95% 0,58 a 0,70) · razão vs. referência 0,82.

| Grupo | n | Métrica principal | Resultado (IC 95%) | Razão vs. referência |
| ----- | - | ------------------ | ------------------ | ---------------------- |
| Geral |   |                    |                    | 1,00                   |
|       |   |                    |                    |                        |
|       |   |                    |                    |                        |

Fonte e versão:

**Erros no ponto de corte operacional** · [A · RC02.4]

> Taxas de erro calculadas no ponto de corte usado na prática, e não apenas por métricas sem limiar, como a AUC.

| Grupo | Taxa de falsos negativos | Razão vs. referência | Taxa de falsos positivos | Razão vs. referência |
| ----- | ------------------------ | ---------------------- | ------------------------ | ---------------------- |
| Geral |                          | 1,00                   |                          | 1,00                   |
|       |                          |                        |                          |                        |
|       |                          |                        |                          |                        |

Fonte e versão:

**Diferenças encontradas** · [A + J · RC02.3]

> Diferenças relevantes entre os grupos: as que passam do limiar de disparidade e as que não podem ser descartadas por IC largo ou n pequeno. Para cada uma: grupo, métrica, valor e razão.
> Ex. (proposta): 80+ anos: sensibilidade com razão 0,82, fora do limiar. Pessoas com poucas consultas: razão 0,86, com IC de 0,70 a 1,02; não é possível descartar a diferença.

Preenchimento:

### 2.3 Decisões e consequências no uso · CONDICIONAL

**Decisões por grupo** · [A + J · RC02.5]

> Quando a tarefa já está em uso: quem foi indicado ou deixou de ser, por grupo, comparado à necessidade observada no mesmo grupo.
> Ex.: Pessoas com 80 anos ou mais: 9% das indicações para acompanhamento e 21% das reinternações observadas.

Preenchimento:
Fonte e versão:

**Se a Tarefa não influencia decisões no uso atual**

> Registre isso e explique.
> Ex.: tarefa ainda não implantada.

Preenchimento:

### 2.4 Interpretação e julgamento · OBRIGATÓRIO

**Interpretação** · [J · RC02.6]

> Significado clínico, técnico ou operacional de cada diferença listada em "Diferenças encontradas". Traduza cada diferença em consequência prática.
> Ex.: A diferença de 14 pontos na sensibilidade significa que, a cada 100 pessoas com 80 anos ou mais que serão reinternadas, 14 a mais deixam de ser indicadas para acompanhamento.

Preenchimento:

**Classificação das diferenças** · [J · RC02.7]

> Para cada diferença listada em "Diferenças encontradas", inclusive as com IC largo ou n pequeno: justificada, injustificada ou sem conclusão. Explicite o critério usado para classificar e o fundamento (clínico, epidemiológico, normativo). Use "sem conclusão" quando os dados não permitem decidir (IC largo, n pequeno, falta de referência clínica) e diga o que falta para concluir.
> Até que o NIAR defina critérios formais, use como referência: é justificada a diferença com base clínica ou epidemiológica documentada e consequência aceitável no uso; é, em regra, injustificada a diferença que reflete acesso, registro ou qualidade dos dados, e não necessidade.
> Ex.: Calibração pior em 18 a 39 anos: justificada (baixa prevalência, baixo impacto no uso). Sensibilidade menor em 80+ anos: injustificada, pois reflete acesso e não necessidade.
> Ex. (proposta): Sensibilidade em pessoas com poucas consultas: sem conclusão; a amostra não permite decidir; nova análise com os dados de 2024.

| Diferença | Classificação (justificada, injustificada ou sem conclusão) | Critério e fundamento, ou o que falta para concluir |
| ---------- | -------------------------------------------------------------- | ---------------------------------------------------- |
|            |                                                                |                                                      |
|            |                                                                |                                                      |

**Participantes da análise**

> Nome e papel de quem participou, incluindo especialista do domínio.

Preenchimento:

### 2.5 Mitigação · OBRIGATÓRIO

**Ações de mitigação** · [A + J · RC02.8]

> Registre o que foi considerado, o que foi feito e com que efeito, ou por que nada foi feito. O relatório não exige que o projeto mitigue; exige que registre. Uma ação descartada, com o motivo, é registro válido. Métodos e ferramentas: Anexo A.
> Etapa: formulação, dados, treinamento, saída ou uso. Situação: considerada, realizada ou descartada (com motivo).
> Desconfie de "nivelar por baixo": uma disparidade menor pode vir de piora no grupo favorecido. Mostre sempre as métricas de cada grupo antes e depois, e não só a diferença entre eles.
> Ex.: Recalibração por faixa etária · saída · scikit-learn CalibratedClassifierCV por grupo · realizada · taxa de falsos negativos em 80+ de 0,36 para 0,25 e em 40 a 59 sem alteração (0,22); AUC global de 0,81 para 0,80.

| Ação | Etapa | Ferramenta | Situação | Efeito por grupo (antes → depois) |
| ------ | ----- | ---------- | ---------- | ---------------------------------- |
|        |       |            |            |                                    |
|        |       |            |            |                                    |

### 2.6 Riscos residuais · OBRIGATÓRIO

**Diferenças residuais** · [J · RC02.9]

> Diferenças injustificadas ou sem conclusão que permanecem após a mitigação, e outros riscos relevantes, com os grupos afetados.
> Ex.: A sensibilidade menor em pessoas com poucas consultas persiste.

Preenchimento:

**Próximos passos da equipe** · [J]

> O que a equipe vai fazer: revisão clínica, restrição de uso, nova coleta, nova análise, monitoramento.
> Ex.: A equipe fará revisão clínica antes de excluir pessoas com poucas consultas da lista de acompanhamento.

Preenchimento:

---

## Seção 3. Dados, variável-alvo e padrão de referência

> Verifica se os dados, a variável-alvo e o padrão de referência são adequados para todos os grupos (RC03). Problemas aqui costumam explicar as diferenças da Seção 2 e não se resolvem com ajustes no modelo.

### 3.1 Informações factuais · OBRIGATÓRIO

**Representação dos grupos em cada conjunto de dados** · [A · RC03.1]

> n e proporção de cada grupo em cada conjunto, e prevalência do desfecho por grupo, com fonte e versão.
> Ex.: 80+ anos: 9% no desenvolvimento e 9% na avaliação; reinternação em 30 dias de 21% (geral: 12%).

| Grupo | Desenvolvimento n (%) | Avaliação n (%) | Prevalência do desfecho | Fonte e versão |
| ----- | --------------------- | ----------------- | ------------------------ | --------------- |
| Geral |                       |                   |                          |                 |
|       |                       |                   |                          |                 |
|       |                       |                   |                          |                 |

**Grupos sub-representados** · [A · RC03.1]

> Grupos abaixo do n mínimo ou com muitos valores ausentes, com o limiar usado.

Preenchimento:
Fonte e versão:

**Origem e seleção dos dados** · [A · RC03.1]

> Resumo da origem e do processo de seleção dos dados, com a fonte (Data Card, seção e versão).

Preenchimento:
Fonte e versão:

**Variável-alvo** · [A · RC03.1]

> Definição operacional: evento, janela de tempo e fonte. Resumo com a fonte (Model Card, seção e versão).
> Ex.: Nova AIH em qualquer hospital do SUS-MG até 30 dias após a alta.

Preenchimento:
Fonte e versão:

**Padrão de referência** · [A · RC03.1]

> Como o resultado considerado correto foi estabelecido em cada etapa (desenvolvimento, validação e avaliação), inclusive rotulagem ou adjudicação, com a fonte. O item 8a do TRIPOD+AI pede que a forma de aferir o desfecho seja consistente entre grupos sociodemográficos e que as discrepâncias sejam relatadas.
> Ex.: Registro no SIH, sem revisão de prontuário, igual em desenvolvimento e avaliação.

Preenchimento:
Fonte e versão:

**Uso de atributos sensíveis**

> Se raça/cor, sexo e outros atributos entram como variável preditora, proxy, rótulo ou só estratificação, e por quê (STANDING Together 2.2c). Retirar o atributo não elimina o viés, porque as proxies continuam. Cite a fonte (Data Card, seção e versão).
> Ex.: Raça/cor: apenas estratificação, não entra no modelo. Sexo: variável preditora, por diferença clínica documentada na taxa de reinternação.

Preenchimento:
Fonte e versão:

**Limitações conhecidas** · [J · RC03.1]

> Limitações dos dados, da variável-alvo e do padrão de referência.

Preenchimento:

### 3.2 Análise para Justiça · OBRIGATÓRIO

**Efeito da seleção** · [A + J · RC03.2]

> Como cada critério de seleção altera a composição dos grupos (antes e depois).
> Ex.: Excluir internações de menos de 24 h removeu 18% dos homens de 18 a 39 anos e 6% das mulheres da mesma faixa.

Preenchimento:
Fonte e versão:

**Qualidade dos dados por grupo** · [A + J · RC03.3]

> Valores ausentes, forma de registro e mensuração por grupo, e conclusão.
> Ex.: Exames ausentes: 12% no geral e 31% em hospitais de pequeno porte.

Preenchimento:
Fonte e versão:

**Validade da variável-alvo** · [J · RC03.4]

> A variável-alvo mede o mesmo fenômeno em todos os grupos? Se ela mede uso do serviço, quem tem menos acesso parece ter menos risco.
> Ex.: Reinternações em hospitais privados não entram no SIH; para quem tem plano de saúde, o alvo subestima as reinternações.

Preenchimento:

**Desigualdades no alvo** · [J · RC03.5]

> A variável-alvo reflete desigualdades preexistentes? Compare, se possível, com uma medida independente de necessidade.

Preenchimento:

**Validade do padrão de referência** · [J · RC03.6]

> O padrão de referência é menos completo ou menos válido para algum grupo?

Preenchimento:

**Relação com a Seção 2** · [J · RC03.7]

> Quais limitações desta seção ajudam a explicar as diferenças da Seção 2. Ligue cada limitação a uma diferença observada, com a evidência da ligação.
> Ex.: Exames ausentes → menor sensibilidade em hospitais de pequeno porte → no subconjunto com exames completos, a diferença cai de 12 para 4 pontos.

Preenchimento:

**Decisão sobre o tratamento** · [J · RC03.8]

> Para cada problema desta seção que afeta algum grupo: a decisão tomada e o fundamento. A decisão pode ser corrigir (etapas 1 e 2 do Anexo A), restringir o uso, aceitar como limitação com justificativa ou tratar em nova versão.
> Ex. (proposta): Reinternações em hospitais privados fora do SIH: aceitas como limitação; a equipe propõe restringir o uso a pacientes sem plano de saúde.

Preenchimento:

> Atenção: mitigação no modelo não corrige variável-alvo ou padrão de referência inválidos. Se esta seção apontar esse problema, registre a decisão em "Decisão sobre o tratamento". Métodos: etapas 1 e 2 do Anexo A.

---

## Seção 4. Acesso e possibilidade de benefício

> Verifica se a forma de disponibilizar a tarefa cria ou agrava desigualdades em quem pode se beneficiar dela (RC04). Um modelo com desempenho igual entre grupos ainda pode ser injusto se só puder ser usado onde há mais recursos. Nenhuma das diretrizes de referência (STANDING Together, TRIPOD+AI, HEAAL) traz um procedimento para avaliar o acesso ao benefício. Esta seção é uma contribuição própria do FIAR-Saúde, alinhada ao princípio de equidade do SUS.

**Disponibilização no uso atual**

> Se a Tarefa não está disponível de nenhuma forma no uso atual (por exemplo, só em pesquisa), registre isso e explique por que esta seção não se aplica. Nesse caso, não preencha 4.1 a 4.3. O NIAR-Saúde confirma.

Preenchimento:
Fonte e versão:

### 4.1 Disponibilização · CONDICIONAL

**Forma de disponibilização** · [A · RC04.1]

> Canal, usuários, locais e momento de uso no fluxo de trabalho. Resumo com a fonte (Model Card, seção e versão).
> Ex.: Painel web consultado na alta por enfermeiros de 5 dos 12 hospitais da rede.

Preenchimento:
Fonte e versão:

**Requisitos de uso** · [A · RC04.2]

> Requisitos técnicos e de dados para usar a tarefa. Inclua requisitos de dados, não só técnicos.
> Ex.: internet estável, login institucional, exames dos últimos 12 meses registrados no prontuário.

Preenchimento:
Fonte e versão:

**Disponibilidade por local** · [A · RC04.4]

> Locais ou serviços que usam e que não usam a tarefa, e a população que cobrem.
> Ex.: 5 de 12 hospitais usam o painel; cobrem 40% das altas da rede; nenhum hospital do interior.

Preenchimento:
Fonte e versão:

### 4.2 Condições de acesso por grupo · CONDICIONAL

**Condições de acesso** · [J · RC04.3, RC04.5, RC04.6]

> Uma linha por condição que limita o uso ou o benefício (idioma, conectividade, localização, custo, letramento, acessibilidade, dados exigidos), para pacientes e para serviços. Os grupos são os da Seção 1. Classifique cada condição: justificada, injustificada ou sem conclusão, com o critério e o fundamento.
> Ex.: Conectividade · pacientes dos 3 hospitais do interior com internet instável · alta sem consulta ao escore · injustificada: há prontuário eletrônico, falta só conexão.

| Condição de uso | Grupos da Seção 1 afetados (e locais) | Efeito sobre o acesso ou benefício | Classificação (justificada, injustificada ou sem conclusão) e fundamento |
| ----------------- | --------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------- |
|                   |                                         |                                     |                                                                             |
|                   |                                         |                                     |                                                                             |

### 4.3 Medidas e limitações residuais · CONDICIONAL

**Medidas** · [J · RC04.7]

> Para cada barreira injustificada ou sem conclusão: a medida e a situação (considerada, realizada ou descartada, com motivo), ou o motivo para não haver medida. Métodos: Anexo A, etapa 5.
> Ex.: Lista impressa diária de pacientes priorizados (realizada); versão offline (descartada: custo).

Preenchimento:

**Limitações residuais** · [J · RC04.8]

> Desigualdades de acesso injustificadas ou sem conclusão que permanecem, e os próximos passos da equipe.
> Ex.: Hospitais do interior sem cobertura até a expansão; registrado na Seção 5.

Preenchimento:

---

## Seção 5. Síntese da equipe

Apresentada ao Comitê Gestor no relatório do NIAR-Saúde.

> Apresenta a posição da equipe em forma curta. O NIAR-Saúde leva esta seção ao Comitê Gestor no seu relatório, separada da própria análise. Registra quem assina. No rascunho pré-preenchido, os resumos vêm marcados [a confirmar] e as assinaturas ficam em branco.

**Grupos considerados e não analisáveis**

> Resumo de 1.1 e 1.2.

Preenchimento:

**Diferenças encontradas, classificação e fundamento**

> Resumo de 2.2 a 2.4 e de 4.2.

Preenchimento:

**Decisão sobre cada diferença**

> Para cada diferença ou barreira injustificada ou sem conclusão: o que a equipe decidiu (mitigar, restringir o uso, aceitar com justificativa, nova análise). Inclua as decisões de 3.2.

Preenchimento:

**Limitações**

> Limitações que afetam a leitura dos resultados: grupos não analisáveis, dados, variável-alvo, padrão de referência.

Preenchimento:

**Plano**

> O que a equipe vai fazer, quem responde e até quando.
> Ex. (proposta): Nova análise de sensibilidade com dados de 2024 · Dr. Beltrano · 03/2027.

| O que | Responsável | Prazo |
| ----- | ------------ | ----- |
|       |              |       |

**Riscos residuais e condições de uso propostas pela equipe**

> O que permanece e em que condições a equipe propõe que a Tarefa seja usada.
> Ex. (proposta): Revisão clínica obrigatória para pessoas com 80 anos ou mais antes da exclusão da lista.

Preenchimento:

**Mudanças que exigem nova versão do relatório**

> Mudanças que exigem nova versão do relatório.
> Ex.: Retreinamento do modelo; uso em outra região; inclusão de hospitais privados; mudança no ponto de corte.

Preenchimento:

**Assinaturas**

> O responsável pelo projeto assina a síntese e as decisões. O responsável técnico assina as análises.
> Ex.: Profa. Dra. Fulana de Tal (responsável pelo projeto) e Dr. Beltrano (responsável técnico), 14/10/2026.

| Papel                                            | Nome | Data |
| ------------------------------------------------ | ---- | ---- |
| Responsável pelo projeto (síntese e decisões) |      |      |
| Responsável técnico (análises)                |      |      |

---

## Seção 6. Versionamento e histórico do relatório

> Mantém o histórico do relatório. Uma linha por versão, do rascunho 0.1.0 em diante. Cada nova versão do modelo ou dos dados exige nova versão do relatório.
> Ex.: 1.1.0 · respostas às lacunas RC02-L1 e RC03-L2; inclusão do grupo "pessoas com poucas consultas" · Model Card 1.0.0, Data Card 2.1 · 20/11/2026 · Fulana de Tal

| Versão | Descrição da atualização | Versões de Model Card e Data Card | Data | Responsável (quem aprovou) |
| ------- | ---------------------------- | ---------------------------------- | ---- | --------------------------- |
|         |                              |                                    |      |                             |

---

## Anexo A. Métodos de mitigação por etapa

> Referência para a tabela 2.5 (mitigação), o campo 3.2 Decisão sobre o tratamento (etapas 1 e 2) e o campo 4.3 (medidas). Indica, para cada método, a ferramenta que faz o que o item pede. O relatório não exige mitigação: exige o registro do que foi considerado e feito.
>
> Os métodos mais eficazes em saúde costumam estar nas pontas: na formulação do problema e no uso. Os métodos aplicados só ao modelo (etapas 3 e 4) são os mais conhecidos, mas não corrigem problemas de dados ou de variável-alvo.

**Etapa 1. Formulação do problema**

| Método                                   | Ferramenta                   | Quando usar e cuidados                                                                                                                                                                                      |
| ----------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Redefinir a variável-alvo                | Decisão de modelagem        | Quando a Seção 3 apontar alvo pouco válido. Em Obermeyer et al. (2019), trocar "gasto" por "condições crônicas ativas" aumentaria de 17,7% para 46,5% a proporção de pacientes negros selecionados. |
| Rever variáveis que funcionam como proxy | Fairlearn CorrelationRemover | Ex.: número de consultas como proxy de acesso. Registre o desempenho antes e depois.                                                                                                                       |
| Decidir o papel do atributo sensível     | Decisão de modelagem        | Retirar o atributo não elimina o viés. Registre a decisão.                                                                                                                                               |

**Etapa 2. Dados (pré-processamento)**

| Método                                         | Ferramenta                                                                | Quando usar e cuidados                                                                          |
| ----------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Coletar mais dados dos grupos sub-representados | (nenhuma)                                                                 | O melhor caminho, mas o mais caro.                                                              |
| Reamostrar por grupo e desfecho                 | Amostragem estratificada (pandas, imbalanced-learn) por grupo × desfecho | Diferente do SMOTEENN, que equilibra só as classes do desfecho. Pode distorcer a calibração. |
| Reponderar (reweighing)                         | AIF360 Reweighing                                                         | Torna grupo e desfecho independentes no treino (Kamiran e Calders, 2012). Bom ponto de partida. |
| Remover impacto díspar                         | AIF360 DisparateImpactRemover                                             | Altera os valores das variáveis e prejudica a interpretabilidade.                              |
| Aprender representações justas                | AIF360 LFR, OptimPreproc; Fairlearn PrototypeRepresentationLearner        | Pouco usado em saúde: as variáveis perdem significado clínico.                               |
| Corrigir qualidade diferencial                  | Decisão de dados                                                         | Quando a Seção 3 mostrar valores ausentes ou erros concentrados em algum grupo.               |

**Etapa 3. Treinamento**

| Método                              | Ferramenta                                                                                                                                    | Quando usar e cuidados                                              |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Otimizar com restrição de justiça | Fairlearn ExponentiatedGradient ou GridSearch (TruePositiveRateParity, EqualizedOdds, ErrorRateParity); AIF360 ExponentiatedGradientReduction | Escolha a restrição antes, conforme o uso (Agarwal et al., 2018). |
| Limitar a perda do pior grupo        | Fairlearn BoundedGroupLoss; Group DRO (Sagawa et al., 2020) em implementação própria                                                       | Evita reduzir a disparidade piorando o grupo favorecido.            |
| Penalidade de justiça               | AIF360 PrejudiceRemover                                                                                                                       | Exige ajustar o peso da penalidade.                                 |
| Adversarial debiasing                | Fairlearn AdversarialFairnessClassifier; AIF360 AdversarialDebiasing                                                                          | Treinamento instável e menos interpretável (Zhang et al., 2018).  |
| Grupos interseccionais               | AIF360 GerryFairClassifier                                                                                                                    | Para muitos subgrupos cruzados; instável com grupos pequenos.      |

**Etapa 4. Saída (pós-processamento)**

| Método                       | Ferramenta                                                                                    | Quando usar e cuidados                                                                                                                                          |
| ----------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recalibrar por grupo          | scikit-learn CalibratedClassifierCV ajustado por grupo; AIF360 CalibratedEqOddsPostprocessing | Muito relevante quando o escore ordena pacientes.                                                                                                               |
| Limiares por grupo            | Fairlearn ThresholdOptimizer; AIF360 EqOddsPostprocessing                                     | Exige o atributo sensível no momento do uso e cria tratamento explicitamente diferenciado; discuta as implicações éticas e jurídicas (Hardt et al., 2016). |
| Revisão na zona de incerteza | AIF360 RejectOptionClassification; fluxo de revisão clínica                                 | Casos próximos ao limiar vão para decisão humana. Dimensione a carga de trabalho.                                                                            |
| Reordenar listas priorizadas  | AIF360 DeterministicReranking                                                                 | Quando a saída é uma lista de pacientes priorizados.                                                                                                          |

**Etapa 5. Uso e implantação (campo 4.3)**

| Método                                   | Ferramenta                                                 | Quando usar e cuidados                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Revisão clínica direcionada             | Fluxo de trabalho                                          | Revisão obrigatória para os grupos em que o modelo erra mais. Deve constar dos usos previstos no Model Card. |
| Ampliar o acesso                          | Decisão de implantação                                  | Versão offline, outros canais, outras unidades, capacitação.                                                |
| Monitorar por grupo após a implantação | Fairlearn MetricFrame ou Aequitas aplicados periodicamente | Base no HEAAL (ponto de decisão 7: monitorar a solução).                                                    |
| Excluir do escopo                         | Model Card (usos inadequados)                              | Legítimo quando as demais medidas não são viáveis, mas aumenta a exclusão dos benefícios (RC01.5).       |

**Cuidados gerais**

- Escolha a métrica antes de mitigar. Calibração e taxas de erro iguais não podem ser atingidas ao mesmo tempo quando a prevalência difere entre grupos (Kleinberg et al., 2016; Chouldechova, 2017).
- Mostre as métricas de cada grupo antes e depois, para evitar "nivelar por baixo".
- Mitigação no modelo não corrige variável-alvo inválida: nesse caso, use as etapas 1 e 2.
- Com grupos pequenos, a mitigação fica instável: reporte intervalos de confiança.
- Em tarefas sem predição (ex.: geração de dados sintéticos), use geração condicionada por grupo e pesos amostrais.

---

## Checklist de entrega

- [ ] Seções 0 a 6 preenchidas. A 2.3 preenchida ou com o registro de que a Tarefa não influencia decisões. A Seção 4 preenchida ou com o motivo de a Tarefa não estar disponível no uso atual.
- [ ] Textos de instrução removidos.
- [ ] Todo grupo da Seção 1 aparece nas tabelas da Seção 2 ou consta como não analisável.
- [ ] Nomes de grupos idênticos aos do Data Card e do Model Card.
- [ ] Grupo de referência e limiar de disparidade definidos antes da análise.
- [ ] Toda diferença injustificada ou sem conclusão aparece em 2.5 ou 2.6. Toda barreira injustificada ou sem conclusão aparece em 4.3.
- [ ] Nenhum campo marcado [a confirmar].
- [ ] Todo fato com fonte e versão (para comunicações, arquivo e data). Divergências entre fontes resolvidas ou explicadas.
- [ ] Origem dos resultados identificada na Seção 0 (execução na sala segura ou outra fonte).
- [ ] Versão do relatório preenchida (1.0.0 na primeira versão assinada) e "Lacunas a que esta versão responde" preenchido ("não se aplica" na primeira versão).
- [ ] Seção 5 assinada pelo responsável pelo projeto e pelo responsável técnico.

---

Estruturado a partir de STANDING Together (Alderman et al., Lancet Digit Health, 2025), TRIPOD+AI (Collins et al., BMJ, 2024) e HEAAL (Kim et al., PLOS Digit Health, 2024). Ferramentas: Fairlearn, AI Fairness 360 (IBM) e Aequitas. Requisitos de Justiça FIAR-Saúde (RC01 a RC04).

# FIAR-Saúde — Template de Ciclo de Avaliação

Este repositório fornece uma estrutura operacional reutilizável para organizar e documentar um ciclo de avaliação do FIAR-Saúde associado a uma **Tarefa de IA**, uma **Versão Avaliável** e um **Contexto de Uso** específicos.

O template pode ser utilizado para criar um repositório privado de um projeto, no qual são organizados:

- a documentação inicial da tarefa;
- os artefatos e evidências produzidos pelo projeto;
- as rodadas de validação documental;
- as avaliações realizadas pelo NIAR-Saúde;
- os registros de decisões técnicas;
- as decisões institucionais, quando aplicáveis;
- os relatórios produzidos ao longo do ciclo.

Este repositório não substitui nem replica a documentação metodológica oficial do FIAR-Saúde.

A fonte oficial para conceitos, dimensões, trilhas, procedimentos de avaliação, governança e modelo de maturidade está disponível em:

[https://github.com/niar-saude-ufmg/FIAR-Saude](https://github.com/niar-saude-ufmg/FIAR-Saude)

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

---

## Escopo do template

O repositório pode ser iniciado antes da realização de uma avaliação formal. Nesse caso, os primeiros passos consistem no registro das informações iniciais fornecidas pela equipe do projeto, na triagem pelo NIAR-Saúde e na delimitação da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da Trilha de Execução. A partir dessa delimitação, o NIAR-Saúde define quais artefatos e evidências são necessários para o ciclo.

Cada repositório criado a partir deste template constitui a estrutura documental e técnica de um projeto acompanhado pelo FIAR-Saúde, na qual são registrados seus ciclos de avaliação.

O ciclo é delimitado por:

- uma Tarefa de IA;
- uma Versão Avaliável;
- um Contexto de Uso;
- uma trilha de execução aplicável.

**Estrutura canônica e aplicabilidade.** Este template mantém previamente diretórios, registros e modelos destinados a suportar as diferentes etapas do ciclo FIAR-Saúde. A existência desses elementos na estrutura não significa que todos sejam aplicáveis ou devam ser preenchidos em toda avaliação. A aplicabilidade é determinada no contexto de cada ciclo, considerando a Tarefa de IA, a Versão Avaliável, o Contexto de Uso, a Trilha de Execução e os requisitos analisados. Um template não preenchido não constitui evidência e sua simples existência não deve gerar automaticamente uma pendência, inconsistência ou não conformidade.

A criação do repositório, o preenchimento dos documentos ou a validação factual das informações não constituem:

- resultado de conformidade;
- certificação técnica;
- validação clínica;
- garantia de que o sistema seja justo, seguro ou ético;
- autorização institucional ou regulatória para implantação.

---

## Conceitos fundamentais

### Tarefa de IA

A Tarefa de IA é a unidade de trabalho avaliada pelo FIAR-Saúde.

Ela é definida pela combinação de modelo, dados, procedimentos de treinamento e inferência, objetivo clínico ou operacional e contexto de uso.

Um mesmo projeto pode conter mais de uma Tarefa de IA.

### Versão Avaliável

A Versão Avaliável corresponde a uma configuração específica da tarefa que introduz mudança relevante no modelo, nos dados, nos procedimentos ou no Contexto de Uso e que, por isso, requer nova avaliação integral ou parcial.

Nem toda alteração técnica constitui uma nova Versão Avaliável.

Os critérios e gatilhos aplicáveis devem seguir a documentação oficial vigente do FIAR-Saúde.

### Contexto de Uso

O Contexto de Uso descreve onde, por quem, para qual finalidade e sob quais condições a tarefa será desenvolvida, avaliada ou utilizada.

Uma mesma combinação de modelo e dados pode exigir avaliações distintas quando aplicada a contextos de uso diferentes.

### Trilhas de execução

A trilha é uma propriedade da Tarefa de IA e deve ser enquadrada conforme o destino previsto e o estágio de uso da tarefa.

- **Trilha Experimental:** tarefas orientadas à pesquisa, experimentação, validação metodológica ou produção científica, sem integração a um sistema em operação ativa.
- **Trilha Produção:** tarefas integradas a sistemas em operação ativa e sujeitas a requisitos adicionais de acompanhamento e produção de evidências operacionais.

A equipe do projeto pode informar o uso atual e o uso pretendido da tarefa. O enquadramento da trilha é validado pelo NIAR-Saúde de acordo com a documentação oficial vigente.

### Conformidade e maturidade

A conformidade é pontual e se refere a uma Tarefa de IA em uma Versão Avaliável e um Contexto de Uso específicos.

A maturidade é longitudinal e pertence ao projeto. Ela é inferida a partir da recorrência, continuidade e rastreabilidade das práticas observadas ao longo do histórico de suas tarefas e versões avaliáveis.

Os estados de conformidade definidos pela documentação oficial não devem ser confundidos com os estados de preparação ou validação dos documentos deste repositório.

---

## Papéis no ciclo

### Equipe do projeto

A equipe do projeto é responsável por:

- desenvolver a tarefa e seus componentes;
- produzir, manter e atualizar os artefatos técnicos;
- fornecer informações factuais sobre dados, modelos, versões e resultados;
- produzir ou executar as análises técnicas sob sua responsabilidade;
- registrar responsáveis, limitações, riscos e decisões técnicas;
- validar e complementar as minutas documentais elaboradas a partir dos artefatos fornecidos.

### NIAR-Saúde

O NIAR-Saúde é responsável por:

- orientar a organização das evidências;
- apoiar a delimitação da Tarefa de IA, da Versão Avaliável e do Contexto de Uso;
- validar o enquadramento da trilha;
- avaliar a suficiência, consistência e rastreabilidade dos artefatos;
- identificar lacunas e inconsistências;
- conduzir a avaliação técnica aplicável;
- acompanhar o ciclo de vida das tarefas avaliadas.

A validação factual realizada pela equipe do projeto não substitui a avaliação técnica do NIAR-Saúde.

### Decisão institucional

Questões que ultrapassem o escopo da avaliação técnica, como aceite de risco residual, definição de condicionantes ou outras deliberações institucionais, podem ser encaminhadas à instância competente conforme a governança institucional vigente.

Os Registros de Decisão Técnica produzidos pelo projeto não devem ser confundidos com Registros de Decisão Institucional.

---

## Fluxo resumido do ciclo

1. O repositório privado é criado a partir deste template.
2. O NIAR-Saúde encaminha o Formulário de Entrada à equipe do projeto.
3. A equipe do projeto fornece as informações iniciais disponíveis.
4. O NIAR-Saúde realiza a triagem inicial.
5. O NIAR-Saúde delimita preliminarmente a Tarefa de IA, a Versão Avaliável,
   o Contexto de Uso e a Trilha de Execução.
6. Quando necessário, dúvidas factuais são esclarecidas com a equipe do projeto.
7. O NIAR-Saúde consolida a Identificação da Avaliação.
8. O NIAR-Saúde determina e solicita os artefatos e evidências necessários ao ciclo.
9. A equipe do projeto produz, preenche, atualiza ou fornece os artefatos solicitados.
10. O NIAR-Saúde registra o recebimento e realiza a pré-avaliação documental.
11. Pendências e inconsistências são registradas e tratadas.
12. O NIAR-Saúde realiza a avaliação aplicável.
13. Questões que exigem deliberação institucional são escalonadas quando necessário.
14. Os resultados e registros do ciclo são consolidados de forma rastreável.

O detalhamento do protocolo de validação documental fica registrado no `README.md` da pasta `documentacao_projeto/`.

---

## Como criar uma instância

1. Selecione **Use this template**.
2. Crie um repositório privado para o projeto.
3. Defina as permissões de acesso conforme a sensibilidade dos documentos e artefatos.
4. Utilize `documentacao_projeto/` para registrar as informações iniciais e delimitar o ciclo de avaliação.
5. Após a identificação da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da Trilha de Execução, produza, preencha, atualize ou forneça os artefatos e evidências solicitados pelo NIAR-Saúde nas pastas correspondentes.
6. Registre lacunas, inconsistências e análises pendentes sem preencher informações não sustentadas.
7. Utilize `avaliacao_niar/` para os instrumentos e registros produzidos pelo NIAR-Saúde.
8. Preserve o histórico das versões dos documentos e das rodadas de validação.

Não inclua dados pessoais, dados sensíveis, credenciais, chaves, identificadores diretos ou artefatos cujo armazenamento no Git não tenha sido autorizado.

---

## Estrutura atual do repositório

```text
documentacao_projeto/
	README.md
    formulario_entrada.md
    identificacao_avaliacao.md
  	controle_artefatos.md
  	historico_validacao.md
  	registro_de_pendencias.md
  	comunicacoes/

artefatos_projeto/
	data_cards/
  	model_cards/
  	fairness_reports/
  	explainability_reports/
  	decision_records/
  	consolidated_iar_report/
  	compliance/
    	ripd/
  	operational_artifacts/
    	monitoring/
    	incidents/
    	version_history/
    	periodic_review/

avaliacao_niar/
	avaliacao_por_requisito/
  	avaliacao_por_dimensao/
  	avaliacao_formal/

decisao_institucional/

fiar_sync/

pdf/
```

> A estrutura mantém diretórios e templates mesmo quando ainda não há conteúdo produzido. Sua presença tem função estrutural e orientadora e não implica, por si só, aplicabilidade ou obrigatoriedade da evidência correspondente.
>
> **Observação:** alguns nomes e arquivos desta estrutura serão atualizados progressivamente para refletir o fluxo de validação documental e a terminologia vigente do FIAR-Saúde. Até que essas alterações sejam concluídas, os caminhos acima correspondem à estrutura atualmente implementada no template.

---

## Artefatos do projeto

Os artefatos de desenvolvimento podem incluir, conforme a tarefa e o ciclo:

- Data Card;
- Model Card;
- Fairness Report;
- Explainability Report;
- Registro de Decisão Técnica;
- Relatório Consolidado de IAR;
- documentação de privacidade e proteção de dados;
- outros arquivos técnicos ou documentais necessários.

Tarefas na Trilha Produção podem exigir também artefatos operacionais, como:

- relatórios de monitoramento;
- registros de incidentes;
- histórico de versões;
- registros de implantação ou reimplantação;
- evidências de revisão periódica;
- planos de contingência e resposta a falhas.

A enumeração acima apresenta exemplos de evidências operacionais previstas pelo framework e não corresponde necessariamente a uma relação de diretórios ou artefatos obrigatórios do template.

A presença de um artefato, isoladamente, não demonstra suficiência da evidência nem determina conformidade.

---

## Marcadores de pendências

Quando as informações disponíveis não forem suficientes, utilize os seguintes marcadores:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]

[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]

[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

Informações, resultados, responsáveis, versões, riscos ou decisões não devem ser inventados para completar os arquivos.

---

## Estados documentais

Os documentos podem passar pelos seguintes estados:

- Rascunho interno do NIAR;
- Minuta para validação do projeto;
- Em revisão pelo projeto;
- Retornado pelo projeto;
- Em consolidação pelo NIAR;
- Para confirmação final;
- Validado para início do ciclo;
- Substituído;
- Arquivado.

Esses estados descrevem o andamento documental e não equivalem a um resultado de conformidade.

---

## Versionamento e rastreabilidade

Cada documento produzido ou modificado durante o ciclo deve registrar, quando aplicável:

- versão do documento;
- data de referência;
- responsável pela elaboração;
- responsável pela validação factual;
- fonte das informações;
- alterações realizadas;
- pendências remanescentes;
- documento ou versão substituída.

A Versão Avaliável da tarefa deve estar vinculada, sempre que disponível, a:

- versão dos dados;
- versão do modelo;
- versão do código;
- commit ou tag;
- configuração da execução;
- identificador dos pesos ou artefatos;
- ambiente computacional;
- resultados e evidências correspondentes.

Esses elementos constituem mecanismos possíveis de rastreabilidade quando aplicáveis e disponíveis. A ausência de um identificador específico não deve ser interpretada automaticamente como pendência ou não conformidade; deve ser avaliada em relação ao requisito e às demais evidências disponíveis.

---

## Avaliação pelo NIAR-Saúde

A pasta `avaliacao_niar/` reúne instrumentos e registros produzidos pelo NIAR-Saúde.

A equipe do projeto não deve alterar diretamente os julgamentos técnicos ou registros exclusivos do NIAR-Saúde.

Quando for necessária validação factual, o NIAR-Saúde encaminhará uma minuta ou um conjunto de perguntas à equipe do projeto. As respostas e alterações serão consolidadas de forma rastreável, preservando-se a independência da avaliação.

A pré-avaliação documental não constitui parecer final e não atribui automaticamente estados de conformidade.

---

## Relatório PDF consolidado

O repositório possui suporte para geração de um PDF consolidado a partir dos artefatos documentais.

Consulte [`pdf/README.md`](pdf/README.md) para as instruções de geração local.

O workflow automatizado está localizado em:

```text
.github/workflows/build-document.yml
```

Antes de renomear pastas ou arquivos utilizados pelo processo de geração, verifique e atualize as referências presentes no workflow, nos scripts de sincronização e na configuração do PDF.

---

## Automação

A automação de geração documental pode ser executada:

- em atualizações da branch principal;
- em pull requests;
- manualmente por `workflow_dispatch`.

Os artefatos gerados pelo workflow devem ser revisados antes de sua utilização como documento oficial do ciclo.

---

## Segurança e confidencialidade

Recomenda-se que as instâncias de projetos sejam privadas.

Antes de adicionar qualquer arquivo ao repositório, verifique:

- se o armazenamento em Git foi autorizado;
- se o arquivo contém dados pessoais ou sensíveis;
- se existem informações protegidas por contrato ou propriedade intelectual;
- se há credenciais, tokens ou chaves;
- se o histórico do Git pode preservar conteúdo que deveria ser removido;
- se o acesso está restrito às pessoas autorizadas.

Dados brutos sensíveis, credenciais e segredos não devem ser armazenados neste repositório.

---

## Documentação oficial

A metodologia e os conceitos do FIAR-Saúde devem ser consultados na documentação oficial:

[https://github.com/niar-saude-ufmg/FIAR-Saude](https://github.com/niar-saude-ufmg/FIAR-Saude)

Este template deve permanecer operacional e enxuto, evitando duplicar a documentação metodológica oficial.

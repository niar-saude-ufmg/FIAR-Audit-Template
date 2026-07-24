# Documentação do Projeto

Esta pasta reúne os documentos utilizados para **identificar, delimitar, validar e acompanhar** o ciclo FIAR-Saúde de uma Tarefa de IA em uma Versão Avaliável e um Contexto de Uso específicos.

Os arquivos desta pasta são usados antes e durante a avaliação técnica para registrar:

- a caracterização inicial da tarefa;
- a versão avaliável considerada;
- o contexto de uso;
- a trilha proposta e seu enquadramento;
- as rodadas de validação entre o NIAR-Saúde e a equipe do projeto;
- as lacunas, inconsistências e pendências identificadas;
- as fontes utilizadas para confirmar ou corrigir informações.

Esta pasta não substitui os artefatos técnicos do projeto. Data Cards, Model Cards, relatórios de justiça, relatórios de explicabilidade, registros de decisão técnica e demais evidências devem permanecer em `artefatos_projeto/`.

A documentação metodológica oficial do FIAR-Saúde está disponível em:

[https://github.com/niar-saude-ufmg/FIAR-Saude](https://github.com/niar-saude-ufmg/FIAR-Saude)

Em caso de divergência entre este template e a documentação oficial vigente, prevalece a documentação oficial do FIAR-Saúde.

---

## Arquivos da pasta

```text
documentacao_projeto/
├── README.md
├── identificacao_avaliacao.md
├── historico_validacao.md
└── registro_de_pendencias.md
```

### `identificacao_avaliacao.md`

Documento principal de caracterização do ciclo.

Deve registrar:

- identificação do projeto;
- identificação da Tarefa de IA;
- objetivo clínico ou operacional;
- Contexto de Uso;
- escopo da avaliação;
- itens fora do escopo;
- trilha proposta;
- justificativa da trilha;
- Versão Avaliável;
- versão dos dados;
- versão do modelo;
- versão do código;
- responsáveis;
- data de referência;
- artefatos recebidos;
- pendências de enquadramento.

O documento pode começar como uma minuta preparada pelo NIAR-Saúde a partir dos artefatos recebidos.

A equipe do projeto valida as informações factuais e técnicas. O NIAR-Saúde consolida o enquadramento da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da trilha.

### `historico_validacao.md`

Registra as rodadas de envio, revisão, retorno e consolidação dos documentos.

Deve preservar:

- versão enviada;
- data de envio;
- remetente;
- destinatário;
- prazo;
- data de retorno;
- alterações realizadas;
- pendências remanescentes;
- decisão sobre a próxima rodada.

### `registro_de_pendencias.md`

Consolida as pendências identificadas ao longo da inspeção e da validação documental.

As pendências podem ser classificadas como:

- informação;
- evidência;
- análise;
- inconsistência;
- enquadramento;
- decisão institucional.

O registro deve indicar responsável, prioridade, fonte, prazo, estado e resolução.

---

## Princípios da validação documental

### 1. Não inventar informações

Informações, resultados, métricas, decisões, riscos, responsáveis, versões ou evidências não devem ser preenchidos quando não estiverem sustentados pelos documentos fornecidos ou por confirmação explícita da equipe do projeto.

### 2. Preservar lacunas e inconsistências

Quando uma informação necessária não estiver disponível, use:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]
```

Quando uma conclusão depender de análise técnica ainda não realizada, use:

```text
[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]
```

Quando houver divergência entre artefatos, use:

```text
[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]
```

Quando o enquadramento depender de validação metodológica do NIAR-Saúde, use:

```text
[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]
```

Quando o tema exigir deliberação além da avaliação técnica, use:

```text
[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

### 3. Separar validação factual de avaliação técnica

A equipe do projeto valida:

- nomes;
- objetivos;
- dados utilizados;
- versões;
- arquitetura;
- resultados;
- responsáveis;
- limitações;
- riscos conhecidos;
- decisões técnicas efetivamente tomadas;
- existência e localização das evidências.

O NIAR-Saúde:

- orienta a estruturação dos documentos;
- verifica suficiência, consistência e rastreabilidade;
- consolida a delimitação da Tarefa de IA;
- consolida a Versão Avaliável e o Contexto de Uso;
- valida o enquadramento da trilha;
- identifica lacunas e inconsistências;
- conduz a avaliação técnica aplicável.

A validação factual pelo projeto não substitui a avaliação técnica do NIAR-Saúde.

### 4. Exigir fonte para correções

Sempre que possível, uma correção ou complementação deve indicar a fonte correspondente, como:

- Data Card;
- Model Card;
- relatório técnico;
- artigo;
- planilha;
- log de execução;
- repositório;
- commit ou tag;
- arquivo de configuração;
- registro de reunião;
- confirmação nominal de responsável técnico.

### 5. Preservar o histórico

Uma nova versão não deve apagar silenciosamente:

- informações anteriormente registradas;
- divergências;
- pendências;
- justificativas;
- fontes;
- decisões de enquadramento.

Alterações relevantes devem ser registradas no histórico de versões ou no `historico_validacao.md`.

---

## Protocolo de validação documental

### Etapa 1 — Recebimento dos artefatos

A equipe do projeto disponibiliza os documentos e evidências já existentes.

Exemplos:

- Data Card;
- Model Card;
- artigos e relatórios;
- código e repositórios;
- registros de execução;
- resultados;
- documentação ética, de privacidade ou regulatória;
- decisões técnicas já registradas.

O NIAR-Saúde registra a data, a versão e a origem de cada artefato recebido.

### Etapa 2 — Inspeção documental pelo NIAR-Saúde

O NIAR-Saúde realiza uma inspeção comparativa dos artefatos para identificar:

- projeto;
- Tarefa de IA;
- objetivo;
- Contexto de Uso;
- população ou unidade de análise;
- dados;
- versões;
- modelo;
- código;
- responsáveis;
- estágio de desenvolvimento;
- provável trilha;
- resultados;
- limitações;
- riscos;
- análises existentes;
- decisões técnicas documentadas;
- lacunas;
- inconsistências.

Nenhum resultado formal de conformidade é atribuído nesta etapa.

### Etapa 3 — Elaboração da minuta

O NIAR-Saúde preenche `identificacao_avaliacao.md` com as informações sustentadas pelos artefatos recebidos.

O documento deve ser identificado como:

```text
Versão: 0.1
Status: Minuta para validação do projeto
```

As lacunas, análises pendentes e inconsistências devem permanecer visíveis.

### Etapa 4 — Validação pela equipe do projeto

A equipe do projeto revisa a minuta e utiliza, para cada ponto aplicável, uma das seguintes respostas:

```text
VALIDADO
CORRIGIDO
COMPLEMENTADO
NÃO SE APLICA — justificativa obrigatória
NÃO É POSSÍVEL INFORMAR — justificativa obrigatória
REQUER DISCUSSÃO COM O NIAR
```

Correções e complementações devem indicar a fonte utilizada sempre que possível.

### Etapa 5 — Consolidação pelo NIAR-Saúde

O NIAR-Saúde:

- incorpora correções sustentadas;
- mantém divergências não resolvidas;
- atualiza o registro de pendências;
- solicita evidências adicionais quando necessário;
- separa questões factuais, técnicas, metodológicas e institucionais;
- define se é necessária entrevista de esclarecimento.

O documento pode passar para:

```text
Versão: 0.2
Status: Em consolidação pelo NIAR-Saúde
```

### Etapa 6 — Entrevista de esclarecimento

A entrevista deve ser usada apenas para questões que:

- não foram resolvidas documentalmente;
- permanecem contraditórias;
- afetam a delimitação da tarefa;
- afetam a Versão Avaliável;
- afetam o Contexto de Uso;
- afetam a trilha;
- afetam riscos, responsabilidades ou rastreabilidade.

As respostas relevantes devem ser incorporadas aos documentos. A ata ou gravação da reunião não substitui a atualização dos artefatos.

### Etapa 7 — Confirmação final

Ao final:

- a equipe do projeto confirma a correção factual e técnica das informações sob sua responsabilidade;
- o NIAR-Saúde confirma o enquadramento metodológico para fins do ciclo.

A versão pode ser identificada como:

```text
Versão: 1.0
Status: Validado para início do ciclo
```

Essa validação não constitui resultado de conformidade, certificação técnica, validação clínica ou autorização de implantação.

---

## Estados documentais

Os documentos podem passar pelos seguintes estados:

1. `Rascunho interno do NIAR`
2. `Minuta para validação do projeto`
3. `Em revisão pelo projeto`
4. `Retornado pelo projeto`
5. `Em consolidação pelo NIAR`
6. `Para confirmação final`
7. `Validado para início do ciclo`
8. `Substituído`
9. `Arquivado`

Esses estados descrevem o andamento documental e não equivalem aos resultados de uma avaliação formal de conformidade.

---

## Registro de validação

O documento `identificacao_avaliacao.md` deve conter, ao final, um bloco semelhante ao seguinte:

```markdown
## Registro de validação

### Validação pela equipe do projeto

A equipe do projeto confirma que as informações factuais e técnicas deste documento correspondem à tarefa, aos dados, ao modelo e ao estágio de desenvolvimento na data de referência indicada.

- Nome:
- Papel:
- Data:
- Observações:

### Validação pelo NIAR-Saúde

O NIAR-Saúde confirma o enquadramento da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da trilha para fins de organização deste ciclo.

Esta validação não constitui resultado de conformidade, certificação técnica, validação clínica ou autorização de implantação.

- Nome:
- Papel:
- Data:
- Observações:
```

---

## Responsabilidade sobre os arquivos

| Arquivo                        | Elaboração inicial | Validação factual                           | Consolidação |
| ------------------------------ | -------------------- | --------------------------------------------- | -------------- |
| `identificacao_avaliacao.md` | NIAR-Saúde          | Equipe do projeto                             | NIAR-Saúde    |
| `historico_validacao.md`     | NIAR-Saúde          | Não aplicável                               | NIAR-Saúde    |
| `registro_de_pendencias.md`  | NIAR-Saúde          | Projeto contribui com respostas e evidências | NIAR-Saúde    |

A equipe do projeto não deve alterar silenciosamente julgamentos, enquadramentos ou registros exclusivos do NIAR-Saúde.

Quando a colaboração ocorrer por pull request ou edição direta, as alterações devem ser revisadas e consolidadas pelo NIAR-Saúde antes da incorporação à versão validada.

---

## Relação com a avaliação técnica

A conclusão da validação documental permite iniciar ou organizar a avaliação técnica, mas não implica que:

- os artefatos sejam suficientes;
- as análises estejam completas;
- a tarefa esteja conforme;
- os riscos sejam aceitáveis;
- o sistema possa ser implantado.

As pendências identificadas nesta fase devem orientar:

- produção ou atualização de artefatos;
- análises adicionais;
- entrevistas;
- verificações de rastreabilidade;
- avaliação por dimensão;
- eventual escalonamento institucional.

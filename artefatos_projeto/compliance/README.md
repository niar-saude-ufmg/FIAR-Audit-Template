# Artefatos de Conformidade e Proteção de Dados

Esta pasta reúne documentos produzidos ou aprovados pelas áreas institucionais competentes relacionados a obrigações legais, regulatórias, éticas e de proteção de dados aplicáveis à Tarefa de IA.

A inclusão de um documento nesta pasta não significa, por si só, que:

- todas as obrigações legais tenham sido atendidas;
- o documento seja suficiente para o Contexto de Uso;
- a análise esteja atualizada;
- a tarefa esteja em conformidade;
- o risco institucional tenha sido aceito;
- a implantação tenha sido autorizada.

O NIAR-Saúde utiliza esses documentos como evidências no processo de avaliação, mas não substitui as competências das áreas jurídica, ética, de proteção de dados, segurança da informação ou regulação.

---

## 1. Estrutura

```text
compliance/
├── README.md
└── ripd/
    ├── README.md
    └── RIPD.docx
```

Outras subpastas podem ser criadas quando necessárias, por exemplo:

```text
compliance/
├── etica/
├── protecao_de_dados/
├── regulatorio/
├── termos_e_autorizacoes/
└── pareceres_institucionais/
```

Novas pastas somente devem ser adicionadas quando houver artefatos efetivamente aplicáveis ao projeto.

---

## 2. Responsabilidade institucional

Os documentos desta pasta devem indicar, sempre que aplicável:

* instituição responsável;
* área responsável;
* pessoa ou função responsável;
* data de emissão;
* versão;
* escopo;
* validade;
* projeto relacionado;
* Tarefa de IA relacionada;
* Contexto de Uso relacionado;
* condições ou restrições;
* forma de verificação.

A equipe técnica do projeto não deve se apresentar como autoridade responsável por aprovar documentos que dependam de uma instância institucional específica.

---

## 3. Relação com o FIAR-Saúde

O FIAR-Saúde pode verificar:

* se o documento existe;
* se está associado à tarefa avaliada;
* se corresponde à versão e ao Contexto de Uso;
* se está vigente;
* se seu escopo cobre o tratamento realizado;
* se existem condições ou restrições;
* se há inconsistências com outros artefatos;
* se há necessidade de atualização;
* se há pendências ou riscos relacionados.

O NIAR-Saúde não deve:

* emitir parecer jurídico em substituição à área competente;
* aprovar tratamento de dados;
* aprovar protocolo de pesquisa;
* declarar base legal sem evidência institucional;
* concluir que um RIPD é desnecessário sem avaliação competente;
* aceitar risco institucional em nome da instância responsável.

---

## 4. Tipos de artefatos

Podem ser armazenados nesta pasta, quando aplicáveis:

* Relatório de Impacto à Proteção de Dados Pessoais;
* parecer de comitê de ética;
* protocolo de pesquisa aprovado;
* termos de consentimento;
* termos de uso;
* termos de compartilhamento;
* acordos de tratamento de dados;
* autorizações institucionais;
* pareceres jurídicos;
* avaliações regulatórias;
* documentos de segurança da informação;
* registros de base legal;
* registros de legítimo interesse;
* políticas institucionais;
* documentos de governança de dados.

Não criar documentos fictícios apenas para completar a estrutura.

---

## 5. Identificação dos documentos

Cada artefato deve possuir, quando aplicável:

| Campo                  | Conteúdo esperado                               |
| ---------------------- | ------------------------------------------------ |
| Nome do documento      | Nome oficial                                     |
| Tipo                   | RIPD, parecer, autorização, protocolo ou outro |
| Versão                | Identificador da versão                         |
| Data                   | Data de emissão ou aprovação                  |
| Instituição          | Instituição responsável                       |
| Área responsável     | Área competente                                 |
| Responsável           | Pessoa, função ou instância                   |
| Escopo                 | Tratamento, projeto, tarefa ou sistema coberto   |
| Tarefa de IA           | Tarefa relacionada                               |
| Versão Avaliável     | Versão relacionada, quando aplicável           |
| Contexto de Uso        | Contexto coberto                                 |
| Validade               | Prazo ou condição de revisão                  |
| Restrições de acesso | Pública, interna, restrita ou sigilosa          |
| Localização          | Caminho no repositório ou ambiente controlado   |

---

## 6. Documentos que não podem ser armazenados no Git

Alguns documentos podem conter:

* dados pessoais;
* dados pessoais sensíveis;
* segredos comerciais;
* informações de segurança;
* pareceres jurídicos restritos;
* assinaturas;
* identificadores;
* informações institucionais confidenciais.

Quando o documento não puder ser incluído no repositório, registrar apenas:

```text
Documento existente, mantido em ambiente institucional controlado.

Responsável:
Versão:
Data:
Localização controlada:
Procedimento de acesso pelo NIAR-Saúde:
Restrições:
```

Não inserir cópias não autorizadas no histórico do Git.

---

## 7. Versionamento e atualização

Os documentos devem ser revistos quando houver mudança relevante em:

* finalidade do tratamento;
* categorias de dados;
* fontes dos dados;
* população;
* compartilhamento;
* responsáveis pelo tratamento;
* sistema ou infraestrutura;
* Contexto de Uso;
* modelo ou funcionalidade;
* processo decisório;
* riscos;
* controles;
* base legal;
* requisito regulatório;
* incidente;
* condição institucional.

A necessidade de atualização deve ser confirmada com a área competente.

---

## 8. Estados dos artefatos

Podem ser utilizados:

* `Em elaboração`
* `Em revisão pela área competente`
* `Aprovado`
* `Aprovado com condições`
* `Vigente`
* `Requer atualização`
* `Substituído`
* `Expirado`
* `Não aplicável — justificativa da área competente`
* `Não disponível para armazenamento no repositório`

Esses estados não equivalem a resultado de conformidade do FIAR-Saúde.

---

## 9. Pendências

Quando faltar informação ou documento, registrar em:

```text
documentacao_projeto/registro_de_pendencias.md
```

Utilizar, conforme aplicável:

```text
[INFORMAÇÃO PENDENTE — preencher pelo projeto]

[ANÁLISE PENDENTE — não inferível a partir dos documentos fornecidos]

[INCONSISTÊNCIA IDENTIFICADA — verificar entre os artefatos]

[DECISÃO INSTITUCIONAL PENDENTE — requer análise da instância competente]
```

---

## 10. Distinção entre evidência e decisão

Um documento de conformidade pode servir como evidência para a avaliação.

Entretanto:

* aprovação ética não equivale a validação clínica;
* aprovação ética não substitui análise de proteção de dados;
* RIPD não substitui avaliação de segurança;
* base legal não determina que todo uso seja adequado;
* autorização de acesso não equivale a autorização de implantação;
* parecer técnico não substitui decisão institucional;
* ausência de exigência formal não significa ausência de risco.

Cada documento deve ser interpretado dentro de seu escopo e competência.

---


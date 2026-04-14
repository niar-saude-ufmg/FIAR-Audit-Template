# FIAR-Audit-Template

Template de repositório para aplicação do **FIAR – Framework de Auditoria de IA Responsável em Saúde**.

Este repositório fornece a estrutura básica para documentar um sistema de IA, coletar artefatos técnicos e realizar a avaliação de auditoria.

---

# Como iniciar uma auditoria

1. Clique em **Use this template** neste repositório.
2. Crie um novo repositório para o sistema que será auditado.
3. Preencha a **Documentação Inicial do Projeto**.
4. Inclua os **artefatos do projeto** (data card, model card, relatórios técnicos).
5. Realize as **avaliações do auditor** para cada dimensão de Responsible AI.
6. Produza o **relatório final de auditoria**.

---

## Nomeando repositórios de auditoria

Recomenda-se utilizar o seguinte padrão para repositórios criados a partir deste template:

fiar-audit-nome-do-sistema

Exemplos:

fiar-audit-predicao-dengue  
fiar-audit-triagem-covid  

---

## Papéis no processo de auditoria

O processo de auditoria FIAR envolve dois papéis principais:

**Equipe do projeto (desenvolvedores ou responsáveis pelo sistema de IA)**  
Responsável por fornecer a documentação e os artefatos técnicos do sistema.

Isso inclui:

- documentação inicial do projeto
- data cards e model cards
- relatórios técnicos produzidos pela equipe
- evidências utilizadas na auditoria

Esses documentos são armazenados nas pastas:

- `documentacao_projeto/`
- `artefatos_projeto/`

**Equipe de auditoria (NIAR)**  
Responsável por avaliar o sistema com base nos artefatos fornecidos pelo projeto.

Os auditores produzem avaliações independentes para cada dimensão de Responsible AI.

Essas avaliações são armazenadas na pasta:

- `avaliacao_auditor/`
- `auditoria_final`

---

# Estrutura do repositório

```
documentacao_projeto/
documentacao_inicial_projeto.docx

artefatos_projeto/
data_card.docx
model_card.docx
relatorio_justica.docx
relatorio_explicabilidade.docx
relatorio_auditabilidade.docx

avaliacao_auditor/
avaliacao_justica.docx
avaliacao_explicabilidade.docx
avaliacao_auditabilidade.docx
avaliacao_privacidade.docx
avaliacao_governanca.docx

auditoria_final/
relatorio_final_auditoria.docx

```

Os documentos acima devem ser preenchidos utilizando os templates disponibilizados na seção abaixo.

---

# Templates (Google Docs)

Os templates abaixo são mantidos em **Google Docs** para facilitar edição colaborativa.

Ao acessar o link, será criada automaticamente **uma cópia editável no seu Google Drive**.

| Documento | Template |
|---|---|
Documentação Inicial do Projeto | https://docs.google.com/document/d/1413BabalmWr3lH9xqPT37aNQ3yF7m-PL-qYjOsisA7I/copy |
Relatório de Justiça  | link |
Relatório de Explicabilidade | link |
Relatório de Auditabilidade | link |
Relatório de Privacidade | link |
Relatório de Governança | link |

---

# Sobre o FIAR

O FIAR é um framework para documentação e auditoria de sistemas de IA em saúde pública, baseado em:

- evidências documentadas
- artefatos verificáveis
- avaliação por dimensões de Responsible AI
- relatórios de auditoria estruturados

Mais informações:

https://github.com/marisavas/FIAR-Saude/

# Pipeline de Geração do PDF (FIAR-Saúde)

Este documento define as regras técnicas de construção do relatório PDF consolidado da auditoria FIAR-Saúde.

---

## 1. Escopo do pipeline

O pipeline percorre a estrutura do repositório e consolida documentos das seguintes pastas:

1. documentacao_projeto/
2. artefatos_projeto/
3. avaliacao_niar/
4. auditoria_final/

---

## 2. Regras de inclusão

São incluídos no PDF apenas:

- arquivos `.pdf`
- arquivos `.docx` (convertidos automaticamente via LibreOffice)

Arquivos ignorados:

- arquivos temporários (`~$*.docx`)
- `.gitkeep`
- arquivos fora da estrutura FIAR
- duplicações fora do fluxo oficial

---

## 3. Ordem de consolidação

A ordem é sempre fixa e obrigatória:

1. documentacao_projeto/
2. artefatos_projeto/
3. avaliacao_niar/
4. auditoria_final/

Dentro de cada diretório, a ordenação segue a hierarquia de caminhos.

---

## 4. Conversão de arquivos

- `.docx` → convertido para PDF antes da consolidação
- conversão realizada via LibreOffice (`soffice` ou `libreoffice`)

---

## 5. Regras de agregação

- cada documento gera uma seção no PDF final
- sumário automático com páginas iniciais
- paginação contínua entre seções
- cabeçalho e rodapé aplicados em todas as páginas

---

## 6. Regras de exclusão

O pipeline deve ignorar:

- pastas fora da estrutura FIAR
- relatórios duplicados ou legados fora de `artefatos_projeto`
- arquivos temporários ou de sistema
- artefatos não referenciados no fluxo de auditoria

---

## 7. Saída

O PDF final deve ser salvo em:

```text
relatorio/relatorio-auditoria-fiar-saude.pdf
```

# Notas Arquiteturais do Sistema de PDF (FIAR-Saúde)

---

## Objetivo

O sistema de geração de PDF existe para consolidar uma instância completa de auditoria FIAR em um único artefato navegável.

---

## Decisões de design

### 1. Separação por camadas

A estrutura do PDF segue o fluxo FIAR:

- documentação do projeto (contexto)
- artefatos técnicos (evidência)
- avaliação NIAR (controle externo)
- auditoria final (decisão)

---

### 2. Ordem fixa

A ordem não é configurável porque:

- garante rastreabilidade
- evita manipulação da narrativa da auditoria
- mantém consistência entre versões

---

### 3. Conversão de documentos

A conversão `.docx → PDF` é usada para:

- padronizar visualização
- evitar dependência de software externo
- garantir compatibilidade de auditoria

---

## Limitações conhecidas

- dependência de LibreOffice instalado
- desempenho pode variar com volume de documentos
- ordenação depende da estrutura de diretórios

---

## Evoluções futuras

- suporte opcional a Markdown nativo
- geração incremental de PDF por versão avaliável
- validação automática de consistência FIAR antes do build

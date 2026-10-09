# FIAR-Saúde: modelo de repositório de projeto

Estrutura para registrar a avaliação de IA Responsável de um projeto pelo NIAR-Saúde.
Cada projeto acompanhado usa uma cópia privada deste repositório.

O FIAR-Saúde não é certificação, validação clínica nem autorização de implantação.

> Esta versão reflete a revisão simplificada do fluxo. A documentação metodológica
> (PDF e repositório FIAR-Saude) ainda será atualizada para acompanhá-la.

## Papéis

- Equipe do projeto: produz e mantém os artefatos e responde às perguntas do NIAR.
- NIAR-Saúde: delimita, avalia os requisitos e prepara o relatório ao Comitê. Não edita artefatos da equipe.
- Comitê Gestor: valida os relatórios e delibera sobre riscos e questões encaminhadas, inclusive condicionantes.

## Estrutura

```text
entrada/                 formulário de entrada (uma vez por projeto)
artefatos/               artefatos da equipe: Data Card, Model Card etc.
comunicacoes/            mensagens enviadas e respostas recebidas
ciclos/Cxx/              identificacao.md e avaliacao.md de cada ciclo
relatorios/              relatórios ao Comitê Gestor (RCG-xxx)
decisoes/                decisões do Comitê Gestor (DCG-xxx)
documentacao_metodologica/  guias, prompts e material de apoio
fiar_sync/               validação da estrutura
pdf/                     geração do PDF dos artefatos
```

A presença de um modelo ou pasta não torna o artefato obrigatório. Modelo vazio não é pendência.

## Como usar

1. Leia `documentacao_metodologica/guia_fluxo.md` (fluxo, resultados, pendências, relatório).
2. Para avaliar requisitos, use `documentacao_metodologica/guia_requisitos_avaliacao.md`.
3. Para um projeto novo: **Use this template**, crie um repositório privado e defina os acessos.
4. Para cada novo ciclo, copie `ciclos/C01/` para `ciclos/C02/` e assim por diante.
5. O histórico fica no Git; commits citam os IDs (D-xx, RCxx-Px, RCG-xxx, DCG-xxx) quando pertinente.

Validar a estrutura: `python3 fiar_sync/validate_structure.py`
Gerar o PDF: ver `pdf/README.md`.

## Segurança e confidencialidade

Instâncias de projetos devem ser privadas. Antes de adicionar um arquivo, verifique:

- se o armazenamento em Git foi autorizado;
- se contém dados pessoais ou sensíveis;
- se há informação protegida por contrato ou propriedade intelectual;
- se há credenciais, tokens ou chaves;
- se o histórico do Git pode preservar conteúdo que deveria ser removido.

Dados brutos sensíveis, credenciais e segredos não devem ser armazenados neste repositório.

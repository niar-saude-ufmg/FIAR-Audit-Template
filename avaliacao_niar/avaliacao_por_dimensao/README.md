# Avaliação por Dimensão

Esta pasta contém as avaliações individuais dos requisitos e a consolidação dos resultados de cada dimensão do FIAR-Saúde.

As sete dimensões são:

- Governança;
- Segurança;
- Privacidade;
- Responsabilização;
- Rastreabilidade;
- Justiça;
- Transparência.

## Avaliação dos requisitos

A avaliação técnica é realizada inicialmente por requisito.

Para cada requisito a ser analisado:

1. consultar sua formulação canônica na documentação vigente do FIAR-Saúde;
2. consultar as orientações operacionais em:
   `documentacao_metodologica/guia_requisitos_avaliacao.md`;
3. utilizar:
   `template_avaliacao_requisito.md`;
4. determinar a aplicabilidade antes da análise das evidências;
5. registrar somente evidências efetivamente verificadas no ciclo;
6. registrar os mecanismos de verificação efetivamente utilizados;
7. analisar suficiência, consistência, rastreabilidade e contextualização;
8. registrar achados, limitações, pendências, inconsistências e eventual sinal de governança quando sustentados pela análise.

Os arquivos preenchidos devem utilizar o identificador canônico do requisito, por exemplo:

```text
governanca/GOV-01.md
governanca/GOV-02.md

privacidade/PRI-01.md

justica/JUS-01.md
````

A existência de um requisito na documentação do FIAR-Saúde não implica que ele seja aplicável em qualquer avaliação. A aplicabilidade deve ser determinada no contexto da Tarefa de IA, da Versão Avaliável, do Contexto de Uso e da Trilha de Execução.

A existência de um template ou diretório também não implica obrigatoriedade de determinado artefato ou evidência.

## Consolidação por dimensão

Após a análise dos requisitos pertinentes, os resultados são consolidados por dimensão.

A consolidação considera:

* requisitos aplicáveis;
* requisitos não aplicáveis e respectivas justificativas;
* suficiência global das evidências;
* consistência entre requisitos e evidências;
* rastreabilidade dos resultados;
* contextualização dos resultados;
* pendências e inconsistências relevantes;
* sinais de governança.

A dimensão não recebe nível de maturidade próprio.

A consolidação não resulta de soma, média, percentual ou regra de maioria.

O resultado da dimensão deve decorrer de análise contextual dos requisitos aplicáveis e das evidências que os sustentam.

A consolidação por dimensão deve preservar a rastreabilidade até as avaliações individuais dos requisitos.

Ela não deve:

* reclassificar automaticamente ausência de evidência como Não Conformidade;
* eliminar pendências ou inconsistências registradas nas avaliações individuais;
* substituir a análise dos requisitos por uma contagem de resultados;
* inferir maturidade do projeto;
* extrapolar conclusões para requisitos ou dimensões não avaliados.

## Templates

Para avaliação individual de requisito:

[`template_avaliacao_requisito.md`](template_avaliacao_requisito.md)

Para consolidação da dimensão:

[`template_avaliacao_dimensao.md`](template_avaliacao_dimensao.md)

## Guia operacional

A interpretação operacional dos requisitos está disponível em:

`documentacao_metodologica/guia_requisitos_avaliacao.md`


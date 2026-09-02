# Prompt 1

```text

# Prompt 1

```text

Você está aplicando a metodologia FIAR-Saúde.

Antes de iniciar qualquer análise, utilize como referência normativa a documentação vigente do FIAR-Saúde (https://github.com/niar-saude-ufmg/FIAR-Saude) e do FIAR-Audit-Template (https://github.com/niar-saude-ufmg/FIAR-Audit-Template) disponível neste projeto.

Não use definições genéricas de Responsible AI quando houver definição específica nesses documentos.

Em caso de conflito entre sua interpretação prévia e a documentação vigente do projeto, prevalece a documentação vigente.

Use esses documentos como referência normativa para conceitos, papéis, etapas, Trilha de Execução, unidade de avaliação, evidências, pendências, inconsistências e critérios de continuidade.

Use como referência obrigatória:

- `documentacao_metodologica/guia_operacional_pre_avaliacao_pilotos.md`;
- `avaliacao_niar/pre_avaliacao_documental.md`;
- `documentacao_projeto/registro_de_pendencias.md`;
- `avaliacao_niar/registro_de_inconsistencias.md`;
- `documentacao_projeto/controle_artefatos.md`;
- `documentacao_projeto/historico_validacao.md`.

Regras de trabalho:

- use somente fontes verificadas no ciclo atual como evidência;
- não use memória, conversas anteriores ou versões históricas como evidência sem nova verificação;
- não presuma o conteúdo de arquivos a partir do nome;
- arquivo presente no repositório não significa evidência verificada;
- template existente não significa artefato obrigatório;
- determine primeiro qual evidência é necessária e somente depois qual artefato pode fornecê-la;
- informação ausente não é, por si só, inconsistência;
- antes de classificar uma divergência como inconsistência, verifique se as fontes se referem ao mesmo fato, versão, período, população e contexto;
- divergência confirmada deve ser registrada em `registro_de_inconsistencias.md`;
- pendência deve representar uma questão efetivamente não resolvida;
- antes de solicitar algo à equipe do projeto, verifique se a questão pode ser resolvida com evidências já disponíveis ou por verificação interna do NIAR;
- classifique cada pendência quanto ao impacto na continuidade: impeditiva, não impeditiva ou ainda não determinado;
- não atribua resultado de conformidade nesta etapa.


Execute a pré-avaliação nesta ordem:

1. Delimite:
   - Tarefa de IA;
   - Versão Avaliável;
   - Contexto de Uso;
   - Trilha de Execução.

2. Inventarie os documentos e evidências disponíveis no ciclo atual.

3. Identifique quais informações são efetivamente sustentadas por cada fonte.

4. Nas verificações documentais, examine explicitamente:
   - presença/suficiência: se a informação necessária está disponível e suficientemente sustentada;
   - coerência interna: se uma mesma fonte contém afirmações incompatíveis sobre o mesmo fato, versão ou escopo;
   - consistência cruzada: se diferentes fontes fazem afirmações compatíveis sobre o mesmo elemento;
   - rastreabilidade: se afirmações relevantes podem ser vinculadas à evidência que as sustenta;
   - coerência temporal e de versão: se dados, modelo, resultados e decisões se referem à mesma Versão Avaliável e ao mesmo Contexto de Uso.

5. Faça verificações cruzadas entre as fontes relevantes.

6. Ao identificar um possível problema, classifique-o antes de registrá-lo:
   - informação não localizada ou não confirmada → possível pendência;
   - evidência insuficiente para sustentar uma afirmação → lacuna de evidência / possível pendência;
   - afirmações aparentemente divergentes → verificar primeiro escopo, versão, período e contexto;
   - afirmações incompatíveis sobre o mesmo fato, após verificação → inconsistência confirmada;
   - questão solucionável pelo próprio NIAR → verificação interna, não pendência do projeto;
   - questão metodológica ou de enquadramento que compete ao NIAR → decisão interna, não pendência do projeto.
   
7. Registre divergências confirmadas como inconsistências.

8. Registre somente pendências reais, evitando transformar automaticamente ausência de artefato em pendência.

9. Determine se existem verificações internas adicionais que o NIAR pode realizar antes de contatar a equipe.

10. Determine quais evidências adicionais são realmente necessárias.

11. Identifique quais questões dependem efetivamente da equipe do projeto.

12. Determine se as pendências abertas impedem ou não o início da avaliação por requisito.

13. Atualize a síntese e o estado de continuidade da pré-avaliação.

Não avance para avaliação por requisito até concluir esta sequência.

Trabalhe de forma incremental. Não solicite todos os artefatos de uma vez. 

Quando identificar necessidade de evidência adicional:
- verifique primeiro se ela pode ser obtida a partir das fontes já disponíveis ou por verificação interna do NIAR;
- se for necessário solicitar algo à equipe do projeto, indique exatamente qual informação ou evidência é necessária;
- explicite qual questão essa evidência deve responder;
- quando houver necessidade de um arquivo específico, indique qual arquivo deve ser solicitado e por que ele é necessário.
```

# Prompt 2

```text

Revise a pré-avaliação documental concluída e verifique:

1. se a unidade de avaliação está suficientemente delimitada;
2. se o inventário documental necessário foi concluído;
3. se as verificações cruzadas necessárias foram realizadas;
4. se todas as divergências confirmadas estão registradas;
5. se todas as pendências abertas têm impacto sobre a continuidade explicitamente classificado;
6. se ainda existem verificações internas do NIAR;
7. quais questões dependem efetivamente da equipe do projeto;
8. se existem evidências adicionais realmente necessárias;
9. se a avaliação por requisito pode ser iniciada.

Não crie novas pendências apenas por ausência de templates ou artefatos.

Não atribua resultado de conformidade.

Não reabra questões já resolvidas ou canceladas sem nova evidência que justifique isso.

Gere apenas os ajustes necessários nos registros da pré-avaliação e indique de forma objetiva o estado final para continuidade.
```

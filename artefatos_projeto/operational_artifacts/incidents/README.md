# Registros de Incidentes

Esta pasta reúne registros de incidentes relacionados à Tarefa de IA, aos dados, ao modelo, à integração, à infraestrutura ou ao Contexto de Uso.

O registro de incidente deve ser factual, rastreável e preservado, inclusive após a resolução.

---

## 1. O que deve ser registrado

Pode constituir incidente:

- dano ou risco de dano;
- resultado incorreto relevante;
- uso fora do escopo;
- falha de integração;
- indisponibilidade;
- degradação material;
- exposição de dados;
- acesso não autorizado;
- corrupção de dados;
- implantação de versão incorreta;
- violação de condicionante;
- ausência de supervisão;
- automação indevida;
- falha no processo de contestação;
- alerta não tratado;
- erro repetitivo;
- mudança não autorizada.

Não limitar incidentes apenas a falhas de segurança da informação.

---

## 2. Estrutura dos arquivos

Utilizar:

```text
incident_record_template.md
````

Criar um arquivo por incidente:

```text
INC-OP-001-descricao-resumida.md
INC-OP-002-descricao-resumida.md
```

Não reutilizar identificadores.

---

## 3. Severidade

A classificação deve seguir critérios institucionais quando existentes.

Na ausência de escala institucional, pode-se utilizar provisoriamente:

* baixa;
* moderada;
* alta;
* crítica.

A classificação deve considerar:

* pessoas afetadas;
* gravidade do impacto;
* duração;
* reversibilidade;
* exposição de dados;
* impacto assistencial;
* impacto operacional;
* abrangência;
* recorrência;
* risco institucional.

A classificação técnica não substitui decisão institucional.

---

## 4. Etapas

O tratamento deve registrar:

1. detecção;
2. contenção;
3. comunicação;
4. investigação;
5. identificação de causa;
6. correção;
7. prevenção;
8. validação da correção;
9. encerramento;
10. revisão posterior.

---

## 5. Preservação

Não apagar:

* descrição original;
* versões afetadas;
* evidências;
* decisões;
* ações;
* responsáveis;
* prazos;
* limitações;
* registros de comunicação.

Correções devem ser adicionadas por nova versão do documento.

---

## 6. Relação com outros registros

Um incidente pode exigir:

* registro de mudança;
* decisão técnica;
* atualização de Data Card;
* atualização de Model Card;
* atualização de RIPD;
* atualização de análise de segurança;
* nova avaliação;
* decisão institucional;
* revisão periódica;
* suspensão ou restrição.

---

## 7. Confidencialidade

O registro no Git não deve conter:

* nomes de pacientes;
* identificadores;
* dados clínicos individuais;
* credenciais;
* vulnerabilidades exploráveis;
* informações protegidas.

Quando necessário, manter a evidência em ambiente controlado e registrar apenas
sua referência.

---

## 8. Comunicação

O incidente deve indicar quem foi comunicado:

* equipe técnica;
* responsável institucional;
* segurança da informação;
* proteção de dados;
* comitê de ética;
* NIAR-Saúde;
* instância institucional competente;
* usuários;
* titulares;
* autoridade competente, quando aplicável.

Não presumir comunicação realizada sem evidência.


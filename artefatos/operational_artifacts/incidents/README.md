# Registros de Incidentes

Esta pasta reúne registros de incidentes relacionados à Tarefa de IA, aos dados, ao modelo, à integração, à infraestrutura ou ao Contexto de Uso.

Quando houver incidente registrado, o registro deve ser factual, rastreável e preservado, inclusive após a resolução.

---

## 1. Eventos que podem constituir incidente

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

Quando houver incidente aplicável ao escopo desta pasta, pode ser utilizado:

```text
incident_record_template.md
```

Recomenda-se manter um arquivo por incidente, com identificador próprio, por exemplo:

```text
INC-OP-001-descricao-resumida.md
INC-OP-002-descricao-resumida.md
```

Não reutilizar identificadores.

---

## 3. Severidade

Quando houver classificação de severidade, devem ser priorizados os critérios institucionais vigentes, quando existentes.

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

O tratamento do incidente deve registrar, quando aplicável, as etapas relevantes do seu ciclo, que podem incluir:

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

Quando houver necessidade de comunicação, o registro do incidente deve indicar, quando aplicável, as partes comunicadas, que podem incluir:

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

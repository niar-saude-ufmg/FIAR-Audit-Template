# Passo 7c e 7d: campo Trilha e marcadores do NIAR nos artefatos; referências a caminhos antigos.
import json, pathlib, re, sys
R = pathlib.Path(".")
def edit(p, pairs):
    f = R / p
    t = f.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in t:
            sys.exit(f"ERRO: trecho não encontrado em {p}: {old[:60]!r}")
        t = t.replace(old, new)
    f.write_text(t, encoding="utf-8")
    print("ok", p)

MARC = "[ENQUADRAMENTO PENDENTE — validar pelo NIAR-Saúde]"
PEND_OLD = "documentacao_projeto/registro_de_pendencias.md"
PEND_NEW = "ciclos/Cxx/avaliacao.md (pendências da avaliação, registradas pelo NIAR-Saúde)"

# 7c: julgamentos do NIAR dentro de artefatos da equipe
edit("artefatos/consolidated_iar_report/consolidated_report_v1.md", [(f"| Trilha                | {MARC} |", "| Trilha                |  |")])
edit("artefatos/explainability_reports/explainability_report_inicial.md", [(f"| Trilha                | {MARC} |", "| Trilha                |  |")])
edit("artefatos/operational_artifacts/incidents/incident_record_template.md",
     [(f"| Nova Versão Avaliável necessária | {MARC} |", "| Nova Versão Avaliável necessária (proposta da equipe; o NIAR define o tratamento) |  |")])
edit("artefatos/operational_artifacts/version_history/version_change_record_template.md",
     [(f"Mudança relevante\n\n{MARC}\n", "Mudança relevante\n"),
      (f"### Classificação\n\n{MARC}\n", "### Classificação\n\nProposta da equipe. O tratamento da mudança é definido pelo NIAR-Saúde.\n")])

# 7d: referências a caminhos antigos dentro de artefatos/
for p in ["artefatos/compliance/ripd/README.md", "artefatos/compliance/README.md",
          "artefatos/operational_artifacts/README.md", "artefatos/explainability_reports/explainability_report_inicial.md"]:
    edit(p, [(PEND_OLD, PEND_NEW)])
edit("artefatos/consolidated_iar_report/consolidated_report_v1.md", [
    (PEND_OLD, PEND_NEW),
    ("avaliacao_niar/registro_de_inconsistencias.md", "ciclos/Cxx/avaliacao.md (inconsistências, registradas pelo NIAR-Saúde)"),
    ("artefatos_projeto/decision_records/", "artefatos/decision_records/")])
edit("artefatos/README.md", [("```text\nartefatos_projeto/\n", "```text\nartefatos/\n")])
edit("artefatos/accountability/README.md", [
    ("* `documentacao_projeto/formulario_entrada.md`;\n* `documentacao_projeto/identificacao_avaliacao.md`;",
     "* `entrada/formulario_entrada.md`;\n* `ciclos/Cxx/identificacao.md`;"),
    ("registradas separadamente em `decisao_institucional/`.", "registradas separadamente em `decisoes/`.")])

# 7d: pdf
roots_old = """const orderedRoots = [
  'documentacao_projeto',
  'artefatos_projeto',
  'avaliacao_niar',
  'decisao_institucional',
  'auditoria_final'
];"""
roots_new = """const orderedRoots = [
  'entrada',
  'artefatos',
  'ciclos',
  'relatorios',
  'decisoes'
];"""
edit("pdf/scripts/build-document.mjs", [
    (roots_old, roots_new),
    ("normalized.startsWith('documentacao_projeto/')", "normalized.startsWith('entrada/')"),
    ("section: 'Documentação do projeto'", "section: 'Entrada do projeto'"),
    ("normalized.startsWith('artefatos_projeto/operational_artifacts/')", "normalized.startsWith('artefatos/operational_artifacts/')"),
    ("normalized.startsWith('artefatos_projeto/')", "normalized.startsWith('artefatos/')"),
    ("normalized.startsWith('avaliacao_niar/')", "normalized.startsWith('ciclos/')"),
    ("normalized.startsWith('decisao_institucional/')", "normalized.startsWith('decisoes/')"),
    ("section: 'Decisões institucionais'", "section: 'Decisões do Comitê Gestor'"),
    ("normalized.startsWith('auditoria_final/')", "normalized.startsWith('relatorios/')"),
    ("section: 'Resultado consolidado do ciclo'", "section: 'Relatórios ao Comitê Gestor'")])
lista_old = "documentacao_projeto/\n2. artefatos_projeto/\n3. avaliacao_niar/\n4. auditoria_final/"
lista_new = "entrada/\n2. artefatos/\n3. ciclos/\n4. relatorios/\n5. decisoes/"
t = (R/"pdf/docs/pipeline_specification.md").read_text(encoding="utf-8")
assert t.count(lista_old) == 2
t = t.replace(lista_old, lista_new).replace("fora de `artefatos_projeto`", "fora de `artefatos`")
(R/"pdf/docs/pipeline_specification.md").write_text(t, encoding="utf-8"); print("ok pdf/docs/pipeline_specification.md")
edit("pdf/README.md", [("- documentacao_projeto/\n- artefatos_projeto/\n- avaliacao_niar/\n- auditoria_final/",
                        "- entrada/\n- artefatos/\n- ciclos/\n- relatorios/\n- decisoes/")])

# 7d: fiar_sync/fiar_structure.json
p = R/"fiar_sync/fiar_structure.json"
s = json.loads(p.read_text(encoding="utf-8"))
art = s["required_root_directories"]["artefatos_projeto"]
s["required_root_directories"] = {
    "entrada": {"required_files": ["formulario_entrada.md"]},
    "comunicacoes": {"required_files": ["README.md"]},
    "ciclos": {"required_directories": {"C01": {"required_files": ["identificacao.md", "avaliacao.md"]}}},
    "relatorios": {"required_files": ["RCG-001.md"]},
    "decisoes": {"required_files": ["DCG-001.md"]},
    "artefatos": art,
    "documentacao_metodologica": {"required_files": ["guia_fluxo.md", "guia_requisitos_avaliacao.md",
                                                     "prompts_avaliacao.md", "apoio_roteiro_entrevista.md"]},
    "fiar_sync": s["required_root_directories"]["fiar_sync"],
    "pdf": s["required_root_directories"]["pdf"]}
s["legacy_paths"] = {"directories": {"artefatos_projeto": "artefatos",
                                     "artefatos_operacionais": "artefatos/operational_artifacts"},
                     "files": {}}
p.write_text(json.dumps(s, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("ok", p)

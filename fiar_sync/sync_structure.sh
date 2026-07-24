#!/usr/bin/env bash

# Sincroniza a estrutura operacional do FIAR-Audit-Template.
#
# O script:
# - cria diretórios obrigatórios ausentes;
# - cria arquivos obrigatórios ausentes;
# - não sobrescreve arquivos existentes;
# - não migra automaticamente caminhos legados;
# - executa o validador ao final.
#
# Uso:
#   bash fiar_sync/sync_structure.sh
#
# Opções:
#   --dry-run     Mostra as ações sem alterar o repositório.
#   --no-validate Não executa a validação ao final.
#   --help        Exibe ajuda.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOSITORY_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SCHEMA_PATH="${SCRIPT_DIR}/fiar_structure.json"
VALIDATOR_PATH="${SCRIPT_DIR}/validate_structure.py"

DRY_RUN=false
RUN_VALIDATION=true
CREATED_DIRECTORIES=0
CREATED_FILES=0
SKIPPED_PATHS=0
ERRORS=0

usage() {
    cat <<'EOF'
Uso:
  bash fiar_sync/sync_structure.sh [opções]

Opções:
  --dry-run
      Mostra os diretórios e arquivos que seriam criados, sem alterar
      o repositório.

  --no-validate
      Não executa validate_structure.py ao final.

  --help
      Exibe esta mensagem.

O script cria apenas caminhos obrigatórios ausentes.

Ele não:
  - sobrescreve arquivos;
  - move arquivos;
  - renomeia caminhos legados;
  - remove arquivos;
  - preenche conteúdo substantivo;
  - resolve pendências documentais.
EOF
}

log_info() {
    printf '[INFO] %s\n' "$1"
}

log_create() {
    printf '[CRIAR] %s\n' "$1"
}

log_skip() {
    printf '[MANTER] %s\n' "$1"
}

log_warning() {
    printf '[AVISO] %s\n' "$1" >&2
}

log_error() {
    printf '[ERRO] %s\n' "$1" >&2
}

for argument in "$@"; do
    case "${argument}" in
        --dry-run)
            DRY_RUN=true
            ;;
        --no-validate)
            RUN_VALIDATION=false
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            log_error "Opção desconhecida: ${argument}"
            usage
            exit 2
            ;;
    esac
done

if [[ ! -f "${SCHEMA_PATH}" ]]; then
    log_error "Arquivo de estrutura não encontrado: ${SCHEMA_PATH}"
    exit 2
fi

if [[ ! -f "${VALIDATOR_PATH}" ]]; then
    log_error "Validador não encontrado: ${VALIDATOR_PATH}"
    exit 2
fi

PYTHON_BIN=""

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    log_error "Python não encontrado."
    exit 2
fi

create_directory() {
    local relative_path="$1"
    local absolute_path="${REPOSITORY_ROOT}/${relative_path}"

    if [[ -d "${absolute_path}" ]]; then
        SKIPPED_PATHS=$((SKIPPED_PATHS + 1))
        log_skip "Diretório existente: ${relative_path}"
        return 0
    fi

    if [[ -e "${absolute_path}" ]]; then
        ERRORS=$((ERRORS + 1))
        log_error "O caminho existe, mas não é diretório: ${relative_path}"
        return 1
    fi

    log_create "Diretório: ${relative_path}"

    if [[ "${DRY_RUN}" == false ]]; then
        if ! mkdir -p "${absolute_path}"; then
            ERRORS=$((ERRORS + 1))
            log_error "Não foi possível criar o diretório: ${relative_path}"
            return 1
        fi
    fi

    CREATED_DIRECTORIES=$((CREATED_DIRECTORIES + 1))
}

create_file() {
    local relative_path="$1"
    local absolute_path="${REPOSITORY_ROOT}/${relative_path}"
    local parent_directory

    parent_directory="$(dirname "${relative_path}")"

    if [[ -f "${absolute_path}" ]]; then
        SKIPPED_PATHS=$((SKIPPED_PATHS + 1))
        log_skip "Arquivo existente: ${relative_path}"
        return 0
    fi

    if [[ -e "${absolute_path}" ]]; then
        ERRORS=$((ERRORS + 1))
        log_error "O caminho existe, mas não é arquivo: ${relative_path}"
        return 1
    fi

    create_directory "${parent_directory}"

    log_create "Arquivo: ${relative_path}"

    if [[ "${DRY_RUN}" == false ]]; then
        if ! touch "${absolute_path}"; then
            ERRORS=$((ERRORS + 1))
            log_error "Não foi possível criar o arquivo: ${relative_path}"
            return 1
        fi
    fi

    CREATED_FILES=$((CREATED_FILES + 1))
}

collect_required_paths() {
    "${PYTHON_BIN}" - "${SCHEMA_PATH}" "${REPOSITORY_ROOT}" <<'PYTHON'
import json
import sys
from pathlib import Path, PurePosixPath

schema_path = Path(sys.argv[1])
repository_root = Path(sys.argv[2])

with schema_path.open("r", encoding="utf-8") as file:
    schema = json.load(file)

validation = schema.get("validation", {})
allow_legacy = validation.get(
    "allow_legacy_paths_during_transition",
    False,
)

legacy_paths = schema.get("legacy_paths", {})
legacy_directory_map = legacy_paths.get("directories", {})
legacy_file_map = legacy_paths.get("files", {})

emitted: set[tuple[str, str]] = set()


def normalize(path: str) -> str:
    value = path.replace("\\", "/").strip()

    while value.startswith("./"):
        value = value[2:]

    return value.rstrip("/")


def emit(path_type: str, path: PurePosixPath) -> None:
    key = (path_type, path.as_posix())

    if key in emitted:
        return

    emitted.add(key)
    print(f"{path_type}\t{path.as_posix()}")


def existing_legacy_directories(
    canonical_relative: PurePosixPath,
    node: dict,
) -> list[Path]:
    candidates: list[Path] = []

    for directory_name in node.get(
        "accepted_legacy_directories",
        [],
    ):
        candidates.append(
            repository_root
            / canonical_relative.parent
            / directory_name
        )

    canonical_normalized = normalize(
        canonical_relative.as_posix()
    )

    for legacy_path, canonical_path in legacy_directory_map.items():
        if normalize(canonical_path) == canonical_normalized:
            candidates.append(
                repository_root / normalize(legacy_path)
            )

    return [
        candidate
        for candidate in candidates
        if candidate.is_dir()
    ]


def existing_legacy_files(
    canonical_relative: PurePosixPath,
    actual_directory: Path,
    node: dict,
) -> list[Path]:
    candidates: list[Path] = []

    for legacy_filename in node.get(
        "accepted_legacy_files",
        [],
    ):
        candidates.append(
            actual_directory / legacy_filename
        )

    canonical_normalized = normalize(
        canonical_relative.as_posix()
    )

    for legacy_path, canonical_path in legacy_file_map.items():
        if normalize(canonical_path) == canonical_normalized:
            candidates.append(
                repository_root / normalize(legacy_path)
            )

    return [
        candidate
        for candidate in candidates
        if candidate.is_file()
    ]


def walk_directory(
    canonical_relative: PurePosixPath,
    node: dict,
) -> None:
    canonical_absolute = repository_root / canonical_relative

    if canonical_absolute.is_dir():
        actual_directory = canonical_absolute
    else:
        legacy_directories = (
            existing_legacy_directories(
                canonical_relative,
                node,
            )
            if allow_legacy
            else []
        )

        if legacy_directories:
            actual_directory = legacy_directories[0]
        else:
            emit("DIR", canonical_relative)
            actual_directory = canonical_absolute

    for filename in node.get("required_files", []):
        canonical_file_relative = (
            canonical_relative / filename
        )
        canonical_file_absolute = (
            repository_root / canonical_file_relative
        )

        if canonical_file_absolute.is_file():
            continue

        legacy_files = (
            existing_legacy_files(
                canonical_file_relative,
                actual_directory,
                node,
            )
            if allow_legacy
            else []
        )

        if legacy_files:
            continue

        emit("DIR", canonical_relative)
        emit("FILE", canonical_file_relative)

    for child_name, child_node in node.get(
        "required_directories",
        {},
    ).items():
        walk_directory(
            canonical_relative / child_name,
            child_node,
        )


for filename in schema.get("required_root_files", []):
    relative_path = PurePosixPath(filename)
    absolute_path = repository_root / relative_path

    if not absolute_path.is_file():
        emit("FILE", relative_path)

for directory_name, directory_node in schema.get(
    "required_root_directories",
    {},
).items():
    walk_directory(
        PurePosixPath(directory_name),
        directory_node,
    )
PYTHON
}


log_info "Raiz do repositório: ${REPOSITORY_ROOT}"
log_info "Esquema: ${SCHEMA_PATH}"

if [[ "${DRY_RUN}" == true ]]; then
    log_info "Modo de simulação ativado. Nenhum arquivo será alterado."
fi

while IFS=$'\t' read -r path_type relative_path; do
    if [[ -z "${path_type}" || -z "${relative_path}" ]]; then
        continue
    fi

    case "${path_type}" in
        DIR)
            create_directory "${relative_path}"
            ;;
        FILE)
            create_file "${relative_path}"
            ;;
        *)
            ERRORS=$((ERRORS + 1))
            log_error "Tipo de caminho desconhecido: ${path_type}"
            ;;
    esac
done < <(collect_required_paths)

printf '\nResumo da sincronização\n'
printf '  Diretórios a criar ou criados: %d\n' "${CREATED_DIRECTORIES}"
printf '  Arquivos a criar ou criados: %d\n' "${CREATED_FILES}"
printf '  Caminhos preservados: %d\n' "${SKIPPED_PATHS}"
printf '  Erros: %d\n' "${ERRORS}"

if [[ "${ERRORS}" -gt 0 ]]; then
    log_error "A sincronização terminou com erros."
    exit 1
fi

if [[ "${DRY_RUN}" == true ]]; then
    log_info "Simulação concluída."
    exit 0
fi

if [[ "${RUN_VALIDATION}" == true ]]; then
    printf '\n'
    log_info "Executando validação da estrutura."

    "${PYTHON_BIN}" "${VALIDATOR_PATH}" --root "${REPOSITORY_ROOT}"
    VALIDATION_STATUS=$?

    if [[ "${VALIDATION_STATUS}" -ne 0 ]]; then
        log_error "A estrutura foi sincronizada, mas a validação falhou."
        exit "${VALIDATION_STATUS}"
    fi
else
    log_warning "Validação final desativada por --no-validate."
fi

log_info "Sincronização concluída."
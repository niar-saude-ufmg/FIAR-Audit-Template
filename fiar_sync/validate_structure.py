#!/usr/bin/env python3
"""
Validador da estrutura do FIAR-Audit-Template.

O script verifica:

- arquivos e diretórios obrigatórios;
- estruturas aninhadas;
- arquivos opcionais;
- caminhos legados aceitos durante a transição;
- templates obrigatórios vazios;
- arquivos potencialmente sensíveis;
- consistência básica do arquivo fiar_structure.json.

Códigos de saída:
    0: estrutura válida, podendo conter avisos;
    1: estrutura inválida;
    2: erro de configuração ou execução.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_REPOSITORY_ROOT = SCRIPT_DIR.parent
DEFAULT_SCHEMA_PATH = SCRIPT_DIR / "fiar_structure.json"


@dataclass
class ValidationResult:
    """Resultado acumulado da validação."""

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    information: list[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_information(self, message: str) -> None:
        self.information.append(message)

    @property
    def is_valid(self) -> bool:
        return not self.errors


class SchemaError(ValueError):
    """Erro de estrutura ou conteúdo do arquivo de configuração."""


def load_json(path: Path) -> dict[str, Any]:
    """Carrega e valida superficialmente um arquivo JSON."""

    if not path.exists():
        raise SchemaError(f"Arquivo de estrutura não encontrado: {path}")

    if not path.is_file():
        raise SchemaError(f"O caminho da estrutura não é um arquivo: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise SchemaError(
            f"JSON inválido em {path}, linha {exc.lineno}, coluna {exc.colno}: "
            f"{exc.msg}"
        ) from exc
    except OSError as exc:
        raise SchemaError(f"Não foi possível ler {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise SchemaError("A raiz do fiar_structure.json deve ser um objeto JSON.")

    return data


def ensure_string_list(value: Any, field_name: str) -> list[str]:
    """Confirma que um campo é uma lista de strings."""

    if value is None:
        return []

    if not isinstance(value, list):
        raise SchemaError(f"'{field_name}' deve ser uma lista.")

    invalid_items = [item for item in value if not isinstance(item, str)]
    if invalid_items:
        raise SchemaError(
            f"'{field_name}' deve conter apenas strings. "
            f"Itens inválidos: {invalid_items!r}"
        )

    return value


def ensure_mapping(value: Any, field_name: str) -> dict[str, Any]:
    """Confirma que um campo é um objeto JSON."""

    if value is None:
        return {}

    if not isinstance(value, dict):
        raise SchemaError(f"'{field_name}' deve ser um objeto JSON.")

    return value


def normalize_relative_path(path: str) -> str:
    """Normaliza caminhos declarados no JSON para comparação."""

    normalized = path.replace("\\", "/").strip()

    while normalized.startswith("./"):
        normalized = normalized[2:]

    return normalized.rstrip("/")


def display_path(path: Path, repository_root: Path) -> str:
    """Retorna caminho relativo legível."""

    try:
        return path.relative_to(repository_root).as_posix()
    except ValueError:
        return path.as_posix()


def is_effectively_empty(path: Path) -> bool:
    """
    Considera vazio um arquivo sem conteúdo útil.

    Espaços em branco e quebras de linha não contam como conteúdo.
    Arquivos binários não são tratados como vazios por este método.
    """

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    except OSError:
        return False

    return not content.strip()


def validate_required_file(
    *,
    expected_path: Path,
    repository_root: Path,
    result: ValidationResult,
    fail_on_empty: bool,
    legacy_candidates: Iterable[Path] = (),
    allow_legacy: bool,
    warn_on_legacy: bool,
) -> bool:
    """
    Valida um arquivo obrigatório.

    Retorna True quando o arquivo canônico ou uma alternativa legada aceita
    estiver disponível.
    """

    if expected_path.exists():
        if not expected_path.is_file():
            result.add_error(
                f"Era esperado um arquivo, mas foi encontrado outro tipo de "
                f"objeto: {display_path(expected_path, repository_root)}"
            )
            return False

        if fail_on_empty and is_effectively_empty(expected_path):
            result.add_error(
                f"Template obrigatório vazio: "
                f"{display_path(expected_path, repository_root)}"
            )
            return False

        return True

    if allow_legacy:
        for legacy_path in legacy_candidates:
            if not legacy_path.exists() or not legacy_path.is_file():
                continue

            if fail_on_empty and is_effectively_empty(legacy_path):
                result.add_error(
                    f"Arquivo legado aceito, mas vazio: "
                    f"{display_path(legacy_path, repository_root)}"
                )
                return False

            if warn_on_legacy:
                result.add_warning(
                    "Caminho legado em uso: "
                    f"{display_path(legacy_path, repository_root)}. "
                    "Destino canônico: "
                    f"{display_path(expected_path, repository_root)}."
                )

            return True

    result.add_error(
        f"Arquivo obrigatório ausente: "
        f"{display_path(expected_path, repository_root)}"
    )
    return False


def validate_optional_file(
    *,
    path: Path,
    repository_root: Path,
    result: ValidationResult,
) -> None:
    """Verifica apenas se um caminho opcional existente é realmente arquivo."""

    if path.exists() and not path.is_file():
        result.add_warning(
            f"Caminho opcional existe, mas não é arquivo: "
            f"{display_path(path, repository_root)}"
        )


def resolve_legacy_file_candidates(
    *,
    canonical_file: Path,
    repository_root: Path,
    local_legacy_files: list[str],
    legacy_file_map: dict[str, str],
) -> list[Path]:
    """Obtém os arquivos legados que podem satisfazer um arquivo canônico."""

    candidates: list[Path] = []

    for filename in local_legacy_files:
        candidates.append(canonical_file.parent / filename)

    canonical_relative = normalize_relative_path(
        display_path(canonical_file, repository_root)
    )

    for legacy_path, canonical_path in legacy_file_map.items():
        if normalize_relative_path(canonical_path) == canonical_relative:
            candidates.append(
                repository_root / normalize_relative_path(legacy_path)
            )

    return unique_paths(candidates)


def resolve_legacy_directory_candidates(
    *,
    canonical_directory: Path,
    repository_root: Path,
    local_legacy_directories: list[str],
    legacy_directory_map: dict[str, str],
) -> list[Path]:
    """Obtém diretórios legados que podem substituir um diretório canônico."""

    candidates: list[Path] = []

    for directory_name in local_legacy_directories:
        candidates.append(canonical_directory.parent / directory_name)

    canonical_relative = normalize_relative_path(
        display_path(canonical_directory, repository_root)
    )

    for legacy_path, canonical_path in legacy_directory_map.items():
        if normalize_relative_path(canonical_path) == canonical_relative:
            candidates.append(
                repository_root / normalize_relative_path(legacy_path)
            )

    return unique_paths(candidates)


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    """Remove caminhos duplicados preservando a ordem."""

    output: list[Path] = []
    seen: set[str] = set()

    for path in paths:
        key = str(path.resolve(strict=False))
        if key not in seen:
            output.append(path)
            seen.add(key)

    return output


def choose_directory_path(
    *,
    canonical_directory: Path,
    repository_root: Path,
    result: ValidationResult,
    legacy_candidates: list[Path],
    allow_legacy: bool,
    warn_on_legacy: bool,
) -> Path | None:
    """
    Escolhe o diretório canônico ou um diretório legado aceito.

    O diretório escolhido será usado para validar os arquivos internos.
    """

    if canonical_directory.exists():
        if not canonical_directory.is_dir():
            result.add_error(
                f"Era esperado um diretório, mas foi encontrado outro tipo de "
                f"objeto: {display_path(canonical_directory, repository_root)}"
            )
            return None

        return canonical_directory

    if allow_legacy:
        for legacy_directory in legacy_candidates:
            if not legacy_directory.exists() or not legacy_directory.is_dir():
                continue

            if warn_on_legacy:
                result.add_warning(
                    "Diretório legado em uso: "
                    f"{display_path(legacy_directory, repository_root)}. "
                    "Destino canônico: "
                    f"{display_path(canonical_directory, repository_root)}."
                )

            return legacy_directory

    result.add_error(
        f"Diretório obrigatório ausente: "
        f"{display_path(canonical_directory, repository_root)}"
    )
    return None


def validate_directory_node(
    *,
    canonical_directory: Path,
    node: dict[str, Any],
    repository_root: Path,
    result: ValidationResult,
    validation_options: dict[str, Any],
    legacy_directory_map: dict[str, str],
    legacy_file_map: dict[str, str],
) -> None:
    """Valida recursivamente um diretório descrito no esquema."""

    local_legacy_directories = ensure_string_list(
        node.get("accepted_legacy_directories"),
        (
            f"{display_path(canonical_directory, repository_root)}."
            "accepted_legacy_directories"
        ),
    )

    legacy_directory_candidates = resolve_legacy_directory_candidates(
        canonical_directory=canonical_directory,
        repository_root=repository_root,
        local_legacy_directories=local_legacy_directories,
        legacy_directory_map=legacy_directory_map,
    )

    allow_legacy = bool(
        validation_options.get("allow_legacy_paths_during_transition", False)
    )
    warn_on_legacy = bool(
        validation_options.get("warn_on_legacy_path", True)
    )
    fail_on_empty = bool(
        validation_options.get("fail_on_empty_required_template", False)
    )

    actual_directory = choose_directory_path(
        canonical_directory=canonical_directory,
        repository_root=repository_root,
        result=result,
        legacy_candidates=legacy_directory_candidates,
        allow_legacy=allow_legacy,
        warn_on_legacy=warn_on_legacy,
    )

    if actual_directory is None:
        return

    required_files = ensure_string_list(
        node.get("required_files"),
        f"{display_path(canonical_directory, repository_root)}.required_files",
    )

    optional_files = ensure_string_list(
        node.get("optional_files"),
        f"{display_path(canonical_directory, repository_root)}.optional_files",
    )

    accepted_legacy_files = ensure_string_list(
        node.get("accepted_legacy_files"),
        (
            f"{display_path(canonical_directory, repository_root)}."
            "accepted_legacy_files"
        ),
    )

    for required_filename in required_files:
        canonical_file = canonical_directory / required_filename

        local_legacy_files = accepted_legacy_files

        legacy_candidates = resolve_legacy_file_candidates(
            canonical_file=canonical_file,
            repository_root=repository_root,
            local_legacy_files=local_legacy_files,
            legacy_file_map=legacy_file_map,
        )

        # Quando o diretório inteiro é legado, também procuramos o arquivo
        # obrigatório dentro dele. Isso permite migração gradual de diretório
        # e nome do arquivo.
        if actual_directory != canonical_directory:
            legacy_candidates.insert(
                0,
                actual_directory / required_filename,
            )

            for legacy_filename in accepted_legacy_files:
                legacy_candidates.append(
                    actual_directory / legacy_filename
                )

        validate_required_file(
            expected_path=canonical_file,
            repository_root=repository_root,
            result=result,
            fail_on_empty=fail_on_empty,
            legacy_candidates=unique_paths(legacy_candidates),
            allow_legacy=allow_legacy,
            warn_on_legacy=warn_on_legacy,
        )

    for optional_filename in optional_files:
        validate_optional_file(
            path=actual_directory / optional_filename,
            repository_root=repository_root,
            result=result,
        )

    required_directories = ensure_mapping(
        node.get("required_directories"),
        (
            f"{display_path(canonical_directory, repository_root)}."
            "required_directories"
        ),
    )

    for child_name, child_node_raw in required_directories.items():
        if not isinstance(child_name, str):
            raise SchemaError(
                "Os nomes em 'required_directories' devem ser strings."
            )

        child_node = ensure_mapping(
            child_node_raw,
            (
                f"{display_path(canonical_directory, repository_root)}/"
                f"{child_name}"
            ),
        )

        canonical_child = canonical_directory / child_name

        # Se o diretório pai ainda está no caminho legado, a busca inicial do
        # filho deve ocorrer dentro do diretório real selecionado.
        if actual_directory != canonical_directory:
            actual_child_candidate = actual_directory / child_name

            if actual_child_candidate.exists():
                child_node = dict(child_node)
                inherited_legacy = ensure_string_list(
                    child_node.get("accepted_legacy_directories"),
                    (
                        f"{display_path(canonical_child, repository_root)}."
                        "accepted_legacy_directories"
                    ),
                )
                inherited_legacy.insert(0, child_name)
                child_node["accepted_legacy_directories"] = inherited_legacy

        validate_directory_node(
            canonical_directory=canonical_child,
            node=child_node,
            repository_root=repository_root,
            result=result,
            validation_options=validation_options,
            legacy_directory_map=legacy_directory_map,
            legacy_file_map=legacy_file_map,
        )


def validate_root_structure(
    *,
    schema: dict[str, Any],
    repository_root: Path,
    result: ValidationResult,
) -> None:
    """Valida arquivos e diretórios declarados na raiz."""

    validation_options = ensure_mapping(
        schema.get("validation"),
        "validation",
    )

    fail_on_empty = bool(
        validation_options.get("fail_on_empty_required_template", False)
    )
    allow_legacy = bool(
        validation_options.get("allow_legacy_paths_during_transition", False)
    )
    warn_on_legacy = bool(
        validation_options.get("warn_on_legacy_path", True)
    )

    legacy_paths = ensure_mapping(
        schema.get("legacy_paths"),
        "legacy_paths",
    )
    legacy_directory_map = ensure_mapping(
        legacy_paths.get("directories"),
        "legacy_paths.directories",
    )
    legacy_file_map = ensure_mapping(
        legacy_paths.get("files"),
        "legacy_paths.files",
    )

    required_root_files = ensure_string_list(
        schema.get("required_root_files"),
        "required_root_files",
    )

    for filename in required_root_files:
        canonical_file = repository_root / filename

        legacy_candidates = resolve_legacy_file_candidates(
            canonical_file=canonical_file,
            repository_root=repository_root,
            local_legacy_files=[],
            legacy_file_map=legacy_file_map,
        )

        validate_required_file(
            expected_path=canonical_file,
            repository_root=repository_root,
            result=result,
            fail_on_empty=fail_on_empty,
            legacy_candidates=legacy_candidates,
            allow_legacy=allow_legacy,
            warn_on_legacy=warn_on_legacy,
        )

    required_root_directories = ensure_mapping(
        schema.get("required_root_directories"),
        "required_root_directories",
    )

    for directory_name, node_raw in required_root_directories.items():
        if not isinstance(directory_name, str):
            raise SchemaError(
                "Os nomes em 'required_root_directories' devem ser strings."
            )

        node = ensure_mapping(
            node_raw,
            f"required_root_directories.{directory_name}",
        )

        validate_directory_node(
            canonical_directory=repository_root / directory_name,
            node=node,
            repository_root=repository_root,
            result=result,
            validation_options=validation_options,
            legacy_directory_map=legacy_directory_map,
            legacy_file_map=legacy_file_map,
        )

    optional_root_directories = ensure_string_list(
        schema.get("optional_root_directories"),
        "optional_root_directories",
    )

    for directory_name in optional_root_directories:
        path = repository_root / directory_name
        if path.exists() and not path.is_dir():
            result.add_warning(
                f"Caminho opcional de raiz existe, mas não é diretório: "
                f"{display_path(path, repository_root)}"
            )


def should_ignore_path(
    path: Path,
    repository_root: Path,
    ignored_paths: list[str],
) -> bool:
    """Indica se um caminho deve ser ignorado nas verificações adicionais."""

    relative = normalize_relative_path(display_path(path, repository_root))

    for ignored in ignored_paths:
        normalized_ignored = normalize_relative_path(ignored)

        if relative == normalized_ignored:
            return True

        if relative.startswith(f"{normalized_ignored}/"):
            return True

    return False


def scan_sensitive_files(
    *,
    repository_root: Path,
    result: ValidationResult,
    validation_options: dict[str, Any],
) -> None:
    """Procura arquivos cujo nome corresponde a padrões sensíveis."""

    if not bool(
        validation_options.get("warn_on_unexpected_sensitive_files", False)
    ):
        return

    patterns = ensure_string_list(
        validation_options.get("sensitive_file_patterns"),
        "validation.sensitive_file_patterns",
    )
    ignored_paths = ensure_string_list(
        validation_options.get("ignored_paths"),
        "validation.ignored_paths",
    )

    if not patterns:
        return

    for path in repository_root.rglob("*"):
        if not path.is_file():
            continue

        if should_ignore_path(path, repository_root, ignored_paths):
            continue

        relative = display_path(path, repository_root)
        filename = path.name

        if any(
            fnmatch.fnmatch(filename.lower(), pattern.lower())
            or fnmatch.fnmatch(relative.lower(), pattern.lower())
            for pattern in patterns
        ):
            result.add_warning(
                f"Arquivo potencialmente sensível identificado: {relative}. "
                "Verifique se sua inclusão no Git é autorizada."
            )


def validate_schema_metadata(
    schema: dict[str, Any],
    result: ValidationResult,
) -> None:
    """Valida metadados básicos do esquema."""

    schema_version = schema.get("schema_version")
    template_name = schema.get("template_name")

    if not isinstance(schema_version, str) or not schema_version.strip():
        result.add_error(
            "O campo 'schema_version' deve ser uma string não vazia."
        )

    if not isinstance(template_name, str) or not template_name.strip():
        result.add_error(
            "O campo 'template_name' deve ser uma string não vazia."
        )

    if isinstance(schema_version, str):
        result.add_information(f"Versão do esquema: {schema_version}")

    if isinstance(template_name, str):
        result.add_information(f"Template: {template_name}")


def print_section(title: str, items: list[str], marker: str) -> None:
    """Imprime uma seção do relatório."""

    if not items:
        return

    print(f"\n{title}")

    for item in items:
        print(f"  {marker} {item}")


def print_result(result: ValidationResult, repository_root: Path) -> None:
    """Imprime o relatório final."""

    print("Validação da estrutura FIAR-Saúde")
    print(f"Repositório: {repository_root}")

    print_section("Informações", result.information, "•")
    print_section("Avisos", result.warnings, "⚠")
    print_section("Erros", result.errors, "✖")

    print("\nResumo")
    print(f"  Erros: {len(result.errors)}")
    print(f"  Avisos: {len(result.warnings)}")

    if result.is_valid:
        print("\n✔ Estrutura válida.")
    else:
        print("\n✖ Estrutura inválida.")


def parse_arguments() -> argparse.Namespace:
    """Lê argumentos de linha de comando."""

    parser = argparse.ArgumentParser(
        description="Valida a estrutura do FIAR-Audit-Template."
    )

    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_REPOSITORY_ROOT,
        help=(
            "Raiz do repositório. "
            f"Padrão: {DEFAULT_REPOSITORY_ROOT}"
        ),
    )

    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA_PATH,
        help=(
            "Arquivo fiar_structure.json. "
            f"Padrão: {DEFAULT_SCHEMA_PATH}"
        ),
    )

    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Retorna erro quando houver qualquer aviso.",
    )

    return parser.parse_args()


def main() -> int:
    """Executa a validação."""

    arguments = parse_arguments()

    repository_root = arguments.root.resolve()
    schema_path = arguments.schema.resolve()

    if not repository_root.exists():
        print(
            f"Erro: raiz do repositório não encontrada: {repository_root}",
            file=sys.stderr,
        )
        return 2

    if not repository_root.is_dir():
        print(
            f"Erro: a raiz informada não é um diretório: {repository_root}",
            file=sys.stderr,
        )
        return 2

    try:
        schema = load_json(schema_path)
        result = ValidationResult()

        validate_schema_metadata(schema, result)

        validate_root_structure(
            schema=schema,
            repository_root=repository_root,
            result=result,
        )

        validation_options = ensure_mapping(
            schema.get("validation"),
            "validation",
        )

        scan_sensitive_files(
            repository_root=repository_root,
            result=result,
            validation_options=validation_options,
        )

    except SchemaError as exc:
        print(f"Erro de configuração: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Erro de sistema de arquivos: {exc}", file=sys.stderr)
        return 2

    print_result(result, repository_root)

    if result.errors:
        return 1

    if arguments.warnings_as_errors and result.warnings:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
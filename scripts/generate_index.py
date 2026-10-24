#!/usr/bin/env python3
"""Genera la tabla de informes del README.md a partir de los metadata.yml.

Estructura esperada del repositorio:

    <AAAA>/<nombre-corto>/metadata.yml

Busca todos los metadata.yml (excepto los de template/), valida sus campos y
reemplaza el contenido del README que está entre los marcadores INDEX:START e
INDEX:END.

Uso:
    python scripts/generate_index.py           # actualiza el README
    python scripts/generate_index.py --check   # no escribe; falla si está desactualizado

Requiere PyYAML:  pip install pyyaml
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"
EXCLUDED_DIRS = {"template"}
YEAR_RE = re.compile(r"^\d{4}$")

REQUIRED_FIELDS = ["titulo", "anio", "integrantes", "director", "resumen", "estado"]
ESTADOS = {"terminado": "Terminado", "linea-abierta": "Línea abierta"}


def find_metadata_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("metadata.yml"):
        dirs = path.relative_to(root).parts[:-1]
        if any(p.startswith(".") or p in EXCLUDED_DIRS for p in dirs):
            continue
        files.append(path)
    return sorted(files)


def load_entry(path: Path, root: Path) -> tuple[dict | None, list[str]]:
    """Lee un metadata.yml y devuelve (datos, errores)."""
    rel = path.relative_to(root).as_posix()
    dirs = path.relative_to(root).parts[:-1]

    if len(dirs) != 2 or not YEAR_RE.match(dirs[0]):
        return None, [f"{rel}: debe estar en <AAAA>/<nombre-corto>/metadata.yml"]

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return None, [f"{rel}: YAML inválido ({exc})"]
    if not isinstance(data, dict):
        return None, [f"{rel}: el archivo debe ser un mapa YAML"]

    errors = []
    for field in REQUIRED_FIELDS:
        if data.get(field) in (None, "", []):
            errors.append(f"{rel}: falta el campo obligatorio '{field}'")

    if data.get("anio") and not isinstance(data["anio"], int):
        errors.append(f"{rel}: 'anio' debe ser un número (por ejemplo 2024)")
    elif isinstance(data.get("anio"), int) and str(data["anio"]) != dirs[0]:
        errors.append(
            f"{rel}: la carpeta '{dirs[0]}' no coincide con anio: {data['anio']}"
        )
    if data.get("estado") and data["estado"] not in ESTADOS:
        errors.append(f"{rel}: 'estado' debe ser uno de {sorted(ESTADOS)}")
    if data.get("integrantes") and not isinstance(data["integrantes"], list):
        errors.append(f"{rel}: 'integrantes' debe ser una lista")
    if data.get("trabajo_futuro") is not None and not isinstance(
        data["trabajo_futuro"], list
    ):
        errors.append(f"{rel}: 'trabajo_futuro' debe ser una lista de tareas")
    if data.get("relacionados") is not None and not isinstance(
        data["relacionados"], list
    ):
        errors.append(f"{rel}: 'relacionados' debe ser una lista")

    data["_dir"] = "/".join(dirs)
    return data, errors


def cell(text: object) -> str:
    """Limpia un texto para usarlo dentro de una celda de tabla Markdown."""
    return " ".join(str(text).split()).replace("|", "\\|")


def build_table(entries: list[dict]) -> str:
    header = [
        "| Año | Proyecto | Integrantes | Estado | Trabajo futuro |",
        "|-----|----------|-------------|--------|----------------|",
    ]
    rows = []
    # Más recientes primero; dentro del mismo año, orden alfabético.
    for e in sorted(entries, key=lambda e: (-e["anio"], e["titulo"].lower())):
        title = cell(e.get("titulo_corto") or e["titulo"])
        link = quote(e["_dir"])
        integrantes = cell(", ".join(str(i) for i in e["integrantes"]))
        pendientes = len(e.get("trabajo_futuro") or [])
        futuro = "1 tarea" if pendientes == 1 else f"{pendientes} tareas"
        rows.append(
            f"| {e['anio']} | [{title}]({link}/) | {integrantes} "
            f"| {ESTADOS[e['estado']]} | {futuro} |"
        )
    return "\n".join(header + rows)


def render_block(entries: list[dict]) -> str:
    note = "<!-- Esta tabla se genera automáticamente a partir de los metadata.yml. No editar a mano. -->"
    return f"{START}\n{note}\n\n{build_table(entries)}\n\n{END}"


def replace_block(readme: str, block: str) -> str:
    start = readme.find(START)
    end = readme.find(END)
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"El README debe contener los marcadores {START} y {END}")
    return readme[:start] + block + readme[end + len(END) :]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="raíz del repositorio (por defecto, la carpeta padre de scripts/)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="no escribe nada; sale con error si el README está desactualizado",
    )
    args = parser.parse_args()
    root: Path = args.root

    files = find_metadata_files(root)
    entries, errors = [], []
    for path in files:
        data, errs = load_entry(path, root)
        errors.extend(errs)
        if data is not None and not errs:
            entries.append(data)

    # Las referencias de 'relacionados' deben tener el formato AAAA/nombre-corto
    # y apuntar a un informe existente.
    known = {path.parent.relative_to(root).as_posix() for path in files}
    for e in entries:
        for ref in e.get("relacionados") or []:
            if str(ref).strip("/") not in known:
                errors.append(
                    f"{e['_dir']}/metadata.yml: 'relacionados' apunta a '{ref}', "
                    "que no existe (el formato es AAAA/nombre-corto)"
                )

    if errors:
        print("Errores en los metadata.yml:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    readme_path = root / "README.md"
    current = readme_path.read_text(encoding="utf-8")
    try:
        updated = replace_block(current, render_block(entries))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if updated == current:
        print(f"README al día ({len(entries)} informes).")
        return 0
    if args.check:
        print(
            "El índice del README está desactualizado.\n"
            "Ejecutá 'python scripts/generate_index.py' (necesita PyYAML), "
            "y commiteá el README.md resultante.",
            file=sys.stderr,
        )
        return 1

    readme_path.write_text(updated, encoding="utf-8")
    print(f"README actualizado ({len(entries)} informes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

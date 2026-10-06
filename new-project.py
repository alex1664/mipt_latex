#!/usr/bin/env python3
"""Создать независимый LaTeX-проект из локального шаблона."""

import argparse
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Папка нового проекта, например projects/algebra")
    args = parser.parse_args()
    target = args.folder.expanduser().absolute()
    if target.exists():
        parser.error(f"Папка уже существует: {target}. Укажите новую папку.")
    template = Path(__file__).resolve().parent / ".templates" / "project"
    try:
        shutil.copytree(template, target)
    except OSError as error:
        parser.exit(1, f"Не удалось создать проект: {error}\n")
    print(f"Проект создан: {target}\nОткройте main.tex или любой файл из sections/ в VS Code.")


if __name__ == "__main__":
    main()

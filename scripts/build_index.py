#!/usr/bin/env python3
"""Пересобирает оглавление конспектов в README.md.

Обходит semester-*/предмет/тип/*.md, читает YAML-фронтматтер каждой заметки
и записывает вложенный список ссылок между маркерами INDEX:START / INDEX:END.
Ссылки абсолютные, на GitHub: папки ведут на /tree/, файлы — на /blob/.
Текст вне маркеров не трогается. Зависимостей нет, только стандартная библиотека.

Запуск из корня репозитория:  python scripts/build_index.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"
SEMESTER_RE = re.compile(r"<!--\s*CURRENT-SEMESTER:\s*(\d+)\s*-->")
REPO_RE = re.compile(r"<!--\s*REPO:\s*([\w.-]+/[\w.-]+)\s*-->")

DEFAULT_REPO = "aimnoux/synergy-mag"
DEFAULT_BRANCH = "main"

SKIP_DIRS = {".git", ".github", "scripts", "_inbox", "node_modules", ".venv"}

# Отображаемые названия для типовых папок; всё остальное берётся из фронтматтера.
TYPE_LABELS = {
    "lectures": "Лекции",
    "seminars": "Семинары",
    "labs": "Лабораторные",
    "practices": "Практики",
}


def git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args], capture_output=True, text=True, timeout=5, check=False
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = out.stdout.strip()
    return value if out.returncode == 0 and value else None


def detect_repo(content: str) -> str:
    """owner/repo: маркер в README > git remote > константа по умолчанию."""
    match = REPO_RE.search(content)
    if match:
        return match.group(1)
    remote = git("remote", "get-url", "origin")
    if remote:
        slug = re.sub(r"^.*github\.com[:/]", "", remote)
        slug = re.sub(r"\.git$", "", slug).strip("/")
        if re.fullmatch(r"[\w.-]+/[\w.-]+", slug):
            return slug
    return DEFAULT_REPO


def detect_branch() -> str:
    return git("symbolic-ref", "--short", "HEAD") or DEFAULT_BRANCH


class Linker:
    def __init__(self, repo: str, branch: str) -> None:
        self.base = f"https://github.com/{repo}"
        self.branch = branch

    def url(self, path: Path, root: Path, kind: str) -> str:
        rel = quote(path.relative_to(root).as_posix())
        return f"{self.base}/{kind}/{self.branch}/{rel}"

    def folder(self, path: Path, root: Path) -> str:
        return self.url(path, root, "tree")

    def file(self, path: Path, root: Path) -> str:
        return self.url(path, root, "blob")


def read_current_semester(content: str) -> int | None:
    """Читает актуальный семестр из служебного комментария в README."""
    match = SEMESTER_RE.search(content)
    return int(match.group(1)) if match else None


def guess_semester(root: Path) -> int:
    numbers = [
        int(m.group(1))
        for p in root.iterdir()
        if p.is_dir() and p.name.startswith("semester")
        for m in [re.search(r"(\d+)", p.name)]
        if m
    ]
    return max(numbers) if numbers else 1


def parse_frontmatter(path: Path) -> dict[str, str]:
    """Достаёт простые ключ-значение из YAML-фронтматтера. Без вложенности."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line.strip())
        if match:
            meta[match.group(1)] = match.group(2).strip().strip("\"'")
    return meta


def humanize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").capitalize()


def semester_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 999, path.name)


def collect(root: Path, link: Linker, current: int | None = None) -> list[str]:
    lines: list[str] = []

    semesters = sorted(
        (p for p in root.iterdir() if p.is_dir() and p.name.startswith("semester")),
        key=semester_sort_key,
    )
    if not semesters:
        return ["_Пока ни одного конспекта._"]

    for semester in semesters:
        match = re.search(r"(\d+)", semester.name)
        number = int(match.group(1)) if match else None
        title = f"Семестр {number}" if number else humanize(semester.name)
        suffix = " (текущий)" if current is not None and number == current else ""
        lines.append(f"### [{title}]({link.folder(semester, root)}){suffix}")
        lines.append("")

        subjects = sorted(p for p in semester.iterdir() if p.is_dir() and p.name not in SKIP_DIRS)
        if not subjects:
            lines.append("_Пусто._")
            lines.append("")
            continue

        for subject in subjects:
            notes_by_type: dict[Path, list[Path]] = {}
            for note in sorted(subject.rglob("*.md")):
                if any(part in SKIP_DIRS for part in note.parts):
                    continue
                notes_by_type.setdefault(note.parent, []).append(note)

            if not notes_by_type:
                continue

            # Русское название предмета берём из первой найденной заметки.
            first_note = next(iter(next(iter(notes_by_type.values()))), None)
            subject_meta = parse_frontmatter(first_note) if first_note else {}
            subject_title = subject_meta.get("subject") or humanize(subject.name)

            lines.append(f"**[{subject_title}]({link.folder(subject, root)})**")
            lines.append("")

            for folder in sorted(notes_by_type):
                notes = notes_by_type[folder]
                if folder != subject:
                    label = TYPE_LABELS.get(folder.name)
                    if not label:
                        folder_meta = parse_frontmatter(notes[0])
                        label = folder_meta.get("type") or humanize(folder.name)
                    lines.append(f"- [{label}]({link.folder(folder, root)})")
                    indent = "    "
                else:
                    indent = ""

                for note in notes:
                    meta = parse_frontmatter(note)
                    title = meta.get("title") or humanize(note.stem)
                    date = meta.get("date", "")
                    date_suffix = f" — {date}" if date else ""
                    # Номер конспекта в оглавлении — тот же, что в имени файла.
                    number = re.match(r"^(\d{2,})-", note.name)
                    # Жирным, иначе GitHub примет "- 01." за вложенный нумерованный список.
                    number_prefix = f"**{number.group(1)}.** " if number else ""
                    lines.append(
                        f"{indent}- {number_prefix}[{title}]({link.file(note, root)}){date_suffix}"
                    )
            lines.append("")

    return lines


def check_naming(root: Path) -> list[str]:
    """Проверяет нумерацию внутри группы «семестр / предмет / тип».

    Нумерация в каждой такой папке своя: начинается с 01, идёт двузначно,
    плотно и без дублей. Всё остальное ломает сортировку или порядок чтения.
    """
    warnings: list[str] = []
    for folder in sorted(p for p in root.rglob("*") if p.is_dir()):
        if any(part in SKIP_DIRS for part in folder.parts) or not folder.name:
            continue
        notes = [n for n in folder.glob("*.md") if n.name != "README.md"]
        if not notes:
            continue
        where = folder.relative_to(root).as_posix()
        seen: dict[str, str] = {}
        for note in sorted(notes):
            match = re.match(r"^(\d{2,})-", note.name)
            if not match:
                warnings.append(f"без двузначного номера в имени: {note.relative_to(root).as_posix()}")
                continue
            number = match.group(1)
            if number in seen:
                warnings.append(
                    f"номер {number} занят дважды в {where}: {seen[number]} и {note.name}"
                )
            else:
                seen[number] = note.name
        numbers = sorted(int(n) for n in seen)
        if numbers and numbers != list(range(1, len(numbers) + 1)):
            expected = ", ".join(f"{i:02d}" for i in range(1, len(numbers) + 1))
            actual = ", ".join(f"{i:02d}" for i in numbers)
            warnings.append(
                f"нумерация в {where} не сплошная: {actual} вместо {expected} "
                f"(счётчик внутри семестра/предмета/типа начинается с 01 и идёт без пропусков)"
            )
    return warnings


def main() -> int:
    root = Path.cwd()
    readme = root / "README.md"

    if readme.exists():
        content = readme.read_text(encoding="utf-8")
    else:
        content = "# Конспекты\n\n## Оглавление\n\n" + START + "\n" + END + "\n"

    current = read_current_semester(content)
    if current is None:
        current = guess_semester(root)
        marker = f"<!-- CURRENT-SEMESTER: {current} -->"
        lines = content.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines.insert(insert_at, "")
        lines.insert(insert_at + 1, marker)
        content = "\n".join(lines)
        print(f"Добавлен маркер текущего семестра: {marker}")

    repo = detect_repo(content)
    branch = detect_branch()
    link = Linker(repo, branch)

    index = "\n".join([START, "", *collect(root, link, current), END])

    if START in content and END in content:
        content = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            lambda _: index,
            content,
            flags=re.DOTALL,
        )
    else:
        content = content.rstrip() + "\n\n## Оглавление\n\n" + index + "\n"

    readme.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"Оглавление обновлено: {readme}")
    print(f"Репозиторий: {repo}, ветка: {branch}, текущий семестр: {current}")

    if not (root / f"semester-{current}").exists():
        print(f"⚠️  папки semester-{current} ещё нет — она будет создана при первой записи")

    for warning in check_naming(root):
        print(f"⚠️  {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

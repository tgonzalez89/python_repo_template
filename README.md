# MY_PROJECT_NAME

> A short description of MY_PROJECT_NAME.

---

## Quickstart from template

This repository is a **project template**. To create a new project named `my_package`:

### Unix / macOS (bash / zsh)

```bash
# 1. Clone / copy the template
git clone https://github.com/YOUR_USERNAME/MY_PROJECT_NAME.git my_package
cd my_package

# 2. Rename every occurrence of the placeholder (files + contents)
NEWNAME="my_package"
PLACEHOLDER="MY_PROJECT_NAME"

# Rename the package directory first
mv src/${PLACEHOLDER} src/${NEWNAME}

# Replace all occurrences inside files (git-tracked files only)
git grep -rl "${PLACEHOLDER}" | xargs sed -i "s/${PLACEHOLDER}/${NEWNAME}/g"

# Rename any remaining files whose names contain the placeholder
find . -depth -name "*${PLACEHOLDER}*" | while IFS= read -r f; do
  mv "$f" "$(dirname "$f")/$(basename "$f" | sed "s/${PLACEHOLDER}/${NEWNAME}/g")"
done

# 3. Re-initialise git history
rm -rf .git && git init && git add . && git commit -m "chore: initial commit"
```

### Windows (PowerShell)

```powershell
$newname    = "my_package"
$placeholder = "MY_PROJECT_NAME"

# Rename package directory
Rename-Item "src\$placeholder" "src\$newname"

# Replace in all text files
Get-ChildItem -Recurse -File | Where-Object { $_.Extension -match '\.(py|toml|yaml|yml|json|md|txt|cfg)$' } | ForEach-Object {
    (Get-Content $_.FullName -Raw) -replace $placeholder, $newname | Set-Content $_.FullName
}

# Rename files/dirs containing the placeholder
Get-ChildItem -Recurse -Filter "*$placeholder*" | Sort-Object -Descending FullName | ForEach-Object {
    Rename-Item $_.FullName ($_.Name -replace $placeholder, $newname)
}

# Re-init git
Remove-Item .git -Recurse -Force; git init; git add .; git commit -m "chore: initial commit"
```

---

## Development setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Install dependencies & create virtualenv

```bash
uv sync
```

### Install pre-commit hooks

```bash
uv run pre-commit autoupdate
uv run pre-commit install --install-hooks
```

### Run the CLI

```bash
uv run MY_PROJECT_NAME greet World
uv run MY_PROJECT_NAME greet World --shout
```

### Run tests

```bash
uv run pytest
```

### Lint & format

```bash
# Check
uv run ruff check .

# Fix
uv run ruff check --fix .

# Format
uv run ruff format .
```

### Type check

```bash
uv run ty check src tests
```

---

## Project layout

```
.
├── src/
│   └── MY_PROJECT_NAME/
│       ├── __init__.py      # package version
│       ├── cli.py           # CLI entry point
│       └── py.typed         # PEP 561 marker (typed package)
├── tests/
│   ├── conftest.py
│   ├── test_cli.py
│   └── test_MY_PROJECT_NAME.py
├── .editorconfig
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   └── settings.json
├── pyproject.toml           # single source of truth for all config
└── uv.lock                  # committed lockfile
```

---

## Tools

| Tool | Purpose |
|------|---------|
| [uv](https://docs.astral.sh/uv/) | Fast package manager & virtualenv |
| [ruff](https://docs.astral.sh/ruff/) | Linting + formatting (replaces black, isort, flake8) |
| [ty](https://github.com/astral-sh/ty) | Type checker (Astral) |
| [pytest](https://pytest.org) | Test framework |
| [pytest-cov](https://pytest-cov.readthedocs.io) | Coverage |
| [pre-commit](https://pre-commit.com) | Git hooks |
| [hatchling](https://hatch.pypa.io) | Build backend |
| [commitizen](https://commitizen-tools.github.io/commitizen/) | Conventional commits |

---

## License

See [LICENSE](LICENSE).

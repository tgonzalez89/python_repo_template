# project_name

A short description of project_name.

---

## Quickstart from template

This repository is a **project template**. Use the following commands to rename it.
Replace the `NEWNAME` variable value `your_actual_project_name` with the name of your actual project.

### Unix / macOS (bash / zsh)

```bash
NEWNAME="your_actual_project_name"
PLACEHOLDER="project_name"

git clone https://github.com/tgonzalez89/project_name.git "$NEWNAME"
cd "$NEWNAME"

# Rename the package directory
mv src/${PLACEHOLDER} src/${NEWNAME}

# Replace in all text files containing the PLACEHOLDER
git grep -rl "${PLACEHOLDER}" | xargs sed -i "s/${PLACEHOLDER}/${NEWNAME}/g"

# Rename files/dirs containing the PLACEHOLDER
find . -depth -name "*${PLACEHOLDER}*" | while IFS= read -r f; do
  mv "$f" "$(dirname "$f")/$(basename "$f" | sed "s/${PLACEHOLDER}/${NEWNAME}/g")"
done

# Re-init git
rm -rf .git && git init && git add . && git commit -m "chore: initial commit"
```

### Windows (PowerShell)

```powershell
$NEWNAME = "your_actual_project_name"
$PLACEHOLDER = "project_name"

git clone https://github.com/tgonzalez89/project_name.git "$NEWNAME"
Set-Location -Path "$PLACEHOLDER"

# Rename package directory
Rename-Item "src\$PLACEHOLDER" "src\$NEWNAME"

# Replace in all text files containing the PLACEHOLDER
Get-ChildItem -Recurse -File | Where-Object { $_.Extension -match '\.(py|toml|yaml|yml|json|md|txt|cfg)$' } | ForEach-Object {
    (Get-Content $_.FullName -Raw) -replace $PLACEHOLDER, $NEWNAME | Set-Content $_.FullName
}

# Rename files/dirs containing the PLACEHOLDER
Get-ChildItem -Recurse -Filter "*$PLACEHOLDER*" | Sort-Object -Descending FullName | ForEach-Object {
    Rename-Item $_.FullName ($_.Name -replace $PLACEHOLDER, $NEWNAME)
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
uv run project_name greet World
uv run project_name greet World --shout
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

## Tools

| Tool | Purpose |
|------|---------|
| [uv](https://docs.astral.sh/uv/) | Package manager & virtualenv |
| [ruff](https://docs.astral.sh/ruff/) | Linting + formatting |
| [ty](https://github.com/astral-sh/ty) | Type checker |
| [pytest](https://pytest.org) | Test framework |
| [pytest-cov](https://pytest-cov.readthedocs.io) | Coverage |
| [pre-commit](https://pre-commit.com) | Git hooks |
| [commitizen](https://commitizen-tools.github.io/commitizen/) | Conventional commits |

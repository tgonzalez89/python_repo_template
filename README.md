# project_name

A short description of project_name.

---

## Quickstart from template

This repository is a **project template**. Use the following commands to rename it.
Set `NEWNAME` to a valid Python package name (for example, `my_project`).

### Linux, macOS, Unix (POSIX-style shell)

```sh
NEWNAME="your_actual_project_name"
PLACEHOLDER=project_name

# Clone the template into the new project directory.
git clone https://github.com/tgonzalez89/python_repo_template.git "$NEWNAME"
cd "$NEWNAME"

# Substitute the placeholder in tracked text files.
git grep -Il "$PLACEHOLDER" | while IFS= read -r file; do
  sed "s/$PLACEHOLDER/$NEWNAME/g" "$file" > "$file.tmp" &&
    mv "$file.tmp" "$file"
done

# Rename the package directory and matching test file.
mv "src/$PLACEHOLDER" "src/$NEWNAME"
mv "tests/test_$PLACEHOLDER.py" "tests/test_$NEWNAME.py"

# Remove the template's Git history and initialize a fresh repository.
rm -rf .git
git init -b main
git add .
git commit -m "chore: initial commit"
```

### Windows (PowerShell)

```powershell
$NEWNAME = "your_actual_project_name"
$PLACEHOLDER = "project_name"

# Clone the template into the new project directory.
git clone https://github.com/tgonzalez89/python_repo_template.git "$NEWNAME"
Set-Location -Path "$NEWNAME"

# Substitute the placeholder in tracked text files.
git grep -Il -- $PLACEHOLDER | ForEach-Object {
    $path = $_
    $content = [System.IO.File]::ReadAllText($path)
    [System.IO.File]::WriteAllText($path, $content.Replace($PLACEHOLDER, $NEWNAME))
}

# Rename the package directory and matching test file.
Move-Item "src\$PLACEHOLDER" "src\$NEWNAME"
Move-Item "tests\test_$PLACEHOLDER.py" "tests\test_$NEWNAME.py"

# Remove the template's Git history and initialize a fresh repository.
Remove-Item .git -Recurse -Force
git init -b main
git add .
git commit -m "chore: initial commit"
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

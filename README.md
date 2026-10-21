# Modern Python Refresher

Hands-on materials for a 90-minute refresher: **uv**, reading Python (functions, type hints, docstrings, classes), and how code gets written today with Ruff, type checking and AI agents.

## 1. Install uv

Windows (recommended):

```powershell
winget install --id=astral-sh.uv -e
```

If winget asks you to accept the source agreements, type `Y`. If `winget` isn't recognised, install **App Installer** from the Microsoft Store, or use the PowerShell installer instead:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Open a **new** terminal and check that it worked: `uv --version`

Last resort, if you already have Python: `python -m pip install uv`, then use `python -m uv` wherever these instructions say `uv`.

## 2. Get the exercises

```bash
git clone https://github.com/smuotoe/mcda-python-refresher
cd mcda-python-refresher
uv sync
```

No git? On GitHub, click **Code > Download ZIP**, unzip it, and `cd` into the folder.

`uv sync` creates `.venv` from `uv.lock`, and downloads Python 3.13 if you don't have it.

## 3. Open it in VS Code

```bash
code .
```

`pyproject.toml` turns on basic type checking for VS Code's Python extension, so type errors show up as red squiggles.

## 4. Exercises

| # | File | What to do | Run |
|---|---|---|---|
| 1 | `exercises/gradebook.py` | Fill in `letter_grade`, `Student.add_score` and `Student.average` | `uv run exercises/gradebook.py` |
| 2 | `exercises/review.py` | An AI wrote this file. It runs, but has three bugs: find and fix them | `uv run exercises/review.py` |
| 3 | `starter/` | In pairs: write your own AGENTS.md and have an AI agent follow it (below) | |

Exercises 1 and 2 print their results; compare them with the `# expected:` comments.

### Exercise 3: your own AGENTS.md

Create a project next to this folder (not inside it) and copy the starter files in:

```bash
uv init --no-package grades
cd grades
cp ../mcda-python-refresher/starter/* .
```

1. Add one rule of your own to `AGENTS.md`.
2. Ask your AI agent: *"Read scores.csv and print each student's average score and letter grade."* Using a chat tool instead? Paste `AGENTS.md` and the prompt, then run the commands yourself.
3. Check its work: does `uv run main.py` run, with Ada at 91.67 (an A)? Is `uvx ruff check .` clean? Did it add any dependencies, and do they exist? Did it follow your rule?

## 5. Demos

| File | What it shows | Run |
|---|---|---|
| `demos/race.py` | pip and uv install the same packages at the same moment, with a live timer each. `--cold` makes both ignore their cache | `uv run demos/race.py` |
| `demos/type_hints.py` | A function with no hints or docstring. Add them, and watch what VS Code can tell you | open it in VS Code |
| `demos/pypi_check.py` | Checks that package names exist on PyPI. Use it before installing a package an AI suggested | `uv run demos/pypi_check.py requests polars definitely-not-a-real-pkg` |

`race.py` and `pypi_check.py` list their dependencies inside the file (PEP 723), so uv runs each in its own environment with no setup.

## 6. Check code the way teams do

```bash
uvx ruff check .      # lint: bug patterns, imports, docstrings
uvx ruff format .     # format
uvx ty check          # type check (ty is in beta)
```

The rules live in `pyproject.toml`. `exercises/review.py` and `demos/type_hints.py` fail on purpose until you fix them.

## uv cheat sheet

| I want to... | Command |
|---|---|
| Start a project (creates `main.py`) | `uv init --no-package my-app` |
| Add or remove a dependency | `uv add httpx` / `uv remove httpx` |
| Add a development-only tool | `uv add --dev ruff` |
| Run code in the project environment | `uv run main.py` |
| Recreate the exact environment | `uv sync` |
| Upgrade one package | `uv lock --upgrade-package httpx` |
| See the dependency tree | `uv tree` |
| Install or pin a Python version | `uv python install 3.13` / `uv python pin 3.13` |
| Create a script with inline dependencies | `uv init --script check.py`, then `uv add --script check.py httpx` |
| Use a package for one command | `uv run --with rich python -c "import rich"` |
| Run a tool without installing it | `uvx ruff check .` |
| Install a tool globally | `uv tool install ruff` |
| Work with an old requirements.txt | `uv pip install -r requirements.txt` or `uv add -r requirements.txt` |
| Update uv itself | `uv self update` (installer script) or `winget upgrade --id=astral-sh.uv -e` (winget) |

## Slides

The slides are in `slides/` (Slidev). To run them locally: `cd slides`, `npm install`, `npm run dev`.

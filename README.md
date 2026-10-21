# Modern Python Refresher

Hands-on materials for a 90-minute refresher on **uv**, functions, docstrings, classes, and coding with AI.

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
git clone https://github.com/smuotoe/modern-python-refresher
cd modern-python-refresher
uv sync
```

No git? On GitHub, click **Code > Download ZIP**, unzip it, and `cd` into the folder.

`uv sync` creates `.venv` from `uv.lock`, and downloads Python 3.13 if you don't have it.

## 3. Exercises

Fill in the TODOs in each file, run it, and compare the output with the expected values in the comments.

| # | File | What to do | Run |
|---|---|---|---|
| 1 | `exercises/functions.py` | Implement `slugify` and `chunk`; fix the bug in `add_tag` | `uv run exercises/functions.py` |
| 2 | `exercises/docstrings.py` | Write Google-style docstrings | `uv run exercises/docstrings.py` |
| 3 | `exercises/classes.py` | Implement the `ShoppingCart` methods | `uv run exercises/classes.py` |
| 4 | `exercises/spec_first.py` | Build `parse_duration` with an AI assistant | `uv run exercises/spec_first.py` |

## 4. Coding with AI: specify, generate, verify, explain

1. **Specify**: the signature, type hints and docstring say exactly what the function must do.
2. **Generate**: ask any AI assistant. Try a vague prompt first, then give it the full docstring.
3. **Verify**: run the file, compare with the expected output, and read the code.
4. **Explain**: walk your neighbour through every line. If you can't explain it, you don't own it yet.

`AGENTS.md` holds project rules that most AI coding agents read automatically.

## 5. A script that brings its own dependencies

`demos/pypi_check.py` lists its dependencies inside the file (PEP 723), so uv runs it in its own environment with no setup:

```bash
uv run demos/pypi_check.py requests polars definitely-not-a-real-pkg
```

It checks whether packages exist on PyPI. Use it before installing a package an AI suggested.

## uv cheat sheet

| I want to... | Command |
|---|---|
| Start a project | `uv init my-app` |
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

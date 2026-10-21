# AGENTS.md

Rules for AI coding agents working in this project.

## Environment

- Use uv for everything: `uv add <package>` to add a dependency and `uv run <file>` to run code. Never call pip, and never activate a virtual environment.
- Ask before adding a dependency, and check that it exists on PyPI first.

## Code

- Add type hints and a Google-style docstring (Args, Returns, Raises) to every function.
- Keep functions small, with one job each. No mutable default arguments.
- Never put secrets in code; read them from environment variables.

## Before you finish

- Run `uvx ruff format .` and `uvx ruff check .`, and fix what they report.
- Run the code and show me the output.

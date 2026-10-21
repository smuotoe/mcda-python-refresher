# AGENTS.md

Instructions for AI coding agents working in this repository.

- Use uv: `uv add <package>` to add dependencies and `uv run <file>` to run code. Never call pip directly.
- Add type hints and a Google-style docstring (Args, Returns, Raises) to every function.
- Keep functions small, with one job each. No mutable default arguments.
- Don't add a dependency without asking, and check that it exists on PyPI first.
- Never put secrets in code; read them from environment variables.

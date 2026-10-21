"""Exercise 2: docstrings.

These functions work, but nobody can tell how to use them without reading
the code. Give each one a Google-style docstring (a one-line summary, then
Args, Returns and Raises sections), then run:

    uv run exercises/docstrings.py

It prints each docstring. "None" means you're not done yet.
"""

import inspect


def apply_discount(price: float, percent: float) -> float:
    # TODO: add a docstring
    if not 0 <= percent <= 100:
        raise ValueError(f"percent must be between 0 and 100, got {percent}")
    return round(price * (1 - percent / 100), 2)


def split_full_name(full_name: str) -> tuple[str, str]:
    # TODO: add a docstring
    parts = full_name.split()
    if len(parts) < 2:
        raise ValueError(f"expected at least two names, got {full_name!r}")
    return " ".join(parts[:-1]), parts[-1]


if __name__ == "__main__":
    for function in (apply_discount, split_full_name):
        print(f"--- {function.__name__} ---")
        print(inspect.getdoc(function))

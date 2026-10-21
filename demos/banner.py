#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyfiglet>=1.0.4",
#     "rich>=15.0.0",
# ]
# ///
"""A script that brings its own dependencies.

The block above lists what this script needs (PEP 723). ``uv run`` reads it,
installs pyfiglet and rich into a cached environment of their own, and runs
the script: no project, no venv, no pip.

    uv run demos/banner.py
    uv run demos/banner.py "Hello, class"
"""

import sys

import pyfiglet
from rich.console import Console
from rich.panel import Panel

DEFAULT_TEXT = "uv"


def render_banner(text: str) -> Panel:
    """Turn text into a large ASCII-art banner inside a panel.

    Args:
        text: The text to draw.

    Returns:
        A rich panel holding the banner.
    """
    art = pyfiglet.figlet_format(text, font="slant")
    return Panel(art.strip("\n"), title="installed by uv run", border_style="green")


def main() -> None:
    """Print a banner for the text given on the command line."""
    text = " ".join(sys.argv[1:]) or DEFAULT_TEXT
    Console().print(render_banner(text))


if __name__ == "__main__":
    main()

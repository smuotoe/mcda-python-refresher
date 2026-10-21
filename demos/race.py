#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///
"""Race pip against uv: both install the same packages at the same moment.

Each tool gets its own fresh virtual environment in a temporary folder, so
nothing touches your project. Only the install is timed, not the setup.

    uv run demos/race.py                 # warm: both tools may use their cache
    uv run demos/race.py --cold          # cold: both ignore their cache
    uv run demos/race.py requests flask  # race your own packages

Run it once before presenting so both caches are warm. In --cold mode the
two installs share your network connection, so compare them with care.
"""

import argparse
import subprocess
import sys
import tempfile
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

from rich.columns import Columns
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

DEFAULT_PACKAGES = ["jupyterlab", "pandas", "scikit-learn", "matplotlib"]
REFRESH_PER_SECOND = 20
PANEL_WIDTH = 48


@dataclass
class Racer:
    """One install command, and what has happened to it so far.

    Attributes:
        name: Label shown on the panel.
        style: Rich colour for the panel border and timer.
        command: The install command to run.
        started: ``time.perf_counter()`` when the install began, or 0.
        finished: ``time.perf_counter()`` when the install ended, or 0.
        last_line: Most recent line of output, shown under the timer.
        return_code: Exit status once finished, otherwise None.
        lock: Guards the fields above, which two threads read and write.
    """

    name: str
    style: str
    command: list[str]
    started: float = 0.0
    finished: float = 0.0
    last_line: str = ""
    return_code: int | None = None
    lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def elapsed(self) -> float:
        """Return seconds since the install started, frozen once it ends.

        Returns:
            Elapsed seconds, or 0.0 if the install hasn't started.
        """
        if not self.started:
            return 0.0
        end = self.finished or time.perf_counter()
        return end - self.started


def venv_python(venv: Path) -> Path:
    """Return the path to the Python executable inside a virtual environment.

    Args:
        venv: Root folder of the virtual environment.

    Returns:
        ``Scripts/python.exe`` on Windows, ``bin/python`` elsewhere.
    """
    if sys.platform == "win32":
        return venv / "Scripts" / "python.exe"
    return venv / "bin" / "python"


def create_venvs(root: Path) -> tuple[Path, Path]:
    """Create one venv for pip (with pip inside) and one for uv.

    Args:
        root: Empty folder to create both environments in.

    Returns:
        The pip venv folder and the uv venv folder.

    Raises:
        subprocess.CalledProcessError: If either environment can't be created.
    """
    pip_venv, uv_venv = root / "pip-venv", root / "uv-venv"
    subprocess.run([sys.executable, "-m", "venv", pip_venv], check=True)
    subprocess.run(["uv", "venv", "--quiet", uv_venv], check=True)
    return pip_venv, uv_venv


def build_racers(
    pip_venv: Path, uv_venv: Path, packages: list[str], cold: bool
) -> list[Racer]:
    """Build the pip and uv install commands for the race.

    Args:
        pip_venv: Environment that pip installs into.
        uv_venv: Environment that uv installs into.
        packages: Packages for both tools to install.
        cold: If True, both tools ignore their cache.

    Returns:
        The pip racer, then the uv racer.
    """
    pip_command = [str(venv_python(pip_venv)), "-m", "pip", "install"]
    pip_command += ["--disable-pip-version-check", *packages]
    uv_command = ["uv", "pip", "install", "--python", str(venv_python(uv_venv))]
    uv_command += packages
    if cold:
        pip_command.append("--no-cache-dir")
        uv_command.append("--no-cache")
    return [
        Racer("pip", "orange1", pip_command),
        Racer("uv", "green3", uv_command),
    ]


def run_racer(racer: Racer, start: threading.Barrier) -> None:
    """Run one install, recording its output and timing on ``racer``.

    Args:
        racer: The racer to run; updated in place as the install progresses.
        start: Barrier that releases both racers at the same moment.
    """
    start.wait()
    with racer.lock:
        racer.started = time.perf_counter()
    process = subprocess.Popen(
        racer.command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    assert process.stdout is not None
    for line in process.stdout:
        if line.strip():
            with racer.lock:
                racer.last_line = line.strip()
    return_code = process.wait()
    with racer.lock:
        racer.finished = time.perf_counter()
        racer.return_code = return_code


def render_panel(racer: Racer) -> Panel:
    """Draw one racer's panel: a big timer and its latest output line.

    Args:
        racer: The racer to draw.

    Returns:
        A panel showing the elapsed time and status.
    """
    with racer.lock:
        elapsed, line, code = racer.elapsed(), racer.last_line, racer.return_code
    if code is None:
        status = Text("installing...", style="dim", justify="center")
    elif code == 0:
        status = Text("done", style=f"bold {racer.style}", justify="center")
    else:
        status = Text(f"failed (exit {code})", style="bold red", justify="center")
    timer = Text(f"{elapsed:6.2f} s", style=f"bold {racer.style}", justify="center")
    output = Text(line, style="dim", overflow="ellipsis", no_wrap=True)
    return Panel(
        Group(timer, status, output),
        title=racer.name,
        border_style=racer.style,
        width=PANEL_WIDTH,
    )


def render(racers: list[Racer]) -> Columns:
    """Draw all racers side by side.

    Args:
        racers: The racers to draw.

    Returns:
        The panels in a row.
    """
    return Columns([render_panel(racer) for racer in racers])


def race(racers: list[Racer], console: Console) -> None:
    """Start every racer at the same moment and redraw until all finish.

    Args:
        racers: The racers to run.
        console: Console to draw the live panels on.
    """
    start = threading.Barrier(len(racers))
    threads = [
        threading.Thread(target=run_racer, args=(racer, start), daemon=True)
        for racer in racers
    ]
    for thread in threads:
        thread.start()
    with Live(
        render(racers), console=console, refresh_per_second=REFRESH_PER_SECOND
    ) as live:
        while any(thread.is_alive() for thread in threads):
            live.update(render(racers))
            time.sleep(1 / REFRESH_PER_SECOND)
        live.update(render(racers))


def print_result(racers: list[Racer], console: Console) -> None:
    """Print how many times faster the winner was.

    Args:
        racers: The finished racers, all with a return code.
        console: Console to print on.
    """
    if any(racer.return_code != 0 for racer in racers):
        console.print("[red]An install failed, so there is no result.[/red]")
        return
    winner, loser = sorted(racers, key=lambda racer: racer.elapsed())
    ratio = loser.elapsed() / max(winner.elapsed(), 1e-9)
    console.print(
        f"\n[bold]{winner.name} was {ratio:.0f}x faster than {loser.name}.[/bold]"
    )


def parse_args() -> argparse.Namespace:
    """Read the command-line arguments.

    Returns:
        The packages to install and whether to ignore the caches.
    """
    parser = argparse.ArgumentParser(description="Race pip against uv.")
    parser.add_argument("packages", nargs="*", default=DEFAULT_PACKAGES)
    parser.add_argument("--cold", action="store_true", help="ignore both caches")
    return parser.parse_args()


def main() -> None:
    """Set up two fresh environments, race the installs, and show the result."""
    args = parse_args()
    console = Console()
    mode = "cold: no cache" if args.cold else "warm: cache allowed"
    console.print(
        f"[bold]Installing[/bold] {' '.join(args.packages)}  [dim]({mode})[/dim]"
    )
    with tempfile.TemporaryDirectory(prefix="race-") as root:
        console.print("[dim]Creating two fresh environments (not timed)...[/dim]")
        pip_venv, uv_venv = create_venvs(Path(root))
        racers = build_racers(pip_venv, uv_venv, args.packages, args.cold)
        race(racers, console)
    print_result(racers, console)


if __name__ == "__main__":
    main()

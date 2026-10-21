#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "orjson",
#     "rich",
# ]
# ///
"""Check that package names exist on PyPI before you install them.

AI assistants sometimes suggest packages that don't exist, and attackers
register some of those made-up names ("slopsquatting"). Check first:

    uv run demos/pypi_check.py requests polars definitely-not-a-real-pkg

The exit status is 1 if any package is missing, so it can guard an install
(macOS/Linux shells and PowerShell 7):

    uv run demos/pypi_check.py some-package && uv add some-package
"""

import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial

import httpx
import orjson
from rich.console import Console
from rich.markup import escape
from rich.table import Table

PYPI_JSON_URL = "https://pypi.org/pypi/{name}/json"
REQUEST_TIMEOUT_SECONDS = 10.0
MAX_WORKERS = 8
EXIT_ALL_FOUND = 0
EXIT_SOME_MISSING = 1
EXIT_ERROR = 2

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PackageInfo:
    """What PyPI knows about one package name.

    Attributes:
        name: The name that was looked up.
        exists: Whether PyPI has a project with this name.
        version: Latest version, or an empty string if the package is missing.
        released: Upload date (YYYY-MM-DD) of the latest version, if known.
        summary: One-line description from the package metadata.
    """

    name: str
    exists: bool
    version: str = ""
    released: str = ""
    summary: str = ""


def fetch_package_info(client: httpx.Client, name: str) -> PackageInfo:
    """Look up ``name`` on PyPI.

    Args:
        client: HTTP client used for the request.
        name: Package name to look up.

    Returns:
        The package details, with ``exists=False`` if PyPI has no such project.

    Raises:
        httpx.HTTPError: If the request fails for any reason other than a 404.
    """
    response = client.get(PYPI_JSON_URL.format(name=name))
    if response.status_code == httpx.codes.NOT_FOUND:
        return PackageInfo(name=name, exists=False)
    response.raise_for_status()
    data = orjson.loads(response.content)
    upload_times = [file["upload_time_iso_8601"] for file in data["urls"]]
    return PackageInfo(
        name=name,
        exists=True,
        version=data["info"]["version"],
        released=min(upload_times)[:10] if upload_times else "",
        summary=data["info"]["summary"] or "",
    )


def build_table(packages: list[PackageInfo]) -> Table:
    """Build a table that summarises the lookups.

    Args:
        packages: Results from ``fetch_package_info``.

    Returns:
        A rich table with one row per package.
    """
    table = Table(title="PyPI check")
    for column in ("Package", "Exists", "Latest", "Released", "Summary"):
        table.add_column(column)
    for package in packages:
        table.add_row(
            escape(package.name),
            "yes" if package.exists else "[bold red]NO[/]",
            package.version,
            package.released,
            escape(package.summary),
        )
    return table


def main(names: list[str]) -> int:
    """Check every name on PyPI and print the results.

    Args:
        names: Package names from the command line.

    Returns:
        The process exit status: 0 if every package exists, 1 if any is
        missing, and 2 on a usage or network error.
    """
    if not names:
        logger.error("usage: uv run demos/pypi_check.py PACKAGE [PACKAGE ...]")
        return EXIT_ERROR
    with (
        httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS, follow_redirects=True) as client,
        ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor,
    ):
        try:
            packages = list(executor.map(partial(fetch_package_info, client), names))
        except httpx.HTTPError as error:
            logger.error("Could not reach PyPI: %s", error)
            return EXIT_ERROR
    Console().print(build_table(packages))
    return EXIT_ALL_FOUND if all(p.exists for p in packages) else EXIT_SOME_MISSING


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s")
    sys.exit(main(sys.argv[1:]))

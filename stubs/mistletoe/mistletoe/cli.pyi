from collections.abc import Iterable
from typing import Protocol

from mistletoe.base_renderer import BaseRenderer

version_str: str

def main(args: list[str]) -> None: ...
def convert(filenames: Iterable[str], renderer: BaseRenderer) -> None: ...
def convert_file(filename, renderer: BaseRenderer) -> None: ...
def interactive(renderer: BaseRenderer) -> None: ...

class _ParsedArgs(Protocol):  # argparse.Namespace result.
    renderer: type[BaseRenderer]
    version: str
    filenames: list[str]

def parse(args: list[str]) -> _ParsedArgs: ...

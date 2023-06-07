from collections.abc import Generator
from typing import NamedTuple

from mistletoe.token import Token

class TraverseResult(NamedTuple):
    node: Token
    parent: Token
    depth: int

def traverse(
    source: Token, klass: type[Token] | None = ..., depth: int | None = ..., include_source: bool = False
) -> Generator[Token, None, None]: ...

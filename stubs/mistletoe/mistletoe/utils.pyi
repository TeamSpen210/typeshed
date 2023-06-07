from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class TraverseResult(NamedTuple):
    node: Incomplete
    parent: Incomplete
    depth: Incomplete

def traverse(
    source, klass: Incomplete | None = ..., depth: Incomplete | None = ..., include_source: bool = ...
) -> Generator[Incomplete, None, None]: ...

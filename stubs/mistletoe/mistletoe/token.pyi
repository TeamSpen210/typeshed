from collections.abc import Iterable
from typing import ClassVar

class Token:
    repr_attributes: ClassVar[Iterable[str]]

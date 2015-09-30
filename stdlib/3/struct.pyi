# Stubs for struct

# Based on http://docs.python.org/3.2/library/struct.html

from typing import overload, Any, AnyStr, Tuple

class error(Exception): ...

def pack(fmt: AnyStr, *v: Any) -> bytes: ...
# TODO buffer type
def pack_into(fmt: AnyStr, buffer: Any, offset: int, *v: Any) -> None: ...

# TODO buffer type
def unpack(fmt: AnyStr, buffer: Any) -> Tuple[Any, ...]: ...
def unpack_from(fmt: AnyStr, buffer: Any, offset: int = 0) -> Tuple[Any, ...]: ...

def calcsize(fmt: AnyStr) -> int: ...

class Struct:
    format = b''
    size = 0

    def __init__(self, format: AnyStr) -> None: ...

    def pack(self, *v: Any) -> bytes: ...
    # TODO buffer type
    def pack_into(self, buffer: Any, offset: int, *v: Any) -> None: ...
    # TODO buffer type
    def unpack(self, buffer: Any) -> Tuple[Any, ...]: ...
    def unpack_from(self, buffer: Any, offset: int = 0) -> Tuple[Any, ...]: ...

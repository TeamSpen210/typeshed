from collections.abc import Callable, Iterable, Sequence
from typing import Any, ClassVar, Literal, NoReturn, Protocol, TypeAlias, TypeVar, overload

import re

import span_token
from _typeshed import Incomplete

from mistletoe.block_tokenizer import ParseBuffer
from mistletoe.span_token import SpanToken
from mistletoe import core_tokens, token

class BlockToken(token.Token):
    children: Sequence[token.Token]
    def __init__(self, lines: list[str], tokenize_func: Callable[[list[str]], token.Token]) -> None: ...
    def __contains__(self, text: str) -> bool: ...
    @staticmethod
    def read(lines: Iterable[str]) -> Any: ...

class Document(BlockToken):
    footnotes: dict[str, core_tokens._DestTitle]
    children: list[BlockToken]
    def __init__(self, lines: Iterable[str]) -> None: ...

class Heading(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    level: int
    content: list[SpanToken]
    def __init__(self, match: tuple[int, list[str]]) -> None: ...
    @classmethod
    def start(cls, line: str) -> bool: ...
    @classmethod
    def read(cls, lines: list[str]) -> tuple[int, list[str]]: ...

class SetextHeading(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    level: int
    content: list[SpanToken]
    def __init__(self, lines: list[str]) -> None: ...
    @classmethod
    def start(cls, line: int) -> NoReturn: ...
    @classmethod
    def read(cls, lines: list[str]) -> NoReturn: ...

class Quote(BlockToken):
    children: list[BlockToken]
    def __init__(self, parse_buffer: ParseBuffer) -> None: ...
    @staticmethod
    def start(line: str) -> bool: ...
    @classmethod
    def read(cls, lines: list[str]) -> ParseBuffer: ...
    @staticmethod
    def convert_leading_tabs(string: str) -> str: ...

class Paragraph(BlockToken):
    setext_pattern: ClassVar[re.Pattern[str]]
    parse_setext: ClassVar[bool]
    children: list[SpanToken]
    @overload
    def __new__(cls, lines: SetextHeading) -> SetextHeading: ...
    @overload
    def __new__(cls, lines: list[str]) -> Paragraph: ...
    def __init__(self, lines: list[str]) -> None: ...
    @staticmethod
    def start(line: str) -> bool: ...
    @classmethod
    def read(cls, lines) -> SetextHeading | list[str]: ...
    @classmethod
    def is_setext_heading(cls, line: str) -> re.Match[str] | None: ...

class BlockCode(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    language: Literal['']
    children: tuple[span_token.RawText]
    def __init__(self, lines: list[str]) -> None: ...
    @property
    def content(self) -> str: ...
    @staticmethod
    def start(line: str) -> bool: ...
    @classmethod
    def read(cls, lines: list[str]) -> list[str]: ...
    @staticmethod
    def strip(string: str) -> str: ...

class CodeFence(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    language: str
    children: tuple[span_token.RawText]
    def __init__(self, match: tuple[list[str], tuple[int, str, str]]) -> None: ...
    @property
    def content(self) -> str: ...
    @classmethod
    def start(cls, line: str) -> bool: ...
    @classmethod
    def read(cls, lines: list[str]) -> tuple[list[str], tuple[int, str, str]]: ...

# List().start is int | None, while List.start() is a classmethod.
class _ListStart(Protocol):
    def __call__(self, line: str) -> re.Match[str] | None: ...
class _ListStartDescriptor:
    @overload
    def __get__(self, instance: None, owner: object) -> _ListStart: ...
    @overload
    def __get__(self, instance: List, owner: object) -> int | None: ...
    def __set__(self, instance: List, value: int | None) -> None: ...
_ListMarker: TypeAlias = tuple[int, str, str] | None

class List(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    children: list[ListItem]
    loose: bool
    def __init__(self, matches: tuple[ParseBuffer, int, str]) -> None: ...

    start: ClassVar[_ListStartDescriptor]
    @classmethod
    def read(cls, lines: Paragraph) -> list[tuple[ParseBuffer, int, str]]: ...
    @staticmethod
    def same_marker_type(leader, other): ...

class ListItem(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    continuation_pattern: ClassVar[re.Pattern[str]]

    leader: str
    prepend: int
    children: list[BlockToken]
    loose: bool
    def __init__(self, parse_buffer: ParseBuffer, prepend: int, leader: str) -> None: ...
    @classmethod
    def parse_continuation(cls, line: str, prepend: int) -> str | None: ...
    @staticmethod
    def other_token(line: str) -> bool: ...
    @classmethod
    def parse_marker(cls, line: str) -> _ListMarker: ...
    @classmethod
    def read(cls, lines: ParseBuffer, prev_marker: _ListMarker = None) -> tuple[tuple[ParseBuffer, int, str], _ListMarker]: ...

_TableAlign: TypeAlias = Literal[0, 1, None]

class Table(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    column_align: list[_TableAlign]
    header: TableRow
    children: list[TableRow]
    def __init__(self, lines: list[str]) -> None: ...
    @staticmethod
    def split_delimiter(delimiter: str) -> list[str]: ...
    @staticmethod
    def parse_align(column: str) -> _TableAlign: ...
    @staticmethod
    def start(line: str) -> bool: ...
    @staticmethod
    def read(lines: ParseBuffer) -> list[str]: ...

class TableRow(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    split_pattern: ClassVar[re.Pattern[str]]
    escaped_pipe_pattern: ClassVar[re.Pattern[str]]
    row_align: Incomplete
    children: list[TableCell]
    def __init__(self, line: list[str], row_align: list[_TableAlign] | None = None) -> None: ...

class TableCell(BlockToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    align: _TableAlign
    children: list[SpanToken]
    def __init__(self, content: str, align: _TableAlign = None) -> None: ...

_LabelDestTitle: TypeAlias = tuple[str, str, str]

class Footnote(BlockToken):
    def __new__(cls, _: Any) -> None: ...  # type: ignore
    @classmethod
    def start(cls, line: str) -> bool: ...
    @classmethod
    def read(cls, lines: ParseBuffer) -> list[_LabelDestTitle] | None: ...
    @classmethod
    def match_reference(cls, string: str, offset: int) -> tuple[int, _LabelDestTitle] | None: ...
    @classmethod
    def match_link_label(cls, string: str, offset: int) -> core_tokens._StartEndMatch | None: ...
    @classmethod
    def match_link_dest(cls, string: str, offset: int) -> core_tokens._StartEndMatch | None: ...
    @classmethod
    def match_link_title(cls, string: str, offset: int) -> core_tokens._StartEndMatch | None: ...
    @staticmethod
    def append_footnotes(matches: Iterable[_LabelDestTitle], root: Document) -> None: ...

class ThematicBreak(BlockToken):
    pattern: ClassVar[re.Pattern[str]]
    def __init__(self, _: object) -> None: ...
    @classmethod
    def start(cls, line: str) -> bool: ...
    @staticmethod
    def read(lines: list[str]) -> list[str]: ...

class HTMLBlock(BlockToken):
    multiblock: ClassVar[re.Pattern[str]]
    predefined: ClassVar[re.Pattern[str]]
    custom_tag: ClassVar[re.Pattern[str]]

    children: list[span_token.RawText]
    def __init__(self, lines: list[str]) -> None: ...
    @property
    def content(self) -> str: ...
    @classmethod
    def start(cls, line: list[str]) -> Literal[False, 1, 2, 3, 4, 5, 6, 7]: ...
    @classmethod
    def read(cls, lines: list[str]) -> list[str]: ...

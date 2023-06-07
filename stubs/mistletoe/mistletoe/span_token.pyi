import re
from typing import ClassVar

from mistletoe import token
from mistletoe.core_tokens import MatchObj
from mistletoe.span_tokenizer import ParseToken

def tokenize_inner(content: str) -> list[SpanToken]: ...
def add_token(token_cls: type[SpanToken], position: int = 1) -> None: ...
def remove_token(token_cls: type[SpanToken]) -> None: ...
def reset_tokens() -> None: ...

class SpanToken(token.Token):
    parse_inner: ClassVar[bool] = True
    parse_group: ClassVar[int] = 1
    precedence: ClassVar[int] = 5
    content: str
    def __init__(self, match: MatchObj) -> None: ...
    def __contains__(self, text: str) -> bool: ...
    @classmethod
    def find(cls, string: str) -> list[str]: ...

class CoreTokens(SpanToken):
    precedence: ClassVar[int] = 3
    def __new__(self, match: ParseToken) -> SpanToken: ...
    @classmethod
    def find(cls, string: str) -> list[MatchObj]: ...

class Strong(SpanToken):
    children: list[SpanToken]

class Emphasis(SpanToken):
    children: list[SpanToken]

class InlineCode(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 2
    children: tuple[RawText]
    def __init__(self, match: MatchObj) -> None: ...
    @classmethod
    def find(cls, string: str) -> list[MatchObj]: ...

class Strikethrough(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    children: list[SpanToken]

class Image(SpanToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    src: str
    title: str
    children: list[SpanToken]
    def __init__(self, match: MatchObj) -> None: ...

class Link(SpanToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    target: str
    title: str
    children: list[SpanToken]
    def __init__(self, match: MatchObj) -> None: ...

class AutoLink(SpanToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    children: tuple[RawText]
    target: str
    mailto: bool
    def __init__(self, match: MatchObj) -> None: ...

class EscapeSequence(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    precedence: ClassVar[int] = 2
    children: tuple[RawText]
    def __init__(self, match: MatchObj) -> None: ...
    @classmethod
    def strip(cls, string: str) -> str: ...

class LineBreak(SpanToken):
    repr_attributes: ClassVar[tuple[str, ...]]
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 0
    soft: bool
    content: str
    def __init__(self, match: MatchObj) -> None: ...

class RawText(SpanToken):
    content: str
    def __init__(self, content: str) -> None: ...

class HTMLSpan(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 0

class XWikiBlockMacroStart(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 1

class XWikiBlockMacroEnd(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 1

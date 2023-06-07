from _typeshed import Incomplete

from mistletoe import token

class SpanToken(token.Token):
    parse_inner: bool
    parse_group: int
    precedence: int
    content: Incomplete
    def __init__(self, match) -> None: ...
    def __contains__(self, text) -> bool: ...
    @classmethod
    def find(cls, string): ...

class CoreTokens(SpanToken):
    precedence: int
    def __new__(self, match): ...
    @classmethod
    def find(cls, string): ...

class Strong(SpanToken): ...
class Emphasis(SpanToken): ...

class InlineCode(SpanToken):
    pattern: Incomplete
    parse_inner: bool
    parse_group: int
    children: Incomplete
    def __init__(self, match) -> None: ...
    @classmethod
    def find(cls, string): ...

class Strikethrough(SpanToken):
    pattern: Incomplete

class Image(SpanToken):
    repr_attributes: Incomplete
    src: Incomplete
    title: Incomplete
    def __init__(self, match) -> None: ...

class Link(SpanToken):
    repr_attributes: Incomplete
    target: Incomplete
    title: Incomplete
    def __init__(self, match) -> None: ...

class AutoLink(SpanToken):
    repr_attributes: Incomplete
    pattern: Incomplete
    parse_inner: bool
    children: Incomplete
    target: Incomplete
    mailto: Incomplete
    def __init__(self, match) -> None: ...

class EscapeSequence(SpanToken):
    pattern: Incomplete
    parse_inner: bool
    precedence: int
    children: Incomplete
    def __init__(self, match) -> None: ...
    @classmethod
    def strip(cls, string): ...

class LineBreak(SpanToken):
    repr_attributes: Incomplete
    pattern: Incomplete
    parse_inner: bool
    parse_group: int
    soft: Incomplete
    content: str
    def __init__(self, match) -> None: ...

class RawText(SpanToken):
    content: Incomplete
    def __init__(self, content) -> None: ...

class HTMLSpan(SpanToken):
    pattern: Incomplete
    parse_inner: bool
    parse_group: int

class XWikiBlockMacroStart(SpanToken):
    pattern: Incomplete
    parse_inner: bool
    parse_group: int

class XWikiBlockMacroEnd(SpanToken):
    pattern: Incomplete
    parse_inner: bool
    parse_group: int

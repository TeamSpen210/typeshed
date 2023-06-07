import re
from collections import ChainMap
from collections.abc import Callable, Sequence
from typing import ClassVar, TypeAlias

from mistletoe.base_renderer import BaseRenderer
from mistletoe.block_token import BlockToken
from mistletoe.core_tokens import MatchObj
from mistletoe.span_token import SpanToken

class Program(BlockToken):
    children: list[SpanToken]
    def __init__(self, lines) -> None: ...

class Expr(SpanToken):
    @classmethod
    def find(cls, string: str) -> list[MatchObj]: ...

class Number(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    number: object
    def __init__(self, match) -> None: ...

class Variable(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    name: str
    def __init__(self, match: MatchObj) -> None: ...

class Whitespace(SpanToken):
    parse_inner: ClassVar[bool] = False
    def __new__(self, _) -> None: ...

_SchemeTokens: TypeAlias = Expr | Number | Variable | Whitespace
_Env: TypeAlias = ChainMap[str, object]

class Procedure:
    params: list[str]
    body: Sequence[_SchemeTokens]
    env: _Env
    def __init__(self, expr_token, body, env: _Env) -> None: ...

class Scheme(BaseRenderer[object]):
    render_map: dict[str, Callable[[_SchemeTokens], object]]
    env: _Env
    def __init__(self) -> None: ...
    def render_inner(self, token: _SchemeTokens) -> object: ...
    def render_expr(self, token: Expr) -> object: ...
    def render_number(self, token: Number) -> object: ...
    def render_variable(self, token: Variable) -> object: ...
    def define(self, *args: _SchemeTokens) -> None: ...
    def cond(self, *exprs: _SchemeTokens) -> object: ...
    def apply(self, proc: Procedure, args: SpanToken) -> object: ...

from typing import Callable, TypeAlias

from mistletoe.base_renderer import BaseRenderer
from mistletoe.token import Token

class ASTRenderer(BaseRenderer[str]):
    def render(self, token: Token) -> str: ...
    def __getattr__(self, name: str) -> Callable[[Token], str]: ...

_JSON: TypeAlias = dict[str, _JSON] | list[_JSON] | int | bool | float | str | None

def get_ast(token: Token) -> dict[str, _JSON]: ...

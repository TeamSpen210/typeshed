from collections.abc import Callable

from mistletoe.token import Token
from mistletoe.html_renderer import HTMLRenderer
from mistletoe import block_token

class TOCRenderer(HTMLRenderer):
    depth: int
    omit_title: bool
    filter_conds: list[Callable[[str], bool]]
    def __init__(self, depth: int = ..., omit_title: bool = ..., filter_conds=..., *extras: Token) -> None: ...
    @property
    def toc(self) -> block_token.List: ...
    def render_heading(self, token: block_token.Heading) -> str: ...
    @staticmethod
    def parse_rendered_heading(rendered: str) -> str: ...

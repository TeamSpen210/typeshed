from typing import ClassVar

from mistletoe import HTMLRenderer
from mistletoe.block_token import BlockCode
from mistletoe.token import Token
from pygments.formatters.html import HtmlFormatter

class PygmentsRenderer(HTMLRenderer):
    formatter: ClassVar[HtmlFormatter[str]]
    def __init__(self, *extras: Token, style: str = "default") -> None: ...
    def render_block_code(self, token: BlockCode) -> str: ...

from typing import TypeVar, overload

__version__: str
__all__ = ["html_renderer", "ast_renderer", "block_token", "block_tokenizer", "span_token", "span_tokenizer"]

from mistletoe.base_renderer import BaseRenderer
from mistletoe.block_token import Document as Document
from mistletoe.html_renderer import HTMLRenderer as HTMLRenderer

from . import ast_renderer, block_token, block_tokenizer, html_renderer, span_token, span_tokenizer

_T = TypeVar("_T")

@overload
def markdown(iterable: list[str]) -> str: ...
@overload
def markdown(iterable: list[str], renderer: type[BaseRenderer[_T]]) -> _T: ...

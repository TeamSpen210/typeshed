from typing import TypeVar, overload



__version__: str
__all__ = ['html_renderer', 'ast_renderer', 'block_token', 'block_tokenizer',
           'span_token', 'span_tokenizer']

from mistletoe.block_token import Document as Document
from mistletoe.html_renderer import HTMLRenderer as HTMLRenderer
from mistletoe.base_renderer import BaseRenderer

T = TypeVar('T')

@overload
def markdown(iterable: list[str]) -> str: ...
@overload
def markdown(iterable: list[str], renderer: BaseRenderer[T]) -> T: ...

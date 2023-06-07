from typing import ClassVar

from mistletoe.block_token import Document
from mistletoe.html_renderer import HTMLRenderer
from mistletoe.latex_renderer import LaTeXRenderer
from mistletoe.latex_token import Math

class MathJaxRenderer(HTMLRenderer, LaTeXRenderer):
    mathjax_src: ClassVar[str]
    def render_math(self, token: Math): ...
    def render_document(self, token: Document): ...

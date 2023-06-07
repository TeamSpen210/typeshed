from mistletoe.html_renderer import HTMLRenderer
from mistletoe.latex_renderer import LaTeXRenderer

class MathJaxRenderer(HTMLRenderer, LaTeXRenderer):
    mathjax_src: str
    def render_math(self, token): ...
    def render_document(self, token): ...

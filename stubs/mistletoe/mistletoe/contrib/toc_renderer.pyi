from _typeshed import Incomplete

from mistletoe.html_renderer import HTMLRenderer

class TOCRenderer(HTMLRenderer):
    depth: Incomplete
    omit_title: Incomplete
    filter_conds: Incomplete
    def __init__(self, depth: int = ..., omit_title: bool = ..., filter_conds=..., *extras) -> None: ...
    @property
    def toc(self): ...
    def render_heading(self, token): ...
    @staticmethod
    def parse_rendered_heading(rendered): ...

from _typeshed import Incomplete

from mistletoe import HTMLRenderer

class PygmentsRenderer(HTMLRenderer):
    formatter: Incomplete
    def __init__(self, *extras, style: str = ...) -> None: ...
    def render_block_code(self, token): ...

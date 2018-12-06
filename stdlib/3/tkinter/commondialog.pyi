from tkinter import Frame, _Window
from typing import Any, Mapping, Optional

class Dialog:
    command: str
    master: _Window
    options: Mapping[str, Any]
    def __init__(self, master: _Window=None, *, parent: _Window=None, **options): ...
    def show(self, **options) -> Any: ...

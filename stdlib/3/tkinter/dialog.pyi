from typing import Any, Dict, Union, Iterable, Mapping, Optional
from tkinter import Widget, Misc

DIALOG_ICON: str

class Dialog(Widget):
    widgetName: str = ...
    num: int = ...
    def __init__(
        self,
        master: Misc = None,
        cnf: Mapping[str, Union[str, Iterable[str]] = ..., 
        *,
        title: str='',
        text: str='',
        bitmap: str='',
        default: str='',
        strings: Iterable[str]=(),
    ) -> None: ...
    def destroy(self) -> None: ...

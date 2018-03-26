from typing import List, Union, TypeVar, Generic, Optional

from tkinter import *

class SimpleDialog:
    root: Toplevel
    message: Message
    frame: Frame
    num: int
    cancel: int
    default: int

    def __init__(
        self,
        master: Union[Toplevel, Tk],
        text: str='',
        buttons: List[str]=...,
        default: int=None,
        cancel: int=None,
        title: str=None,
        class_: str=None,
    ): ...
    def go(self) -> int: ...
    def return_event(self, event: Event) -> None: ...
    def wm_delete_window(self) -> None: ...
    def done(self, num: int) -> None: ...

ParentT = TypeVar('ParentT', Toplevel, Tk)

class Dialog(Toplevel, Generic[ParentT]):
    parent: ParentT
    result: None
    initial_focus: Optional[Misc]

    def __init__(self, parent: ParentT, title: str=None): ...
    def destroy(self) -> None: ...
    def body(self, master: Frame) -> Misc: ...
    def buttonbox(self) -> None: ...
    def ok(self, event: Event=None) -> None: ...
    def cancel(self, event: Event=None) -> None: ...
    def validate(self) -> bool: ...
    def apply(self) -> None:...

def askinteger(
    title: str,
    prompt: str,
    *,
    parent: Window=None,
    initialvalue: int=None,
    minvalue: int=None,
    maxvalue: int=None,
) -> int: ...

def askfloat(
    title: str,
    prompt: str,
    *,
    parent: Window=None,
    initialvalue: int=None,
    minvalue: int=None,
    maxvalue: int=None,
) -> float: ...

def askstring(
    title: str,
    prompt: str,
    *,
    parent: Window=None,
    initialvalue: int=None,
    minvalue: int=None,
    maxvalue: int=None,
) -> str: ...

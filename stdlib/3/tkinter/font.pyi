from tkinter import Tk, Toplevel

from typing import Tuple, Dict, Any, Union, Iterator, overload

NORMAL: str
ROMAN: str
BOLD: str
ITALIC: str

Window = Union[Tk, Toplevel]

def nametofont(name) -> 'Font': ...
def families(root: Tk=None, displayof: Window=None) -> Tuple[str]: ...
def names(root: Tk=None) -> Tuple[str]: ...

# The types for the config values.
ConfValue = Union[str, int, bool]

class Font:
    counter: Iterator[int]
    delete_font: bool
    name: str

    @overload
    def __init__(
        self,
        root: Tk=None,
        name: str=None,
        exists: bool=False,
        *,
        family: str=None,
        size: int=None,
        weight: str=None,
        slant: str=None,
        underline: bool=None,
        overstike: bool=None,
    ) -> None: ...
    @overload
    def __init__(
        self, 
        root: Tk=None, 
        font: Font=None, 
        name: str=None, 
        exists: bool=False,
    ) -> None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, key: str) -> ConfValue: ...
    def __setitem__(self, key: str, value: ConfValue) -> None: ...
    def __del__(self) -> None: ...

    def copy(self) -> Font: ...

    @overload
    def actual(self, option: str, displayof: Window=None) -> Any: ...
    @overload
    def actual(self, displayof: Window=None) -> Dict[str, ConfValue]: ...
     
    def cget(self, option: str) -> ConfValue: ...
    
    @overload
    def config(self) -> Dict[str, ConfValue]: ...
    @overload
    def config(
        self,
        *,
        family: str=None,
        size: int=None,
        weight: str=None,
        slant: str=None,
        underline: bool=None,
        overstike: bool=None,
    ) -> None: ...

    configure = config

    def measure(self, text: str, displayof: Window=None) -> int: ...
        
    @overload
    def metrics(self, _option: str, *, displayof: Window=None) -> int: ...
    @overload
    def metrics(self, displayof: Window=None) -> Dict[str, int]: ...

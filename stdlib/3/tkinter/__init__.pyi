from types import TracebackType
from typing import (
    Any, overload, Union, Optional,
    Dict, List, Tuple,
    Callable, Iterable, Type, NewType
)
from tkinter.constants import *  # noqa: F403
from tkinter.font import Font
from types import TracebackType

# Font values can be several values:
# * Font object
# * (family, size)
# * (family, size, bold/italic/underline/overstrike)
# * TK categories matching the OS (string)
_FontValue = Union[Font, Tuple[str, Union[str, int]], Tuple[str, Union[str, int], str], str]
_Padding = Union[float, Tuple[float, float]]
_Window = Union[Tk, TopLevel]

# The IDs given to callable functions.
_BindID = NewType('BindID', str)
# IDs for objects on canvases.
_CanvID = NewType('CanvID', int)
# Most of the time you can also pass a string tag.
_CanvTagOrID = Union[str, _CanvID]

class TclError(Exception):
    ...

wantobjects: Any
TkVersion: float
TclVersion: float
READABLE: int
WRITABLE: int
EXCEPTION: int

class Event:
    serial: int
    num: int
    focus: bool
    height: int
    width: int
    keycode: int
    state: int
    time: int
    x: int
    y: int
    x_root: int
    y_root: int
    char: str
    send_event: bool
    keysym: str
    keysym_num: int
    type: int
    widget: Misc
    delta: int

def NoDefaultRoot() -> None: ...

class Variable:
    def __init__(self, master: Misc = None, value: Any = None, name: str = None) -> None: ...
    def __del__(self) -> None: ...
    def __str__(self) -> str: ...
    def set(self, value: Any) -> None: ...
    def initialize(self, value: Any) -> None: ...
    def get(self) -> Any: ...
    def trace_variable(self, mode: str, callback: Callable) -> str: ...
    def trace(self, mode: str, callback: Callable) -> str: ...
    def trace_vdelete(self, mode: str, cbname: str) -> None: ...
    def trace_vinfo(self) -> list: ...
    def __eq__(self, other) -> bool: ...

class StringVar(Variable):
    def __init__(self, master: str=None, value: str=None, name: str=None) -> None: ...
    def get(self) -> str: ...
    def set(self, value: str) -> None: ...
    def initialize(self, value: str) -> None: ...

class IntVar(Variable):
    """Value holder for integer variables."""
    def __init__(self, master: str=None, value: int=None, name: str=None) -> None: ...
    def get(self) -> int: ...
    def set(self, value: int) -> None: ...
    def initialize(self, value: int) -> None: ...

class DoubleVar(Variable):
    def __init__(self, master: str=None, value: float=None, name: str=None) -> None: ...
    def get(self) -> float: ...
    def set(self, value: float) -> None: ...
    def initialize(self, value: float) -> None: ...

class BooleanVar(Variable):
    def __init__(self, master: str=None, value: bool=None, name: str=None) -> None: ...
    def get(self) -> bool: ...
    def set(self, value: bool) -> None: ...
    def initialize(self, value: bool) -> None: ...

def mainloop(n: int = ...) -> None: ...

def getint(x: str) -> int: ...
def getdouble(x: str) -> float: ...
def getboolean(s: bool) -> int: ...

class Misc:
    def destroy(self) -> None: ...
    def deletecommand(self, name: _BindID) -> None: ...
    def tk_strictMotif(self, boolean: int=None) -> bool: ...
    def tk_bisque(self) -> None: ...
    def tk_setPalette(
        self,
        *args: str,
        activeBackground: str=None,
        foreground: str=None,
        selectColor: str=None,
        activeForeground: str=None,
        highlightBackground: str=None,
        selectBackground: str=None,
        background: str=None,
        highlightColor: str=None,
        selectForeground: str=None,
        disabledForeground: str=None,
        insertBackground: str=None,
        troughColor: str=None
        ) -> None: ...
    def tk_menuBar(self, *args) -> None: ...
    def wait_variable(self, name: Union[str, Variable]= 'PY_VAR') -> None: ...
    def waitvar(self, name: Union[str, Variable]= 'PY_VAR') -> None: ...

    def wait_window(self, window: Misc=None) -> None: ...
    def wait_visibility(self, window: Misc=None) -> None: ...

    def setvar(self, name: str='PY_VAR', value: Any = '1') -> None: ...
    def getvar(self, name: str='PY_VAR') -> Any: ...

    def getint(self, s) -> int: ...
    def getdouble(self, s) -> float: ...
    def getboolean(self, s) -> bool: ...

    def focus_set(self) -> None: ...
    def focus(self) -> None: ...
    def focus_force(self) -> None: ...
    def focus_get(self) -> Misc: ...
    def focus_displayof(self) -> Misc: ...
    def focus_lastfor(self) -> Misc: ...
    def tk_focusFollowsMouse(self) -> None: ...
    def tk_focusNext(self) -> Misc: ...
    def tk_focusPrev(self) -> Misc: ...

    def after(self, ms: int, func: Callable[..., Any]=None, *args: Any) -> str: ...
    def after_idle(self, func: Callable[..., Any], *args: Any) -> str: ...
    def after_cancel(self, id: str) -> None: ...
    def bell(self, displayof=Misc) -> None: ...

    def clipboard_get(
        self,
        *,
        type: str='STRING',
        window: _Window=None
    ) -> str: ...
    def clipboard_clear(self, *, displayof: Misc=...) -> None: ...
    def clipboard_append(self, string: str, *, displayof: Misc=...) -> None: ...

    def grab_current(self) -> Optional[Misc]: ...
    def grab_release(self) -> None: ...
    def grab_set(self) -> None: ...
    def grab_set_global(self) -> None: ...
    def grab_status(self) -> Optional[str]: ...

    def option_add(
        self,
        pattern: str,
        value: str,
        priority: Union[int, str]=80,
    ) -> None: ...
    def option_clear(self) -> None: ...
    def option_get(self, name: str, className: Union[str, Type[Misc]]) -> str: ...
    def option_readfile(
        self,
        fileName: str,
        priority: Union[int, str]=80,
    ) -> None: ...

    def selection_clear(
        self,
        *,
        displayof: Misc=None,
        selection: str='PRIMARY'
    ) -> None: ...
    def selection_get(
        self,
        *,
        displayof: Misc=None,
        selection: str='PRIMARY',
        type: str='STRING'
    ) -> None: ...
    def selection_handle(
        self,
        command: Callable[[int, int], str],
        *,
        selection: str='PRIMARY',
        type: str='STRING'
    ) -> None: ...
    def selection_own(self, **kw) -> None: ...
    def selection_own_get(self, **kw) -> None: ...

    def send(self, interp, cmd, *args) -> None: ...

    def lower(self, belowThis: Misc=None) -> None: ...
    def tkraise(self, aboveThis: Misc=None) -> None: ...
    def lift(self, aboveThis: Misc=None) -> None: ...

    def winfo_atom(self, name, displayof=0) -> None: ...
    def winfo_atomname(self, id, displayof=0) -> None: ...
    def winfo_cells(self) -> int: ...
    def winfo_children(self) -> List[Misc]: ...
    def winfo_class(self) -> str: ...
    def winfo_colormapfull(self) -> bool: ...
    def winfo_containing(
        self,
        rootX: int,
        rootY: int,
        displayof: Misc=...,
    ) -> Optional[Misc]: ...
    def winfo_depth(self) -> int: ...
    def winfo_exists(self) -> int: ...
    def winfo_fpixels(self, number) -> None: ...
    def winfo_geometry(self) -> str: ...
    def winfo_height(self) -> None: ...
    def winfo_id(self) -> None: ...
    def winfo_interps(self, displayof=0) -> None: ...
    def winfo_ismapped(self) -> None: ...
    def winfo_manager(self) -> None: ...
    def winfo_name(self) -> None: ...
    def winfo_parent(self) -> None: ...
    def winfo_pathname(self, id, displayof=0) -> None: ...
    def winfo_pixels(self, number) -> None: ...
    def winfo_pointerx(self) -> int: ...
    def winfo_pointerxy(self) -> Tuple[int, int]: ...
    def winfo_pointery(self) -> int: ...
    def winfo_reqheight(self) -> int: ...
    def winfo_reqwidth(self) -> int: ...
    def winfo_rgb(self, color) -> None: ...
    def winfo_rootx(self) -> int: ...
    def winfo_rooty(self) -> int: ...
    def winfo_screen(self) -> None: ...
    def winfo_screencells(self) -> None: ...
    def winfo_screendepth(self) -> None: ...
    def winfo_screenheight(self) -> int: ...
    def winfo_screenmmheight(self) -> int: ...
    def winfo_screenmmwidth(self) -> int: ...
    def winfo_screenvisual(self) -> None: ...
    def winfo_screenwidth(self) -> int: ...
    def winfo_server(self) -> None: ...
    def winfo_toplevel(self) -> None: ...
    def winfo_viewable(self) -> bool: ...
    def winfo_visual(self) -> str: ...
    def winfo_visualid(self) -> None: ...
    def winfo_visualsavailable(self, includeids=0) -> None: ...
    def winfo_vrootheight(self) -> int: ...
    def winfo_vrootwidth(self) -> int: ...
    def winfo_vrootx(self) -> int: ...
    def winfo_vrooty(self) -> int: ...
    def winfo_width(self) -> int: ...
    def winfo_x(self) -> int: ...
    def winfo_y(self) -> int: ...

    def update(self) -> None: ...
    def update_idletasks(self) -> None: ...

    @overload
    def bindtags(self, tagList: List[str]) -> None: ...
    @overload
    def bindtags(self) -> List[str]: ...
    @overload
    def bind(
        self,
        sequence: str=None,
    ) -> Union[_BindID, List[_BindID]]: ...
    @overload
    def bind(
        self,
        sequence: str=None,
        func: Callable[[Event], Optional[str]]=None,
        add: str=None,
    ) -> _BindID: ...
    def unbind(self, sequence: str, funcid: _BindID=None) -> None: ...
    def bind_all(
        self,
        sequence: str=None,
        func: Callable[[Event], Optional[str]]=None,
        add: str=None,
    ) -> _BindID: ...
    def unbind_all(self, sequence: _BindID) -> None: ...
    def bind_class(
        self,
        className: str,
        sequence: str=None,
        func: Callable[[Event], Optional[str]]=None,
        add: str=None,
    ) -> _BindID: ...
    def unbind_class(self, className: str, sequence: str) -> None: ...

    def mainloop(self, n=0) -> None: ...
    def quit(self) -> None: ...

    def nametowidget(self, name: str) -> Misc: ...
    register = ...  # type: Any

    # We can't really specify any useful return value for this, 
    # it depends on the widget.
    @overload
    def configure(self) ->  Dict[str, Any]: ...
    @overload
    def configure(self, cnf: Dict[str, Any]=None, **kw: Any) -> None: ...
        
    @overload
    def config(self) ->  Dict[str, Any]: ...
    @overload
    def config(self, cnf: Dict[str, Any]=None, **kw: Any) -> None: ...

    def cget(self, key: str) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...

    def keys(self) -> List[str]: ...

    @overload
    def pack_propagate(self, flag: bool) -> None: ...
    @overload
    def pack_propagate(self) -> bool: ...

    @overload
    def propagate(self, flag: bool) -> None: ...
    @overload
    def propagate(self) -> bool: ...

    def pack_slaves(self) -> List[Misc]: ...
    def slaves(self) -> List[Misc]: ...

    def place_slaves(self) -> List[Misc]: ...

    def grid_anchor(self, anchor: str=None) -> None: ...

    @overload
    def grid_bbox(self) -> Optional[Tuple[int, int, int, int]]: ...
    @overload
    def grid_bbox(self, column: int, row: int) -> Optional[
        Tuple[int, int, int, int]]: ...
    @overload
    def grid_bbox(self, column: int, row: int, col2: int, row2: int) -> Optional[
        Tuple[int, int, int, int]]: ...

    def grid_columnconfigure(
        self,
        index: int,
        cnf: Dict[str, int]={},
        *,
        minsize: float=None,
        weight: int=None,
        pad: Union[float, Tuple[float, float]]=None
    ) -> None: ...
    def grid_location(self, x, y) -> None: ...

    @overload
    def grid_propagate(self) -> bool: ...
    @overload
    def grid_propagate(self, flag: bool) -> None: ...

    def grid_rowconfigure(
        self,
        index: int,
        cnf: Dict[str, int]={},
        *,
        minsize: float=None,
        weight: int=None,
        pad: Union[float, Tuple[float, float]]=None
    ) -> None: ...
    
    def grid_size(self) -> Tuple[int, int]: ...

    columnconfigure = grid_columnconfigure
    rowconfigure = grid_rowconfigure
    size = grid_size
    bbox = grid_bbox
    anchor = grid_anchor
    propagate = pack_propagate

    def grid_slaves(self, row: int=None, column: int=None) -> List[Misc]: ...

    def event_add(self, virtual: str, *sequences: str) -> None: ...
    def event_delete(self, virtual: str, *sequences: str) -> None: ...
    def event_generate(self, sequence: str, **kw: Any) -> None: ...
    def event_info(self, virtual: str=None) -> None: ...

    def image_names(self) -> List[str]: ...
    def image_types(self) -> List[str]: ...

class CallWrapper:
    func: Callable[..., Any]
    subst: Optional[Callable[..., Iterable[Any]]]
    widget: Misc
    def __init__(
        self,
        func: Callable[..., Any],
        subst: Optional[Callable[..., Iterable[Any]]],
        widget: Misc,
    ) -> None: ...
    def __call__(self, *args: Any) -> Any: ...

class XView:
    @overload
    def xview(self) -> Tuple[float, float]: ...
    @overload
    def xview(self, *args: float) -> None: ...

    def xview_moveto(self, fraction: float) -> None: ...
    def xview_scroll(self, number: float, what: str) -> None: ...

class YView:
    @overload
    def yview(self) -> Tuple[float, float]: ...
    @overload
    def yview(self, *args: float) -> None: ...

    def yview_moveto(self, fraction: float) -> None: ...
    def yview_scroll(self, number: float, what: str) -> None: ...

class Wm:
    @overload
    def wm_aspect(self) -> Tuple[int, int, int, int]: ...
    @overload
    def wm_aspect(self, minNumer: int, minDenom: int, maxNumer: int, maxDenom: int) -> None: ...
    aspect = wm_aspect

    # Platform-specfic values
    @overload
    def wm_attributes(self) -> Tuple[Any, ...]: ...
    @overload
    def wm_attributes(self, *args: Any) -> None: ...
    attributes = wm_attributes

    def wm_client(self, name: str=None) -> str: ...
    client = wm_client

    @overload
    def wm_colormapwindows(self) -> List[Misc]: ...
    @overload
    def wm_colormapwindows(self, *wlist: Misc) -> None: ...
    colormapwindows = wm_colormapwindows

    @overload
    def wm_command(self) -> str: ...
    @overload
    def wm_command(self, value: Callable[[], None]) -> None: ...
    command = wm_command

    def wm_deiconify(self) -> None: ...
    deiconify = wm_deiconify

    @overload
    def wm_focusmodel(self) -> str: ...
    @overload
    def wm_focusmodel(self, model: str=None) -> None: ...
    focusmodel = wm_focusmodel

    def wm_forget(self, window: _Window) -> None: ...
    forget = wm_forget

    def wm_frame(self) -> str: ...
    frame = wm_frame

    @overload
    def wm_geometry(self) -> str: ...
    @overload
    def wm_geometry(self, newGeometry: str) -> None: ...
    geometry = wm_geometry

    def wm_grid(
        self,
        baseWidth: int=None,
        baseHeight: int=None,
        widthInc: int=None,
        heightInc: int=None,
    ) -> Tuple[int, int, int, int]: ...
    grid = wm_grid

    @overload
    def wm_group(self) -> str: ...
    @overload
    def wm_group(self, pathName: str) -> None: ...
    group = wm_group

    @overload
    def wm_iconbitmap(self) -> str: ...
    @overload
    def wm_iconbitmap(self, bitmap: str) -> None: ...
    # This can also be called like wm_iconbitmap(bitmap, default),
    # but bitmap won't be used.
    @overload
    def wm_iconbitmap(self, *, default: str) -> None: ...
    iconbitmap = wm_iconbitmap

    def wm_iconify(self) -> None: ...
    iconify = wm_iconify

    @overload
    def wm_iconmask(self) -> str: ...
    @overload
    def wm_iconmask(self, bitmap: str) -> None: ...
    iconmask = wm_iconmask

    def wm_iconname(self) -> str: ...
    @overload
    def wm_iconname(self, newName: str) -> None: ...
    iconname = wm_iconname

    def wm_iconphoto(self, default: bool=False, *args: str) -> None: ...
    iconphoto = wm_iconphoto

    @overload
    def wm_iconposition(self) -> Tuple[int, int]: ...
    @overload
    def wm_iconposition(self, x: int=None, y: int=None) -> None: ...
    iconposition = wm_iconposition

    @overload
    def wm_iconwindow(self) -> str: ...
    @overload
    def wm_iconwindow(self, pathName: Misc) -> None: ...
    iconwindow = wm_iconwindow

    def wm_manage(self, widget: Misc) -> None: ...
    manage = wm_manage

    @overload
    def wm_maxsize(self) -> Tuple[int, int]: ...
    @overload
    def wm_maxsize(self, width: int=None, height: int=None) -> None: ...
    maxsize = wm_maxsize

    @overload
    def wm_minsize(self) -> Tuple[int, int]: ...
    @overload
    def wm_minsize(self, width: int=None, height: int=None) -> None: ...
    minsize = wm_minsize

    @overload
    def wm_overrideredirect(self) -> bool: ...
    @overload
    def wm_overrideredirect(self, boolean: Union[bool, int]) -> None: ...
    overrideredirect = wm_overrideredirect

    @overload
    def wm_positionfrom(self) -> str: ...
    @overload
    def wm_positionfrom(self, who: str) -> None: ...
    positionfrom = wm_positionfrom

    @overload
    def wm_protocol(self) -> List[str]: ...
    @overload
    def wm_protocol(self, name: str) -> str: ...
    @overload
    def wm_protocol(self, name: str, func: Callable[[], None]=None) -> None: ...
    protocol = wm_protocol

    @overload
    def wm_resizable(self) -> Tuple[int, int]: ...
    @overload
    def wm_resizable(self, width: bool, height: bool) -> str: ...
    resizeable = wm_resizable

    @overload
    def wm_sizefrom(self) -> str: ...
    @overload
    def wm_sizefrom(self, who: str) -> None: ...
    sizefrom = wm_sizefrom

    @overload
    def wm_state(self) -> str: ...
    def wm_state(self, newstate: str=None) -> None: ...
    state = wm_state

    @overload
    def wm_title(self) -> str: ...
    @overload
    def wm_title(self, string: str) -> None: ...
    title = wm_title

    @overload
    def wm_transient(self) -> str: ...
    @overload
    def wm_transient(self, master: Union[Misc, str]=None) -> None: ...
    transient = wm_transient

    def wm_withdraw(self) -> None: ...
    withdraw = wm_withdraw

class Tk(Misc, Wm):
    master: None
    children: Dict[str, Any]
    tk: Any  # tk interpreter
    def __init__(self, screenName: str=None, baseName: str=None, className='', useTk: bool=1, sync: Any=0, use: Any=None) -> None: ...
    def loadtk(self) -> None: ...
    def destroy(self) -> None: ...
    def readprofile(self, baseName: str, className: str) -> None: ...
    def report_callback_exception(self, exc: Type[Exception], val: Exception, tb: TracebackType) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...

def Tcl(screenName: str = None, baseName: str = None, className: str = '', useTk: bool = 0) -> Tk: ...

class Pack:
    def pack_configure(self, cnf=Dict[str, Any], *, after: Misc=None, anchor: str='', before: Misc=None, expand: bool=False, fill: str=NONE, in_: Misc=None, ipadx: _Padding=None, ipady: _Padding=None, padx: _Padding=None, pady: _Padding=None, side: str=None) -> None: ...
    pack = pack_configure

    def pack_forget(self) -> None: ...
    def forget(self) -> None: ...
    def pack_info(self) -> None: ...
    def info(self) -> None: ...

    propagate = Misc.pack_propagate
    slaves = Misc.pack_slaves

class Place:
    def place_configure(self, cnf: Dict[str, Union[Misc, int, float, str]]=..., *, in_: Misc=None, x: int=None, y: int=None, relx: float=None, rely: float=None, anchor: str=None, width: int=None, height: int=None, relwidth: float=None, relheight: float=None, bordermode: str=None) -> None: ...
    place = configure = config = place_configure

    def place_forget(self) -> None: ...
    forget = place_forget

    def place_info(self) -> Dict[str, Union[Misc, str]]: ...
    info = place_info
    slaves = Misc.place_slaves

class Grid:
    def grid_configure(self, cnf: Dict[str, Union[Misc, int, float, str]]=..., *, column: int=None, columnspan: int=None, in_: Misc=None, ipadx: _Padding=None, ipady: _Padding=None, padx: _Padding=None, pady: _Padding=None, row: int=None, rowspan: int=None, sticky: str=...) -> None: ...
    grid = configure = config = grid_configure

    bbox = grid_bbox = Misc.grid_bbox

    columnconfigure = grid_columnconfigure = Misc.grid_columnconfigure

    def grid_forget(self) -> None: ...
    forget = grid_forget

    def grid_remove(self) -> None: ...

    def grid_info(self) -> Dict[str, Union[Misc, str]]: ...
    info = grid_info

    location = grid_location = Misc.grid_location
    propagate = grid_propagate = Misc.grid_propagate
    rowconfigure = grid_rowconfigure = Misc.grid_rowconfigure
    size = grid_size = Misc.grid_size
    slaves = grid_slaves = Misc.grid_slaves

class BaseWidget(Misc):
    widgetName: str
    tk: Tk
    _w: str  # undocumented

    def __init__(
        self,
        master: Misc,
        widgetName: str,
        cnf: Mapping[Union[str, type], Any]=...,
        kw: Mapping[Union[str, type], Any]=...,
        extra: Iterable[Any]=...,
    ) -> None: ...
    def destroy(self) -> None: ...

class Widget(BaseWidget, Pack, Place, Grid):
    pass

class Toplevel(BaseWidget, Wm):
    def __init__(
        self,
        master: _Window,
        cnf=Mapping[str, Any],
        *,
        class_: str='TopLevel',
        menu: Menu=None,
        bd: int=0,
        borderwidth: int=0,
        colormap: str='',
        container: bool=False,
        cursor: str='arrow',
        height: int=None,
        width: int=None,
        background: str='',
        bg: str='',
        highlightbackground: str='',
        highlightcolor: str='',
        highlightthickness: int=1,
        relief: str=FLAT,
        takefocus: int=1,
        visual: str='',
    ) -> None: ...

class Button(Widget):
    def __init__(
        self,
        master: Misc=None,
        cnf: Mapping[str, Any]=..., 
        *,
        activebackground: str=None,
        activeforeground: str=None,
        background: str=None,
        foreground=None,
        disabledforeground: str=None,

        anchor: str=None,
        bitmap: str=None,
        borderwidth: int=None,
        cursor: str=None,
        font: _FontValue=None,
        highlightbackground: str=None,
        highlightcolor: str=None,
        highlightthickness: Union[str, int]=None,
        image: Image=None,

        justify: str=None,
        padx: _Padding=None,
        pady: _Padding=None,

        relief: str=None,
        overrelief: str=None,

        repeatdelay: int=None,
        repeatinterval: int=None,

        takefocus: bool=None,

        text: str=None,
        textvariable: StringVar=None,

        underline: int=None,
        command: Callable[[], None]=None,
        compound: str=None,
        default: str=None,
        state: str=None,

        width: int=None,
        height: int=None,
        wraplength: int=None,
        ) -> None: ...
    def flash(self) -> None: ...
    def invoke(self) -> None: ...

class Canvas(Widget, XView, YView):
    def __init__(
        self,
        master: Misc=None,
        cnf: Dict[str, Any]=...,
        *,
        bg: str=None,
        background: str=None,

        bd: str=None,
        borderwidth: str=None,

        cursor: str=None,

        highlightbackground: str=None,
        highlightcolor: str=None,
        hightlightthickness: Union[str, int]=None,

        insertbackground: str=None,
        insertborderwidth: Union[str, int]=None,
        insertofftime: Union[str, int]=None,
        insertontime: Union[str, int]=None,
        insertwidth: str=None,

        width: int=None,
        height: int=None,
        relief: str=None,

        selectbackground: str=None,
        selectborderwidth: Union[str, int]=None,
        selectforeground: str=None,

        closeenough: float=None,
        confine: bool=None,
        scrollregion: Tuple[float, float, float, float]=None,
        state: str=None,
        
        xscrollcommand: Callable[[float, float], None]=None,
        xscrollincrement: Union[float, str]=None,
        yscrollcommand: Callable[[float, float], None]=None,
        yscrollincrement: Union[float, str]=None,
    ) -> None: ...
    def addtag(self, *args: str) -> None: ...
    def addtag_above(self, newtag: str, tagOrId: _CanvTagOrID) -> None: ...
    def addtag_all(self, newtag: str) -> None: ...
    def addtag_below(self, newtag: str, tagOrId: _CanvTagOrID) -> None: ...
    def addtag_closest(
        self, 
        newtag: str, 
        x: float, 
        y: float, 
        halo: float=None, 
        start: str=None,
    ) -> None: ...
    
    def addtag_enclosed(
        self, 
        newtag: str, 
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> None: ...
    
    def addtag_overlapping(
        self, 
        newtag: str, 
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> None: ...
    
    def addtag_withtag(self, newtag: str, tagOrId: _CanvTagOrID) -> None: ...
    def bbox(
        self,
        *args: str,
    ) -> Optional[Tuple[float, float, float, float]]: ...

    def tag_unbind(self, tagOrId: _CanvTagOrID, sequence: str, funcid: _BindID=None) -> None: ...
    def tag_bind(
        self,
        tagOrId: _CanvTagOrID,
        sequence: str=None,
        func: Callable[[Event], Optional[str]]=None,
        add: bool=None
    ) -> _BindID: ...

    def canvasx(self, screenx: int, gridspacing: int=None) -> float: ...
    def canvasy(self, screeny: int, gridspacing: int=None) -> float: ...
    @overload
    def coords(self, _id: str) -> List[float]: ...
    @overload
    def coords(self, _id: str, *args: float) -> None: ...


    def create_arc(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        extent: float=None,
        start: float=None,
        style: str=None,

        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...
    @overload
    def create_bitmap(
        self,
        x: float,
        y: float,
        *,
        background: str=None,
        activebackground: str=None,
        disabledbackground: str=None,

        bitmap: str=None,
        activebitmap: str=None,
        disabledbitmap: str=None,

        foreground: str=None,
        activeforeground: str=None,
        disabledforeground: str=None,

        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> _CanvID: ...
    @overload
    def create_bitmap(
        self,
        xy: Tuple[float, float],
        *,
        background: str=None,
        activebackground: str=None,
        disabledbackground: str=None,

        bitmap: str=None,
        activebitmap: str=None,
        disabledbitmap: str=None,

        foreground: str=None,
        activeforeground: str=None,
        disabledforeground: str=None,

        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> _CanvID: ...

    @overload
    def create_image(
        self,
        x: float,
        y: float,
        *,
        image: Image=None,
        activebitmap: Image=None,
        disabledbitmap: Image=None,

        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> _CanvID: ...
    @overload
    def create_image(
        self,
        xy: Union[List[float], Tuple[float, float]],
        *,
        image: Image=None,
        activebitmap: Image=None,
        disabledbitmap: Image=None,
        # Standard:
        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> _CanvID: ...

    @overload
    def create_line(
        self,
        *args: float,
        arrow: str=None,
        arrowshape: Tuple[float, float, float]=None,
        capstyle: str=None,
        joinstyle: str=None,
        smoothmethod: Union[str, bool]=None,
        splinesteps: int=None,

        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...
    @overload
    def create_line(
        self,
        args: Union[List[float], Tuple[float, ...]],
        *,
        arrow: str=None,
        arrowshape: Tuple[float, float, float]=None,
        capstyle: str=None,
        joinstyle: str=None,
        smoothmethod: Union[str, bool]=None,
        splinesteps: int=None,

        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...

    @overload
    def create_oval(
        self,
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        *,
        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        offset: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...
    @overload
    def create_oval(
        self,
        xy: Union[List[float], Tuple[float, float, float, float]],
        *,
        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        offset: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...

    def create_polygon(
        self,
        *args: Union[float, List[float], Tuple[float, ...]],
        joinstyle: str=None,
        smooth: Union[str, bool]=None,
        splinesteps: int=None,

        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        offset: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...

    @overload
    def create_rectangle(
        self,
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        *,
        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        offset: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...
    @overload
    def create_rectangle(
        self,
        xy: Union[List[float], Tuple[float, float, float, float]],
        *,
        dash: str=None,
        activedash: str=None,
        disableddash: str=None,
        dashoffset: int=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        outline: str=None,
        activeoutline: str=None,
        disabledoutline: str=None,
        offset: str=None,
        outlineoffset: str=None,

        outlinestipple: str=None,
        activeoutlinestipple: str=None,
        disabledoutlinestipple: str=None,
        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,

        width: Union[float, str]=None,
        activewidth: Union[float, str]=None,
        disabledwidth: Union[float, str]=None,
    ) -> _CanvID: ...

    @overload
    def create_text(
        self,
        x: float,
        y: float,
        *,
        angle: float=None,
        font: _FontValue=None,
        justify: str=None,
        text: str=None,
        underline: int=None,
        width: int=None,

        anchor: str=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,
    ) -> str: ...
    @overload
    def create_text(
        self,
        xy: Union[List[float], Tuple[float, float]],
        *,
        angle: float=None,
        font: _FontValue=None,
        justify: str=None,
        text: str=None,
        underline: int=None,
        width: int=None,

        anchor: str=None,

        fill: str=None,
        activefill: str=None,
        disabledfill: str=None,

        stipple: str=None,
        activestipple: str=None,
        disabledstipple: str=None,

        state: str=None,
        tags: List[str]=None,
    ) -> str: ...

    @overload
    def create_window(
        self,
        x: float,
        y: float,
        *,
        width: Union[float, str]=None,
        height: Union[float, str]=None,
        window: Misc=None,

        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> str: ...
    @overload
    def create_window(
        self,
        xy: Union[List[float], Tuple[float, float]],
        *,
        width: Union[float, str]=None,
        height: Union[float, str]=None,
        window: Misc=None,

        anchor: str=None,
        state: str=None,
        tags: List[str]=None,
    ) -> str: ...

    def dchars(self, *args: str) -> None: ...
    def delete(self, *args: str) -> None: ...
    def dtag(self, *args: str) -> None: ...
    def find(self, *args: str) -> Tuple[_CanvID]: ...
    def find_above(self, tagOrId: _CanvTagOrID) -> Tuple[_CanvID]: ...
    def find_all(self) -> Tuple[_CanvID]: ...
    def find_below(self, tagOrId: _CanvTagOrID) -> Tuple[_CanvID]: ...
    def find_closest(self, x, y, halo=None, start=None) -> None: ...
    def find_enclosed(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> Tuple[_CanvID]: ...
    def find_overlapping(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> Tuple[_CanvID]: ...
    def find_withtag(self, tagOrId: _CanvTagOrID) -> Tuple[_CanvID]: ...

    @overload
    def focus(self) -> _CanvID: ...
    @overload
    def focus(self, _arg: str) -> None: ... # focus('')
    @overload
    def focus(self, *args: _CanvTagOrID) -> None: ...

    def gettags(self, *args: _CanvTagOrID) -> Tuple[str]: ...
    def icursor(self, _tagOrID: _CanvTagOrID, _index: Union[str, int]) -> None: ...
    def index(self, _tagOrID: _CanvTagOrID, _index: Union[str, int], _x: float, _y:float) -> int: ...

    @overload
    def insert(self, _tagOrID: _CanvTagOrID, _index: Union[str, int], _string: str) -> None: ...
    @overload
    def insert(self, _tagOrID: _CanvTagOrID, _index: Tuple[float, float], _string: Tuple[float, float]) -> None: ...

    def itemcget(self, tagOrId: _CanvTagOrID, option: str) -> Any: ...
    def itemconfigure(
        self,
        tagOrId: _CanvTagOrID,
        cnf: Dict[str, Any]=None,
        # Union of all the create_*'s keyword arguments:
        activebackground: str=None,
        activebitmap: Union[str, Image]=None,
        activedash: str=None,
        activefill: str=None,
        activeforeground: str=None,
        activeoutline: str=None,
        activeoutlinestipple: str=None,
        activestipple: str=None,
        activewidth: Union[float, str]=None,
        anchor: str=None,
        angle: float=None,
        arrow: str=None,
        arrowshape: Tuple[float, float, float]=None,
        background: str=None,
        bitmap: str=None,
        capstyle: str=None,
        dash: str=None,
        dashoffset: int=None,
        disabledbackground: str=None,
        disabledbitmap: Union[str, Image]=None,
        disableddash: str=None,
        disabledfill: str=None,
        disabledforeground: str=None,
        disabledoutline: str=None,
        disabledoutlinestipple: str=None,
        disabledstipple: str=None,
        disabledwidth: Union[float, str]=None,
        extent: float=None,
        fill: str=None,
        font: _FontValue=None,
        foreground: str=None,
        height: Union[float, str]=None,
        image: Image=None,
        joinstyle: str=None,
        justify: str=None,
        offset: str=None,
        outline: str=None,
        outlineoffset: str=None,
        outlinestipple: str=None,
        smooth: Union[str, bool]=None,
        smoothmethod: Union[str, bool]=None,
        splinesteps: int=None,
        start: float=None,
        state: str=None,
        stipple: str=None,
        style: str=None,
        tags: List[str]=None,
        text: str=None,
        underline: int=None,
        width: Union[float, str, int]=None,
        window: Misc=None,
    ) -> None: ...
    itemconfig = itemconfigure

    def tag_lower(self, _items: _CanvTagOrID, _below: _CanvTagOrID=None) -> None: ...
    lower = tag_lower
    def move(self, _items: _CanvTagOrID, _x: float, _y: float) -> None: ...
    def postscript(
        self,
        cnf: Dict[str, Any],
        *,
        channel: str,
        colormap: str,
        colormode: str,
        file: str,
        fontmap: str,
        height: int,
        pageanchor: str,
        pageheight: Union[str, float],
        pagewidth: Union[str, float],
        pagex: Union[str, float],
        pagey: Union[str, float],
        rotate: bool,
        width: int,
        x: float,
        y: float,
    ) -> None: ...
    def tag_raise(self, _items: _CanvTagOrID, _above: _CanvTagOrID=None) -> None: ...
    lift = tag_raise

    def scale(
        self,
        _tagOrId: _CanvTagOrID,
        _xOrigin: float,
        _yOrigin: float,
        _xScale: float,
        _yScale: float,
    ) -> None: ...

    def scan_mark(self, x: float, y: float) -> None: ...
    def scan_dragto(self, x: float, y: float, gain: float=10) -> None: ...

    def select_adjust(self, tagOrId: _CanvTagOrID, index: str) -> None: ...
    def select_clear(self) -> None: ...
    def select_from(self, tagOrId: _CanvTagOrID, index: str) -> None: ...
    def select_item(self) -> None: ...
    def select_to(self, tagOrId: _CanvTagOrID, index: str) -> None: ...
    def type(self, tagOrId: StringVar) -> Optional[str]: ...

class Checkbutton(Widget):
    def __init__(
        self,
        master: Misc=None,
        cnf: Dict[str, Union[str, int, float, Image, _Padding, StringVar]]=...,
        *,
        activebackground: str=None,
        activeforeground: str=None,
        anchor: str=None,
        background: str=None,
        bg: str=None,
        bitmap: str=None,
        borderwidth: int=None,
        bd: int=None,
        compound: str=None,
        cursor: str=None,
        disabledforeground: str=None,
        font: _FontValue=None,
        foreground: str=None,
        highlightbackground: str=None,
        highlightcolor: str=None,
        highlightthickness: float=None,
        image: Image=None,
        justify: str=None,
        padx: _Padding=None,
        pady: _Padding=None,
        relief: str=None,
        takefocus: str=None,
        text: str=None,
        textvariable: StringVar=None,
        underline: int=None,
        wraplength: int=None,
    ) -> None: ...
    def deselect(self) -> None: ...
    def flash(self) -> None: ...
    def invoke(self) -> None: ...
    def select(self) -> None: ...
    def toggle(self) -> None: ...

class Entry(Widget, XView):
    def __init__(self, master=None, cnf=..., **kw) -> None: ...
    def delete(self, first: Union[int, str], last: Union[int, str]=None) -> None: ...
    def get(self) -> str: ...
    def icursor(self, index: Union[int, str]) -> None: ...
    def index(self, index: Union[int, str]) -> None: ...
    def insert(self, index: Union[int, str], string: str) -> None: ...
    def scan_mark(self, x: int) -> None: ...
    def scan_dragto(self, x: int) -> None: ...

    def selection_adjust(self, index: Union[int, str]) -> None: ...
    select_adjust = selection_adjust

    def selection_clear(self) -> None: ...
    select_clear = selection_clear
    def selection_from(self, index: Union[int, str]) -> None: ...
    select_from = selection_from
    def selection_present(self) -> bool: ...
    select_present = selection_present
    def selection_range(self, start: Union[int, str], end: Union[int, str]) -> None: ...
    select_range = selection_range
    def selection_to(self, index: Union[int, str]) -> None: ...
    select_to = selection_to

class Frame(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Label(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Listbox(Widget, XView, YView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def activate(self, index): ...
    def bbox(self, index): ...
    def curselection(self): ...
    def delete(self, first, last: Optional[Any] = ...): ...
    def get(self, first, last: Optional[Any] = ...): ...
    def index(self, index): ...
    def insert(self, index, *elements): ...
    def nearest(self, y): ...
    def scan_mark(self, x, y): ...
    def scan_dragto(self, x, y): ...
    def see(self, index): ...
    def selection_anchor(self, index): ...
    select_anchor = ...  # type: Any
    def selection_clear(self, first, last: Optional[Any] = ...): ...  # type: ignore
    select_clear = ...  # type: Any
    def selection_includes(self, index): ...
    select_includes = ...  # type: Any
    def selection_set(self, first, last: Optional[Any] = ...): ...
    select_set = ...  # type: Any
    def size(self): ...
    def itemcget(self, index, option): ...
    def itemconfigure(self, index, cnf: Optional[Any] = ..., **kw): ...
    itemconfig = ...  # type: Any

class Menu(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def tk_popup(self, x, y, entry: str = ...): ...
    def tk_bindForTraversal(self): ...
    def activate(self, index): ...
    def add(self, itemType, cnf=..., **kw): ...
    def add_cascade(self, cnf=..., **kw): ...
    def add_checkbutton(self, cnf=..., **kw): ...
    def add_command(self, cnf=..., **kw): ...
    def add_radiobutton(self, cnf=..., **kw): ...
    def add_separator(self, cnf=..., **kw): ...
    def insert(self, index, itemType, cnf=..., **kw): ...
    def insert_cascade(self, index, cnf=..., **kw): ...
    def insert_checkbutton(self, index, cnf=..., **kw): ...
    def insert_command(self, index, cnf=..., **kw): ...
    def insert_radiobutton(self, index, cnf=..., **kw): ...
    def insert_separator(self, index, cnf=..., **kw): ...
    def delete(self, index1, index2: Optional[Any] = ...): ...
    def entrycget(self, index, option): ...
    def entryconfigure(self, index, cnf: Optional[Any] = ..., **kw): ...
    entryconfig = ...  # type: Any
    def index(self, index) -> None: ...
    def invoke(self, index) -> None: ...
    def post(self, x, y) -> None: ...
    def type(self, index) -> None: ...
    def unpost(self) -> None: ...
    def xposition(self, index) -> None: ...
    def yposition(self, index) -> None: ...

class Menubutton(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Message(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Radiobutton(Widget):
    def __init__(
        self,
        master=None,
        cnf=...,
        *,
        cursor: str='',
        takefocus: int=1,
        variable: Variable,
        value: Any,

        compound: str=NONE,
        text: str='',
        textvariable: StringVar=None,
        underline: int=-1,
        wraplength: int=None,

        anchor=CENTER,
        justify: str=CENTER,
        command: Callable[[], Any],
        bitmap: str='',
        image: Image=None,
        selectimage: Image=None,
        font: _FontValue=None,
        indicatoron: int=0,
        state: str=NORMAL,

        offrelief: str=RAISED,
        overrelief: str=FLAT,
        relief: str=FLAT,

        padx: _Padding=1,
        pady: _Padding=1,

        height=1,
        width: int=None,
        borderwidth: int=2,
        bd: int=2,
        highlightthickness=1,

        background='',
        bg='',
        foreground='',
        fg='',
        activebackground='',
        activeforeground='',
        disabledforeground: str='',
        highlightbackground='',
        highlightcolor='',
        selectcolor=None
    ) -> None: ...
    def deselect(self) -> None: ...
    def flash(self) -> None: ...
    def invoke(self) -> None: ...
    def select(self) -> None: ...

class Scale(Widget):
    def __init__(
        self,
        master: Misc=None,
        cnf=...,
        *,
        digits: int=0,
        from_: float=0.0,
        to: float=100.0,
        tickinterval: float=0.0,
        repeatdelay: int=300,
        repeatinterval: int=100,
        resolution: float=-1.0,
        showvalue: int=1,

        length: int=100,
        width: int=15,
        relief: str=FLAT,
        sliderlength: int=30,
        sliderrelief: str=RAISED,

        variable: Union[IntVar, DoubleVar, StringVar]=None,
        font: _FontValue=None,
        label: str='',
        cursor='',
        orient: str=VERTICAL,
        state: str=NORMAL,
        takefocus: int=1,

        borderwidth: Union[int, str]=2,
        bd: Union[int, str]=2,

        troughcolor: str=None,
        activebackground: str=None,
        background: str=None,
        bg: str=None,
        foreground: str=None,
        fg: str=None,
        highlightbackground: str=None,
        highlightcolor: str=None,
        highlightthickness: int=1
    ) -> None: ...
    def get(self) -> float: ...
    def set(self, value: float) -> None: ...
    def coords(self, value: float=None) -> Tuple[int, int]: ...
    def identify(self, x: int, y: int) -> str: ...

class Scrollbar(Widget):
    def __init__(
        self,
        master=None,
        cnf=...,
        *,
        takefocus: int=1,
        cursor: str=None,

        command: Callable[..., None]=None,
        jump: int=0,
        orient: str=VERTICAL,
        repeatdelay: int=300,
        repeatinterval: int=100,

        activerelief: str=SUNKEN,
        relief: str=SUNKEN,
        width: int=16,

        elementborderwidth: int=-1,
        borderwidth: int=2,
        bd: int=2,
        highlightthickness=1,

        background='',
        bg='',
        activebackground='',
        activeforeground='',
    ) -> None: ...

    @overload
    def activate(self) -> str: ...
    @overload
    def activate(self, index: str) -> None: ...

    def delta(self, deltax: int, deltay: int) -> float: ...
    def fraction(self, x: int, y: int) -> float: ...
    def identify(self, x: int, y: int) -> str: ...
    def get(self) -> Tuple[float, float]: ...
    def set(self, first: float, last: float) -> None: ...

class Text(Widget, XView, YView):
    def __init__(self, master=None, cnf=..., **kw) -> None: ...

    def bbox(
        self,
        index: Union[int, str]
    ) -> Optional[Tuple[int, int, int, int]]: ...
    def compare(
        self,
        index1: Union[int, str],
        op: str,
        index2: Union[int, str]
    ) -> None: ...
    def count(self, index1, index2, *args) -> None: ...
    def debug(self, boolean=None) -> None: ...
    def delete(self, index1: Union[float, str], index2: Union[float, str]=None) -> None: ...
    def dlineinfo(
        self,
        index: Union[int, str]
    ) -> Optional[Tuple[int, int, int, int]]: ...
    def dump(self, index1, index2=None, command=None, **kw) -> None: ...
    def edit(self, *args) -> None: ...

    @overload
    def edit_modified(self) -> bool: ...
    @overload
    def edit_modified(self, arg: bool) -> None: ...

    def edit_redo(self) -> None: ...
    def edit_reset(self) -> None: ...
    def edit_separator(self) -> None: ...
    def edit_undo(self) -> None: ...

    def get(self, index1, index2=None) -> None: ...
    def image_cget(self, index, option) -> None: ...
    def image_configure(self, index, cnf=None, **kw) -> None: ...
    def image_create(self, index, cnf=..., **kw) -> None: ...
    def image_names(self) -> Tuple[str, ...]: ...
    def index(self, index) -> None: ...
    def insert(self, index, chars, *args) -> None: ...

    @overload
    def mark_gravity(self, markName: str) -> str: ...
    @overload
    def mark_gravity(self, markName: str, direction: str) -> None: ...

    def mark_names(self) -> Tuple[str, ...]: ...
    def mark_set(self, markName: str, index: Union[int, str]) -> None: ...
    def mark_unset(self, *markNames: str) -> None: ...
    def mark_next(self, index: Union[int, str]) -> str: ...
    def mark_previous(self, index: Union[int, str]) -> str: ...
    def peer_create(self, newPathName, cnf=..., **kw) -> None: ...
    def peer_names(self) -> None: ...
    def replace(self, index1, index2, chars, *args) -> None: ...
    def scan_mark(self, x: int, y: int) -> None: ...
    def scan_dragto(self, x: int, y: int) -> None: ...
    def search(
        self,
        pattern: str,
        index: Union[int, str],
        stopindex: Union[int, str]=None,
        forwards: bool=True,
        backwards: bool=False,
        exact: bool=True,
        regexp: bool=False,
        nocase: bool=False,
        count: IntVar=None,
        elide: bool=False,
    ) -> str: ...
    def see(self, index: Union[int, str]) -> None: ...
    def tag_add(
        self,
        tagName: str,
        index1: Union[int, str],
        *args: Union[int, str]
    ) -> None: ...
    def tag_unbind(self, tagName: str, sequence, funcid: int=None) -> None: ...
    def tag_bind(self, tagName: str, sequence, func, add=None) -> None: ...
    def tag_cget(self, tagName: str, option: str) -> Any: ...

    def tag_configure(
        self,
        tagName: str,
        cnf=None,
        *,
        borderwidth: int=0,
        font: _FontValue=None,
        justify: str=LEFT,
        overstrike: int=0,
        underline: int=0,
        relief: str=FLAT,
        wrap: str=CHAR,
        tabs=Tuple[Union[int, str], ...],

        offset: Union[int, str]=0,
        rmargin: Union[int, str]=0,
        lmargin1: Union[int, str]=0,
        lmargin2: Union[int, str]=0,
        spacing1: Union[int, str]=0,
        spacing2: Union[int, str]=0,
        spacing3: Union[int, str]=0,

        background='',
        foreground='',
        bgstipple='',
        fgstipple=''
    ) -> Dict[str, Any]: ...
    tag_config = tag_configure

    def tag_delete(self, *tagNames: str) -> None: ...
    def tag_lower(self, tagName: str, belowThis: str=None) -> None: ...
    def tag_names(self, index: Union[int, str]=None) -> Tuple[str, ...]: ...
    def tag_nextrange(self, tagName: str, index1: Union[int, str], index2: Union[int, str]=None) -> Tuple[int, int]: ...
    def tag_prevrange(self, tagName: str, index1: Union[int, str], index2: Union[int, str]=None) -> Tuple[int, int]: ...
    def tag_raise(self, tagName: str, aboveThis: str=None) -> None: ...
    def tag_ranges(self, tagName: str) -> Tuple[int, ...]: ...
    def tag_remove(self, tagName: str, index1: Union[int, str], index2: Union[int, str]=None) -> None: ...

    def window_cget(self, index: Union[int, str], option: str) -> None: ...
    def window_configure(self, index: Union[int, str], cnf=None, **kw) -> None: ...
    window_config = window_configure

    def window_create(
        self,
        index: Union[int, str],
        cnf=...,
        *,
        window: Misc=None,
        create: Callable[[], Misc]=None,
        align: str=CENTER,
        padx: _Padding=0,
        pady: _Padding=0,
        stretch: bool=0
    ) -> None: ...

    def window_names(self) -> List[str]: ...
    def yview_pickplace(self, *what) -> None: ...

class _setit:
    def __init__(self, var, value, callback=None) -> None: ...
    def __call__(self, *args) -> None: ...

class OptionMenu(Menubutton):
    widgetName: str
    menuname: str
    def __init__(self, master, variable, value, *values, **kwargs) -> None: ...
    def __getitem__(self, name: str) -> Misc: ...
    def destroy(self) -> None: ...

class Image:
    name: str
    tk: Tk
    def __init__(
        self,
        imgtype: str,
        name: str=None,
        master: Misc=None,
        cnf: Dict[str, Any]=...,
        **kw: Dict[str, Any]
    ) -> None: ...
    def __del__(self) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def configure(self, **kw) -> None: ...
    def config(self, **kw) -> None: ...

    def type(self) -> str: ...
    def height(self) -> int: ...
    def width(self) -> int: ...

class PhotoImage(Image):
    def __init__(
        self,
        name: str=None,
        cnf=...,
        master: Misc=None,
        *,
        data: str=None,
        file: str=None,
        format: str=None,
        palette: Union[str, float]=None,
        gamma: float=1.0,
        height: int=0,
        width: int=0
    ) -> None: ...
    def blank(self) -> None: ...
    def cget(self, option: str) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def copy(self) -> PhotoImage: ...
    def zoom(self, x: float, y: float='') -> PhotoImage: ...
    def subsample(self, x: float, y: float='') -> PhotoImage: ...
    def get(self, x: int, y: int) -> Tuple[int, int, int]: ...
    def put(
        self,
        data: Any,
        # (x1, y1) or (x1, y1, x2, y2)
        to: Union[Tuple[int, int], Tuple[int, int, int, int]]=None,
    ) -> None: ...
    def write(
        self,
        filename: str,
        format: str=None,
        from_coords: Union[Tuple[int, int], Tuple[int, int, int, int]]=None,
    ) -> None: ...

class BitmapImage(Image):
    def __init__(
        self,
        name=None,
        cnf=...,
        master=None,
        *,
        data: str=None,
        file: str=None,
        background: str=None,
        foreground: str=None,
        maskdata: str=None,
        maskfile: str=None
    ) -> None: ...

def image_names() -> Tuple[str, ...]: ...
def image_types() -> Tuple[str, ...]: ...

class Spinbox(Widget, XView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def bbox(self, index): ...
    def delete(self, first, last: Optional[Any] = ...): ...
    def get(self): ...
    def icursor(self, index): ...
    def identify(self, x, y): ...
    def index(self, index): ...
    def insert(self, index, s): ...
    def invoke(self, element): ...
    def scan(self, *args): ...
    def scan_mark(self, x): ...
    def scan_dragto(self, x): ...
    def selection(self, *args): ...
    def selection_adjust(self, index): ...
    def selection_clear(self): ...
    def selection_element(self, element: Optional[Any] = ...): ...

class LabelFrame(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class PanedWindow(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def add(self, child, **kw): ...
    def remove(self, child: Misc) -> None: ...
    def remove(self, child: Misc) -> None: ...
    def identify(self, x, y): ...
    def proxy(self, *args): ...
    def proxy_coord(self): ...
    def proxy_forget(self): ...
    def proxy_place(self, x, y): ...
    def sash(self, *args): ...
    def sash_coord(self, index): ...
    def sash_mark(self, index): ...
    def sash_place(self, index, x, y): ...
    def panecget(self, child, option): ...
    def paneconfigure(self, tagOrId, cnf: Optional[Any] = ..., **kw): ...
    def paneconfig(self, tagOrId, cnf: Optional[Any] = ..., **kw): ...
    def panes(self): ...

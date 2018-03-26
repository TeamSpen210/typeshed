from tkinter.commondialog import Dialog
from tkinter import Misc

from typing import Tuple

class Chooser(Dialog):
    command: str

def askcolor(
    color: Tuple[int, int, int]=None,
    *,
    title: str=None,
    parent: Misc=None
) -> Tuple[Tuple[float, float, float], str]: ...

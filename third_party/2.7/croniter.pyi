# Stubs for croniter.croniter (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class croniter:
    MONTHS_IN_YEAR = ... # type: Any
    RANGES = ... # type: Any
    DAYS = ... # type: Any
    ALPHACONV = ... # type: Any
    LOWMAP = ... # type: Any
    bad_length = ... # type: Any
    tzinfo = ... # type: Any
    cur = ... # type: Any
    exprs = ... # type: Any
    expanded = ... # type: Any
    def __init__(self, expr_format, start_time=None): ...
    def get_next(self, ret_type=...): ...
    def get_prev(self, ret_type=...): ...
    def get_current(self, ret_type=...): ...
    def __iter__(self): ...
    __next__ = ... # type: Any
    def all_next(self, ret_type=...): ...
    def all_prev(self, ret_type=...): ...
    iter = ... # type: Any
    def is_leap(self, year): ...

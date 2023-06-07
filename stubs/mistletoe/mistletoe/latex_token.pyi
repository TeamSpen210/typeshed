import re
from typing import ClassVar

import mistletoe.span_token as span_token

class Math(span_token.SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    parse_inner: ClassVar[bool] = False
    parse_group: ClassVar[int] = 0

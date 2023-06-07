import re
from typing import ClassVar

from mistletoe.core_tokens import MatchObj
from mistletoe.html_renderer import HTMLRenderer
from mistletoe.span_token import SpanToken

class GithubWiki(SpanToken):
    pattern: ClassVar[re.Pattern[str]]
    target: str
    def __init__(self, match: MatchObj) -> None: ...

class GithubWikiRenderer(HTMLRenderer):
    def __init__(self) -> None: ...
    def render_github_wiki(self, token: GithubWiki) -> str: ...

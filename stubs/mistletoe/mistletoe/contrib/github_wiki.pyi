from _typeshed import Incomplete

from mistletoe.html_renderer import HTMLRenderer
from mistletoe.span_token import SpanToken

class GithubWiki(SpanToken):
    pattern: Incomplete
    target: Incomplete
    def __init__(self, match) -> None: ...

class GithubWikiRenderer(HTMLRenderer):
    def __init__(self) -> None: ...
    def render_github_wiki(self, token): ...

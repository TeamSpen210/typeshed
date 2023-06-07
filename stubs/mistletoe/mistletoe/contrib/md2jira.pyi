from _typeshed import Incomplete

usageString: Incomplete
helpString: str

class CommandLineParser:
    def __init__(self) -> None: ...

class MarkdownToJIRA:
    version: str
    options: dict[str, str]
    def __init__(self) -> None: ...
    def run(self, optlist: list[tuple[str, str]], args: list[str]) -> None: ...

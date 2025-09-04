from typing import Any, Protocol


class OutputHandler(Protocol):
    def display_output(self, content: Any): ...

from typing import Protocol


class OutputHandler(Protocol):
    def display_output(self, content: str): ...

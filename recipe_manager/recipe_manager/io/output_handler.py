from dataclasses import dataclass
from typing import Protocol


@dataclass
class OutputHandler(Protocol):
    def display_output(self, content: str): ...

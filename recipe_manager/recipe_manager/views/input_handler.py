from dataclasses import dataclass
from typing import Protocol


@dataclass
class InputHandler(Protocol):
    def get_input(self, prompt: str) -> str: ...

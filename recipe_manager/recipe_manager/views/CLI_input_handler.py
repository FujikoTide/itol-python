from dataclasses import dataclass
from typing import Protocol


@dataclass
class CLIInputHandler(Protocol):
    def get_input(self, prompt: str) -> str:
        return input(prompt)

    # add helper functions for validation

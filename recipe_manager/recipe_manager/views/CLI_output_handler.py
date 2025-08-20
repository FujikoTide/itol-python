from dataclasses import dataclass
from .console import console


@dataclass
class CLIOutputHandler:
    def display_output(self, content: str) -> None:
        console.print(content)

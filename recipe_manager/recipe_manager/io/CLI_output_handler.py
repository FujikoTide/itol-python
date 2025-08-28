from dataclasses import dataclass
from recipe_manager.views.console import console


@dataclass
class CLIOutputHandler:
    def display_output(self, content: str) -> None:
        console.print(f"{content}")

from dataclasses import dataclass
from typing import Any
from recipe_manager.views.console import console


@dataclass
class CLIOutputHandler:
    def display_output(self, content: Any) -> None:
        console.print(content)

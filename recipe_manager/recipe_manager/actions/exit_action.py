from recipe_manager.io.output_handler import OutputHandler
from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction


@dataclass(kw_only=True)
class ExitAction(BaseMenuAction):
    output_handler: OutputHandler

    name: str = "Exit"
    doc: str = "Exit the program."

    def execute(self):
        self.output_handler.display_output("[violet]Exiting application...[/]")
        exit()

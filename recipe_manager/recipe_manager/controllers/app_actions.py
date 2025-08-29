from recipe_manager.io.output_handler import OutputHandler
from dataclasses import dataclass


@dataclass
class AppActions:
    output_handler: OutputHandler

    def exit_program(self):
        self.output_handler.display_output("[violet]Exiting application...[/]")
        exit()

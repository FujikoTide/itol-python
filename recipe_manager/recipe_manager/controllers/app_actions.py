from recipe_manager.views import OutputHandler
from dataclasses import dataclass


@dataclass
class AppActions:
    output_handler: OutputHandler

    def exit_program(self):
        self.output_handler.display_output("Exiting application...")
        exit()

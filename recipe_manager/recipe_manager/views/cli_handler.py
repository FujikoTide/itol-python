from dataclasses import dataclass
from .input_handler import InputHandler


@dataclass
class CLIHandler(InputHandler):
    def get_input(self) -> None:
        pass

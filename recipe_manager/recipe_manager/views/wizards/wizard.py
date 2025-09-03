from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from typing import Protocol


class Wizard(Protocol):
    input_handler: InputHandler
    output_handler: OutputHandler

    def run(self) -> BaseMenuAction: ...

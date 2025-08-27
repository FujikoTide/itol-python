from recipe_manager.views import InputHandler, OutputHandler
from dataclasses import dataclass
from recipe_manager._types import Ingredient


@dataclass
class AddIngredientWizard:
    input_handler: InputHandler
    output_handler: OutputHandler

    def run(self) -> Ingredient:
        self.output_handler.display_output("Starting New Ingredient Wizard")
        name = self.input_handler.get_input("Enter ingredient name: ")
        quantity = self.input_handler.get_input("Enter quantity: ")
        unit = self.input_handler.get_input("Enter unit of measurement: ")

        new_ingredient = (name, quantity, unit)
        return new_ingredient

from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from dataclasses import dataclass
from recipe_manager.models.ingredient import Ingredient


@dataclass
class AddIngredientWizard:
    input_handler: InputHandler
    output_handler: OutputHandler

    def run(self) -> Ingredient:
        self.output_handler.display_output(
            "[orange1][magenta1]-[/][medium_orchid1]-[/][plum1]-[/] Starting New Ingredient Wizard [plum1]-[/][medium_orchid1]-[/][magenta1]-[/][/]"
        )
        name = self.input_handler.get_string("[orange1]Enter ingredient name:[/] ")
        quantity = self.input_handler.get_float("[orange1]Enter quantity:[/] ")
        unit = self.input_handler.get_string("[orange1]Enter unit of measurement:[/] ")

        new_ingredient = Ingredient(name, quantity, unit)
        return new_ingredient

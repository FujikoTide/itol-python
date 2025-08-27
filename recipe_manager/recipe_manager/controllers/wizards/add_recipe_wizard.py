from recipe_manager.views import InputHandler, OutputHandler
from recipe_manager.models import Recipe
from .add_ingredient_wizard import AddIngredientWizard


from dataclasses import dataclass


@dataclass
class AddRecipeWizard:
    input_handler: InputHandler
    output_handler: OutputHandler

    def run(self) -> Recipe:
        self.output_handler.display_output("--- Starting New Recipe Wizard ---")

        name = self.input_handler.get_input("Enter recipe name: ")
        description = self.input_handler.get_input("Enter a description: ")
        instructions = self.input_handler.get_input("Enter instructions: ")

        ingredient_wizard = AddIngredientWizard(self.input_handler, self.output_handler)
        ingredients = []
        ingredients.append(ingredient_wizard.run())

        new_recipe = Recipe(name, description, instructions, ingredients)
        self.output_handler.display_output(f"Added recipe: {new_recipe.name}")
        return new_recipe

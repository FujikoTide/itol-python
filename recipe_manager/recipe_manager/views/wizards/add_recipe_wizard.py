from recipe_manager.core.menu_action import MenuAction
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.recipe import Recipe
from recipe_manager.models.recipe_manager import RecipeManager
from .add_ingredient_wizard import AddIngredientWizard
from recipe_manager.utils.widgets.recipe_table import DisplayTable
from dataclasses import dataclass


@dataclass
class AddRecipeWizard:
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    recipe_table: DisplayTable

    def run(self) -> MenuAction:
        self.output_handler.display_output(
            "[orange1][green]-[/][bright_yellow]-[/][red1]-[/] Starting New Recipe Wizard [red1]-[/][bright_yellow]-[/][green]-[/][/]"
        )

        name = self.input_handler.get_string("[orange1]Enter recipe name:[/] ")
        description = self.input_handler.get_string("[orange1]Enter a description:[/] ")
        instructions = self.input_handler.get_string("[orange1]Enter instructions:[/] ")

        ingredient_wizard = AddIngredientWizard(self.input_handler, self.output_handler)
        ingredients = []
        while True:
            choice = self.input_handler.get_yes_no(
                "[orange1]Would you like to add an ingredient?[/] "
            )
            if not choice:
                break
            ingredient = ingredient_wizard.run()
            ingredients.append(ingredient)
            self.recipe_table.display_ingredients(ingredients)

        new_recipe = Recipe(name, description, instructions, ingredients)

        def action_method():
            return self.recipe_manager.add_recipe(new_recipe)

        self.recipe_table.display_recipe(new_recipe)
        self.output_handler.display_output(
            f"[bright_green]Recipe added: [bold dark_orange]{new_recipe.name}[/].[/]"
        )
        return MenuAction("Add Recipe", action_method, None)

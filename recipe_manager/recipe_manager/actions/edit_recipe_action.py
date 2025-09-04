from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.models.recipe import Recipe
from recipe_manager.views.wizards.add_ingredient_wizard import AddIngredientWizard
from recipe_manager.utils.widgets.display_table import DisplayTable


@dataclass(kw_only=True)
class EditRecipeAction(BaseMenuAction):
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    display_table: DisplayTable

    name: str = "Edit Recipe"
    doc: str = "Edit a recipe in the collection."

    def execute(
        self,
    ) -> None:
        self.output_handler.display_output(
            "[orange1][dark_orange]-[/][gold1]-[/][deep_pink2]-[/] Edit Recipe [deep_pink2]-[/][gold1]-[/][dark_orange]-[/][/]"
        )

        recipe_name = self.input_handler.get_string(
            "[orange1]Enter name of recipe to edit:[/] "
        )

        old_recipe = self.recipe_manager.get_recipe(recipe_name)
        if not old_recipe:
            self.output_handler.display_output(
                f"[violet]Recipe not found: [bold dark_orange]{recipe_name}[/]. No action has been taken.[/]"
            )
            return

        name = old_recipe.name
        description = self.input_handler.get_string("[orange1]Enter a description:[/] ")
        instructions = self.input_handler.get_string("[orange1]Enter instructions:[/] ")

        ingredient_wizard = AddIngredientWizard(self.input_handler, self.output_handler)
        ingredients = {}
        while True:
            choice = self.input_handler.get_yes_no(
                "[orange1]Would you like to add an ingredient?[/] "
            )
            if not choice:
                break
            ingredient = ingredient_wizard.run()
            ingredients[ingredient.name] = ingredient
            self.display_table.display_ingredients(ingredients)

        new_recipe = Recipe(name, description, instructions, ingredients)

        updated_recipe = self.recipe_manager.add_recipe(new_recipe)
        if updated_recipe:
            self.display_table.display_recipe(updated_recipe)
            self.output_handler.display_output(
                f"[bright_green]Recipe edited: [bold dark_orange]{updated_recipe.name}[/].[/]"
            )
        else:
            self.output_handler.display_output(
                f"[bright_red]An unexpected error has occurred when editing [bold dark_orange]{recipe_name}[/].[/]"
            )

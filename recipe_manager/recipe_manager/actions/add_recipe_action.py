from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.recipe import Recipe
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.utils.widgets.display_table import DisplayTable
from recipe_manager.views.wizards.add_ingredient_wizard import AddIngredientWizard


@dataclass(kw_only=True)
class AddRecipeAction(BaseMenuAction):
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    display_table: DisplayTable

    name: str = "Add Recipe"
    doc: str = "Add a new recipe to the collection."

    def execute(self) -> None:
        self.output_handler.display_output(
            "[orange1][green]-[/][bright_yellow]-[/][red1]-[/] Starting New Recipe Wizard [red1]-[/][bright_yellow]-[/][green]-[/][/]"
        )

        name = self.input_handler.get_string("[orange1]Enter recipe name:[/] ")
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
        result = self.recipe_manager.add_recipe(new_recipe)

        if isinstance(result, Recipe):
            self.display_table.display_recipe(new_recipe)
            self.output_handler.display_output(
                f"[bright_green]Recipe added: [bold dark_orange]{result.name}[/].[/]"
            )
        else:
            self.output_handler.display_output("[bright_red]Failed to add recipe.[/]")

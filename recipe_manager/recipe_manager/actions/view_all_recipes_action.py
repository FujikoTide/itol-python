from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.utils.widgets.display_table import DisplayTable


@dataclass(kw_only=True)
class ViewAllRecipesAction(BaseMenuAction):
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    display_table: DisplayTable

    name: str = "View Recipes"
    doc: str = "View all recipes in the collection."

    def execute(self) -> None:
        self.output_handler.display_output(
            "[orange1][pale_green1]-[/][light_goldenrod2]-[/][light_coral]-[/] View All Recipes [light_coral]-[/][light_goldenrod2]-[/][pale_green1]-[/][/]"
        )
        all_recipes = self.recipe_manager.get_all_recipes()
        if not all_recipes:
            self.output_handler.display_output("[violet]No recipes have been saved.[/]")
            return

        for recipe in all_recipes.values():
            self.display_table.display_recipe(recipe)

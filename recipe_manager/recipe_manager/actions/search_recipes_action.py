from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.utils.widgets.display_table import DisplayTable


@dataclass(kw_only=True)
class SearchRecipesAction(BaseMenuAction):
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    display_table: DisplayTable

    name: str = "Search Recipes"
    doc: str = "Find recipes in the collection that contain your search term."

    def execute(self) -> None:
        self.output_handler.display_output(
            "[orange1][pale_green1]-[/][light_goldenrod2]-[/][light_coral]-[/] Search Recipes [light_coral]-[/][light_goldenrod2]-[/][pale_green1]-[/][/]"
        )

        search_term = self.input_handler.get_string("[orange1]Enter search term:[/] ")
        matched_recipes = self.recipe_manager.search_recipes(search_term)
        if not matched_recipes:
            self.output_handler.display_output(
                f"[violet]No recipes have matched [bold dark_orange]{search_term}[/].[/]"
            )
            return

        for recipe in matched_recipes.values():
            self.display_table.display_recipe(recipe)

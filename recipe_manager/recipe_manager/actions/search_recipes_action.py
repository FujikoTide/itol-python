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
            "[orange1][green]-[/][bright_yellow]-[/][red1]-[/] Search Recipes [red1]-[/][bright_yellow]-[/][green]-[/][/]"
        )

        # [orange1][cyan1]-[/][magenta]-[/][purple]-[/] Search Recipes [purple]-[/][magenta]-[/][cyan1]-[/]
        # [orange1][dark_orange]-[/][gold1]-[/][deep_pink2]-[/] Search Recipes [deep_pink2]-[/][gold1]-[/][dark_orange]-[/]
        # [orange1][dark_orange3]-[/][sandy_brown]-[/][burly_wood]-[/] Search Recipes [burly_wood]-[/][sandy_brown]-[/][dark_orange3]-[/]
        # [orange1][deep_pink4]-[/][dark_violet]-[/][deep_sky_blue4]-[/] Search Recipes [deep_sky_blue4]-[/][dark_violet]-[/][deep_pink4]-[/]
        # [orange1][light_cyan2]-[/][light_sky_blue2]-[/][steel_blue]-[/] Search Recipes [steel_blue]-[/][light_sky_blue2]-[/][light_cyan2]-[/]
        # [orange1][tan]-[/][sandy_brown]-[/][dark_olive_green]-[/] Search Recipes [dark_olive_green]-[/][sandy_brown]-[/][tan]-[/]
        # [orange1][pale_green1]-[/][light_goldenrod2]-[/][light_coral]-[/] Search Recipes [light_coral]-[/][light_goldenrod2]-[/][pale_green1]-[/]

        search_term = self.input_handler.get_string("[orange1]Enter search term:[/] ")
        matched_recipes = self.recipe_manager.search_recipes(search_term)
        if not matched_recipes:
            self.output_handler.display_output(
                f"No recipes have matched {search_term}."
            )
            return

        for recipe in matched_recipes.values():
            self.display_table.display_recipe(recipe)

from dataclasses import dataclass
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.utils.widgets.display_table import DisplayTable


@dataclass(kw_only=True)
class DeleteRecipeAction(BaseMenuAction):
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    display_table: DisplayTable

    name: str = "Delete Recipe"
    doc: str = "Delete a recipe from the collection"

    def execute(
        self,
    ) -> None:
        self.output_handler.display_output(
            "[orange1][green]-[/][bright_yellow]-[/][red1]-[/] Starting New Recipe Wizard [red1]-[/][bright_yellow]-[/][green]-[/][/]"
        )

        recipe_name = self.input_handler.get_string(
            "[orange1]Enter name of recipe to delete:[/] "
        )

        # redo colours here for error/ success
        result = self.recipe_manager.get_recipe(recipe_name)
        if not result:
            self.output_handler.display_output(
                f"[bright_green]Recipe not found: [bold dark_orange]{recipe_name}[/]. No action has been taken.[/]"
            )
            return
        deleted_recipe = self.recipe_manager.delete_recipe(recipe_name)
        if deleted_recipe:
            self.display_table.display_recipe(deleted_recipe)
            self.output_handler.display_output(
                f"[bright_green]Recipe deleted successfully: [bold dark_orange]{deleted_recipe.name}[/].[/]"
            )
        else:
            self.output_handler.display_output(
                f"[bright_green]An unexpected error has occurred when deleting {recipe_name}.[/]"
            )

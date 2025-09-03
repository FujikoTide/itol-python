from recipe_manager.io.CLI_input_handler import CLIInputHandler
from recipe_manager.io.CLI_output_handler import CLIOutputHandler
from recipe_manager.views.menu_handler import MenuHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.utils.widgets.CLI_display_table import CLIDisplayTable
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.actions.add_recipe_action import AddRecipeAction
from recipe_manager.actions.delete_recipe_action import DeleteRecipeAction
from recipe_manager.actions.edit_recipe_action import EditRecipeAction
from recipe_manager.actions.exit_action import ExitAction

menu_handler = MenuHandler()
input_handler = CLIInputHandler()
output_handler = CLIOutputHandler()
recipe_manager = RecipeManager()
display_table = CLIDisplayTable()


def create_menu_actions() -> list[BaseMenuAction]:
    return [
        AddRecipeAction(
            input_handler=input_handler,
            output_handler=output_handler,
            display_table=display_table,
            recipe_manager=recipe_manager,
        ),
        DeleteRecipeAction(
            input_handler=input_handler,
            output_handler=output_handler,
            display_table=display_table,
            recipe_manager=recipe_manager,
        ),
        EditRecipeAction(
            input_handler=input_handler,
            output_handler=output_handler,
            display_table=display_table,
            recipe_manager=recipe_manager,
        ),
        ExitAction(output_handler=output_handler),
    ]

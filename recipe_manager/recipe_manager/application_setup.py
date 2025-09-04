from recipe_manager.io.CLI_input_handler import CLIInputHandler
from recipe_manager.io.CLI_output_handler import CLIOutputHandler
from recipe_manager.models.JSON_handler import JSONHandler
from recipe_manager.views.menu_handler import MenuHandler
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.utils.widgets.CLI_display_table import CLIDisplayTable
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.actions.add_recipe_action import AddRecipeAction
from recipe_manager.actions.delete_recipe_action import DeleteRecipeAction
from recipe_manager.actions.edit_recipe_action import EditRecipeAction
from recipe_manager.actions.view_all_recipes_action import ViewAllRecipesAction
from recipe_manager.actions.search_recipes_action import SearchRecipesAction
from recipe_manager.actions.exit_action import ExitAction

menu_handler = MenuHandler()
output_handler = CLIOutputHandler()
input_handler = CLIInputHandler(output_handler)
storage_handler = JSONHandler(output_handler)
recipe_manager = RecipeManager(storage_handler)
display_table = CLIDisplayTable(output_handler)


def create_menu_actions() -> list[BaseMenuAction]:
    common_dependencies = {
        "input_handler": input_handler,
        "output_handler": output_handler,
        "display_table": display_table,
        "recipe_manager": recipe_manager,
    }
    return [
        AddRecipeAction(**common_dependencies),
        DeleteRecipeAction(**common_dependencies),
        EditRecipeAction(**common_dependencies),
        ViewAllRecipesAction(**common_dependencies),
        SearchRecipesAction(**common_dependencies),
        ExitAction(output_handler=output_handler),
    ]

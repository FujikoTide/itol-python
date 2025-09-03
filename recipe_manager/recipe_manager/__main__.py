from recipe_manager.controllers.app_controller import AppController
from recipe_manager.io.CLI_input_handler import CLIInputHandler
from recipe_manager.io.CLI_output_handler import CLIOutputHandler
from recipe_manager.core.menu_action_factory import create_menu_action
from recipe_manager.actions.add_recipe_action import AddRecipeAction
from recipe_manager.actions.delete_recipe_action import DeleteRecipeAction
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.utils.widgets.CLI_display_table import CLIDisplayTable
from recipe_manager.views.menu_runner import MenuRunner
from recipe_manager.views.menu_handler import MenuHandler
from recipe_manager.actions.exit_action import ExitAction


def main():
    menu_handler = MenuHandler()
    input_handler = CLIInputHandler()
    output_handler = CLIOutputHandler()
    recipe_manager = RecipeManager()
    display_table = CLIDisplayTable()

    exit_action = ExitAction(output_handler=output_handler)
    add_recipe_action = AddRecipeAction(
        input_handler=input_handler,
        output_handler=output_handler,
        display_table=display_table,
        recipe_manager=recipe_manager,
    )
    delete_recipe_action = DeleteRecipeAction(
        input_handler=input_handler,
        output_handler=output_handler,
        display_table=display_table,
        recipe_manager=recipe_manager,
    )

    menu_actions = [add_recipe_action, delete_recipe_action, exit_action]

    app_runners = {}
    menu_runner = MenuRunner(
        menu_handler,
        menu_actions,
        input_handler,
        output_handler,
    )
    app_runners["recipe_manager"] = menu_runner

    app_controller = AppController(app_runners)
    app_controller.run_menu("recipe_manager")


if __name__ == "__main__":
    main()

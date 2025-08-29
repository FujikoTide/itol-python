from recipe_manager.menus import ALL_MENUS
from recipe_manager.controllers.app_controller import AppController
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.io.CLI_input_handler import CLIInputHandler
from recipe_manager.io.CLI_output_handler import CLIOutputHandler
from recipe_manager.views.menu_runner import MenuRunner
from recipe_manager.views.menu_handler import MenuHandler
from recipe_manager.views.wizards.add_recipe_wizard import AddRecipeWizard
from recipe_manager.utils.widgets.CLI_display_table import CLIDisplayTable


def main():
    menu_handler = MenuHandler()
    input_handler = CLIInputHandler()
    output_handler = CLIOutputHandler()
    recipe_manager = RecipeManager()
    table = CLIDisplayTable()
    add_recipe_wizard = AddRecipeWizard(
        input_handler, output_handler, recipe_manager, table
    )
    wizards = {"Add recipe": add_recipe_wizard}
    app_runners = {}
    for menu_name, actions_list in ALL_MENUS.items():
        runner = MenuRunner(
            menu_handler,
            actions_list,
            input_handler,
            output_handler,
            recipe_manager,
            wizards,
        )
        app_runners[menu_name] = runner

    app_controller = AppController(app_runners)
    app_controller.run_menu("recipe_manager")


if __name__ == "__main__":
    main()

from .menus import ALL_MENUS
from recipe_manager.controllers import AppController
from recipe_manager.views import (
    MenuRunner,
    MenuHandler,
    CLIOutputHandler,
    CLIInputHandler,
)


def main():
    menu_handler = MenuHandler()
    input_handler = CLIInputHandler()
    output_handler = CLIOutputHandler()
    app_runners = {}
    for menu_name, actions_list in ALL_MENUS.items():
        runner = MenuRunner(menu_handler, actions_list, input_handler, output_handler)
        app_runners[menu_name] = runner

    app_controller = AppController(app_runners)
    app_controller.run_menu("recipe_manager")


if __name__ == "__main__":
    main()

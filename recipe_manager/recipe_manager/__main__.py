from .menus import ALL_MENUS
from recipe_manager.controllers import AppController
from recipe_manager.views import MenuRunner, MenuHandler, CLIOutputHandler, InputHandler


def main():
    menu_handler = MenuHandler()
    input_handler = CLIHandler()
    app_controller = AppController(ALL_MENUS)
    app_controller.run_menu("recipe_manager")


if __name__ == "__main__":
    main()

from .application_setup import (
    create_menu_actions,
    menu_handler,
    input_handler,
    output_handler,
    recipe_manager,
)
from recipe_manager.views.menu_runner import MenuRunner


def main():
    menu_actions = create_menu_actions()

    menu_runner = MenuRunner(
        menu_handler,
        menu_actions,
        input_handler,
        output_handler,
        recipe_manager,
    )
    menu_runner.run()


if __name__ == "__main__":
    main()

from dataclasses import dataclass
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.core.base_action import BaseMenuAction
from recipe_manager.models.recipe_manager import RecipeManager
from .menu_handler import MenuHandler


@dataclass
class MenuRunner:
    menu_handler: MenuHandler
    menu_actions: list[BaseMenuAction]
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager

    def run(self) -> None:
        while True:
            menu_display_string = self.menu_handler.get_actions_for_display(
                self.menu_actions
            )
            self.output_handler.display_output(menu_display_string)

            user_input = self.input_handler.get_int("[yellow1]Enter a number: [/]")

            selected_action = self.menu_handler.get_selected_action(
                user_input - 1, self.menu_actions
            )

            if not selected_action:
                self.output_handler.display_output(
                    "[violet]Invalid input, please enter a valid number.[/]"
                )
                continue
            selected_action.execute()
            self.recipe_manager.save_recipes()

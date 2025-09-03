from dataclasses import dataclass
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from .menu_handler import MenuHandler
from recipe_manager.core.menu_action import MenuAction


@dataclass
class MenuRunner:
    menu_handler: MenuHandler
    menu_actions: list[MenuAction]
    input_handler: InputHandler
    output_handler: OutputHandler

    def run(self) -> None:
        while True:
            menu_display_string = self.menu_handler.get_actions_for_display(
                self.menu_actions
            )
            self.output_handler.display_output(menu_display_string)

            # change to input handler
            user_input = self.input_handler.get_int("[yellow1]Enter a number: [/]")

            # check for input, it should be a number
            selected_action = self.menu_handler.get_selected_action(
                user_input - 1, self.menu_actions
            )

            if not selected_action:
                self.output_handler.display_output(
                    "[violet]Invalid input, please enter a valid number.[/]"
                )
                continue

            selected_action.execute()

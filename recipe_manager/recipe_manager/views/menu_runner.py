from dataclasses import dataclass
from recipe_manager.io.input_handler import InputHandler
from recipe_manager.io.output_handler import OutputHandler
from .menu_handler import MenuHandler
from recipe_manager.core.menu_action import MenuAction
import inspect
from .wizards.wizard import Wizard
from recipe_manager.models.recipe_manager import RecipeManager


@dataclass
class MenuRunner:
    menu_handler: MenuHandler
    menu_actions: list[MenuAction]
    input_handler: InputHandler
    output_handler: OutputHandler
    recipe_manager: RecipeManager
    wizards: dict[str, Wizard]

    def run(self) -> None:
        while True:
            menu_display_string = self.menu_handler.get_actions_for_display(
                self.menu_actions
            )
            self.output_handler.display_output(menu_display_string)

            # change to input handler
            user_input = int(
                self.input_handler.get_string("[yellow1]Enter a number: [/]")
            )

            # check for input, it should be a number
            selected_action = self.menu_handler.get_selected_action(
                user_input - 1, self.menu_actions
            )

            if not selected_action:
                self.output_handler.display_output(
                    "[violet]Invalid input, please enter a valid number.[/]"
                )
                continue

            wizard_to_run = self.wizards.get(selected_action.name)
            if wizard_to_run:
                returned_action = wizard_to_run.run()
                if returned_action.method:
                    returned_action.method()
                elif returned_action.callback:
                    returned_action.callback()

            else:
                try:
                    if selected_action.method:
                        signature = inspect.signature(selected_action.method)
                        kwargs_to_pass = {}
                        if len(signature.parameters) > 0:
                            for param in list(signature.parameters.values())[0:]:
                                # change to input handler too
                                arg_value = self.input_handler.get_string(
                                    f"[yellow1]Enter a value for[/] [plum1]{param.name}[/][yellow1]:[/] "
                                )
                                kwargs_to_pass[param.name] = arg_value

                        selected_action.method(**kwargs_to_pass)
                    elif selected_action.callback:
                        selected_action.callback()

                except Exception as e:
                    self.output_handler.display_output(
                        f"[violet]An unexpected error occurred:[/] [orange1]{e}[/]"
                    )

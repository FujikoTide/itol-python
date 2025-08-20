from dataclasses import dataclass
from .input_handler import InputHandler
from .menu_handler import MenuHandler
from recipe_manager.core import MenuAction
import inspect
from .output_handler import OutputHandler


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
            user_input = int(self.input_handler.get_input("Enter a number: "))

            # check for input, it should be a number
            selected_action = self.menu_handler.get_selected_action(
                user_input - 1, self.menu_actions
            )

            if not selected_action:
                self.output_handler.display_output(
                    "Invalid input, please enter a valid number."
                )
                continue

            # --- START DEBUGGING CODE ---
            self.output_handler.display_output(
                f"Selected action: {selected_action.name}"
            )
            self.output_handler.display_output(
                f"Method object: {selected_action.method}"
            )

            signature = inspect.signature(selected_action.method)
            self.output_handler.display_output(f"Signature: {signature}")
            self.output_handler.display_output(
                f"Number of parameters: {len(signature.parameters)}"
            )
            self.output_handler.display_output(
                f"Is > 1? {len(signature.parameters) > 1}"
            )
            # --- END DEBUGGING CODE ---

            try:
                signature = inspect.signature(selected_action.method)
                kwargs_to_pass = {}
                if len(signature.parameters) > 0:
                    for param in list(signature.parameters.values())[0:]:
                        # change to input handler too
                        arg_value = self.input_handler.get_input(
                            f"Enter a value for {param.name}: "
                        )
                        kwargs_to_pass[param.name] = arg_value

                selected_action.method(**kwargs_to_pass)

            except Exception as e:
                self.output_handler.display_output(f"An unexpected error occurred: {e}")

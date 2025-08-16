from dataclasses import dataclass
from .input_handler import InputHandler
from .console import console


@dataclass
class CLIHandler(InputHandler):
    def display_menu(self) -> None:
        for i, item in enumerate(self.menu_items, 1):
            console.print(
                f"[orange_red1][[/][orange1]{i}[/][orange_red1]][/]   [bold dark_orange][{item.name}][/]"
            )
            console.print(f"      [italic violet]{item.doc}[/]")

    def get_input(self) -> None:
        pass

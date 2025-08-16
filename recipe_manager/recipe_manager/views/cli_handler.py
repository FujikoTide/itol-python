from dataclasses import dataclass
from input_handler import InputHandler


@dataclass
class CLIHandler(InputHandler):
    def display_menu(self) -> None:
        for i, item in enumerate(self.menu_items, 1):
            print(f"[{i}]   [{item.name}]")
            print(f"    - {item.doc}")

    def get_input(self) -> None:
        pass

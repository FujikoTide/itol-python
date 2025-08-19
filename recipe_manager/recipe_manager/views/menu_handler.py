from dataclasses import dataclass
from .console import console
from recipe_manager.utils import MenuGenerator


@dataclass
class MenuHandler:
    def display_menu(self, menu_items: list[MenuGenerator.MenuAction]) -> None:
        for i, item in enumerate(menu_items, 1):
            console.print(
                f"[orange_red1][[/][orange1]{i}[/][orange_red1]][/]   [bold dark_orange][{item.name}][/]"
            )
            console.print(f"      [italic violet]{item.doc}[/]")

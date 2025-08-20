from dataclasses import dataclass
from typing import Optional
from recipe_manager.core import MenuAction


@dataclass
class MenuHandler:
    def get_actions_for_display(self, menu_items: list[MenuAction]) -> str:
        if not menu_items:
            return "No Menu to display."
        menu_string = ""
        for i, item in enumerate(menu_items, 1):
            number = f"[orange_red1][[/][orange1]{i}[/][orange_red1]][/]"
            name = f"   [bold dark_orange][{item.name}][/]\n"
            description = f"      [italic violet]{item.doc}[/]\n"
            menu_string += f"{number}{name}{description}"
        return menu_string.strip()

    @staticmethod
    def get_selected_action(
        user_input: int, menu_items: list[MenuAction]
    ) -> Optional[MenuAction]:
        if not user_input < len(menu_items):
            return None
        index = int(user_input)
        if menu_items[index] is None:
            return None
        return menu_items[index]

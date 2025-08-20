from dataclasses import dataclass, field
from typing import Protocol
from recipe_manager.utils import MenuAction
from recipe_manager.views import MenuHandler


@dataclass
class InputHandler(Protocol):
    menu_handler: MenuHandler = field(init=False)
    menu_actions: list[MenuAction] = field(init=False)

    def display_menu(self, menu_str: str) -> None: ...

    def run(self) -> None: ...

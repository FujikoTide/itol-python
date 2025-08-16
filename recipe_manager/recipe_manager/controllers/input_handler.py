from abc import ABC, abstractmethod
from dataclasses import dataclass
from recipe_manager.views import MenuGenerator


@dataclass
class InputHandler(ABC):
    menu_items: list[MenuGenerator.MenuAction]

    @abstractmethod
    def display_menu(self) -> None:
        pass

    @abstractmethod
    def get_input(self) -> None:
        pass

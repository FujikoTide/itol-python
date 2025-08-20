from dataclasses import dataclass, field
from recipe_manager._types import Menus


@dataclass
class AppController:
    menus: Menus = field(init=False)

    def run_menu(self, menu_name: str) -> None:
        handler = self.menus.get(menu_name)
        if not handler:
            return None
        handler.run()

from dataclasses import dataclass, field
from recipe_manager._types import Runners


@dataclass
class AppController:
    menus: Runners = field(default_factory=dict)

    def run_menu(self, menu_name: str) -> None:
        handler = self.menus.get(menu_name)
        if not handler:
            return None
        handler.run()

from dataclasses import dataclass, field
from recipe_manager.views.menu_runner import MenuRunner


@dataclass
class AppController:
    menus: dict[str, MenuRunner] = field(default_factory=dict)

    def run_menu(self, menu_name: str) -> None:
        handler = self.menus.get(menu_name)
        if not handler:
            return None
        handler.run()

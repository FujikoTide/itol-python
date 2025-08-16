from dataclasses import dataclass, field
import inspect
from typing import Any, Callable, Type, cast
from recipe_manager._types import MenuFunction


class MenuGenerator:
    @dataclass
    class MenuAction:
        name: str
        method: Callable[..., Any]
        doc: str = field(init=False)

        def __post_init__(self):
            self.doc = inspect.getdoc(self.method) or "No description available."

    @staticmethod
    def generate(class_object: Type[Any]) -> list[MenuAction]:
        ordered_members = sorted(
            [
                (name, method)
                for name, method in inspect.getmembers(
                    class_object, predicate=inspect.isfunction
                )
                if hasattr(method, "_order") and not name.startswith("_")
            ],
            key=lambda item: cast(MenuFunction, item[1])._order,
        )

        actions: list[MenuGenerator.MenuAction] = [
            MenuGenerator.MenuAction(name.replace("_", " ").capitalize(), method)
            for name, method in ordered_members
        ]
        return actions

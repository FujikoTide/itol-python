from dataclasses import dataclass, field
import inspect
from typing import Any, Callable, Type


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
        actions: list[MenuGenerator.MenuAction] = []
        for name, method in inspect.getmembers(
            class_object, predicate=inspect.isfunction
        ):
            if not name.startswith("_"):
                action_name: str = name.replace("_", " ").capitalize()
                actions.append(MenuGenerator.MenuAction(action_name, method))
        return actions

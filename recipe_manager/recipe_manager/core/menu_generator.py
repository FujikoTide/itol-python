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
        class_members = inspect.getmembers(class_object)
        ordered_methods = []
        ordered_method_names = [
            value for name, value in class_members if name.endswith("_ORDER")
        ][0]
        for method_name in ordered_method_names:
            method = getattr(class_object, method_name, None)
            if method and inspect.isfunction(method):
                ordered_methods.append((method_name, method))

        actions: list[MenuGenerator.MenuAction] = [
            MenuGenerator.MenuAction(name.replace("_", " ").capitalize(), method)
            for name, method in ordered_methods
        ]

        return actions

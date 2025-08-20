import inspect
from typing import Any, Type
from recipe_manager.core import MenuAction


class MenuGenerator:
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

        actions: list[MenuAction] = [
            MenuAction(name.replace("_", " ").capitalize(), method)
            for name, method in ordered_methods
        ]

        return actions

import inspect
from typing import Any, Type
from recipe_manager.core.menu_action import MenuAction


class MenuGenerator:
    @staticmethod
    def generate(class_object: Type[Any]) -> list[MenuAction]:
        instance = class_object()
        ordered_methods = []
        ordered_method_names = [
            value
            for name, value in inspect.getmembers(class_object)
            if name == "_MENU_ORDER"
        ][0]
        for method_name in ordered_method_names:
            method = getattr(instance, method_name, None)
            if method and inspect.ismethod(method):
                ordered_methods.append((method_name, method))

        actions: list[MenuAction] = [
            MenuAction(name.replace("_", " ").capitalize(), method)
            for name, method in ordered_methods
        ]

        return actions

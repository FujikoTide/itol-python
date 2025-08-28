from dataclasses import dataclass
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager.models.recipe import Recipe
from .menu_generator import MenuGenerator
from recipe_manager.core.menu_action import MenuAction


@dataclass
class MenuFactory:
    def generate(self, class_name: str) -> list[MenuAction] | None:
        MENUS_FROM_CLASSES = {
            "recipe": Recipe,
            "recipe_manager": RecipeManager,
        }

        # make default menu to return to avoid None situation
        class_object = MENUS_FROM_CLASSES.get(class_name, None)
        if class_object is None:
            return class_object
        return MenuGenerator.generate(class_object)

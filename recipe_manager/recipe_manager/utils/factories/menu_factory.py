from dataclasses import dataclass
from enum import StrEnum
from recipe_manager.models import RecipeManager, Recipe
from .menu_generator import MenuGenerator


# move to a config?
class CLASSES(StrEnum):
    RECIPE = "recipe"
    RECIPE_MANAGER = "recipe_manager"


@dataclass
class MenuFactory:
    def generate(self, class_name: str) -> list[MenuGenerator.MenuAction] | None:
        MENUS_FROM_CLASSES = {
            CLASSES.RECIPE: Recipe,
            CLASSES.RECIPE_MANAGER: RecipeManager,
        }

        # make default menu to return to avoid None situation
        class_object = MENUS_FROM_CLASSES.get(CLASSES[class_name], None)
        if class_object is None:
            return class_object
        return MenuGenerator.generate(class_object)

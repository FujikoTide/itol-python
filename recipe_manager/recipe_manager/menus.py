from recipe_manager.utils import MenuGenerator
from recipe_manager.models import Recipe, RecipeManager
from recipe_manager._types import Menus


recipe_manager_actions = MenuGenerator.generate(RecipeManager)
recipe_actions = MenuGenerator.generate(Recipe)

ALL_MENUS: Menus = {
    "recipe_manager": recipe_manager_actions,
    "recipe": recipe_actions,
}

from recipe_manager.utils.factories.menu_generator import MenuGenerator
from recipe_manager.models.recipe import Recipe
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager._types import Menus


recipe_manager_actions = MenuGenerator.generate(RecipeManager)
recipe_actions = MenuGenerator.generate(Recipe)

ALL_MENUS: Menus = {
    "recipe_manager": recipe_manager_actions,
    "recipe": recipe_actions,
}

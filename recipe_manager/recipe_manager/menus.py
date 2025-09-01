from recipe_manager.utils.factories.menu_generator import MenuGenerator
from recipe_manager.models.recipe import Recipe
from recipe_manager.models.recipe_manager import RecipeManager
from recipe_manager._types import Menus
from recipe_manager.core.menu_action import MenuAction


recipe_manager_actions = MenuGenerator.generate(RecipeManager)
recipe_actions = MenuGenerator.generate(Recipe)

ALL_MENUS: Menus = {
    "recipe_manager": recipe_manager_actions,
    "recipe": recipe_actions,
}

# #####################################
# won't need MenuGenerator or MenuFactory now?
# is MenuFactory even being used?!


def get_actions(menu_list):
    actions: list[MenuAction] = [MenuAction(name, method) for name, method in menu_list]

    return actions


recipe_manager = RecipeManager()

# add wizards here?
# don't need tuples of menu name and method? oh for the help?
recipe_methods = [
    ("Add recipe", recipe_manager.add_recipe),
    ("Delete recipe", recipe_manager.delete_recipe),
    ("Get all recipes", recipe_manager.get_all_recipes),
    ("Get recipe", recipe_manager.get_recipe),
    ("Search recipes", recipe_manager.search_recipes),
]
RECIPE_MANAGER_MENU: Menus = {"recipe_manager": get_actions(recipe_methods)}

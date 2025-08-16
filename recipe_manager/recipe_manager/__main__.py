from recipe_manager.models import RecipeManager, Recipe
from recipe_manager.views import CLIHandler
from recipe_manager.core import MenuGenerator


def main():
    recipe_menu = MenuGenerator.generate(Recipe)
    recipe_manager_menu = MenuGenerator.generate(RecipeManager)
    CLIHandler(recipe_menu).display_menu()
    CLIHandler(recipe_manager_menu).display_menu()


if __name__ == "__main__":
    main()

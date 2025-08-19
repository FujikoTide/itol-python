from recipe_manager.models import RecipeManager, Recipe, JSONHandler
from recipe_manager.views import CLIHandler
from recipe_manager.core import MenuGenerator


def main():
    # need menu factory? to feed into input handler? or to feed into recipe manager?
    # or none of these?!
    # or split menus away from input handling? that seems more like it in the end
    recipe_menu = CLIHandler(MenuGenerator.generate(Recipe))
    recipe_manager_menu = CLIHandler(MenuGenerator.generate(RecipeManager))

    json_handler = JSONHandler()
    recipe_manager = RecipeManager(json_handler, recipe_manager_menu)
    recipe = Recipe("cat", "boiled cat", "first take your cat...")
    recipe_manager.add_recipe(recipe)
    recipe_manager.input.display_menu()


if __name__ == "__main__":
    main()

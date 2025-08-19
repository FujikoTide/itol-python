from recipe_manager.models import RecipeManager, Recipe, JSONHandler
from recipe_manager.recipe_manager.utils.factories.menu_factory import MenuFactory
from recipe_manager.recipe_manager.views.menu_handler import MenuHandler
from recipe_manager.views import CLIHandler


def main():
    # need menu factory? to feed into input handler? or to feed into recipe manager?
    # or none of these?!
    # or split menus away from input handling? that seems more like it in the end
    # need a menu factory and a menu handler I think?
    recipe_menu = MenuFactory().generate("recipe")
    recipe_manager_menu = MenuFactory().generate("recipe_manager")

    json_handler = JSONHandler()
    cli_handler = CLIHandler()
    recipe_manager = RecipeManager(json_handler, cli_handler)
    recipe = Recipe("cat", "boiled cat", "first take your cat...")
    recipe_manager.add_recipe(recipe)
    menu = MenuHandler()
    if recipe_menu is not None:
        menu.display_menu(recipe_menu)
    if recipe_manager_menu is not None:
        menu.display_menu(recipe_manager_menu)


if __name__ == "__main__":
    main()

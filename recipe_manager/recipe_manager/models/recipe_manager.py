from dataclasses import dataclass, field
from recipe_manager._types import Recipes, Recipe


@dataclass
class RecipeManager:
    recipes: Recipes = field(init=False)

    _MENU_ORDER = [
        "add_recipe",
        "delete_recipe",
        "edit_recipe",
        "view_recipe",
        "view_all_recipes",
        "search_recipes",
    ]

    # need observer pattern here? when recipes change they automatically call save on the storage handler?
    # and if storage data exists automatically load on instantiation? how to do this?...... Recipes in storage handler not in Recipe Manager?

    def __post_init__(self):
        self.recipes: Recipes = []

    def add_recipe(self, recipe: Recipe) -> Recipe | None:
        """Add a Recipe of type Recipe."""
        pass

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        """Delete a Recipe by Recipe Name."""
        pass

    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        """Edit a Recipe."""
        pass

    def view_recipe(self, name: str) -> Recipe | None:
        """View a Recipe by Recipe Name."""
        pass

    def view_all_recipes(self) -> Recipes | None:
        """View all Recipes."""
        pass

    def search_recipes(self, search_term: str) -> Recipes | None:
        """Search all Recipes."""
        pass

from dataclasses import dataclass, field
from recipe_manager._types import Recipes
from recipe_manager.models.recipe import Recipe


@dataclass
class RecipeManager:
    recipes: Recipes = field(init=False)

    _MENU_ORDER = [
        "add_recipe",
        "delete_recipe",
        "edit_recipe",
        "get_recipe",
        "get_all_recipes",
        "search_recipes",
    ]

    # need observer pattern here? when recipes change they automatically call save on the storage handler?
    # and if storage data exists automatically load on instantiation? how to do this?...... Recipes in storage handler not in Recipe Manager?

    def __post_init__(self):
        self.recipes: Recipes = {}

    def add_recipe(self, recipe: Recipe) -> Recipe:
        """Add a Recipe of type Recipe."""
        self.recipes[recipe.name] = recipe
        return recipe

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        """Delete a Recipe by Recipe Name."""
        if self._find_class_in_dict(recipe_name):
            return self.recipes.pop(recipe_name)
        return None

    # remove, need to implement some other way
    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        """Edit a Recipe."""
        pass

    def get_recipe(self, recipe_name: str) -> Recipe | None:
        """View a Recipe by Recipe Name."""
        found_recipe = self._find_class_in_dict(recipe_name)
        return found_recipe

    def get_all_recipes(self) -> Recipes | None:
        """View all Recipes."""
        return self.recipes

    def search_recipes(self, search_term: str) -> Recipes | None:
        """Search all Recipes."""
        pass

    def _find_class_in_dict(self, recipe_name: str) -> Recipe | None:
        return self.recipes.get(recipe_name)

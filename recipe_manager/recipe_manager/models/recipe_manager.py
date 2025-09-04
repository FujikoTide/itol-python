from dataclasses import dataclass, field
from recipe_manager._types import Recipes
from recipe_manager.models.recipe import Recipe
from recipe_manager.models.storage_handler import StorageHandler


@dataclass
class RecipeManager:
    storage_handler: StorageHandler
    recipes: Recipes = field(init=False)

    def __post_init__(self):
        loaded_recipes = self.storage_handler.load()
        self.recipes = loaded_recipes if loaded_recipes is not None else {}

    def save_recipes(self):
        self.storage_handler.save(self.recipes)

    def add_recipe(self, recipe: Recipe) -> Recipe:
        """Add a Recipe of type Recipe."""
        self.recipes[recipe.name] = recipe
        return recipe

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        """Delete a Recipe by Recipe Name."""
        if self._find_class_in_dict(recipe_name):
            return self.recipes.pop(recipe_name)
        return None

    def get_recipe(self, recipe_name: str) -> Recipe | None:
        """View a Recipe by Recipe Name."""
        found_recipe = self._find_class_in_dict(recipe_name)
        return found_recipe

    def _find_class_in_dict(self, recipe_name: str) -> Recipe | None:
        return self.recipes.get(recipe_name)

    def get_all_recipes(self) -> Recipes | None:
        """View all Recipes."""
        return self.recipes

    def search_recipes(self, search_term: str) -> Recipes | None:
        """Search all Recipes."""
        result = {
            name: recipe
            for name, recipe in self.recipes.items()
            if (
                search_term in recipe.name
                or search_term in recipe.description
                or search_term in recipe.instructions
                or any(
                    search_term in ingredient.name
                    for ingredient in recipe.ingredients.values()
                )
            )
        }
        if not result:
            return None
        return result

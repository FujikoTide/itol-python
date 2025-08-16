from dataclasses import dataclass, field
from recipe_manager.types import Recipes
from recipe import Recipe
from recipe_manager.models import StorageHandler
from recipe_manager.views import InputHandler


@dataclass
class RecipeManager:
    storage: StorageHandler
    input: InputHandler
    recipes: Recipes = field(default_factory=list)

    def add_recipe(self, recipe: Recipe) -> Recipe | None:
        """Add a Recipe of type Recipe."""
        pass

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        """Delete a Recipe by Recipe Name."""
        pass

    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        """Edit a Recipe."""
        pass

    def view_all_recipes(self) -> Recipes | None:
        """View all Recipes."""
        pass

    def search_recipes(self, search_term: str) -> Recipes | None:
        """Search all Recipes."""
        pass

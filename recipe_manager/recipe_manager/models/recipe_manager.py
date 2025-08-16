from dataclasses import dataclass, field
from recipe_manager._types import Recipes
from .recipe import Recipe
from .storage_handler import StorageHandler
from recipe_manager.views import InputHandler
from recipe_manager.utils import order


@dataclass
class RecipeManager:
    storage: StorageHandler
    input: InputHandler
    recipes: Recipes = field(default_factory=list)

    @order(1)
    def add_recipe(self, recipe: Recipe) -> Recipe | None:
        """Add a Recipe of type Recipe."""
        pass

    @order(2)
    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        """Delete a Recipe by Recipe Name."""
        pass

    @order(3)
    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        """Edit a Recipe."""
        pass

    @order(4)
    def view_all_recipes(self) -> Recipes | None:
        """View all Recipes."""
        pass

    @order(5)
    def search_recipes(self, search_term: str) -> Recipes | None:
        """Search all Recipes."""
        pass

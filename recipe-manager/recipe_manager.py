from dataclasses import dataclass, field
from _types import Recipes
from recipe import Recipe
from storage_handler import StorageHandler
from input_handler import InputHandler


@dataclass
class RecipeManager:
    storage: StorageHandler
    input: InputHandler
    recipes: Recipes = field(default_factory=list)

    def add_recipe(self, recipe: Recipe) -> Recipe | None:
        pass

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        pass

    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        pass

    def view_all_recipes(self) -> Recipes | None:
        pass

    def search_recipes(self, search_term: str) -> Recipes | None:
        pass

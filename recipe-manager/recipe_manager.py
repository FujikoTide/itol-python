from dataclasses import dataclass, field
from _types import recipes
from recipe import Recipe
from storage_handler import StorageHandler


@dataclass
class RecipeManager:
    storage: StorageHandler
    recipes: "recipes" = field(default_factory=list)

    def add_recipe(self, recipe: Recipe) -> Recipe | None:
        pass

    def delete_recipe(self, recipe_name: str) -> Recipe | None:
        pass

    def edit_recipe(self, recipe_name: str) -> Recipe | None:
        pass

    def view_all_recipes(self) -> "recipes | None":
        pass

    def search_recipes(self, search_term: str) -> "recipes | None":
        pass

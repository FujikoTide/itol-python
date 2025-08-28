from recipe_manager._types import Ingredients
from recipe_manager.models.recipe import Recipe
from typing import Protocol


class RecipeTable(Protocol):
    @staticmethod
    def display_ingredients(ingredients: Ingredients) -> None: ...

    @staticmethod
    def display_name(name: str) -> None: ...

    @staticmethod
    def display_description(description: str) -> None: ...

    @staticmethod
    def display_instructions(instructions: str) -> None: ...

    @staticmethod
    def display_recipe(recipe: Recipe) -> None: ...

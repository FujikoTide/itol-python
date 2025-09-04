from recipe_manager._types import Ingredients
from recipe_manager.models.recipe import Recipe
from typing import Protocol
from recipe_manager.io.output_handler import OutputHandler


class DisplayTable(Protocol):
    output_handler: OutputHandler

    def display_ingredients(self, ingredients: Ingredients) -> None: ...

    def display_description(self, description: str) -> None: ...

    def display_instructions(self, instructions: str) -> None: ...

    def display_recipe(self, recipe: Recipe) -> None: ...

    def display_list(self, title: str, list: list[str]) -> None: ...

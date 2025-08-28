from recipe_manager._types import Ingredients
from recipe_manager.views.console import console
from rich.table import Table


class RecipeTable:
    @staticmethod
    def display_ingredients(ingredients: Ingredients) -> None:
        table = Table(title="Ingredients")

        table.add_column("Ingredient", justify="right", style="green", no_wrap=True)
        table.add_column("Quantity", justify="left", style="green")
        table.add_column("Unit of Measurement", justify="right", style="green")

        for ingredient in ingredients:
            table.add_row(ingredient.name, str(ingredient.quantity), ingredient.unit)

        console.print(table)

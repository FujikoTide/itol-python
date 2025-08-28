from recipe_manager._types import Ingredients
from recipe_manager.views.console import console
from recipe_manager.models.recipe import Recipe
from rich.table import Table


class CLIRecipeTable:
    @staticmethod
    def display_ingredients(ingredients: Ingredients) -> None:
        table = Table(
            title="[italic]Ingredients[/]",
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
        )

        table.add_column("Ingredient", justify="right", style="orange1", no_wrap=True)
        table.add_column("Quantity", justify="left", style="orange1")
        table.add_column("Unit", justify="right", style="italic orange1")

        for ingredient in ingredients:
            table.add_row(ingredient.name, str(ingredient.quantity), ingredient.unit)

        console.print(table)

    @staticmethod
    def display_name(name: str) -> None:
        pass

    @staticmethod
    def display_description(description: str) -> None:
        pass

    @staticmethod
    def display_instructions(instructions: str) -> None:
        pass

    @staticmethod
    def display_recipe(recipe: Recipe) -> None:
        pass

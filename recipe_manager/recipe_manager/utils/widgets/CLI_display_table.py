from recipe_manager._types import Ingredients
from recipe_manager.views.console import console
from recipe_manager.models.recipe import Recipe
from rich.table import Table
from rich import box


class CLIDisplayTable:
    def display_ingredients(self, ingredients: Ingredients) -> None:
        table = Table(
            title="[italic]Ingredients[/]",
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
            box=box.ROUNDED,
        )

        table.add_column("Ingredient", justify="right", style="orange1", no_wrap=True)
        table.add_column("Quantity", justify="left", style="orange1")
        table.add_column("Unit", justify="right", style="italic orange1")

        for ingredient in ingredients.values():
            table.add_row(ingredient.name, str(ingredient.quantity), ingredient.unit)

        console.print(table)

    def display_description(self, description: str) -> None:
        table = Table(
            title="[italic]Description[/]",
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
            box=box.ROUNDED,
        )

        table.add_column("Description", justify="left", style="orange1", no_wrap=False)
        table.add_row(description)

        console.print(table)

    def display_instructions(self, instructions: str) -> None:
        table = Table(
            title="[italic]Instructions[/]",
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
            box=box.ROUNDED,
        )

        table.add_column("Instructions", justify="left", style="orange1", no_wrap=False)
        table.add_row(instructions)

        console.print(table)

    def display_recipe(self, recipe: Recipe) -> None:
        table_recipe = Table(
            title=None,
            border_style="steel_blue",
            box=box.ROUNDED,
        )
        table_recipe.add_column(
            f":fork_and_knife: [italic gold1]{recipe.name}[/] :cocktail:",
            justify="center",
            style="orange1",
            no_wrap=True,
        )

        table_description = Table(
            title=None,
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
            box=box.ROUNDED,
        )
        table_description.add_column(
            "Description", justify="left", style="orange1", no_wrap=False
        )
        table_description.add_row(recipe.description)

        table_recipe.add_row(table_description)

        if recipe.ingredients:
            table_ingredients = Table(
                title=None,
                title_style="gold1",
                header_style="bold dark_orange",
                border_style="steel_blue",
                box=box.ROUNDED,
            )
            table_ingredients.add_column(
                "Ingredient", justify="right", style="orange1", no_wrap=True
            )
            table_ingredients.add_column("Quantity", justify="left", style="orange1")
            table_ingredients.add_column(
                "Unit", justify="right", style="italic orange1"
            )
            for ingredient in recipe.ingredients.values():
                table_ingredients.add_row(
                    ingredient.name, str(ingredient.quantity), ingredient.unit
                )

            table_recipe.add_row(table_ingredients)

        table_instructions = Table(
            title=None,
            title_style="gold1",
            header_style="bold dark_orange",
            border_style="steel_blue",
            box=box.ROUNDED,
        )
        table_instructions.add_column(
            "Instructions", justify="left", style="orange1", no_wrap=False
        )
        table_instructions.add_row(recipe.instructions)

        table_recipe.add_row(table_instructions)

        console.print(table_recipe)

    def display_list(self, title: str, list: list[str]) -> None:
        pass

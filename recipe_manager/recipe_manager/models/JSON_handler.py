from dataclasses import asdict, dataclass
import json
from typing import Any
from recipe_manager._types import Recipes
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.ingredient import Ingredient
from recipe_manager.models.recipe import Recipe


@dataclass
class JSONHandler:
    output_handler: OutputHandler
    filepath: str = "recipes.json"

    def save(self, recipes: Recipes) -> bool:
        serializable_recipes = {
            name: asdict(recipe) for name, recipe in recipes.items()
        }
        if not self._is_data_different(serializable_recipes):
            self.output_handler.display_output(
                "[violet]No changes detected, skipping save.[/]"
            )
            return True

        try:
            with open(self.filepath, "w") as f:
                json.dump(serializable_recipes, f, indent=4)
                self.output_handler.display_output(
                    f"[bright_green]Recipes saved to: [bold dark_orange]{self.filepath}[/].[/]"
                )
                return True
        except Exception as e:
            self.output_handler.display_output(
                f"[bright_red]Error saving recipes to file: [bold dark_orange]{e}[/].[/]"
            )
            return False

    def load(self) -> Recipes | None:
        recipes = {}
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                for recipe_name, recipe_data in data.items():
                    ingredients = {
                        ingredient_name: Ingredient(**ingredient_data)
                        for ingredient_name, ingredient_data in recipe_data[
                            "ingredients"
                        ].items()
                    }
                    recipes[recipe_name] = Recipe(
                        name=recipe_data["name"],
                        description=recipe_data["description"],
                        instructions=recipe_data["instructions"],
                        ingredients=ingredients,
                    )
            self.output_handler.display_output("[bright_green]Recipes Loaded![/]")
            return recipes
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            self.output_handler.display_output(
                f"[bright_red]Error loading recipes from file: [bold dark_orange]{e}[/].[/]"
            )
            return None

    def _is_data_different(self, in_memory_recipes: dict[str, Any]) -> bool:
        try:
            with open(self.filepath, "r") as f:
                disk_recipes = json.load(f)
            return disk_recipes != in_memory_recipes
        except (FileNotFoundError, json.JSONDecodeError):
            return True

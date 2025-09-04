from dataclasses import asdict, dataclass
import json
from recipe_manager._types import Recipes
from recipe_manager.io.output_handler import OutputHandler
from recipe_manager.models.ingredient import Ingredient
from recipe_manager.models.recipe import Recipe


@dataclass
class JSONHandler:
    output_handler: OutputHandler
    filepath: str = "recipes.json"

    def save(self, recipes: Recipes) -> bool:
        try:
            with open(self.filepath, "w") as f:
                serializable_recipes = {
                    name: asdict(recipe) for name, recipe in recipes.items()
                }
                json.dump(serializable_recipes, f, indent=4)
                self.output_handler.display_output(f"Recipes saved to: {self.filepath}")
                return True
        except Exception as e:
            self.output_handler.display_output(f"Error saving recipes to file: {e}")
            return False

    def load(self) -> Recipes | None:
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                recipes = {}
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
                    self.output_handler.display_output("Recipes Loaded!")
                    return recipes
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            self.output_handler.display_output(f"Error loading recipes from file: {e}")
            return None

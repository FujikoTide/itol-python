from dataclasses import dataclass, field
from recipe_manager._types import Ingredients
from .ingredient import Ingredient


@dataclass
class Recipe:
    name: str = ""
    description: str = ""
    instructions: str = ""
    ingredients: Ingredients = field(default_factory=dict)

    _MENU_ORDER = [
        "set_name",
        "set_description",
        "set_instructions",
        "add_ingredient",
        "delete_ingredient",
        "add_multiple_ingredients",
        "delete_all_ingredients",
    ]

    def set_name(self, new_name: str) -> str | None:
        """Set Name of Recipe to new Name."""
        if not isinstance(new_name, str):
            return None
        self.name = new_name
        return self.name

    def set_description(self, new_description: str) -> str | None:
        """Set Description of Recipe to new Description."""
        if not isinstance(new_description, str):
            return None
        self.description = new_description
        return self.description

    def add_ingredient(self, new_ingredient: Ingredient) -> Ingredient:
        """Add one Ingredient of type Ingredient."""
        self.ingredients[new_ingredient.name] = new_ingredient
        return new_ingredient

    def delete_ingredient(self, ingredient_name: str) -> Ingredient | None:
        """Delete one Ingredient by Ingredient Name."""
        if self._find_ingredient_in_dict(ingredient_name):
            return self.ingredients.pop(ingredient_name)
        return None

    def add_multiple_ingredients(self, new_ingredients: Ingredients) -> Ingredients:
        """Add multiple Ingredients of type list[Ingredient]."""
        self.ingredients.update(new_ingredients)
        return self.ingredients

    def delete_all_ingredients(self) -> Ingredients:
        """Delete all Ingredients."""
        temp_ingredients = self.ingredients
        self.ingredients.clear()
        return temp_ingredients

    def set_instructions(self, new_instructions: str) -> str | None:
        """Set Recipe Instructions to new Instructions."""
        if not isinstance(new_instructions, str):
            return None
        self.instructions = new_instructions
        return self.instructions

    def _find_ingredient_in_dict(self, ingredient_name: str) -> Ingredient | None:
        return self.ingredients.get(ingredient_name)

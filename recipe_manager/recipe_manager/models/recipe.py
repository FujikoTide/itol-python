from dataclasses import dataclass, field
from recipe_manager._types import Ingredient, Ingredients
from recipe_manager.utils import order


@dataclass
class Recipe:
    name: str = ""
    description: str = ""
    ingredients: Ingredients = field(default_factory=list)
    instructions: str = ""

    @order(1)
    def set_name(self, new_name: str) -> str | None:
        """Set Name of Recipe to new Name."""
        if not isinstance(new_name, str):
            return None
        self.name = new_name
        return self.name

    @order(2)
    def set_description(self, new_description: str) -> str | None:
        """Set Description of Recipe to new Description."""
        if not isinstance(new_description, str):
            return None
        self.name = new_description
        return self.description

    @order(3)
    def add_ingredient(self, new_ingredient: Ingredient) -> Ingredient | None:
        """Add one Ingredient of type Ingredient."""
        pass

    @order(4)
    def delete_ingredient(self, ingredient: str) -> Ingredient | None:
        """Delete one Ingredient by Ingredient Name."""
        pass

    @order(5)
    def add_multiple_ingredients(
        self, new_ingredients: Ingredients
    ) -> Ingredients | None:
        """Add multiple Ingredients of type list[Ingredient]."""
        pass

    @order(6)
    def delete_all_ingredients(self) -> Ingredients | None:
        """Delete all Ingredients."""
        pass

    @order(7)
    def set_instructions(self, new_instructions: str) -> str | None:
        """Set Recipe Instructions to new Instructions."""
        if not isinstance(new_instructions, str):
            return None
        self.name = new_instructions
        return self.instructions

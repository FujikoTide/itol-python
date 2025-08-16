from dataclasses import dataclass, field
from _types import Ingredient, Ingredients


@dataclass
class Recipe:
    name: str = ""
    description: str = ""
    ingredients: Ingredients = field(default_factory=list)
    instructions: str = ""

    def change_name(self, new_name: str) -> str | None:
        """Change Name of Recipe to new Name."""
        if not isinstance(new_name, str):
            return None
        self.name = new_name
        return self.name

    def change_description(self, new_description: str) -> str | None:
        """Change Description of Recipe to new Description."""
        if not isinstance(new_description, str):
            return None
        self.name = new_description
        return self.description

    def add_ingredient(self, new_ingredient: Ingredient) -> Ingredient | None:
        """Add one Ingredient of type Ingredient."""
        pass

    def remove_ingredient(self, ingredient: str) -> Ingredient | None:
        """Remove one Ingredient by Ingredient Name."""
        pass

    def add_ingredients(self, new_ingredients: Ingredients) -> Ingredients | None:
        """Add Many Ingredients of type list[Ingredient]."""
        pass

    def remove_all_ingredients(self) -> Ingredients | None:
        """Remove all Ingredients."""
        pass

    def change_instructions(self, new_instructions: str) -> str | None:
        """Change Recipe Instructions to new Instructions."""
        if not isinstance(new_instructions, str):
            return None
        self.name = new_instructions
        return self.instructions

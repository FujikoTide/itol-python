from dataclasses import dataclass, field
from _types import ingredients


@dataclass
class Recipe:
    name: str = ""
    description: str = ""
    ingredients: "ingredients" = field(default_factory=list)
    instructions: str = ""

    def change_name(self, new_name: str) -> str | None:
        if not isinstance(new_name, str):
            return None
        self.name = new_name
        return self.name

    def change_description(self, new_description: str) -> str | None:
        if not isinstance(new_description, str):
            return None
        self.name = new_description
        return self.description

    def change_ingredients(self, new_ingredients: "ingredients") -> "ingredients":
        pass

    def change_instructions(self, new_instructions: str) -> str | None:
        if not isinstance(new_instructions, str):
            return None
        self.name = new_instructions
        return self.instructions

    # change change_ingredients into add/remove ingredients?

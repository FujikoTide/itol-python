from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from recipe_manager.models import Recipe


# list of (ingredient name, quantity of ingredient, unit used for quantity (i.e. grams, millilitres etc))
Ingredient = tuple[str, float, str]
Ingredients = list[Ingredient]

Recipes = list["Recipe"]

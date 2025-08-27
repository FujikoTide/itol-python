from __future__ import annotations
from typing import Protocol
from recipe_manager.views import MenuRunner
from recipe_manager.core import MenuAction


class MenuFunction(Protocol):
    _order: int

    def __call__(self, *args, **kwargs) -> object: ...


# list of (ingredient name, quantity of ingredient, unit used for quantity (i.e. grams, millilitres etc))
Ingredient = tuple[str, float, str]
Ingredients = list[Ingredient]

Recipe = tuple[str, str, str, Ingredients]
Recipes = list[Recipe]

Menus = dict[str, list[MenuAction]]
Runners = dict[str, MenuRunner]

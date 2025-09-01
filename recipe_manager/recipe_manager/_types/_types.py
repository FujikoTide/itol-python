from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
from recipe_manager.core.menu_action import MenuAction

if TYPE_CHECKING:
    from recipe_manager.models.recipe import Recipe
    from recipe_manager.models.ingredient import Ingredient


class MenuFunction(Protocol):
    _order: int

    def __call__(self, *args, **kwargs) -> object: ...


Ingredients = dict[str, "Ingredient"]

Recipes = dict[str, "Recipe"]

Menus = dict[str, list[MenuAction]]

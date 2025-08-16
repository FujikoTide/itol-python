from functools import wraps
from typing import Callable, cast
from recipe_manager._types import MenuFunction


def order(value: int) -> Callable[[Callable], MenuFunction]:
    def decorator(func: Callable) -> MenuFunction:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__dict__["_order"] = value
        return cast(MenuFunction, wrapper)

    return decorator

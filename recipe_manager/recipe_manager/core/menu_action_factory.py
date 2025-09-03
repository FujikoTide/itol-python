from .base_action import BaseMenuAction
from typing import Any, Callable, Optional


def create_menu_action(
    name: str,
    method: Optional[Callable[..., Any]] = None,
    callback: Optional[Callable[..., Any]] = None,
) -> BaseMenuAction:
    return BaseMenuAction(name, method, callback)

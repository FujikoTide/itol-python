from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class BaseMenuAction:
    name: str
    method: Optional[Callable[..., Any]] = None
    callback: Optional[Callable[..., Any]] = None
    doc: str = "No help text available."

    def execute(self) -> None:
        if self.method:
            self.method()
        elif self.callback:
            self.callback()

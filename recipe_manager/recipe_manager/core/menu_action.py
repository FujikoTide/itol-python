from dataclasses import dataclass, field
import inspect
from typing import Any, Callable


@dataclass
class MenuAction:
    name: str
    method: Callable[..., Any]
    doc: str = field(init=False)

    def __post_init__(self):
        self.doc = inspect.getdoc(self.method) or "No description available."

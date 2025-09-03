from typing import Any, Callable, Protocol


class MenuAction(Protocol):
    name: str
    method: Callable[..., Any] | None
    callback: Callable[..., Any] | None
    doc: str = "No description available."

    def execute(self) -> None: ...

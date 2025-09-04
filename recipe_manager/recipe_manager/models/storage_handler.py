from typing import Protocol
from recipe_manager._types import Recipes
from recipe_manager.io.output_handler import OutputHandler


class StorageHandler(Protocol):
    output_handler: OutputHandler
    filepath: str

    def save(self, recipes: Recipes) -> bool: ...

    def load(self) -> Recipes | None: ...

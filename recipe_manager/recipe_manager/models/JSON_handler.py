from dataclasses import dataclass
from .storage_handler import StorageHandler


@dataclass
class JSONHandler(StorageHandler):
    def __post_init__(self):
        # if file exists, load and set _store to file contents.
        pass

    def save(self) -> bool:
        print("Recipe Saved!")
        return True

    def load(self) -> bool:
        print("Recipes Loaded!")
        return True

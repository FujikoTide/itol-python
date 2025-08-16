from dataclasses import dataclass
from .storage_handler import StorageHandler


@dataclass
class JSONHandler(StorageHandler):
    def save(self) -> bool:
        return True

    def load(self) -> bool:
        return True

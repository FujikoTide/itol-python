from dataclasses import dataclass
from typing import Protocol


@dataclass
class StorageHandler(Protocol):
    def save(self) -> bool: ...

    def load(self) -> bool: ...

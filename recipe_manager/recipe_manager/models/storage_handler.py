from typing import Protocol


class StorageHandler(Protocol):
    def save(self) -> bool: ...

    def load(self) -> bool: ...

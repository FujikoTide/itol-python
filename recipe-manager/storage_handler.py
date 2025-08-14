from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class StorageHandler(ABC):
    @abstractmethod
    def save(self) -> bool:
        pass

    @abstractmethod
    def load(self) -> bool:
        pass

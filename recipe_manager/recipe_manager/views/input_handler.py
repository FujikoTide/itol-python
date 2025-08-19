from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class InputHandler(ABC):
    @abstractmethod
    def get_input(self) -> None:
        pass

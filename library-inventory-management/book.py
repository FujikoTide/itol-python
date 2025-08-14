from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    ISBN: str = field(default_factory=lambda: str(uuid4()))

from dataclasses import dataclass


@dataclass
class JSONHandler:
    def __post_init__(self):
        # if file exists, load and set _store to file contents.
        pass

    # use display output here
    def save(self) -> bool:
        print("Recipe Saved!")
        return True

    def load(self) -> bool:
        print("Recipes Loaded!")
        return True

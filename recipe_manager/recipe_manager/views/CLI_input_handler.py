from dataclasses import dataclass


@dataclass
class CLIInputHandler:
    def get_input(self, prompt: str) -> str:
        return input(prompt)

    # add helper functions for validation

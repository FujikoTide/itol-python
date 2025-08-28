import sys
from typing import Callable, TypeVar
from recipe_manager.views.console import console

T = TypeVar("T", int, float, bool, str)


class CLIInputHandler:
    def get_string(self, prompt: str) -> str:
        return console.input(prompt)

    def get_optional_string(self, prompt: str) -> str | None:
        user_input = console.input(prompt)
        return user_input if user_input else None

    def get_yes_no(self, prompt: str, default: bool | None = None) -> bool | None:
        yes_no = "[plum1]([/][bright_green]Yes[/][plum1]/[/][bright_red]No[/][plum1])[/][plum1]:[/] "
        user_input = console.input(f"{prompt}{yes_no}").lower()
        if user_input in ("y", "yes"):
            return True
        if user_input in ("n", "no"):
            return False
        return default

    def get_int(self, prompt: str) -> int:
        return self._get_valid_input(prompt, int)

    def get_float(self, prompt: str) -> float:
        return self._get_valid_input(prompt, float)

    def get_int_in_range(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            try:
                user_input = self.get_int(prompt)
                if min_val <= user_input <= max_val:
                    return user_input
                console.print(
                    f"[violet]Input must be between[/] [orange1]{min_val}[/] [violet]and[/] [orange1]{max_val}[/][violet].[/]"
                )
            except (KeyboardInterrupt, EOFError):
                sys.exit(1)

    def _get_valid_input(self, prompt: str, type_func: Callable[[str], T]) -> T:
        while True:
            try:
                user_input = console.input(prompt)
                return type_func(user_input)
            except (ValueError, KeyboardInterrupt, EOFError):
                console.print("[violet]Invalid input. Please try again.[/]")

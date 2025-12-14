from typing import List
from typing import Any

#   Sum Numbers with Type Hints
def sum_numbers(nums: List[int]) -> int:
    return sum(nums)


# Flexible Printer with *args and **kwargs
def printer(*args: Any, **kwargs: Any) -> None:
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(f"{k}: {v}")

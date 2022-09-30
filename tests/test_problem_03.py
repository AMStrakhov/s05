from typing import Callable, List, Tuple

from problem_03 import concatenate
from .base_test_problem import BaseTestProblem


class TestProblem02(BaseTestProblem):
    _problem_func: Callable = concatenate
    cases: List[Tuple[List, List, str]] = [
        (
            [["Apple", "Black", "Windows"], [14, "RED", "XP"]],
            ["apple_14", "black_red", "windows_xp"],
            "Base case",
        ),
        (
            [[], []],
            [],
            "Empty Lists",
        ),
        (
            [["Apple", "Black", "Windows"], [14, "RED"]],
            ["apple_14", "black_red"],
            "Uneven Lists",
        ),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertLessEqual(expected, self.problem_func(*inputs))

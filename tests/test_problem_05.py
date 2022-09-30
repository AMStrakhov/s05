from typing import Callable, List, Tuple

from problem_05 import collect_letters
from .base_test_problem import BaseTestProblem


class TestProblem05(BaseTestProblem):
    _problem_func: Callable = collect_letters
    cases: List[Tuple[List, List, str]] = [
        (
            [["b", "C", "a", "B"]],
            [("A", "a"), ("B", "b"), ("C", "c")],
            "Base case",
        ),
        (
            [["b", "C", "a", "B", 5, 10]],
            [("A", "a"), ("B", "b"), ("C", "c")],
            "Digits",
        ),
        (
            [["b", "C", "a", "B", "5", "10"]],
            [("A", "a"), ("B", "b"), ("C", "c")],
            "String Digits",
        ),
        (
            [["b", "C", "a", "B", "FF", "Word"]],
            [("A", "a"), ("B", "b"), ("C", "c")],
            "Words",
        ),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertListEqual(expected, self.problem_func(*inputs))

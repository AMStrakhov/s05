from typing import Callable, List, Tuple

from problem_04 import filter_even
from .base_test_problem import BaseTestProblem


class TestProblem04(BaseTestProblem):
    _problem_func: Callable = filter_even
    cases: List[Tuple[List, List, str]] = [
        (
            [[1, 2, 4, 5, 6, 4]],
            [2, 4, 6, 4],
            "Base case",
        ),
        (
            [[]],
            [],
            "Empty List",
        ),
        (
            [[-2, 1, 2, 4, 5, 6]],
            [-2, 2, 4, 6],
            "Negative",
        ),
        (
            [[0, 4, 5]],
            [0, 4],
            "Zero",
        ),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertListEqual(expected, self.problem_func(*inputs))

from typing import Callable, List, Tuple

from problem_01 import summarize
from .base_test_problem import BaseTestProblem


class TestProblem01(BaseTestProblem):
    _problem_func: Callable = summarize
    cases: List[Tuple[List, int, str]] = [
        ([[1, 2, [3, 4], [5, 6]]], 21, "Base case"),
        ([[5, [[1, 3], 4], [4, 6], 8]], 31, "Base Case #2"),
        ([[[], [[], []]]], 0, "Empty List"),
        ([[1, 2, [-3, 4], [-5, 6]]], 5, "Negative numbers"),
    ]

    def test_function(self) -> None:
        self._test_function()

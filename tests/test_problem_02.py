from typing import Callable, List, Tuple

from problem_02 import summarize
from .base_test_problem import BaseTestProblem


class TestProblem02(BaseTestProblem):
    _problem_func: Callable = summarize
    cases: List[Tuple[List, int, str]] = [
        ([6], 12, "Base case"),
        ([10], 30, "Base Case #2"),
        ([0], 0, "Zero"),
        ([-4], 0, "Negative numbers"),
    ]

    def test_function(self) -> None:
        self._test_function()

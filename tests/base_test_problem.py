import io
from abc import ABC
from typing import Any, Callable, List, Tuple
from unittest import TestCase
from unittest.mock import patch


class BaseTestProblem(TestCase, ABC):
    _problem_func: Callable
    # Input, Output, Description
    cases: List[Tuple[List, str, str]] = []
    modules_to_patch: List[str] = []

    @classmethod
    def setUpClass(cls) -> None:
        cls._patch_modules()

    def problem_func(self, *args, **kwargs) -> Any:
        return self.__class__._problem_func(*args, **kwargs)

    def _test_case(self, inputs: List[str], outputs: str) -> None:
        with patch("builtins.input", side_effect=inputs):
            with patch("sys.stdout", new_callable=io.StringIO) as mocked_out:
                self.problem_func()
                self.assertEqual(outputs.strip("\n"), mocked_out.getvalue().strip("\n"))

    def _test_problem(self) -> None:
        for inputs, outputs, description in self.cases:
            with self.subTest(description):
                self._test_case(inputs, outputs)

    def _test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertEqual(expected, self.problem_func(*inputs))

    @classmethod
    def _patch_modules(cls) -> None:
        for module in cls.modules_to_patch:
            try:
                patch(
                    module,
                    side_effect=RuntimeError(f"Usage of `{module}` is not allowed."),
                ).start()
            except:
                ...

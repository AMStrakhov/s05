"""
Description:

Write a function to convert a list of letters in a list of tuples, in which
the first element is the letter in uppercase, the second — the letter in
lowercase. All tuples inside the list should be sorted alphabetically. All
duplicated values should be eliminated. Use map(). Words and digits
should be ignored.

Examples:
arguments: ["b", "C", "a", "B"]
result: [("A", "a"), ("B", "b"), ("C", "c")]

arguments: ["b", "C", "a", "B", 55, "abc", "5"]
result: [("A", "a"), ("B", "b"), ("C", "c")]

"""
from typing import List, Tuple


def collect_letters(letters: List[str]) -> List[Tuple[str, str]]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(collect_letters(["b", "C", "a", "B"]))

"""AoC 2024 Day 1 example tests."""

import pytest

from aoc2024.day01.data import PART_A_EXAMPLES, PART_B_EXAMPLES
from aoc2024.day01.solution import part_a_solution, part_b_solution


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        pytest.param(example.input, example.solution, id=f"{seq:02d}")
        for seq, example in enumerate(PART_A_EXAMPLES)
    ],
)
def test_example_a(given: str, expected: int) -> None:
    """Test the part a solution on the given example."""
    assert part_a_solution(given) == expected


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        pytest.param(example.input, example.solution, id=f"{seq:02d}")
        for seq, example in enumerate(PART_B_EXAMPLES)
    ],
)
def test_example_b(given: str, expected: int) -> None:
    """Test the part a solution on the given example."""
    assert part_b_solution(given) == expected

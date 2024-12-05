"""AoC 2024 Day 2 example tests."""

import pytest

from aoc2024.day02.data import PART_A_EXAMPLES, PART_B_EXAMPLES
from aoc2024.day02.solution import Report, part_a_solution, part_b_solution

TEST_REPORTS_A = (
    (Report((7, 6, 4, 2, 1)), True),
    (Report((1, 2, 7, 8, 9)), False),
    (Report((9, 7, 6, 2, 1)), False),
    (Report((1, 3, 2, 4, 5)), False),
    (Report((8, 6, 4, 4, 1)), False),
    (Report((1, 3, 6, 7, 9)), True),
)

TEST_REPORTS_B = (
    (Report((7, 6, 4, 2, 1)), True),
    (Report((1, 2, 7, 8, 9)), False),
    (Report((9, 7, 6, 2, 1)), False),
    (Report((1, 3, 2, 4, 5)), True),
    (Report((8, 6, 4, 4, 1)), True),
    (Report((1, 3, 6, 7, 9)), True),
)


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        pytest.param(report[0], report[1], id=f"{report[0]!s}")
        for report in TEST_REPORTS_A
    ],
)
def test_part_a_reports(report: Report, expected: int) -> None:
    """Test individual reports from Part A."""
    assert report.safe() == expected


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        pytest.param(report[0], report[1], id=f"{report[0]!s}")
        for report in TEST_REPORTS_B
    ],
)
def test_part_b_reports(report: Report, expected: bool) -> None:
    """Test individual reports from Part A."""
    assert report.damp_safe() == expected


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

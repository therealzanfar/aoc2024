"""AoC 2024 Day 1 example data and input functions."""

from aoc2024.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example(
        input="""3   4
4   3
2   5
1   3
3   9
3   3
""",
        solution=11,
    ),
]

PART_B_EXAMPLES: list[Example] = [
    Example(
        input="""3   4
4   3
2   5
1   3
3   9
3   3
""",
        solution=31,
    ),
]

PUZZLE_INPUT = get_puzzle_input(1)

PUZZLE_ANSWER_A: int | None = 2113135
PUZZLE_ANSWER_B: int | None = 19097157

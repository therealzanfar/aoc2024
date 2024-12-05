"""AoC 2024 Day 2 example data and input functions."""

from aoc2024.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example(
        input="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""",
        solution=2,
    ),
]

PART_B_EXAMPLES: list[Example] = [
    Example(
        input="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""",
        solution=4,
    ),
]

PUZZLE_INPUT = get_puzzle_input(2)

PUZZLE_ANSWER_A: int | None = 407
PUZZLE_ANSWER_B: int | None = 459

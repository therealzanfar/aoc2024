# cSpell:words xmul

"""AoC 2024 Day 3 example data and input functions."""

from aoc2024.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example(
        input="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
        solution=161,
    ),
]

PART_B_EXAMPLES: list[Example] = [
    Example(
        input="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
        solution=48,
    ),
]

PUZZLE_INPUT = get_puzzle_input(3)

PUZZLE_ANSWER_A: int | None = 183788984
PUZZLE_ANSWER_B: int | None = 62098619

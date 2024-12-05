"""AoC 2024 Day 4 example data and input functions."""

from aoc2024.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example(
        input="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
        solution=18,
    ),
]

PART_B_EXAMPLES: list[Example] = [
    Example(
        input="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
        solution=9,
    ),
]

PUZZLE_INPUT = get_puzzle_input(4)

PUZZLE_ANSWER_A: int | None = 2358
PUZZLE_ANSWER_B: int | None = None

"""General tools for working with AOC puzzles."""

from typing import Iterator, Tuple


def input_lines(input_: str) -> Iterator[str]:
    """Process an input into individual lines."""
    for line in input_.splitlines():
        if data := line.strip():
            yield data


def input_integers(input_: str) -> Iterator[int]:
    """Process an input into an integer per line."""
    for line in input_lines(input_):
        yield int(line)


def input_integer_series(input_: str) -> Iterator[Tuple[int, ...]]:
    """Process an input into a tuple of integers per line."""
    for line in input_lines(input_):
        yield tuple(int(n) for n in line.split())

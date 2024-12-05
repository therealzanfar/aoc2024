"""General tools for working with AoC puzzles."""

from collections import deque
from typing import Iterable, Iterator, Tuple, TypeVar


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


T = TypeVar("T")


def window(i: Iterable[T], size: int = 2) -> Iterator[tuple[T, ...]]:
    """Yield a sliding window of items from an iterator."""
    i = iter(i)
    w: deque[T] = deque()

    qsize = max(1, size)

    for _ in range(qsize):
        try:
            w.append(next(i))
        except StopIteration:
            yield tuple(w)
            return

    yield tuple(w)

    for e in i:
        w.append(e)
        w.popleft()
        yield tuple(w)

"""AoC 2024 Day 4 solutions."""

from dataclasses import dataclass
from typing import Iterator, NamedTuple, Optional


@dataclass(frozen=True)
class Coord:
    """A Coordinate."""

    x: int
    y: int

    def __add__(self, other: "Coord") -> "Coord":
        assert isinstance(other, self.__class__)
        return self.__class__(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Coord") -> "Coord":
        assert isinstance(other, self.__class__)
        return self.__class__(
            self.x - other.x,
            self.y - other.y,
        )


class Needle(NamedTuple):
    """A character in a needle."""

    offsets: tuple[Coord, ...]
    value: str


class Puzzle:
    """A word search puzzle."""

    def __init__(self, data: str) -> None:
        self._data = tuple(tuple(row) for row in data.splitlines())

        self.height = len(self._data)
        self.width = len(self._data[0])

    def contains(self, point: Coord) -> bool:
        """Determine if a coordinate is within the puzzle."""
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def points(self) -> Iterator[Coord]:
        """Return the coordinates of all data."""
        for y in range(self.height):
            for x in range(self.width):
                yield Coord(x, y)

    def at(self, point: Coord) -> str:
        """Return the data at the given point."""
        assert self.contains(point)

        return self._data[point.y][point.x]

    def seq(self, *points: Coord) -> str:
        """Return a string data at the given sequence of points."""
        return "".join(self.at(p) for p in points)

    def search(self, *needles: Needle) -> int:
        """Count the number of times `needle` appears in the puzzle."""
        found = 0

        for root in self.points():
            for needle in needles:
                seq = tuple(root + o for o in needle.offsets)
                val = needle.value

                try:
                    if self.seq(*seq) == val:
                        found += 1

                except AssertionError:
                    continue
        return found


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    assert len(input_) > 0

    puz = Puzzle(input_)
    needles = (
        # →
        Needle(
            offsets=(Coord(0, 0), Coord(0, 1), Coord(0, 2), Coord(0, 3)),
            value="XMAS",
        ),
        # ↘
        Needle(
            offsets=(Coord(0, 0), Coord(1, 1), Coord(2, 2), Coord(3, 3)),
            value="XMAS",
        ),
        # ↓
        Needle(
            offsets=(Coord(0, 0), Coord(1, 0), Coord(2, 0), Coord(3, 0)),
            value="XMAS",
        ),
        # ↙
        Needle(
            offsets=(Coord(0, 0), Coord(1, -1), Coord(2, -2), Coord(3, -3)),
            value="XMAS",
        ),
        # ←
        Needle(
            offsets=(Coord(0, 0), Coord(0, -1), Coord(0, -2), Coord(0, -3)),
            value="XMAS",
        ),
        # ↖
        Needle(
            offsets=(Coord(0, 0), Coord(-1, -1), Coord(-2, -2), Coord(-3, -3)),
            value="XMAS",
        ),
        # ↑
        Needle(
            offsets=(Coord(0, 0), Coord(-1, 0), Coord(-2, 0), Coord(-3, 0)),
            value="XMAS",
        ),
        # ↗
        Needle(
            offsets=(Coord(0, 0), Coord(-1, 1), Coord(-2, 2), Coord(-3, 3)),
            value="XMAS",
        ),
    )

    return puz.search(*needles)


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    assert len(input_) > 0

    puz = Puzzle(input_)
    needles = (
        Needle(
            offsets=(
                Coord(0, 0),
                Coord(-1, -1),
                Coord(1, -1),
                Coord(1, 1),
                Coord(-1, 1),
            ),
            value="AMMSS",
        ),
        Needle(
            offsets=(
                Coord(0, 0),
                Coord(1, -1),
                Coord(1, 1),
                Coord(-1, 1),
                Coord(-1, -1),
            ),
            value="AMMSS",
        ),
        Needle(
            offsets=(
                Coord(0, 0),
                Coord(1, 1),
                Coord(-1, 1),
                Coord(-1, -1),
                Coord(1, -1),
            ),
            value="AMMSS",
        ),
        Needle(
            offsets=(
                Coord(0, 0),
                Coord(-1, 1),
                Coord(-1, -1),
                Coord(1, -1),
                Coord(1, 1),
            ),
            value="AMMSS",
        ),
    )

    return puz.search(*needles)

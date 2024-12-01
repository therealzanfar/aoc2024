"""AOC 2024 Day 1 solutions."""

from collections import Counter
from typing import Optional


def parse_location_lists(input_: str) -> dict[str, list[int]]:
    """Parse the Day 1 input into a pair of integer lists."""
    locations: dict[str, list[int]] = {
        "A": [],
        "B": [],
    }

    for line in input_.splitlines():
        a_str, b_str = line.strip().split()

        locations["A"].append(int(a_str))
        locations["B"].append(int(b_str))

    return locations


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    assert len(input_) > 0

    locations = parse_location_lists(input_)

    locations["A"].sort()
    locations["B"].sort()

    total_dist = 0

    for a, b in zip(locations["A"], locations["B"]):
        item_dist = abs(a - b)
        total_dist += item_dist

    return total_dist


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    assert len(input_) > 0

    locations = parse_location_lists(input_)

    counts_a = Counter(locations["A"])
    counts_b = Counter(locations["B"])

    total_similarity = 0
    for id_, a_freq in counts_a.items():
        b_freq = counts_b.get(id_, 0)
        similarity = id_ * a_freq * b_freq

        total_similarity += similarity

    return total_similarity

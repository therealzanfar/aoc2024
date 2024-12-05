"""AoC 2024 Day 2 solutions."""

import logging
from dataclasses import dataclass
from typing import Iterable, Optional

from aoc2024.utils import input_integer_series, window


class Report(tuple):
    """Custom type for a report."""

    def safe_idx(self) -> int:
        """Return the index of the first pair that fails the safe test."""
        logger = logging.getLogger(__name__)

        increasing: bool | None = None

        for idx, (a, b) in enumerate(window(self)):
            pair_safe = is_pair_safe(a, b, increasing)

            increasing = pair_safe.increasing
            if not pair_safe.safe:
                return idx

        logger.debug("Sequence %s is safe", str(self))
        return -1

    def safe(self) -> bool:
        """Is the report safe?"""
        return self.safe_idx() == -1

    def damp_safe(self) -> bool:
        """Is the report safe after dampening?"""
        unsafe_idx = self.safe_idx()

        if unsafe_idx == -1:
            return True

        if unsafe_idx == 1:
            # If the second pair fails, it might be because the first pair is
            # the opposite direction of the rest of the sequence.
            new_report = Report(self[unsafe_idx:])
            if new_report.safe():
                return True

        new_report = Report(self[0:unsafe_idx] + self[unsafe_idx + 1 :])
        if new_report.safe():
            return True

        new_report = Report(self[0 : unsafe_idx + 1] + self[unsafe_idx + 2 :])
        return new_report.safe()


@dataclass
class PairSafeReport:  # noqa: D101
    safe: bool = True
    increasing: bool = True
    fail_direction: bool = False
    fail_gap: bool = False


def parse_reports(input_: str) -> Iterable[Report]:
    """Parse puzzle input into a sequence of Reports."""
    for r in input_integer_series(input_):
        yield Report(r)


def is_pair_safe(a: int, b: int, increasing: bool | None = None) -> PairSafeReport:
    """Determine if a report pair is safe."""
    max_diff = 3
    min_diff = 1

    logger = logging.getLogger(__name__)
    ret = PairSafeReport()

    diff = abs(a - b)
    ret.increasing = b - a > 0

    if ret.increasing != increasing and increasing is not None:
        logger.debug("Pair %d,%d is non-monotonic", a, b)

        ret.fail_direction = True
        ret.safe = False
        return ret

    if diff < min_diff or diff > max_diff:
        logger.debug(
            "Pair %d,%d difference is out-of-bounds",
            a,
            b,
        )

        ret.fail_gap = True
        ret.safe = False
        return ret

    return ret


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    assert len(input_) > 0

    reports = parse_reports(input_)
    return sum(r.safe() for r in reports)


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    assert len(input_) > 0

    reports = parse_reports(input_)
    return sum(r.damp_safe() for r in reports)
    return None

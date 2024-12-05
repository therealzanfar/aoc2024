"""AoC 2024 Day 3 solutions."""

import re
from typing import Optional

RE_MUL_CMD_A = re.compile(r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)", flags=re.IGNORECASE)

RE_MUL_CMD_B = re.compile(
    r"(?P<op>mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)|do\(\)|don't\(\))",
    flags=re.IGNORECASE,
)


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    assert len(input_) > 0

    mul_sum = 0

    for m in RE_MUL_CMD_A.finditer(input_):
        x = int(m["x"])
        y = int(m["y"])

        mul_sum += x * y

    return mul_sum


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    assert len(input_) > 0

    mul_sum = 0
    enabled = True

    for m in RE_MUL_CMD_B.finditer(input_):
        op = m["op"]
        if op.startswith("do("):
            enabled = True

        elif op.startswith("don't("):
            enabled = False

        elif op.startswith("mul(") and enabled:
            x = int(m["x"])
            y = int(m["y"])

            mul_sum += x * y

    return mul_sum

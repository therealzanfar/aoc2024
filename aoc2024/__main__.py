#! /usr/bin/env python3

"""Console script for aoc2024."""

import logging
import sys

import click
from rich.console import Console

from aoc2024.cli import CLICK_CONTEXT, setup_logging
from aoc2024.data import (
    DAY_COUNT_MAX,
    DAY_COUNT_MIN,
    PART_NAMES,
    YEAR,
    day_parts_with_solutions,
    days_with_solutions,
    get_puzzle_inputs,
    get_puzzle_solution,
)

ANSWER_LEN = "10"


@click.command(context_settings=CLICK_CONTEXT)
@click.argument("DAY", required=False, default="")
@click.argument("PART", required=False, default="")
@click.option(
    "--test",
    "-t",
    is_flag=True,
    flag_value=True,
    default=False,
    type=bool,
    help="Processes the example inputs instead of the user input",
)
@click.option("-v", "--verbose", count=True)
def cli(
    day: str = "",
    part: str = "",
    test: bool = False,
    verbose: int = 0,
) -> int:
    """
    Compute the solution for a given day's problem.

    DAY (1-25) and PART (A, B) select which problem to compute the solution
    to. If omitted, the system will attempt to identify the most recent,
    finished solution and compute that.

    Either DAY or PART can be 'ALL' in which case all possible days, or all
    possible parts for the selected days will be computed.
    """
    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s",
        ", ".join(f"{k!s}={v!r}" for k, v in args),
    )

    selected_days = parse_day_selection(day)
    selected_parts = parse_part_selection(selected_days, part)

    for day_no in selected_days:
        for part_id in selected_parts:
            print_day_report(day_no, part_id, test)

    return 0


def parse_day_selection(day: str) -> tuple[int, ...]:
    """Validate the day CLI argument."""
    logger = logging.getLogger(__name__)
    available_days = days_with_solutions()

    if len(available_days) < 1:
        raise click.ClickException("No days have solutions to compute")

    days: tuple[int, ...] = ()

    if day == "":
        days = (available_days[-1],)
        logger.info(f"Selected most recent day, {day}")

    elif day.upper() == "ALL":
        days = tuple(available_days)
        logger.info(f"Selected ALL days, {days}")

    else:
        try:
            day_no = int(day)
        except ValueError as e:
            raise click.ClickException(f"Invalid DAY selection: {day}") from e

        if day_no < DAY_COUNT_MIN or day_no > DAY_COUNT_MAX:
            raise click.ClickException(f"Invalid DAY value: {day_no}")

        days = (day_no,)
        logger.info(f"Selected day {day_no}")

    return days


def parse_part_selection(selected_days: tuple[int, ...], part: str) -> tuple[str, ...]:
    """Validate the part CLI argument."""
    logger = logging.getLogger(__name__)
    parts: tuple[str, ...] = ()

    if len(selected_days) == 1:
        day_no = selected_days[0]
        available_parts = day_parts_with_solutions(day_no)

        if len(available_parts) < 1:
            raise click.ClickException(f"Day {day_no} has no solutions to compute")

        part = part.upper()

        if part == "":
            part = available_parts[-1].upper()
            parts = (part,)
            logger.info("Selected most recent day {day} part, {part}")

        if part == "ALL":
            parts = tuple(PART_NAMES)
            logger.info(f"Selected ALL parts, {parts}")

        else:
            if part not in PART_NAMES:
                raise click.ClickException(f"Invalid PART selection: {part}")

            parts = (part,)
            logger.info(f"Selected part {part}")

    else:
        parts = tuple(PART_NAMES)
        logger.info(f"Multiple days selected; using ALL parts, {parts}")

    return parts


def print_day_report(day: int, part: str, test: bool) -> None:
    """Print the test or puzzle solution and result for a day and part."""
    data = get_puzzle_inputs(day, part, test)
    solution = get_puzzle_solution(day, part)

    c = Console(highlight=False)
    console_print = c.print

    for _idx, example in enumerate(data):
        answer = solution(example.input) or 0

        if _idx == 0:
            console_print(
                rf"Year [blue]{YEAR}[/blue], "
                rf"Day [blue]{day:02d}[/blue], "
                rf"Part [blue]{part.upper()}[/blue]: ",
                end="",
            )
        else:
            console_print(
                "                           ",
                end="",
            )

        if test:
            console_print(f"[yellow](Test {_idx+1:3d})[/yellow] ", end="")
        else:
            console_print("[green](-Puzzle-)[/green] ", end="")

        console_print(
            rf"Solution=[bright_white]{answer:{ANSWER_LEN}d}[/bright_white], ",
            end="",
        )

        expected = example.solution
        if expected is not None:
            console_print(
                rf"Expected=[bright_white]{expected:{ANSWER_LEN}d}[/bright_white]",
                end="",
            )

            if answer == expected:
                console_print(r"   [green]\[CORRECT][/green]")
            else:
                console_print(r"   [red]\[WRONG][/red]")

        else:
            print(f"         {'':{ANSWER_LEN}s}   [no answer found]")


if __name__ == "__main__":
    sys.exit(cli())

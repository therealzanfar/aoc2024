"""AoC 2024 Day 5 solutions."""

import logging
from collections import defaultdict
from typing import Optional

PrintRules = dict[int, set[int]]
PrintJob = tuple[int, ...]


def parse_print_rules(input_: str) -> tuple[PrintRules, list[PrintJob]]:
    """Parse the input into a set of rules and a list of jobs."""
    # logger = logging.getLogger(__name__)

    rules: PrintRules = defaultdict(set)
    jobs: list[PrintJob] = []

    mode = "rules"
    for line_raw in input_.splitlines():
        line = line_raw.strip()

        if mode == "rules":
            if line == "":
                mode = "jobs"

            else:
                a, b = line.split("|")
                rules[int(a)].add(int(b))

        elif mode == "jobs":
            pages = (int(p) for p in line.split(","))
            jobs.append(
                tuple(pages),
            )

        # logger.debug(
        #     "Mode: %s, line: %s | rules: %s, jobs: %s",
        #     mode,
        #     line,
        #     rules,
        #     jobs,
        # )

    return rules, jobs


def job_is_in_order(rules: PrintRules, job: PrintJob) -> bool:
    """Check if the job is in the correct order."""
    logger = logging.getLogger(__name__)
    prev_pages: set[int] = set()

    for page in job:
        page_must_precede = rules[page]
        out_of_order_pages = page_must_precede.intersection(prev_pages)

        if out_of_order_pages:
            logger.debug(
                "Job %s FAILS: %d must precede %s",
                str(job),
                page,
                str(out_of_order_pages),
            )
            # We've seen a page previously that must come
            # after the current page

            return False

        prev_pages.add(page)

    return True


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    assert len(input_) > 0

    logger = logging.getLogger(__name__)
    total_sum = 0
    rules, jobs = parse_print_rules(input_)

    logger.debug("Rules: %s", str(rules))
    logger.debug("Jobs: %s", str(jobs))

    for job in jobs:
        if job_is_in_order(rules, job):
            middle_idx = len(job) // 2
            total_sum += job[middle_idx]

    return total_sum


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    assert len(input_) > 0

    logger = logging.getLogger(__name__)
    total_sum = 0
    rules, jobs = parse_print_rules(input_)

    logger.debug("Rules: %s", str(rules))
    logger.debug("Jobs: %s", str(jobs))

    for job in jobs:
        if not job_is_in_order(rules, job):
            # Reduce the rule set to just the pages in the job
            relevant_rules: PrintRules = defaultdict(set)
            pages = set(job)

            for page in pages:
                relevant_rules[page] = rules[page].intersection(pages)

            # Sort by number of "must be previous to" pages
            # I.e., the last page must not have any pages that must appear
            # after it, and so on...
            ordered_pages = [
                page
                for page, _ in sorted(
                    relevant_rules.items(),
                    key=lambda r: len(r[1]),
                )
            ]

            # We don't care that the pages are actually in order, just sorted
            # because the middle index is the same regardless.
            middle_idx = len(ordered_pages) // 2
            total_sum += ordered_pages[middle_idx]

    return total_sum

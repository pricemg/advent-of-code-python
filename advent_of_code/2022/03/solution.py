"""Initial solution code for Advent of Code 2022 Day 03.

Documentation tests can be run using:
pytest --doctest-modules

Full tests can be run using:
pytest test_solution.py
"""
import logging
import pathlib
from string import ascii_letters

from codetiming import Timer


logger = logging.getLogger(__name__)


# Create mapping of lower + uppercase alphabet to number.
PRIORITY_CODES = {char: i+1 for i, char in enumerate(ascii_letters)}

def read_input(file: str) -> str:
    """Read input from file."""
    return pathlib.Path(file).read_text().strip()


def parse_input(raw_input: str) -> list[str]:
    """Parse input.
    
    Split raw input into entry for each line.
    """
    return raw_input.split('\n')


def part1(puzzle_data: list[str]) -> int:
    """Solve part 1."""
    # Split each string representing a rucksack in half.
    rucksacks = [
        (rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])
        for rucksack in puzzle_data
    ]

    # Use sets to find the common item in each rucksack.
    common_items = [
        # Can use `pop` on the set as rules state there will only ever be a
        # single value in common between the two rucksacks (i.e. number of
        # values in the set will be 1).
        (set(rucksack[0]) & set(rucksack[1])).pop()
        for rucksack in rucksacks
    ]

    # Map the common item for each rucksack to it's priority code.
    common_items_priority = [
        PRIORITY_CODES[item]
        for item in common_items
    ]

    return sum(common_items_priority)


def part2(puzzle_data: list[str]) -> int:
    """Solve part 2."""
    # Use sets to find the common item between rucksacks in groups of three.
    common_items = [
        # Can use `pop` on the set as rules state there will only ever be a
        # single value in common between the three rucksacks (i.e. number of
        # values in the set will be 1).
        (set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])).pop()
        # Use zip to group e.g. rucksacks 0,1,2; rucksacks 3,4,5... n-2,n-1,n.
        for rucksacks in zip(puzzle_data[0::3], puzzle_data[1::3], puzzle_data[2::3])
    ]

    # Map the common item for each rucksack to it's priority code.
    common_items_priority = [
        PRIORITY_CODES[item]
        for item in common_items
    ]

    return sum(common_items_priority)


@Timer(text='\nSolution found in {:0.8f} seconds.\n')
def solve(file: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    raw_input = read_input(file)

    puzzle_data = parse_input(raw_input)

    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input-files',
        type=str,
        nargs='+',
        dest='input_files',
        required=True,
        help='Input files to run.'
    )

    parser.add_argument(
        '--log-level',
        type=int,
        dest='log_level',
        required=False,
        default=20,
        help='The numeric value for desired logging verbosity.'
    )

    # Throw away additional arguments that are not defined.
    known_args, _ = parser.parse_known_args()

    logging.basicConfig(
        level=known_args.log_level,
        format='%(levelname)s: %(message)s',
    )

    for file in known_args.input_files:
        logger.info(f'#################')
        logger.info(f'Using {file=} as input')

        solutions = solve(file)

        logger.info(
            '\n'.join(f'{part}:\n{solution}\n'
            for part, solution in zip(('Part 1', 'Part 2'), solutions))
        )

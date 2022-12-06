"""Initial solution code for Advent of Code 2022 Day 06.

Documentation tests can be run using:
pytest --doctest-modules 
"""
import logging
import pathlib

from codetiming import Timer


logger = logging.getLogger(__name__)


def read_input(file: str) -> str:
    """Read input from file."""
    return pathlib.Path(file).read_text().strip()


def parse_input(puzzle_data: str) -> str:
    """Parse input.

    Example
    -------

    >>> parse_input('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    """
    return puzzle_data


def part1(puzzle_data: str) -> int:
    """Solve part 1.
    
    Example
    -------

    >>> part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    """
    marker_length = 4

    # Loop from 0, up to the start of the final length string.
    for i in range(0, len(puzzle_data)-(marker_length-1)):
        marker = puzzle_data[i:i+marker_length]
        processed_chars = i + marker_length
        if len(set(marker)) == marker_length:
            logger.debug(f"""
            Unique {marker=} found after {processed_chars} characters
            """)
            return processed_chars


def part2(puzzle_data) -> int:
    """Solve part 2.
    
    Example
    -------

    >>> part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    """
    message_length = 14

    # Loop from 0, up to the start of the final length string.
    for i in range(0, len(puzzle_data)-(message_length-1)):
        message = puzzle_data[i:i+message_length]
        processed_chars = i+message_length
        if len(set(message)) == message_length:
            logger.debug(f"""
            Unique {message=} found after {processed_chars} characters
            """)
            return processed_chars


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

"""Advent of Code solution December 9th part 1"""
from pathlib import Path
from typing import List

from int_computer import IntComputer as BOOSTComputer


def parse_puzzle_input() -> List[int]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_9th_puzzle_input.txt'), 'r') as input_file:
        return [int(code) for code in input_file.readline().split(',')]


def solve_part_1():
    c = BOOSTComputer(parse_puzzle_input(), inputs=[1])
    c.run_program()
    return c.outputs


"""
solve_part_1() =3765554916
"""

print(solve_part_1())

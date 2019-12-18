"""Advent of Code solution December 15th part 1"""
from pathlib import Path
from typing import List

def parse_puzzle_input() -> List[int]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_13th_puzzle_input.txt'), 'r') as input_file:
        return [int(code) for code in input_file.readline().split(',')]

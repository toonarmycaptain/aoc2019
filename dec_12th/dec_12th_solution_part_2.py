"""Advent of Code solution December 12th part 2"""
from typing import List

from dec_12th.dec_12th_solution_part_1 import (JupiterMoonSystem,
                                               Moon,
                                               parse_puzzle_input,
                                               )


def solve_part_2(data: List[List[int]]):
    system = JupiterMoonSystem([Moon(*args) for args in data])

    return system.find_repeat()








print(solve_part_2(parse_puzzle_input()))

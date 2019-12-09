"""Advent of Code solution December 9th part 2"""

from dec_9th.dec_9th_solution_part_1 import parse_puzzle_input
from int_computer import IntComputer as BOOSTComputer


def solve_part_2():
    c = BOOSTComputer(parse_puzzle_input(), inputs=[2])
    c.run_program()
    return c.outputs


"""
solve_part_2() = 76642
"""

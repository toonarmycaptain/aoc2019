"""Tests for Advent of Code solution December 8th part 1"""
from dec_8th.dec_8th_solution_part_1 import parse_puzzle_input, solve_part_a

def test_solve_part_a():
    assert solve_part_a(parse_puzzle_input()) == 1677

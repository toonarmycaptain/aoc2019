"""Tests for Advent of Code solution December 13th part 2"""
import pytest

from dec_13th.dec_13th_solution_part_2 import parse_puzzle_input, solve_part_2
def test_solve_part_2():
    assert solve_part_2(parse_puzzle_input()) == 14204
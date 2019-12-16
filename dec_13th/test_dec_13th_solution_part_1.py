"""Tests for Advent of Code solution December 13th part 1"""
import pytest

from dec_13th.dec_13th_solution_part_1 import parse_puzzle_input, solve_part_1

def test_solve_part_1():
    assert solve_part_1(parse_puzzle_input()) == 291
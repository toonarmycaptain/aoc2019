"""Tests for Advent of Code solution December 6th part 1"""
from dec_6th.dec_6th_solution_part_1 import count_direct_and_indirect, parse_puzzle_input


def test_count_direct_and_indirect():
    assert count_direct_and_indirect(['COM)B',
                                      'B)C',
                                      'C)D',
                                      'D)E',
                                      'E)F',
                                      'B)G',
                                      'G)H',
                                      'D)I',
                                      'E)J',
                                      'J)K',
                                      'K)L', ]) == 42


def test_solve():
    assert count_direct_and_indirect(parse_puzzle_input()) == 234446

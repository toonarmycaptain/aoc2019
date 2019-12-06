"""Tests for Advent of Code solution December 6th part 2"""

from dec_6th.dec_6th_solution_part_1 import parse_puzzle_input
from dec_6th.dec_6th_solution_part_2 import shortest_distance


def test_count_direct_and_indirect():
    assert shortest_distance(['COM)B',
                              'B)C',
                              'C)D',
                              'D)E',
                              'E)F',
                              'B)G',
                              'G)H',
                              'D)I',
                              'E)J',
                              'J)K',
                              'K)L',
                              'K)YOU',
                              'I)SAN', ], 'YOU', 'SAN') == (4, 'D')


def test_solve():
    assert shortest_distance(parse_puzzle_input(), 'SAN', 'YOU') == (385, 'QCT')

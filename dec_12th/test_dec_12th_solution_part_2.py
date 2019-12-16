"""Tests for Advent of Code solution December 12th part 2"""
import pytest

from dec_12th.dec_12th_solution_part_2 import solve_part_2, parse_puzzle_input


@pytest.mark.parametrize('test_data, repeat_steps',
                        [([[-1, 0, 2],
                           [2, -10, -7],
                           [4, -8, 8],
                           [3, 5, -1]], 2772),
                         ([[-8, -10, 0],
                           [5, 5, 10],
                           [2, -7, 3],
                           [9, -8, -3]], 4686774924),
                         ])
def test_solve_part_2_example(test_data, repeat_steps):
    assert solve_part_2(test_data) == repeat_steps


# def test_solve_part_2():  # Long running test
#     assert solve_part_2(parse_puzzle_input()) == 528250271633772

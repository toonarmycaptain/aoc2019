"""Tests for Advent of Code solution December 12th part 1"""
import pytest

from dec_12th.dec_12th_solution_part_1 import solve_part_1


@pytest.mark.parametrize('test_data, steps, total_energy, ',
                         [([[-1, 0, 2],
                            [2, -10, -7],
                            [4, -8, 8],
                            [3, 5, -1]], 10, 179),
                          ([[-8, -10, 0],
                            [5, 5, 10],
                            [2, -7, 3],
                            [9, -8, -3]], 100, 1940),
                          ])
def test_solve_part_1(test_data, steps, total_energy):
    assert solve_part_1(test_data, steps) == total_energy

# def test_solve_part_1():   # Long running test
#     assert solve_part_1() == 8287

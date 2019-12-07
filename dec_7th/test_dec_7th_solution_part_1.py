"""Tests for Advent of Code solution December 7th part 1"""
import pytest

from dec_7th.dec_7th_solution_part_1 import run_sequence, run_amplifier_computer, solve_part_1


@pytest.mark.parametrize('test_program, test_input, expected_output',
                         [([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0], 43210),
                          ([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                            101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0], [0, 1, 2, 3, 4], 54321),
                          ([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                            1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2], 65210),
                          ])
def test_run_sequence(test_program, test_input, expected_output):
    assert run_sequence(test_program, test_input) == expected_output


@pytest.mark.parametrize('test_program, test_input, expected_output',
                         [([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 0], 4),
                          ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [3, 4], 43),
                          ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [2, 43], 432),
                          ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [1, 432], 4321),
                          ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [0, 4321], 43210),
                          ])
def test_run_amplifier_computer(test_program, test_input, expected_output):
    assert run_amplifier_computer(test_program, test_input) == expected_output


def test_solve_part_1():
    assert solve_part_1() == 440880

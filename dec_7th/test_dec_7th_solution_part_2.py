"""Tests for Advent of Code solution December 7th part 2"""
import pytest

from dec_7th.dec_7th_solution_part_1 import parse_puzzle_input
from dec_7th.dec_7th_solution_part_2 import (feedback_computer,
                                             solve_part_2,
                                             )

from int_computer import IntComputer as AmpComputer


@pytest.mark.parametrize(
    'test_program, inputs, output',
    [
        ([9, 1, 203, 7, 4, 8, 99, 0, 0], [42], [42])
    ])
def test_pause_on_output(test_program, inputs, output):
    b = AmpComputer(test_program, inputs=inputs, pause_on_output=True)
    assert not b.run_program()  # False because has not completed, merely paused on output.
    assert b.outputs == output


@pytest.mark.parametrize(
    'test_intcode_program, test_phase_inputs, output',
    [([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
       27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5], 139629729),
     ([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
       -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
       53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], [9, 7, 8, 5, 6], 18216)
     ])
def test_feedback_computer(test_intcode_program, test_phase_inputs, output):
    assert feedback_computer(intcode_program=test_intcode_program,
                             phase_sequence=test_phase_inputs) == output


def test_solve_part_two():
    assert solve_part_2(parse_puzzle_input()) == 3745599

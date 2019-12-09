"""Tests for Advent of Code solution December 9th part 1"""
import pytest

from dec_9th.dec_9th_solution_part_1 import solve_part_1
from int_computer import IntComputer as BOOSTComputer


@pytest.mark.parametrize(
    'test_program, output',
    [([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99],
      [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]),
     # takes no input and produces a copy of itself as output.
     ([1102, 34915192, 34915192, 7, 4, 7, 99, 0], [1219070632396864]),
     ([104, 1125899906842624, 99], [1125899906842624]),
     ])
def test_BOOST_computer(test_program, output):
    b = BOOSTComputer(test_program)
    assert b.run_program()
    assert b.outputs == output


@pytest.mark.parametrize(
    'test_program, input, output',
    [
        ([9, 1, 203, 7, 4, 8, 99, 0, 0], [42], [42])
     ])
def test_BOOST_computer_kevins_test(test_program, input, output):
    b = BOOSTComputer(test_program, inputs=input)
    assert b.run_program()
    assert b.outputs == output

@pytest.mark.parametrize(
    'test_program, input, output',
    [
        ([9, 1, 203, 7, 4, 8, 99, 0, 0], [42], [42])
     ])
def test_pause_on_output(test_program, input, output):
    b = BOOSTComputer(test_program, inputs=input, pause_on_output=True)
    assert not b.run_program() # False because has not completed, merely paused on output.
    assert b.outputs == output

def test_solve_part_1():
    assert solve_part_1() == [3765554916]
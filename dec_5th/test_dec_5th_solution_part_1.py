"""Tests for Advent of Code solution December 5th part 1"""
import pytest

from dec_5th.dec_5th_solution_part_1 import TESTComputer


def test_TESTcomputer():
    inputs = [50, ]
    outputs = [50, ]
    intcode_program_initial_state = [3, 0, 4, 0, 99]
    intcode_program_end_state = [50, 0, 4, 0, 99]
    test_computer = TESTComputer(intcode_program_initial_state, inputs)
    program_end_state = test_computer.run_program()
    assert test_computer.outputs == outputs
    assert program_end_state == intcode_program_end_state

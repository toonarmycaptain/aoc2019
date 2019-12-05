"""Tests for Advent of Code solution December 2nd part 1"""
import pytest

from dec_2nd.dec_2nd_solution_part_1 import Computer, fix_program


@pytest.mark.parametrize('test_program_input, output',
                         [([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
                          ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
                          ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
                          ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
                          ])
def test_computer(test_program_input, output):
    c = Computer(test_program_input)
    assert c.run_program() == output


def test_validate_opcode_position():
    with pytest.raises(ValueError):
        assert Computer.validate_opcode_position(5)


def test_solve_day_one():
    assert fix_program() == 6087827

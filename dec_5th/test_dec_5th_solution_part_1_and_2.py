"""Tests for Advent of Code solution December 5th part 1"""
import pytest

from dec_5th.dec_5th_solution_part_1and_2 import TESTComputer, parse_puzzle_input


def test_TESTcomputer():
    inputs = [50, ]
    outputs = [50, ]
    intcode_program_initial_state = [3, 0, 4, 0, 99]
    intcode_program_end_state = [50, 0, 4, 0, 99]
    test_computer = TESTComputer(intcode_program_initial_state, inputs)
    program_end_state = test_computer.run_program()
    assert test_computer.outputs == outputs
    assert program_end_state == intcode_program_end_state


@pytest.mark.parametrize('test_program_input, output',
                         [([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
                          ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
                          ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
                          ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
                          ])
def test_TESTcomputer_original_tests(test_program_input, output):
    c = TESTComputer(test_program_input)
    assert c.run_program() == output


def test_solve_puzzle():
    c = TESTComputer(parse_puzzle_input(), [1])
    c.run_program()
    assert c.outputs[-1] == 15386262


@pytest.mark.parametrize(
    'program, inputs, output',
    [  # Input zero should output 0
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0, ], [0, ]),
        ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [0, ], [0, ]),
        # Input greater than zero should output 1
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [27, ], [1, ]),
        ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [27, ], [1, ]),
    ])
def test_TESTComputer_new_opcodes(program, inputs, output):
    c = TESTComputer(program, inputs)
    c.run_program()
    assert c.outputs == output

larger_example_input = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
@pytest.mark.parametrize(
    'program, inputs, output',
    [  # Input less than 8 should output 999
        (larger_example_input, [7, ], [999, ]),
        # Input 8 should output 1000
        (larger_example_input, [8, ], [1000,]),
        # Input greater than 8 should output 1001
        (larger_example_input, [9, ], [1001, ]),
    ])
def test_TESTComputer_larger_example(program, inputs, output):
    c = TESTComputer(program, inputs)
    c.run_program()
    assert c.outputs == output

def test_solve_puzzle_part_2():
    c = TESTComputer(parse_puzzle_input(), [5])
    c.run_program()
    assert c.outputs[-1] == 10376124
"""Advent of Code solution December 7th part 2"""

import itertools

from typing import List, Sequence

from int_computer import IntComputer as AmpComputer


def feedback_computer(intcode_program: List[int], phase_sequence: Sequence[int]):
    if len(phase_sequence) != 5:
        raise ValueError
    # Setup AmpComputers
    amp_computers: List[AmpComputer] = []
    for phase in phase_sequence:
        amp_computers.append(AmpComputer(intcode_program=intcode_program[:],
                                         inputs=[phase],
                                         pause_on_output=True))

    next_input = 0  # Initial input given to first AmpComputer A
    try:
        while True:
            for amp_computer in amp_computers:
                amp_computer.inputs.append(next_input)
                if amp_computer.run_program():
                    raise StopIteration  # if run_program returns True instead of None, program has ended.
                next_input = amp_computer.outputs[-1]
    except StopIteration:
        return amp_computers[-1].outputs[-1]


def solve_part_2(intcode_program):
    sequences = []
    for sequence in itertools.permutations(list(range(5, 10))):
        output = feedback_computer(intcode_program=intcode_program,
                                   phase_sequence=sequence)
        sequences.append(output)
    return max(sequences)


"""
from dec_7th.dec_7th_solution_part_1 import parse_puzzle_input
solve_part_2(parse_puzzle_input())) = 3745599
"""

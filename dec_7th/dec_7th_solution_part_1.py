"""Advent of Code solution December 7th part 1"""
import itertools

from pathlib import Path
from typing import Iterable, List

from int_computer import IntComputer as AmplifierComputer


def parse_puzzle_input() -> List[int]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_7th_puzzle_input.txt'), 'r') as input_file:
        return [int(code) for code in input_file.readline().split(',')]


def run_amplifier_computer(intcode_program, input_sequence: List[int]) -> int:
    computer = AmplifierComputer(intcode_program=intcode_program,
                                 inputs=input_sequence)
    computer.run_program()
    outputs = computer.outputs
    return int(''.join(map(str, outputs)))


def run_sequence(intcode_program: object, phase_input_sequence: Iterable[int]) -> int:
    final_output_signal = 0
    initial_input = 0
    for phase_input in phase_input_sequence:
        output = run_amplifier_computer(intcode_program=intcode_program,
                                        input_sequence=[phase_input, initial_input])
        print(f'{phase_input_sequence=}, {phase_input=}, {initial_input=}, {output=}, {final_output_signal=}')
        initial_input = output
        final_output_signal = output
    print(f'{final_output_signal=}')
    return final_output_signal


def solve_part_1(intcode_program: List[int] = parse_puzzle_input()):
    sequences = []
    for sequence in itertools.permutations(list(range(5))):
        output = run_sequence(intcode_program=intcode_program,
                              phase_input_sequence=sequence)
        sequences.append(output)
    return max(sequences)


"""
solve_part_1(parse_puzzle_input()) = 440880
"""

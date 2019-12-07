"""Advent of Code solution December 7th part 2"""

import itertools

from pathlib import Path
from typing import List

from dec_5th.dec_5th_solution_part_1and_2 import TESTComputer as AmplifierComputer
from dec_7th.dec_7th_solution_part_1 import parse_puzzle_input


def feedback(intcode_program):
    max_sequence = None
    max_output = 0

    for sequence in itertools.permutations(list(range(5, 10))):
        result = 0

        ###  run each sequence

        if signal > max_output:
            max_output = signal
            max_sequence = sequence

    return max_output, "".join(str(x) for x in max_sequence)


print(feedback(parse_puzzle_input()))

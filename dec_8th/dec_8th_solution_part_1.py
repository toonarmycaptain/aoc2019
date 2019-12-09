"""Advent of Code solution December 8th part 1"""

from pathlib import Path
from typing import List


def parse_puzzle_input(puzzle: str=None, layer_line_length: int = 25, layer_num_lines: int = 6) -> List[List[str]]:
    problem_folder = Path(__file__).parent
    if not puzzle:
        with open(Path(problem_folder, 'dec_8th_puzzle_input.txt'), 'r') as input_file:
            puzzle = input_file.readline()
    layered_puzzle: list = []

    layer_pixels = layer_line_length*layer_num_lines
    while len(puzzle) != 0:
        layered_puzzle.append(list(puzzle[:layer_pixels]))
        puzzle = puzzle[layer_pixels:]

    return layered_puzzle


def solve_part_a(puzzle_layers: List[List[str]], line_length: int = 150):
    least_zeros = line_length + 1
    least_zeros_layer_str = ''
    for layer in puzzle_layers:
        zeros_layer_str = ''.join(layer)
        zeros = zeros_layer_str.count('0')
        if least_zeros > zeros:
            least_zeros, least_zeros_layer_str = zeros, zeros_layer_str

    return least_zeros_layer_str.count('1') * least_zeros_layer_str.count('2')


"""
solve_part_a(parse_puzzle_input()) = 1677
"""

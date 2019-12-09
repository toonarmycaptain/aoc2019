"""Advent of Code solution December 8th part 2"""
from typing import List

from dec_8th.dec_8th_solution_part_1 import parse_puzzle_input


def decode_image(puzzle_input: List[List[str]], line_length: int = 25 , num_lines:int= 6) -> List[str]:
    # split layers into pixels
    final_image = ['*' for pixel in range(line_length*num_lines)]

    for i in final_image:
        assert isinstance(i, str)
        assert len(i) == 1

    for position, pixel in enumerate(final_image):
        for layer in puzzle_input:
            if layer[position] == '2':
                continue
            elif final_image[position] == '*':
                final_image[position] = layer[position]
                break

    return final_image


def print_image(puzzle_input: List[List[str]], line_length: int = 25):
    final_image = decode_image(puzzle_input)

    # "Colourise" for output
    for index, pixel in enumerate(final_image):
        if pixel == '0':
            final_image[index] = '.'
        elif pixel == '1':
            final_image[index] = 'X'

    for i in range(0, len(final_image), line_length):
        print(final_image[i:i + line_length])

    return final_image
# decode_image(parse_puzzle_input())
# print(print_image(parse_puzzle_input(), 25))
#
print_image(parse_puzzle_input(), 25)

"""Advent of Code solution December 4th part 2

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a
 larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly
two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double
22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""
from typing import List

from dec_4th.dec_4th_solution_part_1 import is_six_digits, no_descending_digits


def two_adjacent_digits_not_part_of_larger_group(candidate_password: str) -> bool:
    for char_index, char in enumerate(candidate_password[:-1]):
        if candidate_password[char_index + 1] == char:
            # Case where first 2 chars identical but not third.
            if char_index == 0 and char != candidate_password[char_index + 2]:
                return True
            # Check preceding character != char, char after second character != char
            if candidate_password[char_index - 1] != char:
                # Don't check char following last char in str:
                if char_index == len(candidate_password) - 2:
                    return True
                if char != candidate_password[char_index + 2]:
                    return True
    return False


def find_passwords_pair_not_part_of_larger_group(minimum: int, maximum: int) -> List[str]:
    if maximum < minimum:
        raise ValueError

    valid_passwords = []
    for candidate_password in range(minimum, maximum + 1):
        candidate_password_str = str(candidate_password)
        if all([is_six_digits(candidate_password_str),
                no_descending_digits(candidate_password_str),
                two_adjacent_digits_not_part_of_larger_group(candidate_password_str),
                ]):
            valid_passwords.append(candidate_password_str)
    return valid_passwords


def how_many_passwords_pair_not_part_of_larger_group(raw_input: str) -> int:
    range_min_str, range_max_str = raw_input.split('-')
    range_min, range_max = int(range_min_str), int(range_max_str)
    return len(find_passwords_pair_not_part_of_larger_group(range_min, range_max))


"""
how_many_passwords_pair_not_part_of_larger_group(RAW_PUZZLE_INPUT) = 334
"""

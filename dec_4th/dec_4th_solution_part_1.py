"""Advent of Code solution December 4th part 1

--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had
written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same
(like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 356261-846303.
"""
from typing import List

RAW_PUZZLE_INPUT = '356261-846303'


def is_six_digits(candidate_password: str) -> bool:
    if len(str(candidate_password)) == 6:
        return True
    return False


def two_adjacent_digits(candidate_password: str) -> bool:
    if any([char == candidate_password[char_index + 1] for char_index, char in enumerate(candidate_password[:-1])]):
        return True
    return False


def no_descending_digits(candidate_password: str) -> bool:
    if any([int(char) > int(candidate_password[char_index + 1])
            for char_index, char in enumerate(candidate_password[:-1])]):
        return False
    return True


def find_passwords(minimum: int, maximum: int) -> List[str]:
    if maximum < minimum:
        raise ValueError

    valid_passwords = []
    for candidate_password in range(minimum, maximum + 1):
        candidate_password_str = str(candidate_password)
        if all([is_six_digits(candidate_password_str),
                two_adjacent_digits(candidate_password_str),
                no_descending_digits(candidate_password_str),
                ]):
            valid_passwords.append(candidate_password_str)
    return valid_passwords


def how_many_passwords(raw_input: str) -> int:
    range_min_str, range_max_str = raw_input.split('-')
    range_min, range_max = int(range_min_str), int(range_max_str)
    return len(find_passwords(range_min, range_max))


"""
how_many_passwords(RAW_PUZZLE_INPUT) = 544
"""

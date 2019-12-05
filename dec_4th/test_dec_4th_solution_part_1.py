"""Tests for Advent of Code solution December 4th part 1"""

import pytest

from dec_4th.dec_4th_solution_part_1 import (find_passwords,
                                             how_many_passwords,
                                             is_six_digits,
                                             no_descending_digits,
                                             two_adjacent_digits,
                                             )


@pytest.mark.parametrize(
    'candidate_password',
    ['111111',  # Meets these criteria (double 11, never decreases).
     '123345',  # Meets criteria.
     '223450',  # Does not meet these criteria (decreasing pair of digits 50).
     '123789',  # Does not meet these criteria (no double).
     '431431',  # Does not meet these criteria (no double).
     pytest.param('12345', marks=pytest.mark.xfail),  # 5 digits
     pytest.param('1234567', marks=pytest.mark.xfail),  # 7 digits
     ])
def test_is_six_digits(candidate_password):
    assert is_six_digits(candidate_password)


@pytest.mark.parametrize(
    'candidate_password',
    ['111111',  # Meets these criteria (double 11, never decreases).
     '123345',  # Meets criteria.
     pytest.param('223450', marks=pytest.mark.xfail),  # Does not meet these criteria (decreasing pair of digits 50).
     '123789',
     pytest.param('431431', marks=pytest.mark.xfail),  # Does not meet these criteria (no double).
     ]
)
def test_no_descending_digits(candidate_password):
    assert no_descending_digits(candidate_password)


@pytest.mark.parametrize('candidate_password',
                         ['111111',  # Meets these criteria (double 11, never decreases).
                          '123345',  # Meets criteria.
                          '223450',  # Does not meet these criteria (decreasing pair of digits 50).
                          pytest.param('123789', marks=pytest.mark.xfail),  # Does not meet these criteria (no double).
                          pytest.param('431431', marks=pytest.mark.xfail),  # No double.
                          ])
def test_two_adjacent_digits(candidate_password):
    assert two_adjacent_digits(candidate_password)


test_range = 000000, 999999
test_valid_passwords = find_passwords(*test_range)


@pytest.mark.parametrize(
    'candidate_password',
    ['111111',  # Meets these criteria (double 11, never decreases).
     '123345',  # Meets criteria.
     pytest.param('223450', marks=pytest.mark.xfail),  # Does not meet these criteria (decreasing pair of digits 50).
     pytest.param('123789', marks=pytest.mark.xfail),  # Does not meet these criteria (no double).
     pytest.param('431431', marks=pytest.mark.xfail),  # Does not meet these criteria (no double).
     ])
def test_find_passwords(candidate_password):
    assert candidate_password in test_valid_passwords


def test_how_many_passwords_raising_error():
    with pytest.raises(ValueError):
        how_many_passwords('123449-123445')


def test_how_many_passwords():
    assert how_many_passwords('123449-123455') == 2  # 123449, 123445

"""Tests for Advent of Code solution December 4th part 2"""
import pytest

from dec_4th.dec_4th_solution_part_2 import (how_many_passwords_pair_not_part_of_larger_group,
                                             two_adjacent_digits_not_part_of_larger_group,
                                             )


@pytest.mark.parametrize(
    'candidate_password',
    ['112233',
     pytest.param('123444', marks=pytest.mark.xfail),  # Repeated 44 is part of a larger group of 444).
     '111122',
     pytest.param('431431', marks=pytest.mark.xfail),  # Does not meet these criteria (no double).
     '112112',
     '122122',
     '111221',
     '111211',
     '111233',
     pytest.param('555558', marks=pytest.mark.xfail),
     pytest.param('356777', marks=pytest.mark.xfail),
     '444455',
     pytest.param('444456', marks=pytest.mark.xfail),
     ])
def test_two_adjacent_digits_not_part_of_larger_group(candidate_password):
    assert two_adjacent_digits_not_part_of_larger_group(candidate_password)


def test_how_many_passwords_pair_not_part_of_larger_group_raising_error():
    with pytest.raises(ValueError):
        how_many_passwords_pair_not_part_of_larger_group('123449-123445')


def test_how_many_passwords_pair_not_part_of_larger_group():
    assert how_many_passwords_pair_not_part_of_larger_group('123555-123569') == 5

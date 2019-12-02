"""Tests for Advent of Code solution December 1st part 2"""

import pytest

from dec_1st.dec_1st_solution_part_2 import module_fuel_req_with_fuel, sum_of_fuel_requirements_with_fuel, fuel_fuel_req


@pytest.mark.parametrize(
    'test_module_fuel, fuel_for_fuel_requirement',
    [(2, 0),
     (2, 0),
     (654, 216 + 70 + 21 + 5),
     (33583, 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2),
     ])
def test_fuel_fuel_req(test_module_fuel, fuel_for_fuel_requirement):
    assert fuel_fuel_req(test_module_fuel) == fuel_for_fuel_requirement

@pytest.mark.parametrize(
    'test_module_mass, fuel_requirement',
    [(12, 2),
     (14, 2),
     (1969, 654 + 216 + 70 + 21 + 5),
     (100756, 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2),
     ])
def test_module_fuel_req_with_fuel(test_module_mass, fuel_requirement):
    assert module_fuel_req_with_fuel(test_module_mass) == fuel_requirement


def test_sum_of_fuel_requirements_with_fuel():
    assert sum_of_fuel_requirements_with_fuel([12, 14, 1969, 100756]) == 2+2+966+50346
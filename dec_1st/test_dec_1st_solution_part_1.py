"""Tests for Advent of Code solution December 1st"""

import pytest

from dec_1st.dec_1st_solution_part_1 import mass_fuel_req, sum_of_fuel_requirements


@pytest.mark.parametrize(
    'test_module_mass, fuel_requirement',
    [(12, 2),
     (14, 2),
     (1969, 654),
     (100756, 33583),
     (2, 0),  # Ensure zero or -tve fuel returns 0
     (6, 0 ),
     ])
def test_module_fuel_req(test_module_mass, fuel_requirement):
    assert mass_fuel_req(test_module_mass) == fuel_requirement

def test_sum_of_fuel_requirments():
    assert sum_of_fuel_requirements([12, 14, 1969, 100756]) == 2+2+654+33583
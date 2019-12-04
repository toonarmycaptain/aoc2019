"""Tests for Advent of Code solution December 3rd part 1"""

import pytest

from dec_3rd.dec_3rd_solution_part_1 import ManhattanComputer


@pytest.mark.parametrize(
    'test_wire_1, test_wire_2, min_dist',
    [
        (['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
         159),
        (['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
         135),
    ],
)
def test_compute_manhattan_distance(test_wire_1, test_wire_2, min_dist) -> None:
    computer = ManhattanComputer(test_wire_1, test_wire_2)
    assert computer.compute_manhattan_distance() == min_dist

"""Tests for Advent of Code solution December 3rd part 2"""
import pytest

from dec_3rd.dec_3rd_solution_part_2 import TimingComputer


@pytest.mark.parametrize(
    'test_wire_1, test_wire_2, earliest_intersection',
    [
        (['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
         610),
        (['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
         410),
    ],
)
def test_compute_earliest_intersection(test_wire_1, test_wire_2, earliest_intersection) -> None:
    computer = TimingComputer(test_wire_1, test_wire_2)
    assert computer.compute_earliest_intersection() == earliest_intersection

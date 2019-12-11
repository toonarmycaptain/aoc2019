"""Advent of Code solution December 11th part 2

--- Part Two ---
You're not sure what it's trying to paint, but it's definitely not a
registration identifier. The Space Police are getting impatient.

Checking your external ship cameras again, you notice a white panel marked
"emergency hull painting robot starting panel". The rest of the panels are
still black, but it looks like the robot was expecting to start on a white
panel, not a black one.

Based on the Space Law Space Brochure that the Space Police attached to one of
your windows, a valid registration identifier is always eight capital letters.
After starting the robot on a single white panel instead, what registration
identifier does it paint on your hull?
"""
from collections import defaultdict
from numbers import Complex
from typing import Tuple, Dict

from dec_11th.dec_11th_solution_part_1 import HullPainterRobot, parse_puzzle_input


def print_panels(panels: Dict[Complex, int]) -> Dict[Tuple[float, float], int]:
    pixels = defaultdict(lambda: 0,  # Use a default dict to fill in unpainted panels.
                         {(panel_coord.real, panel_coord.imag): panels[panel_coord]
                          for panel_coord in panels.keys()})

    x_coords, y_coords = set(), set()
    for coord in pixels.keys():
        x_coords.add(coord[0])
        y_coords.add(coord[1])

    x_range = range(int(min(x_coords)), int(max(x_coords)) + 1)
    y_range = range(int(min(y_coords)), int(max(y_coords)) + 1)

    for y in y_range:
        print("".join(["  ", "**"][pixels[x, y]] for x in x_range))

    return pixels


def solve_part_2() -> Dict[Tuple[float, float], int]:
    t = HullPainterRobot(parse_puzzle_input(), initial_panel_colour=1)
    t.paint_panels()

    return print_panels(t.hull_panels)


print(solve_part_2())
"""
solve_part_2() = JFBERBUH (it is upside down)
"""

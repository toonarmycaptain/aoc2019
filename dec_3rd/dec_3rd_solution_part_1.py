"""Advent of Code solution December 3rd part 1

***CREDIT DUE***
I adapted the implementation at https://github.com/anthonywritescode/aoc2019/tree/master/day03

--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station.
During the rush back on Earth, the fuel management system wasn't completely installed, so that's
next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a
central port and extend outward on a grid. You trace the path each wire takes as it leaves the
central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need
to find the intersection point closest to the central port. Because the wires are on a grid, use the
 Manhattan distance for this measurement. While the wires do technically cross right at the central
 port where they both start, this point does not count, nor does a wire count as crossing with
 itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it
goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port:
 its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""

from pathlib import Path
from typing import Callable, List, Set, Tuple


def parse_puzzle_input() -> Tuple[List[str], ...]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_3rd_puzzle_input.txt'), 'r') as input_file:
        wires = tuple(wire_str.split(',') for wire_str in input_file.read().strip().splitlines())
        return wires


PUZZLE_INPUT = parse_puzzle_input()


class ManhattanComputer:
    def __init__(self, wire_1_path: List[str], wire_2_path: List[str]):
        self.wire_1_path = wire_1_path
        self.wire_2_path = wire_2_path

        self.direction_xy = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1),
        }

        self._manhattan_grid: Set[Tuple[int, int]] = set()
        self._manhattan_intersections: List[int] = []

    @staticmethod
    def _increment_position(location_a: Tuple[int, int],
                            location_b: Tuple[int, int]
                            ) -> Tuple[int, int]:
        return location_a[0] + location_b[0], location_a[1] + location_b[1]

    def trace_wire(self, wire_path: List[str], action: Callable[[Tuple[int, int]], None]) -> None:
        position = (0, 0)
        for vector in wire_path:
            direction, magnitude = vector[0], int(vector[1:])
            xy_increment = self.direction_xy[direction]
            for _ in range(magnitude):
                position = self._increment_position(position, xy_increment)
                action(position)

    def _save_to_grid(self, position: Tuple[int, int]) -> None:
        self._manhattan_grid.add(position)

    def _collect_distance_at_intersection(self, position: Tuple[int, int]) -> None:
        if position in self._manhattan_grid:
            self._manhattan_intersections.append(sum(abs(p) for p in position))

    def compute_manhattan_distance(self) -> int:
        self.trace_wire(self.wire_1_path, self._save_to_grid)
        self.trace_wire(self.wire_2_path, self._collect_distance_at_intersection)

        return min(self._manhattan_intersections)


"""
m = ManhattanComputer(*parse_puzzle_input())
m.compute_manhattan_distance() = 316
"""

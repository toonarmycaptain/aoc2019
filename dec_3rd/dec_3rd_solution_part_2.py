"""Advent of Code solution December 3rd part 2

***CREDIT DUE***
I adapted the implementation at https://github.com/anthonywritescode/aoc2019/tree/master/day03

--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal
delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the
intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid
multiple times, use the steps value from the first time it visits that position when calculating the
total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to
that location, including the intersection being considered. Again consider the example from above:

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
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20
steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second
wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""
import collections
import sys

from typing import Dict, List, Tuple

from dec_3rd.dec_3rd_solution_part_1 import ManhattanComputer, parse_puzzle_input


class TimingComputer(ManhattanComputer):
    def __init__(self, wire_1_path: List[str], wire_2_path: List[str]):
        ManhattanComputer.__init__(self, wire_1_path, wire_2_path)
        self._timed_intersections = []
        self._timing_grid: Dict[Tuple[int, int], int] = collections.defaultdict(lambda: sys.maxsize)
        self.__intersection_increment = 0

    def _record_minimum_position(self, position: Tuple[int, int]) -> None:
        self.__intersection_increment += 1
        self._timing_grid[position] = min(self._timing_grid[position], self.__intersection_increment)

    def _record_intersection_actions(self, position: Tuple[int, int]) -> None:
        self.__intersection_increment += 1
        if position in self._timing_grid:
            self._timed_intersections.append(self._timing_grid[position] + self.__intersection_increment)

    def compute_earliest_intersection(self):
        self.__intersection_increment = 0
        self.trace_wire(self.wire_1_path, self._record_minimum_position)
        self.__intersection_increment = 0
        self.trace_wire(self.wire_2_path, self._record_intersection_actions)

        return min(self._timed_intersections)


"""
t = TimingComputer(*parse_puzzle_input())
t.compute_earliest_intersection() = 16368
"""

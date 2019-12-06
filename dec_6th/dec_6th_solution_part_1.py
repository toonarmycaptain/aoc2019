"""Advent of Code solution December 6th part 1

--- Day 6: Universal Orbit Map ---
You've landed at the Universal Orbit Map facility on Mercury. Because
navigation in space often involves transferring between orbits, the orbit maps
here are useful for finding efficient routes between, for example, you and
Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in
orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes
around AAA (drawn with lines) is only partly shown. In the map data, this
orbital relationship is written AAA)BBB, which means "BBB is in orbit around
AAA".

Before you use your map data to plot a course, you need to make sure it wasn't
corrupted during the download. To verify maps, the Universal Orbit Map facility
uses orbit count checksums - the total number of direct orbits (like the one
shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can
be any number of objects long: if A orbits B, B orbits C, and C orbits D, then
A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the
one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7
orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
"""
from pathlib import Path
from typing import Dict, List


def parse_puzzle_input() -> List[str]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_6th_puzzle_input.txt'), 'r') as input_file:
        return [line for line in input_file.read().splitlines()]  # -1 to strip \n


def make_tree(puzzle_input: List[str]) -> Dict[str, str]:
    orbit_tree = {'COM': ''}
    for object_satellite_pair in puzzle_input:
        parent, satellite = object_satellite_pair.split(')')
        orbit_tree[satellite] = parent
    return orbit_tree


def count_direct_and_indirect(puzzle_input: List[str]):
    """Count objects orbited directly and indirectly by each satellite."""
    orbit_tree = make_tree(puzzle_input)
    total = 0
    for satellite in orbit_tree.values():
        while satellite != '':
            total += 1
            satellite = orbit_tree[satellite]
    return total


"""
PUZZLE_INPUT = parse_puzzle_input()
count_direct_and_indirect(PUZZLE_INPUT) = 234446
"""
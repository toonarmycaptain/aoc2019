"""Advent of Code solution December 6th part 2

--- Part Two ---
Now, you just need to figure out how many orbital transfers you (YOU) need to
take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is
orbiting. An orbital transfer lets you move from any object to an object
orbiting or orbited by that object.

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
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To
move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the
object YOU are orbiting to the object SAN is orbiting? (Between the objects
they are orbiting - not between YOU and SAN.)

Although it hasn't changed, you can still get your puzzle input.
"""
from typing import Dict, List, Tuple

from dec_6th.dec_6th_solution_part_1 import make_tree


def distance_to_objects(orbit_tree: Dict[str, str], satellite_name) -> Dict[str, int]:
    """Get distance from satellite our object orbits to other objects."""
    object_distances: Dict[str, int] = {}
    satellite = orbit_tree[satellite_name]
    distance = 0
    while satellite != 'COM':
        # Get distance
        object_distances[satellite] = distance  # Start with distance to object directly orbited, =0 for out calc.
        distance += 1
        # Next satellite name
        satellite = orbit_tree[satellite]
    return object_distances


def shortest_distance(puzzle_input: List[str], satellite_name_a: str, satellite_name_b: str) -> Tuple[int, str]:
    """Find shortest distance between objects directly orbited by given satellites."""
    orbit_tree = make_tree(puzzle_input)

    distances_satellite_a = distance_to_objects(orbit_tree, satellite_name_a)

    distances_satellite_b = distance_to_objects(orbit_tree, satellite_name_b)

    # & gives the intersection between the sets of keys, leaving only the objects they both orbit directly/indirectly
    objects_in_common = set(distances_satellite_a.keys()) & set(distances_satellite_b.keys())
    distances = [
        # Sum of distance from satellite a, b to each object, object name
        (distances_satellite_a[obj] + distances_satellite_b[obj], obj)
        for obj in objects_in_common
    ]

    min_distance, satellite_name = min(distances)
    return min_distance, satellite_name


"""
from dec_6th.dec_6th_solution_part_1 import parse_puzzle_input
shortest_distance(parse_puzzle_input(), 'YOU', 'SAN)) = 385, 'QCT'
"""

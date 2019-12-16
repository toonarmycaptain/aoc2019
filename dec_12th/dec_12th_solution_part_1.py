"""Advent of Code solution December 12th part 1"""

from functools import reduce
from itertools import permutations
from math import gcd
from pathlib import Path
from typing import Iterable, List, Optional


def parse_puzzle_input() -> List[List[int]]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_12th_puzzle_input.txt'), 'r') as input_file:
        parsed = []
        for line in input_file:
            # Strip newlines
            line = line.replace('\n', '')
            # Strip <>
            line = line[1:-1]
            # Split into coords
            splitline = line.split(',')

            moon_coords: List[int] = []
            for coord in splitline:
                moon_coords.append(int(coord.split('=')[1]))
            parsed.append(moon_coords)
        return parsed


class Moon:
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 z: int = 0,
                 x_velocity: int = 0,
                 y_velocity: int = 0,
                 z_velocity: int = 0,
                 ):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.x_velocity: int = x_velocity
        self.y_velocity: int = y_velocity
        self.z_velocity: int = z_velocity

        self.snapshots: set = set()
        self._save_snapshot()  # Save initial position

    def apply_gravity(self, other_object):
        self.x_velocity += self.gravity_calc(self.x, other_object.x)
        self.y_velocity += self.gravity_calc(self.y, other_object.y)
        self.z_velocity += self.gravity_calc(self.z, other_object.z)

    def step_position(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.z += self.z_velocity

        self._save_snapshot()

    def _save_snapshot(self):
        self.current_state = (self.x, self.y, self.z, self.x_velocity, self.y_velocity, self.z_velocity)
        self.snapshots.add(self.current_state)

    @property
    def pe(self):
        """Moon's potential energy."""
        return sum(map(abs, (self.x, self.y, self.z)))

    @property
    def ke(self):
        """Moon's kinetic energy."""
        return sum(map(abs, (self.x_velocity, self.y_velocity, self.z_velocity)))

    @property
    def total_energy(self):
        return self.pe * self.ke


    @staticmethod
    def gravity_calc(moon_coord, other_moon_coord):
        if moon_coord != other_moon_coord:
            if moon_coord > other_moon_coord:
                return -1
            return 1
        return 0


class JupiterMoonSystem:

    def __init__(self, moons: Iterable[Moon]):
        self.moons = moons
        self.moon_pairs = list(permutations(self.moons, 2))
        self.steps = 0

        self.snapshots: set = set()

        self.x_state_snapshots: set = set()
        self.y_state_snapshots: set = set()
        self.z_state_snapshots: set = set()
        self.x_state_cycle_steps: Optional[int] = None
        self.y_state_cycle_steps: Optional[int] = None
        self.z_state_cycle_steps: Optional[int] = None

        self._save_snapshot()

    @property
    def total_energy(self):
        return sum(moon.total_energy for moon in self.moons)

    def step_positions(self):
        for moon_a, moon_b in self.moon_pairs:
            moon_a.apply_gravity(moon_b)

        for moon in self.moons:
            moon.step_position()
        self.steps += 1

        self._save_snapshot()

    def apply_steps(self, steps: int):
        for step in range(steps):
            self.step_positions()

    def _save_snapshot(self):
        self.snapshots.add(tuple(moon.current_state for moon in self.moons))

        x_state_snapshot = tuple((moon.x, moon.x_velocity) for moon in self.moons)
        y_state_snapshot = tuple((moon.y, moon.y_velocity) for moon in self.moons)
        z_state_snapshot = tuple((moon.z, moon.z_velocity) for moon in self.moons)

        if self.x_state_cycle_steps is None and x_state_snapshot in self.x_state_snapshots:
            self.x_state_cycle_steps = self.steps

        if self.y_state_cycle_steps is None and y_state_snapshot in self.y_state_snapshots:
            self.y_state_cycle_steps = self.steps

        if self.z_state_cycle_steps is None and z_state_snapshot in self.z_state_snapshots:
            self.z_state_cycle_steps = self.steps

        self.x_state_snapshots.add(x_state_snapshot)
        self.y_state_snapshots.add(y_state_snapshot)
        self.z_state_snapshots.add(z_state_snapshot)

    def find_repeat(self):
        """
        Non-brute-force solution (saving system state at each step and looking for repeat)
        taken from https://github.com/davidism/advent/blob/master/src/advent/year2019/day12.py"""

        while not all((self.x_state_cycle_steps, self.y_state_cycle_steps, self.z_state_cycle_steps)):
            self.step_positions()

        return lcm_list([self.x_state_cycle_steps, self.y_state_cycle_steps, self.z_state_cycle_steps])


def lcm_pair(n: int, m: int) -> int:
    return (n * m) // gcd(n, m)


def lcm_list(numbers: List[int]):
    """Return the least common multiple of the given numbers"""
    return reduce(lcm_pair, numbers)


def solve_part_1(data, steps: int=1000):
    system = JupiterMoonSystem([Moon(*args) for args in data])
    for moon in system.moons:
        print(moon.current_state)
    system.apply_steps(steps)
    for moon in system.moons:
        print(moon.current_state)
        print(moon.ke, moon.pe)
        print(moon.total_energy)
    return system.total_energy

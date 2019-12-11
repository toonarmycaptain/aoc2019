"""Advent of Code solution December 11th part 1

--- Day 11: Space Police ---
On the way to Jupiter, you're pulled over by the Space Police.

"Attention, unmarked spacecraft! You are in violation of Space Law! All
spacecraft must have a clearly visible registration identifier! You have 24
hours to comply or be sent to Space Jail!"

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for
help. Although it takes almost three hours for their reply signal to reach you,
they send instructions for how to power up the emergency hull painting robot
and even provide a small Intcode program (your puzzle input) that will cause it
to paint your ship appropriately.

There's just one problem: you don't have an emergency hull painting robot.

You'll need to build a new emergency hull painting robot. The robot needs to be
able to move around on the grid of square panels on the side of your ship,
detect the color of its current panel, and paint its current panel black or
white. (All of the panels are currently black.)

The Intcode program will serve as the brain of the robot. The program uses
input instructions to access the robot's camera: provide 0 if the robot is over
a black panel or 1 if the robot is over a white panel. Then, the program will
output two values:

First, it will output a value indicating the color to paint the panel the robot
is over: 0 means to paint the panel black, and 1 means to paint the panel white.
Second, it will output a value indicating the direction the robot should turn:
0 means it should turn left 90 degrees, and 1 means it should turn right 90
degrees.
After the robot turns, it should always move forward exactly one panel. The
robot starts facing up.

The robot will continue running for a while like this and halt when it is
finished drawing. Do not restart the Intcode computer inside the robot during
this process.

For example, suppose the robot is about to start running. Drawing black panels
as ., white panels as #, and the robot pointing the direction it is facing
(< ^ > v), the initial state and region near the robot looks like this:

.....
.....
..^..
.....
.....
The panel under the robot (not visible here because a ^ is shown instead) is
also black, and so any input instructions at this point should be provided 0.
Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left).
After taking these actions and moving forward one panel, the region now looks
like this:

.....
.....
.<#..
.....
.....
Input instructions should still be provided 0. Next, the robot might output 0
(paint black) and then 0 (turn left):

.....
.....
..#..
.v...
.....
After more outputs (1,0, 1,0):

.....
.....
..^..
.##..
.....
The robot is now back where it started, but because it is now on a white panel,
input instructions should be provided 1. After several more outputs
(0,1, 1,0, 1,0), the area looks like this:

.....
..<#.
...#.
.##..
.....
Before you deploy the robot, you should probably have an estimate of the area
it will cover: specifically, you need to know the number of panels it paints at
least once, regardless of color. In the example above, the robot painted 6
panels at least once. (It painted its starting panel twice, but that panel is
still only counted once; it also never painted the panel it ended on.)

Build a new emergency hull painting robot and run the Intcode program on it.
How many panels does it paint at least once?

Your puzzle answer was 2343.
"""

from pathlib import Path
from typing import List

from collections import defaultdict, deque

from int_computer import IntComputer


def parse_puzzle_input() -> List[int]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_11th_puzzle_input.txt'), 'r') as input_file:
        return [int(code) for code in input_file.readline().split(',')]


class HullPainterRobot:
    def __init__(self,
                 data: List[int],
                 *,
                 init_position: tuple = (0, 0),
                 initial_direction: int = 1,  # Pointing upwards
                 initial_panel_colour: int = 0,  # starts on black
                 ):
        self.hull_panels: dict = defaultdict(lambda: 0)
        assert isinstance(init_position, tuple)
        self.position: complex = complex(*init_position)

        self.initial_panel_colour: int = initial_panel_colour
        self.computer = IntComputer(data, pause_on_output=True)

        self.direction = deque([0,  # Right
                                1,  # Upwards
                                2,  # Left
                                3,  # Down
                                ], 4)
        if initial_direction != self.direction[0]:  # Default 1, facing upwards.
            while self.direction[0] != initial_direction:
                self.direction.rotate(1)

        self.movement: dict = {0: + 1,  # move right, increase x by 1
                               1: + 1j,  # move up, increase y by 1
                               2: - 1,  # move left, decrease x by 1
                               3: - 1j,  # move down, decrease y by 1
                               }

    def paint_panels(self):
        self.computer.inputs.append(self.initial_panel_colour)
        while not self.computer.run_program():
            self.computer.run_program()  # run twice to get two outputs

            # Paint panel
            self.hull_panels[self.position], turn_right = self.computer.outputs[-2:]

            # Change_direction
            if turn_right:
                self.direction.rotate(1)
            else:  # Turn left
                self.direction.rotate(-1)
            # Move robot
            self.position += self.movement[self.direction[0]]

            # Add input which is current position.
            self.computer.inputs.append(self.hull_panels[self.position])


def solve_part_1():
    t = HullPainterRobot(parse_puzzle_input())
    t.paint_panels()

    return len(t.hull_panels)


"""
print(solve_part_1()) = 2343
"""

"""Advent of Code solution December 13th part 2

--- Part Two ---
The game didn't run because you didn't put in any quarters. Unfortunately, you
did not bring any quarters. Memory address 0 represents the number of quarters
that have been inserted; set it to 2 to play for free.

The arcade cabinet has a joystick that can move left and right. The software
reads the position of the joystick with input instructions:

If the joystick is in the neutral position, provide 0.
If the joystick is tilted to the left, provide -1.
If the joystick is tilted to the right, provide 1.
The arcade cabinet also has a segment display capable of showing a single
number that represents the player's current score. When three output
instructions specify X=-1, Y=0, the third output instruction is not a tile; the
value instead specifies the new score to show in the segment display. For
example, a sequence of output values like -1,0,12345 would show 12345 as the
player's current score.

Beat the game by breaking all the blocks. What is your score after the last
block is broken?
"""
from typing import List

from dec_13th.dec_13th_solution_part_1 import parse_puzzle_input
from int_computer import IntComputer as ArcadeComputer


class ArcadeMachine:
    def __init__(self, intcode_program: List[int]):
        self.computer = ArcadeComputer(intcode_program, pause_on_output=True)

        # Replace processor input generator with one that supplies needed joystick direction.
        self.computer.next_input = self.move_joystick()

        self.number_of_blocks = 0

        self.score = 0
        self.paddle_x_coordinate = 0
        self.ball_y_coordinate = 0
        self.ball_x_coordinate = 0
        self.steps = 0
        self.moves = 0

    def step_game(self):
        self.steps += 1
        # Take 3 outputs
        end = False
        for step in range(3):
            # print(f'Debug step:\n'
            #       f'{self.score=},{self.steps=},\n'
            #       f'{self.number_of_blocks}\n'
            #       f'{self.paddle_x_coordinate=}, {self.ball_x_coordinate=}, {self.ball_y_coordinate=}, \n'
            #       f'{self.computer.pointer_index=},'
            #       f'next intcode{self.computer._intcode_program[self.computer.pointer_index]=}\n\n\n')
            end = self.computer.run_program()

        x, y, value = self.computer.outputs[-3:]

        # parse screen output
        if value == 0:
            pass
        elif value == 2:
            self.number_of_blocks += 1
        elif value == 3:
            self.paddle_x_coordinate = x
        elif value == 4:
            self.ball_x_coordinate, self.ball_y_coordinate = x, y
        elif (x, y) == (-1, 0):
            self.score = value

        if end:
            return True
        return False

    def move_joystick(self):
        self.moves += 1

        while True:
            joystick_instruction = 0  # default
            diff = self.ball_x_coordinate - self.paddle_x_coordinate
            if diff:
                joystick_instruction = int(diff / (abs(diff)))

            yield joystick_instruction
            # print(f'{self.ball_x_coordinate=},{self.paddle_x_coordinate=}, {diff=}, {joystick_instruction=}')
            # print(f'moved joystick {joystick_instruction}\n')

    def play(self):
        while True:
            if self.step_game():
                return self.score


def solve_part_2(data):
    a = ArcadeMachine(data)
    # Memory 0 change to 2
    a.computer._intcode_program[0] = 2
    return a.play()

"""
solve_part_2(parse_puzzle_input()) = 14204
"""
print(solve_part_2(parse_puzzle_input()))
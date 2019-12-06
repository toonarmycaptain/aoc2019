"""Advent of Code solution December 5th part 1

--- Day 5: Sunny with a Chance of Asteroids ---
You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air conditioner
working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.

The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). The TEST
diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the
instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address
50.
Programs that use these instructions will come with documentation that explains what should be connected to the input
and output. The program 3,0,4,0,99 outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already
understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the
parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in position
mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a parameter is
interpreted as a value - if the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based only on
the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an
instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first
parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's
mode is in the ten-thousands digit, and so on. Any missing modes are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first value, 02, indicate
opcode 2, multiplication. Then, going right to left, the parameter modes are 0 (hundreds digit), 1 (thousands digit),
and 0 (ten-thousands digit, not present and therefore zero):

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
This instruction multiplies its first two parameters. The first parameter, 4 in position mode, works like it did before
- its value is the value stored at address 4 (33). The second parameter, 3 in immediate mode, simply has value 3. The
result of this operation, 33 * 3 = 99, is written according to the third parameter, 4 in position mode, which also works
like it did before - 99 is written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the number of values in the instruction
after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input
instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter
modes, function correctly. For each test, it will run an output instruction indicating how far the result of the test
was from the expected value, where 0 means the test was successful. Non-zero outputs mean that a function is not working
correctly; check the instructions that were run before the output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output
followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code, the
diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program
produce?


--- Part Two ---
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?



******
Used the bare bones of the Computer class from Day 2, but slight changes to operation (eg the
ability to jump instructions as well as running sequentially.
NB I could have subclassed this for the second part, but I did not.
Also, a function that takes an opcode, and a parameter, returning the positional or immediate value
would have been useful. A refactor for another time. NB It would need the full padding by default.
"""
from pathlib import Path
from typing import List


def parse_puzzle_input() -> List[int]:
    problem_folder = Path(__file__).parent
    with open(Path(problem_folder, 'dec_5th_puzzle_input.txt'), 'r') as input_file:
        return [int(code) for code in input_file.readline().split(',')]


class TESTComputer:
    """Thermal Environment Supervision Terminal (TEST) computer."""

    def __init__(self, intcode_program: List[int], inputs: List[int] = None):
        self._intcode_program: List[int] = intcode_program
        if inputs:
            self.inputs = (input_item for input_item in inputs)
        self.outputs: List = []

        self.opcode_switch = {1: self.addiction_opcode,
                              2: self.multiplication_opcode,
                              3: self.input_opcode,
                              4: self.output_opcode,
                              5: self.jump_if_true,
                              6: self.jump_if_false,
                              7: self.less_than,
                              8: self.equals,
                              99: self.halt_opcode,
                              }

    def run_program(self):
        """
        Modification to original day 2 program to use return value from operation
        to move pointer, as some instructions are not 4 ints long.
        :return:
        """
        try:
            pointer_index = 0
            while True:
                opcode = int(str(self._intcode_program[pointer_index])[-2:])
                pointer_index = self.opcode_switch[opcode](pointer_index)

        except (StopIteration, IndexError) as e:
            return self._intcode_program

    def addiction_opcode(self, position: int):

        """Addition opcode."""
        padded_intcode = f'{self._intcode_program[position]:05}'
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]
        arg_a = self._intcode_program[source_a]

        if int(padded_intcode[-4]):
            source_b = position + 2
        else:
            source_b = self._intcode_program[position + 2]
        arg_b = self._intcode_program[source_b]

        target = self._intcode_program[position + 3]
        self._intcode_program[target] = arg_a + arg_b
        return position + 4

    def multiplication_opcode(self, position: int):
        """Multiplication opcode."""
        padded_intcode = f'{self._intcode_program[position]:05}'
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]
        arg_a = self._intcode_program[source_a]

        if int(padded_intcode[-4]):
            source_b = position + 2
        else:
            source_b = self._intcode_program[position + 2]
        arg_b = self._intcode_program[source_b]

        target = self._intcode_program[position + 3]
        self._intcode_program[target] = arg_a * arg_b
        return position + 4

    def input_opcode(self, position: int):
        target = self._intcode_program[position + 1]
        self._intcode_program[target] = next(self.inputs)
        return position + 2

    def output_opcode(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:03}'
        if int(padded_intcode[-3]):
            source = position + 1
        else:
            source = self._intcode_program[position + 1]

        self.outputs.append(self._intcode_program[source])
        return position + 2

    def jump_if_true(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:04}'
        # Get value of first param:
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]

        if self._intcode_program[source_a]:
            # Get value of second param:
            if int(padded_intcode[-4]):  # if arg 2 in immediate mode
                source_b = position + 2
            else:
                source_b = self._intcode_program[position + 2]
            return self._intcode_program[source_b]
        # else:
        return position + 3

    def jump_if_false(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:04}'
        # Get value of first param:
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]

        if not self._intcode_program[source_a]:
            # Get value of second param:
            if int(padded_intcode[-4]):  # if arg 2 in immediate mode
                source_b = position + 2
            else:
                source_b = self._intcode_program[position + 2]
            return self._intcode_program[source_b]
        # else:
        return position + 3

    def less_than(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:05}'
        # Get value of first param:
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]
        arg_a = self._intcode_program[source_a]
        # Get value of second param:
        if int(padded_intcode[-4]):
            source_b = position + 2
        else:
            source_b = self._intcode_program[position + 2]
        arg_b = self._intcode_program[source_b]

        target = self._intcode_program[position + 3]
        if arg_a < arg_b:
            # Assume third arg which will be assigned to is not immediate mode.
            self._intcode_program[target] = 1
        else:
            self._intcode_program[target] = 0
        return position + 4

    def equals(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:05}'
        # Get value of first param:
        if int(padded_intcode[-3]):
            source_a = position + 1
        else:
            source_a = self._intcode_program[position + 1]
        arg_a = self._intcode_program[source_a]
        # Get value of second param:
        if int(padded_intcode[-4]):
            source_b = position + 2
        else:
            source_b = self._intcode_program[position + 2]
        arg_b = self._intcode_program[source_b]

        target = self._intcode_program[position + 3]
        if arg_a == arg_b:
            # Assume third arg which will be assigned to is not immediate mode.
            self._intcode_program[target] = 1
        else:
            self._intcode_program[target] = 0
        return position + 4

    def halt_opcode(self, position: int):
        """Terminate program opcode"""
        raise StopIteration


"""
PUZZLE_INPUT = parse_puzzle_input()

Part 1:
c = TESTComputer(PUZZLE_INPUT, [1])
c.run_program() 
c.outputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 15386262]
= 15386262

Part 2

PUZZLE_INPUT = parse_puzzle_input()
c = TESTComputer(PUZZLE_INPUT, [5,])
c.run_program()
c.outputs = [10376124]
=10376124
"""
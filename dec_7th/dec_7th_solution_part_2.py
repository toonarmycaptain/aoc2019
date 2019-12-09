"""Advent of Code solution December 7th part 2"""

import itertools

from typing import List, Optional, Sequence

from dec_7th.dec_7th_solution_part_1 import parse_puzzle_input


class AmpComputer:
    """Thermal Environment Supervision Terminal (TEST) computer."""

    def __init__(self, intcode_program: List[int], inputs: List[int] = None, pointer_index: int = 0):
        """
        Modification to Day 5 computer to:
        * allow adding new inputs, via a generator operating on self.inputs
            Use AmpComp.inputs.append(new_input) to add next input
        * stop execution after output, resume at pointer on pointer on next
        .run() by making pointer a class attribute rather than var in function.
        * have run_program stop by adding an if opcode == output opcode raise StopIteration at end of while loop
        * Have StopIteration return True to indicate a completed program, instead of returning the ran
         (and altered) intcode program, as this functionality wasn't used except for debugging.


        :param intcode_program:
        :param inputs:
        """
        self._intcode_program: List[int] = intcode_program
        self.pointer_index = pointer_index
        if inputs:
            self.inputs = inputs
        else:
            self.inputs = []
        self.outputs: List = []

        self.next_input = self.input_generator()

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

    def input_generator(self):
        for i in self.inputs:
            yield i

    def run_program(self) -> Optional[bool]:
        """
        Modification to original day 5 to have

        NB use AmpComputer.inputs.send() to add
        :return:
        """
        try:

            while True:
                opcode = int(str(self._intcode_program[self.pointer_index])[-2:])
                self.pointer_index = self.opcode_switch[opcode](self.pointer_index)
                if opcode == 4:
                    break
        except StopIteration:
            return True
        return False

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
        print(f'{self.inputs=}')
        self._intcode_program[target] = next(self.next_input)
        print(f'{self._intcode_program[target]=}')
        return position + 2

    def output_opcode(self, position: int):
        padded_intcode = f'{self._intcode_program[position]:03}'
        if int(padded_intcode[-3]):
            source = position + 1
        else:
            source = self._intcode_program[position + 1]

        self.outputs.append(self._intcode_program[source])
        print(f'output={self._intcode_program[source]=}')
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


def feedback_computer(intcode_program: List[int], phase_sequence: Sequence[int]):
    if len(phase_sequence) != 5:
        raise ValueError
    # Setup AmpComputers
    amp_computers: List[AmpComputer] = []
    for phase in phase_sequence:
        amp_computers.append(AmpComputer(intcode_program=intcode_program[:],
                                         inputs=[phase]))

    next_input = 0  # Initial input given to first AmpComputer A
    try:
        while True:
            for amp_computer in amp_computers:
                amp_computer.inputs.append(next_input)
                if amp_computer.run_program():
                    raise StopIteration  # if run_program returns True instead of None, program has ended.
                next_input = amp_computer.outputs[-1]
    except StopIteration:
        return amp_computers[-1].outputs[-1]


def solve_part_2(intcode_program):
    sequences = []
    for sequence in itertools.permutations(list(range(5, 10))):
        output = feedback_computer(intcode_program=intcode_program,
                                   phase_sequence=sequence)
        sequences.append(output)
    return max(sequences)


"""
solve_part_2(parse_puzzle_input())) = 3745599
"""

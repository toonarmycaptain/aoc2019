from typing import List, Dict, Optional


class IntComputer:
    """Basic Operation Of System Test (BOOST) computer."""

    def __init__(self, intcode_program: List[int],
                 inputs: List[int] = None,
                 *,
                 pause_on_output: bool = False,
                 pointer_index: int = 0,
                 relative_base: int = 0,
                 ):
        """
        Modification to Day 5 computer to:
        * allow adding new inputs, via a generator operating on self.inputs
            Use AmpComp.inputs.append(new_input) to add next input
        * stop execution after output, resume at pointer on pointer on next
            .run() by making pointer a class attribute rather than var in
            function.
        * have run_program stop by adding an if opcode == output opcode raise
            StopIteration at end of while loop
        * Have StopIteration return True to indicate a completed program,
            instead of returning the ran
            (and altered) intcode program, as this functionality wasn't used
            except for debugging.
        * Add kwonly pointer_index and pause_on_output params, run_program
            checks pause_on_output flag if output is called.
        * Abstract parsing modes to find position of arg into function
            mode_based_arg_position
        * Add relative_base instance var, relative_base parameter support.
        * Add relative_base kwonly arg to provide initial value for self.relative_base



        :param intcode_program:
        :param inputs:
        """
        self._intcode_program: Dict[int, int] = {position: value for position, value in enumerate(intcode_program)}
        self.pointer_index = pointer_index
        self.relative_base = relative_base
        self.pause_on_output = pause_on_output

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
                              9: self.adjust_relative_base,
                              99: self.halt_opcode,
                              }

    def input_generator(self):
        for i in self.inputs:
            yield i

    def run_program(self) -> Optional[bool]:

        try:
            # cycles = 0
            # opcode_calls = {1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0, 99: 0}
            while True:
                opcode = int(str(self._intcode_program[self.pointer_index])[-2:])
                # cycles +=1
                # opcode_calls[opcode] += 1
                self.pointer_index = self.opcode_switch[opcode](self.pointer_index)
                if opcode == 4 and self.pause_on_output:
                    break

        except StopIteration:
            # print(f'{cycles=}, {opcode_calls=}')
            return True
        return False

    def mode_based_arg_position(self, position: int, parameter_position: int):
        """returns index of source for parameter value"""
        # eg *any modes* param 1 param 2 param 3
        # eg   0  1  0     13      64      79
        # parameter will == 1 or 2
        padded_intcode = f'{self._intcode_program[position]:05}'
        mode = int(padded_intcode[-2 - parameter_position])
        if mode == 1:
            # immediate mode, parameter refers to value at parameter position
            return position + parameter_position
        if mode == 2:
            # return relative_base + value at position of parameter
            return self.relative_base + self.get_value_at_position(position + parameter_position)
        else:  # regular mode = 0, parameter refers to position in program
            return self.get_value_at_position(position + parameter_position)

    def get_value_at_position(self, position: int):
        """
        Checks if position in intcode program exists, creating indexes in
        _intcode_program initialised with value 0 if it does not.
        """
        # if position > len(self._intcode_program):
        #     self._intcode_program += [0 for _ in
        #                               range(max(self._intcode_program) - len(self._intcode_program))]
        if not self._intcode_program.get(position, None):
            self._intcode_program[position] = 0
        return self._intcode_program[position]

    def addiction_opcode(self, position: int):

        """Addition opcode."""
        source_a = self.mode_based_arg_position(position, 1)
        arg_a = self.get_value_at_position(source_a)

        source_b = self.mode_based_arg_position(position, 2)
        arg_b = self.get_value_at_position(source_b)

        source_c = self.mode_based_arg_position(position, 3)
        target = source_c
        # Ensure target exists:
        self.get_value_at_position(target)

        self._intcode_program[target] = arg_a + arg_b
        return position + 4

    def multiplication_opcode(self, position: int):
        """Multiplication opcode."""
        source_a = self.mode_based_arg_position(position, 1)
        arg_a = self.get_value_at_position(source_a)

        source_b = self.mode_based_arg_position(position, 2)
        arg_b = self.get_value_at_position(source_b)

        source_c = self.mode_based_arg_position(position, 3)
        target = source_c
        # Ensure target exists:
        self.get_value_at_position(target)

        self._intcode_program[target] = arg_a * arg_b
        return position + 4

    def input_opcode(self, position: int):
        target = self.mode_based_arg_position(position, 1)

        # Ensure target exists:
        self.get_value_at_position(target)

        self._intcode_program[target] = next(self.next_input)

        return position + 2

    def output_opcode(self, position: int):
        source = self.mode_based_arg_position(position, 1)

        self.outputs.append(self.get_value_at_position(source))
        return position + 2

    def jump_if_true(self, position: int):
        # Get value of first param:
        source_a = self.mode_based_arg_position(position, 1)

        if self.get_value_at_position(source_a):
            # Get value of second param:
            source_b = self.mode_based_arg_position(position, 2)
            return self.get_value_at_position(source_b)
        # else:
        return position + 3

    def jump_if_false(self, position: int):
        # Get value of first param:
        source_a = self.mode_based_arg_position(position, 1)

        if not self.get_value_at_position(source_a):
            # Get value of second param:
            source_b = self.mode_based_arg_position(position, 2)
            return self.get_value_at_position(source_b)
        # else:
        return position + 3

    def less_than(self, position: int):
        source_a = self.mode_based_arg_position(position, 1)
        arg_a = self.get_value_at_position(source_a)

        source_b = self.mode_based_arg_position(position, 2)
        arg_b = self.get_value_at_position(source_b)

        source_c = self.mode_based_arg_position(position, 3)
        target = source_c
        # Ensure target exists:
        self.get_value_at_position(target)

        if arg_a < arg_b:
            # Assume third arg which will be assigned to is not immediate mode.
            self._intcode_program[target] = 1
        else:
            self._intcode_program[target] = 0
        return position + 4

    def equals(self, position: int):
        # Get value of first param:
        source_a = self.mode_based_arg_position(position, 1)
        arg_a = self.get_value_at_position(source_a)
        # Get value of second param:
        source_b = self.mode_based_arg_position(position, 2)
        arg_b = self.get_value_at_position(source_b)

        source_c = self.mode_based_arg_position(position, 3)
        target = source_c
        # Ensure target exists:
        self.get_value_at_position(target)

        if arg_a == arg_b:
            # Assume third arg which will be assigned to is not immediate mode.
            self._intcode_program[target] = 1
        else:
            self._intcode_program[target] = 0
        return position + 4

    def adjust_relative_base(self, position: int):
        source_a = self.mode_based_arg_position(position, 1)

        self.relative_base += self.get_value_at_position(source_a)
        return position + 2

    def halt_opcode(self, position: int):
        """Terminate program opcode"""
        raise StopIteration

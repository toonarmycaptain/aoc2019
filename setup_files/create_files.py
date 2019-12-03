from pathlib import Path


def make_files():
    days_in_december = 25
    for day in range(1, days_in_december + 1):
        create_day_files(day)


def create_day_files(day: int):
    # Create folder
    day_path = Path(f'dec_{day}{ordinal(day)}')
    day_path.mkdir(exist_ok=True)

    try:
        with open(Path(day_path, '__init__.py'), 'x') as init:
            init.write('')
    except FileExistsError:
        pass
    # Part 1
    try:
        with open(Path(day_path, f'dec_{day}{ordinal(day)}_solution_part_1.py'), 'x') as solution:
            solution.write(f'"""Advent of Code solution December {day}{ordinal(day)} part 1"""')
    except FileExistsError:
        pass

    try:
        with open(Path(day_path, f'test_dec_{day}{ordinal(day)}_solution_part_1.py'), 'x') as test_file:
            test_file.write(f'"""Tests for Advent of Code solution December {day}{ordinal(day)} part 1"""')
    except FileExistsError:
        pass

        # Part 2
        try:
            with open(Path(day_path, f'dec_{day}{ordinal(day)}_solution_part_2.py'), 'x') as solution:
                solution.write(f'"""Advent of Code solution December {day}{ordinal(day)} part 2"""')
        except FileExistsError:
            pass

        try:
            with open(Path(day_path, f'test_dec_{day}{ordinal(day)}_solution_part_2.py'), 'x') as test_file:
                test_file.write(f'"""Tests for Advent of Code solution December {day}{ordinal(day)} part 2"""')
        except FileExistsError:
            pass

def ordinal(num):
    """
    Take number and return the ordinal st, nd, th.
    :num: int
    :return: str
    """
    num_str = str(num)

    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    # Check for 11-14 because those are abnormal
    if int(num_str[-2:]) > 10 and int(num_str[-2:]) < 14:
        return 'th'
    else:
        suffix = SUFFIXES.get(int(num_str[-1:]), 'th')
    return suffix

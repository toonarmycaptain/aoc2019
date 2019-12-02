from pathlib import Path

def make_files():
    days_in_december = 31
    for day in range(1, days_in_december +1):
        # Create folder
        day_path = Path(f'dec_{day}{ordinal(day)}')
        day_path.mkdir(exist_ok=True)

        with open(Path(day_path, '__init__.py'), 'w+') as init:
            init.write('')

        with open(Path(day_path, f'dec_{day}{ordinal(day)}.py'), 'w+') as solution:
            solution.write(f'"""Advent of Code solution December {day}{ordinal(day)}"""')

        with open(Path(day_path, f'test_dec_{day}{ordinal(day)}.py'), 'w+') as test_file:
            test_file.write(f'"""Tests for Advent of Code solution December {day}{ordinal(day)}"""')


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

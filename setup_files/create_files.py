from pathlib import Path


def make_files():
    days_in_december = 25
    for day in range(1, days_in_december + 1):
        create_day_files(day)


def create_day_files(day: int):
    # Create folder
    day_path = Path(f'dec_{day}{ordinal(day)}')
    day_path.mkdir(exist_ok=True)

    init_filepath = Path(day_path, '__init__.py')
    create_file(filepath=init_filepath)

    for part_numeral in (1, 2):
        solution_filepath = Path(day_path, f'dec_{day}{ordinal(day)}_solution_part_{part_numeral}.py')
        solution_content = f'"""Advent of Code solution December {day}{ordinal(day)} part {part_numeral}"""'
        create_file(filepath=solution_filepath,
                    content=solution_content)

        test_filepath = Path(day_path, f'test_dec_{day}{ordinal(day)}_solution_part_{part_numeral}.py')
        test_file_content = f'"""Tests for Advent of Code solution December {day}{ordinal(day)} part {part_numeral}"""'
        create_file(filepath=test_filepath,
                    content=test_file_content)

    # Blank puzzle input.
    puzzle_input_filepath = Path(day_path, f'dec_{day}{ordinal(day)}_puzzle_input.txt')
    create_file(puzzle_input_filepath)


def create_file(filepath: Path, content=None, error_msg: str = None):
    try:
        with open(filepath, 'x') as file:
            if content:
                file.write(content)
        print(f'Created {filepath.name}')
    except FileExistsError:
        if error:
            print(error_msg)
        else:
            print(f'Did not create {filepath.name}, as it already exists.')


def ordinal(num):
    """
    Take number and return the ordinal st, nd, th.
    :num: int
    :return: str
    """
    num_str = str(num)

    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    # Check for 11-14 because those are abnormal
    if 10 < int(num_str[-2:]) < 14:
        return 'th'
    else:
        suffix = SUFFIXES.get(int(num_str[-1:]), 'th')
    return suffix

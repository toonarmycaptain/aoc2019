"""Advent of Code solution December 14th part 2

--- Part Two ---
After collecting ORE for a while, you check your cargo hold: 1 trillion
(1000000000000) units of ORE.

With that much ore, given the examples above:

The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
The 2210736 ORE-per-FUEL example could produce 460664 FUEL.
Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?
"""

from dec_14th.dec_14th_solution_part_1 import find_ore_needed_for_fuel, parse_puzzle_input


def fuel_quantity_from_ore(equations, ore_quantity=1000000000000):
    # Minimum fuel produced will be simply ore quantity divided by ore for 1 unit
    max_ore_per_unit = find_ore_needed_for_fuel(equations, 1)
    fuel_prediction_min = 1  # ore_quantity // max_ore_per_unit didn't work - gave off-by-one results
    fuel_prediction_max = ore_quantity

    fuel_prediction = ore_quantity // 2  # (fuel_prediction_min + fuel_prediction_max) // 2 didn't work - gave off-by-one results

    while fuel_prediction_max != fuel_prediction:
        ore_used = find_ore_needed_for_fuel(equations, fuel_prediction)
        if ore_used > ore_quantity:
            fuel_prediction_max = fuel_prediction - 1
        elif ore_used < ore_quantity:
            fuel_prediction_min = fuel_prediction + 1
        elif ore_used == ore_quantity:
            return fuel_prediction

        fuel_prediction = (fuel_prediction_min + fuel_prediction_max) // 2

    return fuel_prediction


"""
fuel_quantity_from_ore(parse_puzzle_input()) = 3209255 ~ 3209254 was correct.
Ironically, my method which gave off-by-one on the tests gives the right answer.
"""

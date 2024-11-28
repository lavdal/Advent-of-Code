# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:15:37 2023

@author: EBL
"""
from utils import open_input
import re


def puzzle1(data):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum_of_ids = 0

    for line in data:
        print("#" * 20)
        print(line)
        game_number = re.search(r"Game\s+(\d+)", line).group(1)
        print(game_number)

        num_of_reds = re.findall(r"(\d+)\s(?=red)", line)
        highest_red = max([int(x) for x in num_of_reds])

        num_of_greens = re.findall(r"(\d+)\s(?=green)", line)
        highest_green = max([int(x) for x in num_of_greens])

        num_of_blues = re.findall(r"(\d+)\s(?=blue)", line)
        highest_blue = max([int(x) for x in num_of_blues])

        if (
            highest_red <= max_cubes["red"]
            and highest_green <= max_cubes["green"]
            and highest_blue <= max_cubes["blue"]
        ):
            sum_of_ids += int(game_number)

    return sum_of_ids


def puzzle2(data):
    sum_of_power = 0

    for line in data:
        num_of_reds = re.findall(r"(\d+)\s(?=red)", line)
        highest_red = max([int(x) for x in num_of_reds])

        num_of_greens = re.findall(r"(\d+)\s(?=green)", line)
        highest_green = max([int(x) for x in num_of_greens])

        num_of_blues = re.findall(r"(\d+)\s(?=blue)", line)
        highest_blue = max([int(x) for x in num_of_blues])

        sum_of_power += highest_red * highest_green * highest_blue

    return sum_of_power


if __name__ == "__main__":
    data = open_input("day2-input")
    print(puzzle2(data))

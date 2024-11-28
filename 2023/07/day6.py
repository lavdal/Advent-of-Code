# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:48:06 2023

@author: EBL
"""
from utils import open_input
import re
import numpy as np


class Puzzle1:
    def get_races(self):
        tider = [int(x) for x in re.findall(r"\d+", self.data[0])]
        længde = [int(x) for x in re.findall(r"\d+", self.data[1])]
        løbene = zip(tider, længde)
        return løbene

    def calc_times(self):
        løbene = self.get_races()
        wins_per_race = []
        for tid, længde in løbene:
            wins = 0
            for i in range(tid):
                rest = tid - i
                distance = i * rest
                if distance > længde:
                    wins += 1
            wins_per_race.append(wins)
        return wins_per_race

    def get_product_of_wins(self):
        return np.prod(self.calc_times())

    def __init__(self, filnavn):
        self.data = open_input(filnavn)


class Puzzle2:
    def get_races(self):
        tid = re.findall(r"\d+", self.data[0])
        tid = int("".join(tid))
        print(f"{tid=}")
        længde = re.findall(r"\d+", self.data[1])
        længde = int("".join(længde))
        print(f"{længde=}")
        # tider = [int(x) for x in re.findall(r"\d+", self.data[0])]
        # længde = [int(x) for x in re.findall(r"\d+", self.data[1])]
        løbet = [(tid, længde)]
        return løbet

    def calc_times(self):
        løbene = self.get_races()
        wins_per_race = []
        for tid, længde in løbene:
            wins = 0
            for i in range(tid):
                rest = tid - i
                distance = i * rest
                if distance > længde:
                    wins += 1
            wins_per_race.append(wins)
        return wins_per_race

    def get_product_of_wins(self):
        return np.prod(self.calc_times())

    def __init__(self, filnavn):
        self.data = open_input(filnavn)


if __name__ == "__main__":
    opgave1 = Puzzle1("day6-input")
    print(opgave1.get_product_of_wins())

    print("#" * 30)

    opgave2 = Puzzle2("day6-input")
    print(opgave2.get_product_of_wins())

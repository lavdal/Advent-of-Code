# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:14:04 2023

@author: EBL
"""
from utils import open_input
import re


class Puzzle1:
    def get_symbols(self):
        all_chars = set()
        for line in self.data:
            for char in line.rstrip():
                all_chars.add(char)
        for tal in range(10):
            all_chars.remove(str(tal))

        all_chars.remove(".")

        self.symbols = all_chars

    def search_for_chars(self, idx, start, stop):
        chars_around = set()
        for line in range(idx - 1, idx + 2):
            try:
                for loc in range(start - 1, stop + 1):
                    for char in self.data[line][loc]:
                        chars_around.add(char)
            except IndexError:
                pass

            # print(chars_around)
        return any(x in self.symbols for x in chars_around)

    def determine_numbers(self):
        sum_of_parts = 0
        for idx, line in enumerate(self.data):
            print()
            print("#" * 20)
            print(f"###   {idx}   ###")
            results = re.finditer(r"\d+", line)
            for result in results:
                start, stop = result.span()
                if self.search_for_chars(idx, start, stop):
                    sum_of_parts += int(result.group(0))
        return sum_of_parts

    def __init__(self, data_in):
        self.data = data_in
        self.get_symbols()
        print(self.determine_numbers())


class Puzzle2:
    def get_symbols(self):
        all_chars = set()
        for line in self.data:
            for char in line.rstrip():
                all_chars.add(char)
        for tal in range(10):
            all_chars.remove(str(tal))

        all_chars.remove(".")

        self.symbols = set("*")

    def search_for_chars(self, idx, start, stop):
        chars_around = set()
        for line in range(idx - 1, idx + 2):
            try:
                for loc in range(start - 1, stop + 1):
                    for char in self.data[line][loc]:
                        if char in self.symbols:
                            return (line, loc)
            except IndexError:
                pass
        return None

    def add_to_cog_list(self, cog_location, number):
        if cog_location in self.cog_list:
            self.cog_list[cog_location].append(number)
        else:
            self.cog_list[cog_location] = [number]
        return True

    def determine_numbers(self):
        sum_of_parts = 0
        for idx, line in enumerate(self.data):
            print()
            print("#" * 20)
            print(f"###   {idx}   ###")
            results = re.finditer(r"\d+", line)
            for result in results:
                start, stop = result.span()
                loc = self.search_for_chars(idx, start, stop)
                if loc != None:
                    self.add_to_cog_list(loc, result.group(0))
        for value in self.cog_list.values():
            if len(value) > 1:
                temp = [int(x) for x in value]
                sum_of_parts += temp[0] * temp[1]
        return sum_of_parts

    def __init__(self, data_in):
        self.data = data_in
        self.get_symbols()
        self.cog_list = {}
        print(self.determine_numbers())


if __name__ == "__main__":
    data = open_input("day3-input")
    puzzle2 = Puzzle2(data)

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:49:19 2023

@author: EBL
"""
from utils import open_input
import pandas as pd
import re


class Puzzle1:
    def get_headings(self):
        headings = []
        for line in self.data:
            heading = re.search(r"(.*)-to-(.*) map", line)
            if heading:
                headings.append(f"{heading.group(1)}-to-{heading.group(2)}")
        return headings

    def determine_higest_number(self):
        used_numbers = []
        for line in data:
            numbers = re.findall(r"\d+", line)
            for number in numbers:
                used_numbers.append(int(number))
        return max(used_numbers)

    def read_mappings(self):
        conversion_dict = {heading: [] for heading in self.get_headings()}
        for line in self.data[2:]:
            category = re.search(r"(.*-to-.*) map", line)
            if category:
                current_cat = category.group(1)
            else:
                try:
                    stuff = [int(x) for x in line.rstrip().split(" ")]
                    print(f"{current_cat} : {stuff}")
                    for i in range(stuff[2]):
                        conversion_dict[current_cat].append(
                            (stuff[0] + i, stuff[1] + i)
                        )
                except ValueError:
                    pass
        print(conversion_dict)

    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    data = open_input("day5-input")
    puzzle1 = Puzzle1(data)
    puzzle1.read_mappings()

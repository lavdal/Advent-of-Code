# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:03:55 2023

@author: EBL
"""
from utils import open_input
import regex as re


def puzzle1():
    data = open_input("day1-input")
    calibration_values = []
    for line in data:
        digits = re.findall(r"\d", line)
        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)
    return sum(calibration_values)


def puzzle2():
    data = open_input("day1-input")
    calibration_values = []
    replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    words = "|".join([f"{k}|{v}" for k, v in replacements.items()])
    for line in data:
        line = "".join(re.findall(words, line, overlapped=True))
        for word, number in replacements.items():
            line = re.sub(word, number, line)
        calibration_value = int(line[0] + line[-1])
        calibration_values.append(calibration_value)
    return sum(calibration_values)


print(f"{puzzle1()=}")
print(f"{puzzle2()=}")

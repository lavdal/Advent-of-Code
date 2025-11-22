# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:26:48 2023

@author: EBL
"""
from utils import open_input
from dataclasses import dataclass
import re


def puzzle1():
    data = open_input("day4-input")
    sum = 0
    for line in data:
        card = line.rstrip().split(": ")[1]
        winning_numbers, numbers_on_card = card.split(" | ")
        winning_numbers = winning_numbers.split(" ")
        while "" in winning_numbers:
            winning_numbers.remove("")
        numbers_on_card = numbers_on_card.split(" ")
        while "" in numbers_on_card:
            numbers_on_card.remove("")
        # print(f"{line=}\n{winning_numbers=}\n{numbers_on_card=}\n{'#'*20}")

        counter = 0
        for elem in numbers_on_card:
            if elem in winning_numbers:
                counter += 1

        if counter == 0:
            subtotal = 0
        elif counter >= 1:
            subtotal = 1

        for i in range(counter - 1):
            subtotal *= 2

        sum += subtotal

    return sum


@dataclass
class Scratchcard:
    number: int
    winning_numbers: None
    numbers_on_card: None
    copies = 1

    def get_wins(self):
        self.winnings = 0
        for elem in self.numbers_on_card:
            if elem in self.winning_numbers:
                self.winnings += 1
        return self.winnings

    def make_copies(self):
        pass


def puzzle2():
    data = open_input("day4-input")
    scratchcards = []
    for line in data:
        card_number = re.search(r"Card\s+(\d+)", line).group(1)
        card = line.rstrip().split(": ")[1]
        winning_numbers, numbers_on_card = card.split(" | ")
        winning_numbers = winning_numbers.split(" ")
        while "" in winning_numbers:
            winning_numbers.remove("")
        numbers_on_card = numbers_on_card.split(" ")
        while "" in numbers_on_card:
            numbers_on_card.remove("")
        scratchcards.append(
            Scratchcard(card_number, winning_numbers, numbers_on_card)
        )
    for idx, elem in enumerate(scratchcards):
        print(
            f"{elem.number}: has {elem.get_wins()} wins - there are {elem.copies} copies"
        )
        for win in range(1, elem.get_wins() + 1):
            print(f"    creating {elem.copies} of {idx+win+1}")
            scratchcards[idx + win].copies += elem.copies
        try:
            print(f"next elem is {scratchcards[idx+1].number}")
        except IndexError:
            print(f"{elem.number} was the last card")

    sum_of_cards = 0
    for card in scratchcards:
        sum_of_cards += card.copies
    return sum_of_cards


print(f"antal kort i alt: {puzzle2()}")

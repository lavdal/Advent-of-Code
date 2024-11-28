# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:46:53 2023

@author: EBL
"""
from utils import open_input
from collections import Counter


class Hand:
    def determine_type(self):
        self.type = None
        if len(set(self.cardList)) == 1:
            self.type = "Five of a kind"
        elif len(set(self.cardList)) == 2:
            count = Counter(self.cardList)
            num_of_suits = [x for x in count.values()]
            if num_of_suits[0] == 1 or num_of_suits[0] == 4:
                self.type = "Four of a kind"
            else:
                self.type = "Full house"
        elif len(set(self.cardList)) == 3:
            count = Counter(self.cardList)
            if 3 in count.values():
                self.type = "Three of a kind"
            elif 2 in count.values():
                self.type = "Two pairs"
        elif len(set(self.cardList)) == 4:
            self.type = "One Pair"
        elif len(set(self.cardList)) == 5:
            self.type = "High card"

    def __lt__(self, other):
        if self.type != other.type:
            return self.type_strengh[self.type] < self.type_strengh[other.type]
        else:
            for i in range(len(self.cardList)):
                if (
                    self.card_value[self.cardList[i]]
                    != self.card_value[other.cardList[i]]
                ):
                    return (
                        self.card_value[self.cardList[i]]
                        < self.card_value[other.cardList[i]]
                    )

    def __gt__(self, other):
        if self.type != other.type:
            return self.type_strengh[self.type] > self.type_strengh[other.type]
        else:
            for i in range(len(self.cardList)):
                if (
                    self.card_value[self.cardList[i]]
                    != self.card_value[other.cardList[i]]
                ):
                    return (
                        self.card_value[self.cardList[i]]
                        > self.card_value[other.cardList[i]]
                    )

    def __str__(self):
        return f"{self.cards} | {self.type} | {self.bid}"

    def __init__(self, cards, bid):
        self.cards = cards
        self.cardList = [x for x in self.cards]
        self.bid = bid
        self.type_strengh = {
            "Five of a kind": 7,
            "Four of a kind": 6,
            "Full house": 5,
            "Three of a kind": 4,
            "Two pairs": 3,
            "One Pair": 2,
            "High card": 1,
        }
        self.card_value = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }
        self.determine_type()


class Puzzle1:
    def create_hands(self):
        self.hands = []
        for line in self.data:
            cards, bid = line.split(" ")
            self.hands.append(Hand(cards, bid))

        for hand in self.hands:
            hand.determine_type()

    def __init__(self, data):
        self.data = data
        self.create_hands()
        total_winnings = 0
        for rank, hand in enumerate(sorted(self.hands), 1):
            total_winnings += rank * int(hand.bid)

        print(total_winnings)


if __name__ == "__main__":
    puzzleInput = open_input("day7-input")
    puzzle1 = Puzzle1(puzzleInput)

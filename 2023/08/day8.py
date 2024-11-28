# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:54:53 2023

@author: EBL
"""
from utils import open_input

# from dataclasses import dataclass
import re


# @dataclass
# class Node:
#     location: str
#     l: str
#     r: str

#     def __str__(self):
#         return f"{self.location} = ({self.l}, {self.r})"


class Puzzle1:
    def create_note_dict(self):
        self.nodes_input = data[2:]
        for node in self.nodes_input:
            location, l, r = re.findall(r"\w{3}", node)
            self.nodes[location] = (l, r)

    def traverse_map(self):
        starting_location = "AAA"
        current_location = starting_location
        goal = "ZZZ"
        count = 0
        while goal != current_location:
            for direction in self.instructions:
                count += 1
                lr = 0 if direction == "L" else 1
                current_location = self.nodes[current_location][lr]
                print(f"{count}: {current_location}")

    def __init__(self, data):
        self.nodes = {}
        self.instructions = [x for x in data[0].rstrip()]
        self.create_note_dict()


class MapTraverser:
    def go_next(self, direction):
        lr = 0 if direction == "L" else 1
        next_loc = self.map_dict[self.current_location][lr]
        # print(
        #     f"going from {self.current_location} via {self.map_dict[self.current_location][lr]}"
        # )
        self.current_location = next_loc
        return next_loc

    def __init__(self, map_dict, starting_location):
        self.starting_location = starting_location
        self.map_dict = map_dict
        self.current_location = self.starting_location

    def __str__(self):
        return f"{self.current_location[2]}"


class Puzzle2:
    def create_note_dict(self):
        self.nodes_input = data[2:]
        for node in self.nodes_input:
            location, l, r = re.findall(r"\w{3}", node)
            self.nodes[location] = (l, r)

    def get_starting_locations(self):
        starting_locations = [elem for elem in self.nodes if elem[2] == "A"]
        return starting_locations

    def print_traversers(self):
        for traverser in self.traversers:
            print(traverser)

    def goal_found(self):
        endings = [x.current_location[2] for x in self.traversers]
        # print(endings)
        # print(set(endings))
        if set(endings) == set("Z"):
            print(f"goal reached in {self.count} steps")
            return True
        else:
            return False

    def __init__(self, data):
        self.nodes = {}
        self.instructions = [x for x in data[0].rstrip()]
        self.create_note_dict()
        self.traversers = [
            MapTraverser(self.nodes, loc) for loc in self.get_starting_locations()
        ]
        self.count = 0
        goal_is_found = False
        while goal_is_found == False:
            # for i in [1]:
            for lr in self.instructions:
                self.count += 1
                for traverser in self.traversers:
                    traverser.go_next(lr)
                print(f"{self.count}")
                # self.print_traversers()
                if self.goal_found() == True:
                    goal_is_found = True
                    print(f"goal reached in {self.count}")
        print(self.count)


if __name__ == "__main__":
    data = open_input("day8-input")
    puzzle2 = Puzzle2(data)
    puzzle2.get_starting_locations()

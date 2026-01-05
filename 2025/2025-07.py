from rich import print
from pathlib import Path
from utils import Grid, Point
from typing import Any

class Node:
    def __init__(self, point: Point) -> None:
        self.point = point
        self.left = None
        self.right = None



class Part_1:
    def __init__(self, input_path) -> None:
        self.splits = 0
        with open(input_path, "r") as fin:
            lines = [line.rstrip() for line in fin.readlines()]
        self.grid = Grid(lines)
        # self.grid.print_grid()
        for point in self.grid.iter_grid():
            above = self.grid.get_neighbor_dict(point)["N"]
            if above:
                if self.grid.get_point(above) == "S" or self.grid.get_point(above) == "|":
                    if self.grid.get_point(point) == "^":
                        self.splits += 1
                        targets = (self.grid.get_neighbor_dict(point)["E"], self.grid.get_neighbor_dict(point)["W"])
                    else:
                        targets=(point,)
                    
                    for target in targets:
                        try:
                            self.grid.set_point(target, "|")
                        except Exception as e:
                            print(e)
        self.print_ans(self.splits)

        for line in self.grid:
            pass #(tæl antallet af lodrette strege)



    def print_ans(self, value: type[Any]) -> None:
        print(f"[bold cyan]{'#' * 30}[bold cyan]")
        print(f"[bold cyan]svaret på opgave 1 er: {value} [bold cyan]")
        self.grid.print_grid()

class Part2:
    def __init__(self, input_path):
        with open(input_path, "r") as fin:
            ĺines = [line.rstrip() for line in fin.readlines()]
            self.grid = Grid(ĺines)
        tree = []
        for point in self.grid.iter_grid():
            if self.grid.get_point(point) == "S":
                print(self.find_next_split(point))

    def find_next_split(self, point):
        current_location = self.grid.get_neighbor_dict(point)["S"]
        split = False
        while not split:
            if self.grid.get_point(current_location) == "^":
                return current_location
            else:
                try:
                    current_location = self.grid.get_neighbor_dict(current_location)["S"]
                    print(current_location)
                except Exception as e:
                    print(e)
                    return None




if __name__ == "__main__":
    TEST = True
    input_path = (
        Path(r"./inputs/2025-07-example.txt") if TEST else Path(r"./inputs/2025-07.txt")
    )
    Part_1(input_path)
    # Part2(input_path)

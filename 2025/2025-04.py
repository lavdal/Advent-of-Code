from utils import Grid
from rich import print
from pathlib import Path


def part_1() -> None:
    with open(input_path, "r") as fin:
        ans = 0
        lines = [list(line.strip()) for line in fin.readlines()]
        grid = Grid(lines)
        for point in grid.iter_grid():
            if grid.get_point(point) == "@":
                neighbor_values = [
                    grid.get_point(neighbor) for neighbor in grid.get_neighbors(point)
                ]
                if sum([1 for x in neighbor_values if x == "@"]) < 4:
                    ans += 1

    print(
        f"[bold green]Day 4, Part 1:[/bold green] {ans} rolls can be accessed by forklift"
    )

def part_2() -> None:
    with open(input_path, "r") as fin:
        ans = 0
        lines = [list(line.strip()) for line in fin.readlines()]
        grid = Grid(lines)
        changed = 1
        while changed > 0:
            changed = 0
            for point in grid.iter_grid():
                if grid.get_point(point) == "@":
                    neighbor_values = [
                        grid.get_point(neighbor) for neighbor in grid.get_neighbors(point)
                    ]
                    if sum([1 for x in neighbor_values if x == "@"]) < 4:
                        ans += 1
                        grid.set_point(point, ".")
                        changed+=1

    print(
        f"[bold green]Day 4, Part 2:[/bold green] {ans} rolls can be removed by forklift"
    )

if __name__ == "__main__":
    TEST = False
    input_path = (
        Path(r"./inputs/2025-04-example.txt") if TEST else Path(r"./inputs/2025-04.txt")
    )
    part_1()
    part_2()

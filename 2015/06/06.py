from rich import print
from typing import Generator
from dataclasses import dataclass


@dataclass
class Command:
    function: str
    start: tuple
    end: tuple

def parse_input() -> Generator[Command, None, None]:
    with open("input06.txt","r") as fin:
        lines = [line.rstrip().split(" ") for line in fin.readlines()]
        for line in lines:
            if line[0] == "toggle":
                cmd = Command("toggle", tuple(int(i) for i in line[1].split(",")), tuple(int(i) for i in line[3].split(",")))
            else:
                cmd = Command(line[1], tuple(int(i) for i in line[2].split(",")), tuple(int(i) for i in line[4].split(",")))
            yield cmd

def get_selection(start: tuple[int,int], end: tuple[int,int]) -> Generator[tuple[int, int], None, None]:

    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            yield (x,y)

def part1() -> None:
    grid = [[0 for _ in range(1000)] for row in range(1000)]
    for cmd in parse_input():
        for ligth in get_selection(cmd.start, cmd.end):
            x, y = ligth
            if cmd.function == "on":
                # print(f"[green]turning ofn[/green] {grid[x][y]}")
                grid[x][y] = 1
            elif cmd.function == "off":
                # print(f"[red]turning off[/red] {grid[x][y]}")
                grid[x][y] = 0
            elif cmd.function == "toggle":
                # print(f"[blue]toggleling [/blue] {grid[x][y]}")
                grid[x][y] = 1 if grid[x][y] == 0 else 0
                # print(f"[turqoise]new value [/turqoise] {grid[x][y]}")
                
    
    ligths_on = sum([sum(row) for row in grid])
    print(f"[bold green]PART 1:[/bold green]\n[bold turqoise]{ligths_on}[/bold turqoise] ligths are left on")

def part2() -> None:
    grid = [[0 for _ in range(1000)] for row in range(1000)]
    for cmd in parse_input():
        for ligth in get_selection(cmd.start, cmd.end):
            x, y = ligth
            if cmd.function == "on":
                grid[x][y] += 1
            elif cmd.function == "off":
                grid[x][y] = 0 if grid[x][y] == 0 else grid[x][y]-1                
            elif cmd.function == "toggle":
                grid[x][y] += 2
    brigthness = sum([sum(row) for row in grid])
    print(f"[bold red]PART 2:[/bold red]\n[bold turqoise]Total brigthness is {brigthness}[/bold turqoise]")

if __name__ == "__main__":
    part1()
    part2()
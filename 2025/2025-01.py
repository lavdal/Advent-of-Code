"""
Løsning af advent of code 2025 dag 1
"""

from rich import print
from pathlib import Path
from collections import Counter
from typing import Generator

def read_data() -> Generator[int, None, None]:
    input_path = Path(r"./inputs/2025-01.txt")
    with open(input_path, "r") as fin:
        for line in fin.readlines():
            line = line.rstrip()
            direction = line[0]
            amount = int(line[1:])%100
            if direction.upper() == "R":
                yield amount
            else:
                yield amount*-1
            

# Løs opgave 1
def opgave_1() -> None:
    data = read_data()
    positions = [50]
    for move in data:
        new_pos = positions[-1] + move
        if new_pos < 0:
            new_pos += 100
        elif new_pos > 99:
            new_pos -= 100
        positions.append(new_pos)
    answer = Counter(positions)
    print(f"[green] den rammer 0 [/green] {answer[0]} [green] gange [/green]")


# Løs opgave 2
def opgave_2() -> None:
    pass

if __name__ == "__main__":
    opgave_1()
"""
Løsning af advent of code 2025 dag 1

prøvede løsninger til opgave 2:
    5613
    7054
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
            amount = int(line[1:]) % 100
            if direction.upper() == "R":
                yield amount
            else:
                yield amount * -1


# Løs opgave 1
def opgave_1() -> None:
    data = read_data()
    positions = [50]
    for move in data:
        new_pos = positions[-1] + move
        if new_pos > 99:
            new_pos -= 100
        elif new_pos < 0:
            new_pos += 100
        positions.append(new_pos)
    answer = Counter(positions)

    print(
        f"[bold blue]OPGAVE1\n[/bold blue][green]    Den rammer 0 [/green] {answer[0]} [green] gange [/green]"
    )


# Løs opgave 2
def opgave_2() -> None:
    with open(Path(r"./inputs/2025-01.txt"), "r") as fin:
        data = fin.readlines()
    current_pos = 50
    passes_zero = 0
    for line in data:
        small_passes = 0
        line = line.rstrip()
        direction = line[0]
        amount = int(line[1:])
        if direction == "R":
            full_rotations, remainder = divmod(current_pos + amount, 100)
            small_passes += full_rotations
            current_pos = remainder
        else:
            full_rotations, remainder = divmod(amount, 100)
            small_passes -= 1 if current_pos == 0 else 0
            current_pos -= remainder
            small_passes += full_rotations
            while current_pos < 0:
                small_passes += 1
                current_pos += 100
            if current_pos == 0:
                small_passes += 1
        passes_zero += small_passes
    print(
        f"[bold blue]OPGAVE2\n[/bold blue][green]    Den rammer 0 [/green] {passes_zero} [green] gange [/green]"
    )


if __name__ == "__main__":
    opgave_1()
    opgave_2()

from rich import print
from pathlib import Path
from itertools import chain
from tqdm import tqdm

class Interval:
    def __init__(self, beginning: int, end: int) -> None:
        self._beginning = beginning
        self._end = end
    
    def overlaps(self, other) -> bool:
        if other._beginning <= self._beginning <= other._end:
            return True
        if other._beginning <= self._end <= other._end:
            return True
        else:
            return False
    
    def combine(self, other) -> any:
        if self.overlaps(other):
            new_start = min(self._beginning, other._beginning)
            new_end = max(self._end, other._end)
            return Interval(new_start,new_end)
        else:
            raise ValueError("no overlap")


    def __len__(self) -> int:
        return self._end - self._beginning+1

    def __str__(self) -> None:
        return f"{self._beginning} | {self._end}"

    def __repr__(self):
        return f"{self._beginning} | {self._end}"




def parse_input() -> tuple[set, set]:
    with open(input_path, "r") as fin:
        ranges = []
        ids = []
        for line in fin.readlines():
            line = line.rstrip()
            try:
                start, end = [int(r) for r in line.split("-")]
                ranges.append((start, end))
            except ValueError:
                if line != "":
                    ids.append(int(line))
    # print(chain(ranges))
    return ranges, set(ids)

def parse_input2() -> list:
    with open(input_path, "r") as fin:
        ranges = []
        for line in fin.readlines():
            line = line.rstrip()
            try:
                start, end = [int(r) for r in line.split("-")]
                ranges.append((start, end))
            except ValueError:
                pass
    return ranges

def in_range(id: int, interval: tuple[int,int]) ->bool:
    return interval[0] <= id <= interval[1]

def part_1() -> None:
    ranges, ids = parse_input()
    fresh = 0
    for id in tqdm(ids):
        if any([in_range(id, r) for r in ranges]):
            fresh+=1

    print(
        f"[bold bright_cyan]Day 5, Part 1:[/bold bright_cyan]\n\tThere are {fresh} fresh ingredients"
    )

def part_2() -> None:
    ranges = [Interval(s,e) for s,e in parse_input2()]
    parsed_ranges = [ranges[0]]
    ranges = ranges[1:]
    while ranges:
        for interval in ranges[1:]:
            print(f"[red]{interval}[/red]")
            replaced=False
            for comp in parsed_ranges.copy():
                print(f"--checking against {comp}")
                if interval.overlaps(comp):
                    print("---Overlap found")
                    print(f"---Old Parsed ranges\n{parsed_ranges}")
                    parsed_ranges.remove(comp)
                    print(f"---new Parsed ranges\n{parsed_ranges}")
                    ranges.append(interval.combine(comp))
                    replaced = True
                    break

            if not replaced:
                parsed_ranges.append(interval)



    print("RESULT")
    for i in parsed_ranges:
        print(i)
        print(len(i))
    print(sum([len(i) for i in parsed_ranges]))



if __name__ == "__main__":
    TEST = True
    input_path = (
        Path(r"./inputs/2025-05-example.txt") if TEST else Path(r"./inputs/2025-05.txt")
    )
    part_1()
    part_2()

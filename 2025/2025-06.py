from rich import print
from pathlib import Path
from math import prod


def parse_input() -> tuple[set, set]:
    with open(input_path, "r") as fin:
        lines = fin.readlines()
        lines = [line.rstrip().split() for line in lines]
        num_columns = len(lines[0])
        columns = [[line[c] for line in lines] for c in range(num_columns)]

    return columns


def parse_input2():
    with open(input_path, "r") as fin:
        lines = fin.readlines()
    max_columns = max([len(line) for line in lines])
    columns = []
    for col in range(max_columns - 1):
        columns.append([line[col] for line in lines])
    # for col in columns:
    #     print("".join(col).strip().replace(" ",""))

    problems = []
    problem = []
    operator = ""
    for col in columns:
        col = "".join(col).strip().replace(" ", "")
        if not col:
            problems.append((problem, operator))
            problem = []
        else:
            if col[-1] == "*" or col[-1] == "+":
                operator = col[-1]
                problem.append(int(col[:-1]))
            else:
                problem.append(int(col))

    problems.append(
        (problem, operator)
    )  # Sidste sæt kolonner er ikke lagt i listen før nu.
    return problems


def part_1() -> None:
    columns = parse_input()
    column_sums = []
    for column in columns:
        numbers = [int(x) for x in column[:-1]]
        if column[-1] == "+":
            column_sums.append(sum(numbers))
        else:
            column_sums.append(prod(numbers))
    print(
        f"[bold bright_cyan]Day 6, Part 1:[/bold bright_cyan]\n\t Answer: {sum(column_sums)}"
    )


def part_2() -> None:
    problems = parse_input2()
    answers = []
    for problem, operator in problems:
        if operator == "+":
            answers.append(sum(problem))
        elif operator == "*":
            answers.append(prod(problem))

    print(
        f"[bold bright_cyan]Day 6, Part 2:[/bold bright_cyan]\n\t Answer: {sum(answers)}"
    )


if __name__ == "__main__":
    TEST = False
    input_path = (
        Path(r"./inputs/2025-06-example.txt") if TEST else Path(r"./inputs/2025-06.txt")
    )
    part_1()
    part_2()

from rich import print
from pathlib import Path

TEST = False
input_path = (
    Path(r"./inputs/2025-03-example.txt") if TEST else Path(r"./inputs/2025-03.txt")
)


def find_next(bank: list[int], start_idx: int, nums_behind: int) -> tuple[int, int]:
    # for idx, elem in enumerate(bank):
    #     print(f"{idx} = {bank[idx]}")
    # print(f"[bold yellow]BANK: [/bold yellow]{bank}")
    # print(f"[bold yellow]start idx: [/bold yellow]{start_idx}")
    # print(f"[bold yellow]Nums_behind: [/bold yellow]{nums_behind}")

    part = bank[start_idx:]
    # print(f"first slice : {part} - nums behind is{nums_behind}")
    part = part[:-nums_behind] if nums_behind > 0 else part
    # print(f"\t[bold orange]Part: [/bold orange]{part}")

    next_num = max(part)
    # print(f"\t[bold orange]next_num: [/bold orange]{next_num}")

    idx = part.index(next_num) + start_idx
    # print(f"\t[bold orange]idx: [/bold orange]{idx}")
    return (next_num, idx)


def get_joltage2(bank: list[int]) -> int:
    nums = []
    start = 0
    for i in range(11, -1, -1):
        num, start = find_next(bank, start, i)
        start += 1
        nums.append(num)
    return int("".join(nums))


def get_joltage(bank: list[int]) -> int:
    # print(bank[:-1])
    first = max(bank[:-1])
    last = max(bank[bank.index(first) + 1 :])
    return 10 * first + last


def solve1() -> None:
    joltage_sum = 0
    with open(input_path, "r") as fin:
        banks = fin.readlines()
        for bank in banks:
            bank = [int(x) for x in list(bank.strip())]
            joltage_sum += get_joltage(bank)

    print(
        f"[bold bright_cyan]Løst del 1 af dag 3 i 2025![/bold bright_cyan]\n\tTotal output joltage: [bold yellow]{joltage_sum}[/bold yellow]"
    )


def solve2() -> None:
    joltage_sum = 0
    with open(input_path, "r") as fin:
        banks = fin.readlines()
        for bank in banks:
            joltage_sum += get_joltage2(bank.strip())

    print(
        f"[bold bright_cyan]Løst del 2 af dag 3 i 2025![/bold bright_cyan]\n\tTotal output joltage: [bold yellow]{joltage_sum}[/bold yellow]"
    )


if __name__ == "__main__":
    if TEST:
        print(
            f"[red]{'#' * 24}\n#[/red] [magenta1]Running in test mode[/magenta1] [red]#\n{'#' * 24}[/red]"
        )
    solve1()
    solve2()

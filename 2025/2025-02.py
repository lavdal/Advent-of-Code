from rich import print
from pathlib import Path

TEST = True
input_path = (
    Path(r"./inputs/2025-02-example.txt") if TEST else Path(r"./inputs/2025-02.txt")
)


def is_valid(id: int) -> bool:
    """Check if the given ID is valid based on specific criteria."""
    id_str = str(id)
    if len(id_str) % 2 != 0:
        # print(f"{id_str} - ulige")
        return False

    else:
        mid = len(id_str) // 2
        left = id_str[:mid]
        rigth = id_str[mid:]
        # print(f"{id_str}\n{left}[red]|[/red]{rigth}")
        return left == rigth


def is_valid2(id: int) -> bool:
    """Check if the given ID is valid based on specific criteria."""
    id_str = str(id)
    # print(id)
    str_length = len(id_str)
    divisors = [x for x in range(1, str_length + 1) if str_length % x == 0]
    if len(divisors) < 2:
        # print("kan ikke deles")
        return False
    else:
        for divisor in divisors:
            id_slices = [id_str[i : i + divisor] for i in range(0, str_length, divisor)]
            if len(id_slices) > 1:
                invalid = all([x == id_slices[0] for x in id_slices])
                if invalid:
                    # print(id_slices)
                    return True
    return False


def solve1() -> None:
    valid_ids = []
    with open(input_path, "r", encoding="utf-8") as fin:
        ranges = fin.readline().strip().split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))
            # print(f"Range from {start} to {end}")
            for id in range(start, end + 1):
                valid_ids.append(id) if is_valid(id) else None
    print(
        f"[bold bright_cyan]Løst del 1 af dag 2 i 2025![/bold bright_cyan]\n\tTil sammen giver de invalide ID's: [bold yellow]{sum(valid_ids)}[/bold yellow]"
    )


def solve2() -> None:
    valid_ids = []
    with open(input_path, "r", encoding="utf-8") as fin:
        ranges = fin.readline().strip().split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))
            # print(f"Range from {start} to {end}")
            for id in range(start, end + 1):
                valid_ids.append(id) if is_valid2(id) else None
    print(
        f"[bold bright_cyan]Løst del 2 af dag 2 i 2025![/bold bright_cyan]\n\tTil sammen giver de invalide ID's: [bold yellow]{sum(valid_ids)}[/bold yellow]"
    )


if __name__ == "__main__":
    if TEST:
        print(f"[red]{'#'*24}\n#[/red] [magenta1]Running in test mode[/magenta1] [red]#\n{'#'*24}[/red]")
    solve1()
    solve2()

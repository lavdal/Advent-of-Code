from rich import print

print("[bold magenta]Advent of Code 2015 - Dag 2[/bold magenta]")

def load_data(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def solve_part1(data: list):
    sum_area = 0
    for line in data:
        l, w, h = map(int, line.split('x'))
        surface_area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total_area = surface_area + slack
        sum_area += total_area
    print(f"[green]Part 1:[/green] Total wrapping paper needed: {sum_area}")

def solve_part2(data: list):
    total_length = 0
    for line in data:
        l, w, h = map(int, line.split('x'))
        perimiters = [2*(l+w), 2*(w+h), 2*(h+l)]
        used_length = min(perimiters)
        bow_length = l * w * h
        total_length += used_length + bow_length
    print(f"[blue]Part 2:[/blue] Total ribbon needed: {total_length}")

def main():
    data = load_data('input.txt')
    solve_part1(data)
    solve_part2(data)

if __name__ == "__main__":
    main()

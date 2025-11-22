from rich import print

def read_input():
    with open("input.txt", "r") as fin:
        return fin.readlines()[0].strip()


def solve_part1(data):
    starting_position = (0, 0)
    current_position = starting_position
    visited_positions = {current_position}
    for char in data:
        match char:
            case "^":
                new_position = (current_position[0], current_position[1] + 1)
            case "v":
                new_position = (current_position[0], current_position[1] - 1)
            case ">":
                new_position = (current_position[0] + 1, current_position[1])
            case "<":
                new_position = (current_position[0] - 1, current_position[1])
            case _:
                continue
        visited_positions.add(new_position)
        current_position = new_position
    print(f"Opgave 1\nantal unikke besøgte positioner: {len(visited_positions)}")

def solve_part2(data):
    paths= ["",""]
    paths[0] = data[::2]
    paths[1] = data[1::2]

    starting_position = (0, 0)
    visited_positions = {starting_position}
    for path in paths:
        current_position = starting_position
        for char in path:
            match char:
                case "^":
                    new_position = (current_position[0], current_position[1] + 1)
                case "v":
                    new_position = (current_position[0], current_position[1] - 1)
                case ">":
                    new_position = (current_position[0] + 1, current_position[1])
                case "<":
                    new_position = (current_position[0] - 1, current_position[1])
                case _:
                    continue
            visited_positions.add(new_position)
            current_position = new_position
    print(f"Opgave2\nantal unikke besøgte positioner: {len(visited_positions)}")

def main():
    solve_part1(read_input())
    solve_part2(read_input())


if __name__ == "__main__":
    main()
def get_input(filename: str) -> list:
    with open(filename, "r") as fin:
        lines = [list(line.strip()) for line in fin.readlines()]
    return lines

def check_rest(start: tuple, string: str, arr:list) -> int:
    matches = 0
    # hvilke retninger skal der søges i
    directions = [(x,y) for y in [-1,0,1] for x in [-1,0,1]]
    directions.remove((0,0))
    
    for dir in directions:
        current_loc = start
        remaining = string[1:]
        while remaining:
            try:
                new_loc = tuple(map(sum, zip(current_loc, dir)))
                x,y = new_loc
                # test om enten x eller y er mindre en nul
                if any([coord < 0 for coord in [x,y]]):
                    break
                # print(f"{current_loc=} | {dir=} | {new_loc=} {arr[x][y]}")
                if arr[x][y] == remaining[0]:
                    # print(arr[x][y])
                    if len(remaining) == 1:
                        matches += 1
                        break
                    else:
                        remaining = remaining[1:]
                        current_loc = new_loc
                else:
                    break
            except IndexError:
                break
    return matches



def find_start(pattern: str, arr: list) -> list:
    columns = list(range(len(arr[0])))
    rows = list(range(len(arr)))

    possible_starts = []

    for row in rows:
        for column in columns:
            if arr[row][column].upper() == pattern[0].upper():
                possible_starts.append((row, column))
    return possible_starts

def opgave1(pattern: str, arr: list) -> int:
    matches = 0
    for start in find_start(pattern, arr):
        matches += check_rest(start, pattern, arr)
    
    return matches

def check_corners(start: tuple, arr: list) -> list:
    x,y = start
    trues = ["MS", "SM"]
    if 0 < x < len(arr[0]) and 0 < y < len(arr):
        try:
            string1 = arr[x-1][y-1] + arr[x+1][y+1]
            string2 = arr[x-1][y+1] + arr[x+1][y-1]
            return string1 in trues and string2 in trues
        except IndexError:
            return False

def opgave2(arr: list) -> int:
    matches = 0
    starts = find_start("A", arr)
    for start in starts:
        if check_corners(start, arr):
            matches += 1
    return matches



if __name__ == "__main__":
    TESTING = False
    filename = "test_input.txt" if TESTING else "input.txt"
    opgave_1 = opgave1("XMAS", get_input(filename))
    print(f"opgave 1: {opgave_1}")
    opgave_2 = opgave2(get_input(filename))
    print(f"opgave 2: {opgave_2}")


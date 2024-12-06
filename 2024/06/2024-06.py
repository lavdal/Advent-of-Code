from collections import namedtuple

Position = namedtuple("Position", ["row", "column"])
    
class Guard:
    def __init__(self, start_pos: Position, dir: str, map: list) -> None:

        self.start_pos = start_pos
        self.visited = {self.start_pos}
        self.current_pos = self.start_pos
        self.dir = dir
        self.map = map
    
    def is_clear(self, pos: Position) -> bool:
        row, column = pos.row , pos.column
        if row < 0 or column < 0:
            self.still_on_map = False
        else:
            try:
                if self.map[row][column] != "#":
                    return True
                else:
                    return False
            except IndexError:
                self.still_on_map = False

    def move(self) -> int:
        self.still_on_map = True
        self.new_map = self.map
        while self.still_on_map:
            match self.dir:
                case "^":
                    next_pos = Position(self.current_pos.row -1, self.current_pos.column)
                case ">":
                    next_pos = Position(self.current_pos.row, self.current_pos.column +1)
                case "v":
                    next_pos = Position(self.current_pos.row +1, self.current_pos.column)
                case "<":
                    next_pos = Position(self.current_pos.row, self.current_pos.column -1)
                case _:
                    raise ValueError(f"forventede en retning ['^', '>', 'v','<'] men fik {self.dir}")
            if self.is_clear(next_pos):
                self.visited.add(next_pos)
                self.new_map[self.current_pos.row][self.current_pos.column] = self.dir
                self.current_pos = next_pos
            else:
                match self.dir:
                    case "^":
                        self.dir = ">"
                    case ">":
                        self.dir = "v"
                    case "v":
                        self.dir = "<"
                    case "<":
                        self.dir = "^"
                    case _:
                        raise ValueError(f"forventede en retning ['^', '>', 'v','<'] men fik {self.dir}")
        
        with open("output.txt", "w") as fout:
            self.new_map[self.start_pos.row][self.start_pos.column] = "X"
            for line in self.new_map:
                fout.write("".join(line) + "\n")
        check = []
        for pos in self.visited:
            if (pos.row, pos.column) not in check:
                check.append((pos.row, pos.column))

        return len(self.visited)
    

        

    def __str__(self):
        return f"Guard at {self.current_pos} | dir: {self.dir}"
    



class Solver:
    def __init__(self, testing:bool = False):
        if testing:
            self._parse_input("test_input.txt")
        else:
            self._parse_input("input.txt")

    def _parse_input(self, path:str):
        with open(path, "r") as fin:
            self.lines = [[elem for elem in row.strip()] for row in fin.readlines()]
            num_rows =  len(self.lines)
            num_columns = len(self.lines[0])

            for rid, row in enumerate(self.lines):
                for cid, element in enumerate(row):
                    if element == "^":
                        self.start = Position(rid, cid)
        return None
    
    def opgave1(self):
        guard = Guard(self.start, "^", self.lines)
        return guard.move()
    
    def opgave2(self):
        result = 0
        return result

if __name__ == "__main__":
    # TEST
    test1 = Solver(True).opgave1()
    print(f"TEST 1: {test1}")
    
    test2 = Solver(True).opgave2()
    print(f"TEST 2: {test2}")

    # SVAR
    svar1 = Solver()
    print(f"OPGAVE 1: {svar1.opgave1()}")
    
    svar2 = Solver().opgave2()
    print(f"OPGAVE 2: {svar2}")

"""
Forsøg:
Opgave 1:
    9136 - For høj
"""
from collections import namedtuple

Position = namedtuple("Position", ["row", "column"])
    
class Guard:
    def __init__(self, start_pos: Position, direction: str, map: list) -> None:

        self.start_pos = start_pos
        self.visited = [self.start_pos]
        self.current_pos = self.start_pos
        self.visited_pos = []
        self.overlaps = []
        self.direction = direction
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
            match self.direction:
                case "^":
                    next_pos = Position(self.current_pos.row -1, self.current_pos.column)
                case ">":
                    next_pos = Position(self.current_pos.row, self.current_pos.column +1)
                case "v":
                    next_pos = Position(self.current_pos.row +1, self.current_pos.column)
                case "<":
                    next_pos = Position(self.current_pos.row, self.current_pos.column -1)
                case _:
                    raise ValueError(f"forventede en retning ['^', '>', 'v','<'] men fik {self.direction}")
            if self.is_clear(next_pos):
                if next_pos not in self.visited:
                    self.visited.append(next_pos)
                    self.visited_pos.append((next_pos, self.direction))
                else:
                    self.overlaps.append((next_pos, self.direction))
                self.new_map[self.current_pos.row][self.current_pos.column] = self.direction
                self.current_pos = next_pos
            else:
                match self.direction:
                    case "^":
                        self.direction = ">"
                    case ">":
                        self.direction = "v"
                    case "v":
                        self.direction = "<"
                    case "<":
                        self.direction = "^"
                    case _:
                        raise ValueError(f"forventede en retning ['^', '>', 'v','<'] men fik {self.direction}")
        
        return len(self.visited)
    
    def get_travels(self):
        return self.visited_pos, self.overlaps
        

    def __str__(self):
        return f"Guard at {self.current_pos} | direction: {self.direction}"
    



class Solver:
    def __init__(self, testing:bool = False):
        if testing:
            self._parse_input("test_input.txt")
        else:
            self._parse_input("input.txt")

    def _parse_input(self, path:str):
        with open(path, "r") as fin:
            self.lines = [[elem for elem in row.strip()] for row in fin.readlines()]

            for rid, row in enumerate(self.lines):
                for cid, element in enumerate(row):
                    if element == "^":
                        self.start = Position(rid, cid)
        return None
    
    def opgave1(self):
        guard = Guard(self.start, "^", self.lines)
        return guard.move()
    
    def opgave2(self):

        """
        skal ikke gå efter overlaps som i nedenstående.
        men gå den originale path igennem og se om et højresving vil lede den tilbage
        til denne lokation igen
        """
        guard = Guard(self.start, "^", self.lines)
        guard.move()
        travels, overlaps = guard.get_travels()
        new_map = self.lines
        possibles = 0
        for pos, direction in overlaps:
            # print("overlap")
            old_dir = "!"
            # print(pos)
            for point, arrow in travels:
                if point == pos:
                    old_dir = arrow
                    
                    if direction == "^" and old_dir == ">" or direction == ">" and old_dir == "v" or direction == "v" and old_dir == "<" or direction == "<" and old_dir == "^":
                        possibles +=1
            
            
            new_map[pos.row][pos.column] = "?"

        with open("output.txt", "w") as fout:
            for line in new_map:
                fout.write("".join(line) + "\n")
        return possibles

if __name__ == "__main__":
    # TEST
    test1 = Solver(True).opgave1()
    print(f"TEST 1: {test1}")
    
    test2 = Solver(True).opgave2()
    print(f"TEST 2: {test2}")

    # # SVAR
    # svar1 = Solver()
    # print(f"OPGAVE 1: {svar1.opgave1()}")
    
    svar2 = Solver().opgave2()
    print(f"OPGAVE 2: {svar2}")

"""
Forsøg:
Opgave 1:
    9136 - For høj
    
Opgave 2:
        293 - for lav
"""
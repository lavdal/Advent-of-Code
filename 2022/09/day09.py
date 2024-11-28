"""
Advent of Code besvarelser 2022 dag 9
"""
from dataclasses import dataclass

@dataclass
class Koordinat:
    x: int
    y:int
    
    def koord(self):
        return (self.x, self.y)

class Knot:
    def __init__(self):
        self.pos = Koordinat(0,0)
        self.visited=[]
        self._update_visited
    
    def _update_visited(self):
        if self.pos.koord() not in self.visited: self.visited.append(self.pos.koord())

class Head(Knot):
    def move(self, direction):
        match direction:
            case "U":
                self.pos.y += 1
            case "D":
                self.pos.y += -1
            case "R":
                self.pos.x += 1
            case "L":
                self.pos.x += -1
        self._update_visited()

class Tail(Knot):
    def __init__(self, head):
        super().__init__()
        self.head = head
    def next_to_head(self):
        if abs(self.pos.x - self.head.pos.x)>1 or abs(self.pos.y - self.head.pos.y)>1:
            return False
        else:
            return True
    
    def update(self):
        if not self.next_to_head():
            distance_vector = Koordinat(self.head.pos.x - self.pos.x, self.head.pos.y - self.pos.y)
            if distance_vector.x > 0:
                self.pos.x += 1
            if distance_vector.x < 0:
                self.pos.x -= 1
            if distance_vector.y > 0:
                self.pos.y += 1
            if distance_vector.y < 0:
                self.pos.y -= 1
        self._update_visited()

class solver:
    def read_data(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        data = []
        with open(filename, "r") as fin:
            for line in fin.readlines():
                direction, steps = line.strip().split(" ")
                data.append((direction, int(steps)))
        return data
    
    def solve1(self):
        head = Head()
        tail = Tail(head)
        
        for direction, steps in self.read_data():
            for _ in range(steps):
                head.move(direction)
                tail.update()
  
        return len(tail.visited)
        
    def solve2(self):
        head = Head()
        tail1 = Tail(head)
        tail2 = Tail(tail1)
        tail3 = Tail(tail2)
        tail4 = Tail(tail3)
        tail5 = Tail(tail4)
        tail6 = Tail(tail5)
        tail7 = Tail(tail6)
        tail8 = Tail(tail7)
        tail9 = Tail(tail8)
        
        tails = [tail1, tail2, tail3, tail4, tail5, tail6, tail7, tail8, tail9]
                
        for direction, steps in self.read_data():
            for _ in range(steps):
                head.move(direction)
                for tail in tails:
                    tail.update()            
        return len(tail9.visited)
    
    def __init__(self, testmode = False):
        self.test = testmode
        self.data = self.read_data()
        
        print(f"svaret på opgave 1 er: {self.solve1()}")
        print(f"svaret på opgave 2 er: {self.solve2()}")
        

    
    
if __name__ == "__main__":
    print(f"{'#'*5} TESTMODE {'#'*5}")
    solver(True) # testmode
    print(f"\n\n{'#'*5} Final {'#'*5}")
    solver() # Final

    
    
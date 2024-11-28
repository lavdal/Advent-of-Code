"""
Advent of Code besvarelser 2022 dag 10
"""
from collections import defaultdict
class solver:
    def read_data(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        data = []
        with open(filename, "r") as fin:
            lines = [line.strip() for line in fin.readlines()]
            return lines
    
    def get_signal_strenght(self, cycle_ids):
        strength = 0
        for idx in cycle_ids:
            strength += self.cycles[idx] * idx
        
        return strength
    
    def solve1(self):
        self.cycles = defaultdict(int)
        current_cycle = 0
        X = 1
        for line in self.data:
           if line == "noop":
               current_cycle += 1
               self.cycles[current_cycle] = X
           else:
               command, val = line.split(" ")
               current_cycle += 1
               self.cycles[current_cycle] = X
               current_cycle += 1
               self.cycles[current_cycle] = X
               X += int(val)
        self.cycles[current_cycle+1] = X
            
        relevant_cycles= [20,60,100,140,180,220]

        return self.get_signal_strenght(relevant_cycles)
        
    def solve2(self):
        to_print= ""
        for idx, cycle in self.cycles.items():
            printing_loc = idx-1
            if printing_loc%40 in [cycle-1, cycle, cycle+1]:
                char = "#"
            else:
                char = "."
            if idx == 241:
                pass
            elif idx % 40 == 0 and idx !=0:
                print(char)
            else:
                print(char,end="")
        print()
    
    def __init__(self, testmode = False):
        self.test = testmode
        self.data = self.read_data()
        
        print(f"svaret på opgave 1 er: {self.solve1()}")
        print(f"svaret på opgave 2 er:")
        self.solve2()
        

    
    
if __name__ == "__main__":
    print(f"{'#'*5} TESTMODE {'#'*5}")
    solver(True) # testmode
    print(f"\n\n{'#'*5} Final {'#'*5}")
    solver() # Final

    
    
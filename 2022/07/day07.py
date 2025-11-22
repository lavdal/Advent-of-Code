"""
Advent of Code besvarelser 2022 dag 7

LAVET MED HJÆLP FRA ANDRES KODE:
    Part 1 er løst næsten direkte efter:
    https://github.com/narimiran/AdventOfCode2022/blob/main/python/day07.py

"""
from itertools import accumulate
from collections import defaultdict

class solver:
    def read_data(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        data = []
        with open(filename, "r") as fin:
            for line in fin.readlines():
                data.append(line.strip())
        return data
    
    def solve1(self):
        self.sizes = defaultdict(int) #hvis en key ikke findes i den defaultdict, oprettes den med standardværdien (i dette tilfælde int der blivr 0)
        path = ["/"] # denne linie er vist overflødig, men jeg kan ikke lide at en vigtig variabel førs deklareres i en match/case
        for line in self.data:
            match line.split():
                case '$', 'cd', "/":  path = ['/']
                case '$', 'cd', "..": path.pop()
                case '$', 'cd', f:    path.append(f+'/')
                case '$', 'ls':       pass # vi er ligeglade med denne kommando, den giver os bare de data der kommer i de følgende linier der samles op af val-casen
                case 'dir', _:        pass # at der er et dir i en mappe er ligegyldigt, medminde vi skifter ind i den med et cd
                case val, _:
                    for p in accumulate(path):
                        """
                        acuumulate(path) giver alle mapperne op til dette child element. Altså:
                        ['/', '/dir1/', '/dir1/subdir/'...] 
                        filens størrelse beregnes altså ind i alle elementer over denne,
                        da et dirs størrelse beregnes ud fra summen af alle subdirs og filer, fungerer dette.
                        """
                        self.sizes[p] += int(val)
        small_dirs = [size for size in self.sizes.values() if size <= 100000]
        return sum(small_dirs)
    
    def solve2(self):
        used_space = self.sizes["/"]
        available_space = 70000000 - used_space
        missing_space = 30000000 - available_space
        dirs_large_enough = [size for size in self.sizes.values() if size >= missing_space]
        return min(dirs_large_enough)
                
                    
        
    
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

    
    
"""
Advent of Code besvarelser 2024 dag 01
"""
from pathlib import Path

class Solver:
    def read_data(self, input_path):
        with open(input_path, "r") as fin:
            data = fin.readlines()      
        return data
    
    def __init__(self, input_path, verbose= False):
        self.data = self.read_data(input_path)        
        self.verbose = verbose
            
    def opgave1(self):
        return None         
        
    def opgave2(self):
        return None
        
    
if __name__ == "__main__":
    verbose_mode = False
    test_path = Path(r"./test_data.txt")
    if test_path.exists():
        print(f"{' TESTMODE ':#^50}\n")
        test_solver = Solver(test_path, verbose=verbose_mode)
        
        test1 = test_solver.opgave1()
        if test1:
            print(f"svaret på test 1 er: {test1:>{50-len('svaret på test 1 er: ')}}")
        
        test2 = test_solver.opgave2()
        if test2:
            print(f"svaret på test 2 er: {test2:>{50-len('svaret på test 2 er: ')}}")
    
    print(f"\n{' Besvarelser ':#^50}\n")
    input_path = Path(r"./input.txt")
    besvarelse = Solver(input_path)
    
    opgave1 = besvarelse.opgave1()
    if opgave1:
        print(f"svaret på opgave 1 er: {opgave1:>{50-len('svaret på opgave 1 er: ')}}")
    opgave2 = besvarelse.opgave2()
    if opgave2:
        print(f"svaret på opgave 2 er: {opgave2:>{50-len('svaret på opgave 2 er: ')}}")
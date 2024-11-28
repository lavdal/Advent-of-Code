"""
Advent of Code besvarelser 2022 dag 8
"""
import math


class solver:
    def read_digit_matrix(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        arr = []
        with open(filename, "r") as fin:
            for line in fin.readlines():
                arr.append([int(x) for x in line.strip()])
        return arr
    
    def solve1(self):
        visible_trees = 0
        for idy, række in enumerate(self.skov):
            for idx, tree in enumerate(række):
                vest = række[:idx]
                øst = række[idx+1:]
                kolonne = [række[idx] for række in self.skov]
                nord = kolonne[:idy]
                syd = kolonne[idy+1:]
                if any([all([x < tree for x in direction]) for direction in [vest, øst, nord, syd]]):
                        visible_trees += 1
        return visible_trees
    
    def solve2(self):
        best_scenic_score = 0
        for idy, række in enumerate(self.skov):
            for idx, tree in enumerate(række):
                tree_scenic_score = 0
                vest = række[:idx]
                øst = række[idx+1:]
                kolonne = [række[idx] for række in self.skov]
                nord = kolonne[:idy]
                syd = kolonne[idy+1:]
                direction_scores = []
                for direction in [vest, øst, syd, nord]:
                    direction_score = 0
                    if direction in [nord, vest]:
                        direction.reverse()
                    for elem in direction:
                        direction_score += 1
                        if elem >= tree:
                            break
                    direction_scores.append(direction_score)
                tree_scenic_score = math.prod(direction_scores)
                if tree_scenic_score > best_scenic_score:
                    best_scenic_score = tree_scenic_score
        return best_scenic_score
                
                    
        
    
    def __init__(self, testmode = False):
        self.test = testmode
        self.skov = self.read_digit_matrix()
        
        print(f"svaret på opgave 1 er: der er {self.solve1()} træer synlige")
        print(f"svaret på opgave 1 er: beste scenic score er {self.solve2()}")
        

    
    
if __name__ == "__main__":
    print(f"{'#'*5} TESTMODE {'#'*5}")
    solver(True) # testmode
    print(f"\n\n{'#'*5} Final {'#'*5}")
    solver() # Final

    
    
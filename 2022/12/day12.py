"""
Advent of Code besvarelser 2022 dag 12
"""
class Node:
    arr=[]
    def __init__(self, value: int, y: int, x:int, parent= None):
        self.elevation = value
        self.x = x
        self.y = y
        self.parents = parent if parent else None
        self.heritage = []
        self.neighbors = []
        
    def get_neighbors(self):
        possible_neighbors = [(+1,0),(-1,0),(0,+1),(0,-1)]
        for dy, dx in possible_neighbors:
            nx = self.x + dx
            ny = self.y + dy
            if 0 <=  ny < len(self.arr) and 0 <=  nx < len(self.arr[0]):
                if self.arr[ny][nx] <= self.elevation+1:
                    self.neighbors.append(Node(self.arr[ny][nx],ny,nx, self))
   
    def __str__(self):
        return f"node: x:{self.x}; y:{self.y} | elevation = {self.elevation}"

class Solver:
    def read_data(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        arr = []
        
        with open(filename, "r") as fin:
            for line in fin.readlines():
                row = [ord(char)-97 for char in line.strip()]
                arr.append(row)
        
        return arr
    
    def __init__(self, testmode = False, verbose= False):
        self.test = testmode
        self.data = self.read_data()        
        self.verbose = verbose
        Node.arr = self.data
        
        # prints Matrix
        if self.verbose:
            print("#"*20)
            for row in self.data:
                print(row)
            print("#"*20)
            print("\n\n")
            
            
    def opgave1(self):
        for idy, row in enumerate(self.data):
            for idx, elevation in enumerate(row):
                if elevation == -14:
                    starting_node = Node(0, idy, idx)
                if elevation == -28:
                    end_coords = (idx,idy)
                    self.data[idy][idx] = ord("z")-97
        
        # print(starting_node)
        self.que = [starting_node]
        self.visited= {}
        
        while self.que:
            node=self.que.pop(0)
            node_coords = (node.x, node.y)
            if node_coords == end_coords:
                end_node = node
                break
            if node_coords not in self.visited.keys():
                 
                self.visited[node_coords] = node
                node.get_neighbors()
                for neighbor in node.neighbors:
                    if (neighbor.x, neighbor.y) not in self.visited.keys():
                        self.que.append(neighbor)

        current = end_node
        steps = []
        while True:
            current = current.parents
            if current == None:
                break
            else:
                steps.append(current)
        steps.reverse()
        
        if self.verbose:
            for node in steps:
                print(node)
                    
        print(f"Løsning på opgave 1:\nDen korsteste vej er {len(steps)} steps")
        
    def find_path(self, starting_point, end_point):
        y, x = starting_point
        end_coords = end_point
        if self.verbose:
            print()
            print()
            print(f"kører find_path\nStart {x=}:{y=}\nEnd: {end_coords}")
        self.que = [Node(0, y, x)]
        self.visited= {}
        
        while self.que:
            node=self.que.pop(0)
            node_coords = (node.x, node.y)
            end_node = None
            if node_coords == end_coords:
                end_node = node
                break
            if node_coords not in self.visited.keys():
                self.visited[node_coords] = node
                node.get_neighbors()
                for neighbor in node.neighbors:
                    if (neighbor.x, neighbor.y) not in self.visited.keys():
                        self.que.append(neighbor)
        if end_node:
            current = end_node
            steps = []
            while True:
                current = current.parents
                if current == None:
                    break
                else:
                    steps.append(current)
            steps.reverse()
            
            return len(steps)
        else:
            if self.verbose:
                print("End_not_found")
            
        
    def opgave2(self):
        starting_points = []
        for idy, row in enumerate(self.data):
            for idx, elevation in enumerate(row):
                if elevation == -14 or elevation == 0:
                    starting_points.append((idy, idx))
                    
                if elevation == -28:
                    end_coords = (idx,idy)
                    print(end_coords)
                    self.data[idy][idx] = ord("z")-97
        lengths = []
        for starting_point in starting_points:
            length = self.find_path(starting_point, end_coords)
            if length != None:
                lengths.append(length)
        
        print(f"løsningen på opgave 2 er:\n{min(lengths)} steps")
        
       
        

    
    
if __name__ == "__main__":
    Solver(testmode=False, verbose=False).opgave1()
    Solver(testmode=False, verbose=False).opgave2()
"""
Advent of Code besvarelser 2022 dag 5
"""
import regex as re

def opgave1(input_data):
    def read_stacks(lines):
        h_stacks = []
        v_stacks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        for line in lines:
            
            if line[0] == "1":
                break
            else:
                h_stacks.append(line)
        stack_locations = {1:1, 2:5, 3:9, 4:13, 5:17, 6:21, 7:25, 8:29, 9:33}
        for line in h_stacks[::-1]:
            for stack, loc in stack_locations.items():
                if line[loc] != " ":
                    v_stacks[stack].append(line[loc])
        return v_stacks
    
    def print_stacks(stacks):
        for stack_num, stack_cont in stacks.items():
            stack_line = f"[{'] ['.join(stack_cont)}]" if len(stack_cont) > 0 else ""
            print(f"{stack_num} | {stack_line}")
            
    def read_moves(lines):
        moves =  []
        for line in lines:
            move = re.search(r"move (\d+) from (\d) to (\d)", line)
            try:
                moves.append([int(move.group(1)), int(move.group(2)), int(move.group(3))])
            except AttributeError:
                pass
            
        return moves
        
    
    def make_move(stacks, num_of_moves: int, start: int, destination: int):
        for _ in range(num_of_moves):
            stacks[destination].append(stacks[start].pop())
            #print_stacks(stacks)
    
    def read_tops(stacks):
        ans = []
        for stack in stacks:
            ans.append(stacks[stack].pop())
        return "".join(ans)
    
    stacks = read_stacks(input_data)
    # print_stacks(stacks)
    moves = read_moves(input_data)
    for move in moves:
        make_move(stacks, *move)
    print(f"svaret på opgave 1 er: {read_tops(stacks)}")
    
def opgave2(input_data):
    def read_stacks(lines):
        h_stacks = []
        v_stacks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        for line in lines:
            
            if line[0] == "1":
                break
            else:
                h_stacks.append(line)
        stack_locations = {1:1, 2:5, 3:9, 4:13, 5:17, 6:21, 7:25, 8:29, 9:33}
        for line in h_stacks[::-1]:
            for stack, loc in stack_locations.items():
                if line[loc] != " ":
                    v_stacks[stack].append(line[loc])
        return v_stacks
    
    def print_stacks(stacks):
        for stack_num, stack_cont in stacks.items():
            stack_line = f"[{'] ['.join(stack_cont)}]" if len(stack_cont) > 0 else ""
            print(f"{stack_num} | {stack_line}")
            
    def read_moves(lines):
        moves =  []
        for line in lines:
            move = re.search(r"move (\d+) from (\d) to (\d)", line)
            try:
                moves.append([int(move.group(1)), int(move.group(2)), int(move.group(3))])
            except AttributeError:
                pass
            
        return moves
        
    
    def make_move(stacks, num_of_moves: int, start: int, destination: int):
        moving_list = []
        for i in range(num_of_moves):
            moving_list.append(stacks[start].pop())
        
        moving_list.reverse()
        for elem in moving_list:
            stacks[destination].append(elem)
    
    def read_tops(stacks):
        ans = []
        for stack in stacks:
            ans.append(stacks[stack].pop())
        return "".join(ans)
    
    stacks = read_stacks(input_data)
    # print_stacks(stacks)
    moves = read_moves(input_data)
    for move in moves:
        make_move(stacks, *move)
    print(f"svaret på opgave 2 er: {read_tops(stacks)}")
    
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = [line.strip() for line in fin.readlines()]
    
    opgave1(lines)
    opgave2(lines)
"""
Advent of Code besvarelser 2022 dag 1
"""


def opgave1(input_data):
    results = []
    tally = 0    
    for line in input_data:
        line = line.strip()
        if line == "":
            results.append(tally)
            tally = 0
        else:
            tally += int(line)
    results.append(tally)
        
    print(f"svaret på opgave 1 er: {max(results)}")
    
def opgave2(input_data):
    results = []
    tally = 0    
    for line in input_data:
        line = line.strip()
        if line == "":
            results.append(tally)
            tally = 0
        else:
            tally += int(line)
    results.append(tally)
    results.sort()
    print(f"svaret på opgave 2 er: {sum(results[-3:])}")
    
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.readlines()
    
    opgave1(lines)
    opgave2(lines)
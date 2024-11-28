"""
Advent of Code besvarelser 2022 dag X
"""


def opgave1(input_data):
    ans = 0
    for line in input_data:
        
        first, second = line.strip().split(",")
        #first_list = [x for x in range(int(first.split("-")[0]), int(first.split("-")[1])+1)]
        #second_list = [x for x in range(int(second.split("-")[0]), int(second.split("-")[1])+1)]
        #overlap = set(first_list) & set(second_list)
        if int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]):
            #andet sæt indeholder hele første sæt
            ans +=1
        elif int(first.split("-")[0]) <= int(second.split("-")[0]) and int(first.split("-")[1]) >= int(second.split("-")[1]):
            #første sæt indeholder hele andet sæt
            ans +=1
        else:
            #intet sæt er fuldt indeholdt af det andet
            pass
    
    print(f"Opgave 1: {ans}")
    
def opgave2(input_data):
    ans = 0
    for line in input_data:
        first, second = line.strip().split(",")
        first_list = [x for x in range(int(first.split("-")[0]), int(first.split("-")[1])+1)]
        second_list = [x for x in range(int(second.split("-")[0]), int(second.split("-")[1])+1)]
        if any([x in second_list for x in first_list]):
            ans +=1
    
    print(f"Opgave 2: {ans}")
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.readlines()
    
    opgave1(lines)
    opgave2(lines)
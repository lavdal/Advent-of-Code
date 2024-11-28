"""
Advent of Code besvarelser 2022 dag X
"""


def opgave1(input_data):
    ans = 0
    
    values = {key: val for val, key in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),1)}
    
    for line in input_data:
        line = line.strip()
        compartment_a = line[:len(line)//2]
        compartment_b = line[len(line)//2:]
        overlap = set(compartment_a) & set(compartment_b)
        ans += values[list(overlap)[0]]

    print(f"løsningen på opgave 1 er: {ans}")
    
def opgave2(input_data):
    ans = 0
    
    values = {key: val for val, key in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),1)}

    def divide_chunks(l, n):
        for i in range(0, len(l), n):  #n er tallet for hvor mange elementer der er i en chunk
            yield l[i:i + n]
    
    for chunk in divide_chunks(input_data,3):
        badge = set(chunk[0].strip()) & set(chunk[1].strip()) & set(chunk[2].strip()) 
        ans += values[list(badge)[0]]
    
    print(f"løsningen på opgave 2 er: {ans}")
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.readlines()
    
    opgave1(lines)
    opgave2(lines)
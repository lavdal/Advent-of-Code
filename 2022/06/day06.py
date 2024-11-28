"""
Advent of Code besvarelser 2022 dag 6
"""


def opgave1(input_data):
    def is_valid_marker(marker):
        return len(set(marker)) > 3
    
    data_buffer = input_data[0]
    print(data_buffer)
    print("#"*20)
    for idx, char in enumerate(data_buffer):
        if idx > 2:
            marker = data_buffer[idx-3:idx+1]
            if is_valid_marker(marker):
                return idx+1
                
    
    
def opgave2(input_data):
    def is_valid_marker(marker):
        return len(set(marker)) > 13
    
    data_buffer = input_data[0]
    print(data_buffer)
    print("#"*20)
    for idx, char in enumerate(data_buffer):
        if idx > 12:
            marker = data_buffer[idx-13:idx+1]
            if is_valid_marker(marker):
                return idx+1
    
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.readlines()
    lines = [line.strip() for line in lines]
    
    print(f"svaret på ogave 1 er: {opgave1(lines)}")
    print(f"svaret på ogave 2 er: {opgave2(lines)}")

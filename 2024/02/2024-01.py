class Solver:
    def __init__(self, path):
        self.path = path
        self.data = self.parse_as_list()
        self.opgave1()
        self.opgave2()

    def parse_as_list(self) -> list:
        with open(self.path, "r") as fin:
            lines = [[int(x) for x in line.strip().split()] for line in fin.readlines()]
        return lines

    def is_safe(self, line: list[int]) -> bool:
        diffs = [line[i]-line[i-1] for i in range(1,len(line))]
        if all([x > 0 for x in diffs]) or all([x < 0 for x in diffs]):
            if all([abs(x) <= 3 for x in diffs]):
                return True
        return False
    
            
        print(temp_lines)
    def safe_if_dampened(self, line: list[int]) -> bool:
        temp_lines = []
        for elem in line:
            temp_line = line.copy()
            temp_line.remove(elem)
            temp_lines.append(temp_line)
        for newline in temp_lines:
            if self.is_safe(newline):
                return True
        return False

    def opgave1(self) -> None:
        safe_reports = 0
        for line in self.data:
            if self.is_safe(line):
                safe_reports += 1
        print(f"Opgave 1: {safe_reports=}")
    
    def opgave2(self) -> None:
        safe_reports = 0
        for line in self.data:
            if self.is_safe(line):
                safe_reports += 1
            elif self.safe_if_dampened(line):
                safe_reports += 1
        print(f"Opgave 2: {safe_reports=}")
        
            

if __name__ == "__main__":
    print(f"TEST:")
    Solver(r"test_data.txt")
    print(f"\nANSWER")
    Solver(r"input.txt")
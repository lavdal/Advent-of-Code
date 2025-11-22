import re

class Solver:
    def __init__(self, path):
        self.path = path
        self.data = self.parse_as_list()
        self.opgave1()
        self.opgave2()

    def parse_as_list(self) -> list[str]:
        with open(self.path, "r") as fin:
            lines = [line for line in fin.readlines()]
        return lines

    def opgave1(self) -> None:
        result = 0
        for line in self.data:
            # regex til at finde de gyldige patterns
            mul_regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
            muls = re.findall(mul_regex, line)
            # for hver gyldig mul findes tallene og ganges sammen og lægges til resultatet
            for mul in muls:
                digits = re.search(r'(\d{1,3}),(\d{1,3})', mul)
                result += int(digits.group(1)) * int(digits.group(2))
        print(result)
    
    def opgave2(self) -> None:
        result = 0
        mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        # i starten er vi enabled
        enabled = True
        data_remaining = "".join(self.data)
        while data_remaining:
            if enabled:
                # del den resterende data op i data, "Dont" (udgår -> _) og resten
                data, _ , data_remaining = data_remaining.partition(r"don't()")
                
                for match in mul_regex.finditer(data):
                    x, y = match.groups()
                    result += int(x)*int(y)
                
                # vi har nået en dont - sæt enabled til false
                enabled = False
            else:
                # Ignorer alt frem til do
                _, _, data_remaining = data_remaining.partition(r"do()")
                enabled = True
        
        print(result)
if __name__ == "__main__":
    # print(f"TEST:")
    # Solver(r"test_input.txt")
    # print("TEST2")
    # Solver(r"test_input2.txt")
    print("\nANSWER")
    Solver(r"input.txt")
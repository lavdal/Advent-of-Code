class Rule:
    def __init__(self, low: str, high: str):
        self.low = low
        self.high = high

    def __str__(self):
        return f"({self.low} | {self.high})"

    def is_valid(self, ls:list) -> bool:
        try:
            if ls.index(self.low) > ls.index(self.high):
                # hvis index(low) er større end index(high) er reglen ikke overholdt
                return False
            else:
                return True
        except ValueError:
            # hvis ikke begge værdier er i listen er reglen ugyldig, og skal ikke regnes med, kan derfor betragtes som True
            return True

class Solver:
    def __init__(self, testing:bool = False):
        if testing:
            self.parse_input("test_input.txt")
        else:
            self.parse_input("input.txt")

    def parse_input(self, path:str):
        self.rules = []
        self.updates = []
        with open(path, "r") as fin:
            for line in fin.readlines():
                if "|" in line:
                    # der er tale om en regel
                    low, high = line.strip().split("|")
                    self.rules.append(Rule(low, high))
                elif line.strip() != "":
                    # der er tale om en "update"
                    self.updates.append(line.strip().split(","))
        return None
    
    def opgave1(self):
        result = 0
        for update in self.updates:
            if all([rule.is_valid(update) for rule in self.rules]):
                # så fremt alle lister er et ulige antal findes det midterste index med følgende formel int(len(update)/2)
                result += int(update[int(len(update)/2)])
        return result

if __name__ == "__main__":
    test1 = Solver(True).opgave1()
    print(f"TEST 1: {test1}")

    svar1 = Solver().opgave1()
    print(f"OPGAVE 1: {svar1}")
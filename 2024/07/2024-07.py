from collections import namedtuple, defaultdict

Calibration = namedtuple("Calibration", ["ans", "values"])

class Solver:
    def __init__(self, testing:bool = False):
        if testing:
            self._parse_input("test_input.txt")
        else:
            self._parse_input("input.txt")

    def _parse_input(self, path:str):
        self.data = []
        with open(path, "r") as fin:
            for line in fin.readlines():
                ans, values = line.strip().split(": ")
                values = [int(x) for x in values.split(" ")]
                self.data.append(Calibration(int(ans), values))
        return None
    
    def _generate_lookup(self, n_max: int, operators: list[str] = ["+", "*"]) -> defaultdict:
        combinations = defaultdict(list)
        combinations[1] = [[elem] for elem in operators]
        for n in range(2, n_max+1):
            for ls in combinations[n-1]:
                for operator in operators:
                    newlist = ls.copy()
                    newlist.append(operator)
                    combinations[n].append(newlist)
        
        return combinations

    def _passes_calibration(self, calibration: Calibration) -> bool:
        # print(calibration)
        for combination in self.operator_combinations[len(calibration.values)-1]:
            comb_copy = combination.copy()
            values = calibration.values.copy()
            res = values.pop(0)
            while len(values) > 0:
                temp = f"{res}{comb_copy.pop(0)}{values.pop(0)}"
                res = eval(temp)
                
                if res == calibration.ans:
                    print(f"{calibration.ans} true with {calibration.values} {combination}")
                    return True
        
        return False

    def opgave1(self):
        # Lav en lookuptable med de forskellige mulige kombinationer af operators
        n_max = max([len(elem.values) for elem in self.data]) -1
        self.operator_combinations = self._generate_lookup(n_max)

        passed_calibrations = []

        for calibration in self.data:
            if self._passes_calibration(calibration):
                passed_calibrations.append(calibration)
        
        # for calibration in passed_calibrations:
        #     print(calibration)

        return sum([calibration.ans for calibration in passed_calibrations])
    

    
    def opgave2(self):
        pass
       

if __name__ == "__main__":
    # TEST
    test1 = Solver(True).opgave1()
    print(f"TEST 1: {test1}")
    
    test2 = Solver(True).opgave2()
    print(f"TEST 2: {test2}")

    # SVAR
    svar1 = Solver()
    print(f"OPGAVE 1: {svar1.opgave1()}")
    
    # svar2 = Solver().opgave2()
    # print(f"OPGAVE 2: {svar2}")

"""
Forsøg:
Opgave 1:
    for højt: 975761400187
    
Opgave 2:

"""
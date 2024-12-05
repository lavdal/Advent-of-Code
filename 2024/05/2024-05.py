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
            self._parse_input("test_input.txt")
        else:
            self._parse_input("input.txt")

    def _parse_input(self, path:str):
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
    
    def _get_incorrect(self) -> list:
        incorrect_updates = []
        for update in self.updates:
            if not all([rule.is_valid(update) for rule in self.rules]):
                incorrect_updates.append(update)
        
        return incorrect_updates
    
    def _order_update(self, update_list: list) -> list:
        update = update_list.copy()
        sorted = False
        while not sorted:
            for rule in self.rules:
                while not rule.is_valid(update):
                    # så længe regelen ikke er opfyldt bytter den værdi der skal være først plads med værdien inden den.
                    idx = update.index(rule.low)
                    update[idx], update[idx-1] = update[idx-1], update[idx]
                    # når denne regel er opfyldt, tjekkes næste regel.
                    # dette fortsætter indtil alle regler er opfyldt
            if all([rule.is_valid(update) for rule in self.rules]):
                sorted = True
        return update

    def opgave2(self):
        result = 0
        incorrect_updates = self._get_incorrect()
        for update in incorrect_updates:
            ordered_update = self._order_update(update)
            result += int(ordered_update[int(len(ordered_update)/2)])
        return result

if __name__ == "__main__":
    # TEST
    test1 = Solver(True).opgave1()
    print(f"TEST 1: {test1}")
    
    test2 = Solver(True).opgave2()
    print(f"TEST 2: {test2}")

    # SVAR
    svar1 = Solver().opgave1()
    print(f"OPGAVE 1: {svar1}")
    
    svar2 = Solver().opgave2()
    print(f"OPGAVE 2: {svar2}")


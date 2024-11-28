"""
Advent of Code besvarelser 2022 dag 11

måtte søge hjælp til at implementere lowest common denominator
"""
import re

VERBOSE = False

class Monkey:
    lcm = 1 #sætter en lowest common denominator for alle Monkey-objekter
    def __init__(
            self,
            monkey_num: int,
            monkey_dict,
            items: list[int],
            operation: str,
            test: int,
            test_true: int,
            test_false: int,
            ) -> None:
        self.monkey_num = monkey_num
        self.monkeys = monkey_dict
        self.items = items
        self.operation = operation
        self.test = test
        Monkey.lcm *= self.test #opdaterer lovest common denominator
        self.test_true = test_true
        self.test_false = test_false
        self.inspected_items = 0
        self.worry_divider = 3 #bliver 1 i opgave 2
    
    def __str__(self):
        return f"Monkey {self.monkey_num}\n\tItems: {self.items}\n\tOperation: {self.operation}\n\tTest: {self.test}\n\t\tIf true: {self.test_true} | If false: {self.test_false}"
        
    def recieve_item(self, item: int):
        # print(f"####> Monkey {self.monkey_num} recieved item {item}")
        self.items.append(item)
    
    def pass_on(self, item: int, other: int):
        # self.items.pop(item)
        self.monkeys[other].recieve_item(item)
    
    def _operation(self, item: int) -> int:
        operation_elems = self.operation.split(" ")
        if operation_elems[1] == "*" and operation_elems[2] == "old":
            return item * item
        elif operation_elems[1] == "*" and operation_elems[2].isdigit():
            return item * int(operation_elems[2])
        elif operation_elems[1] == "+":
            return item + int(operation_elems[2])
        else:
            print(f"unknown operation = {operation_elems}")
    
    def _test(self, item: int) -> bool:
        return True if item % self.test == 0 else False
    
    def inspect_items(self):
        inspection_list = self.items.copy()
        if VERBOSE: print(f"Monkey {self.monkey_num} :\n\tItems= {inspection_list}")
        for item in inspection_list:
            self.items.remove(item)
            if VERBOSE: print(f"\tCurrent item level = {item}")
            worry_level = self._operation(item)
            if VERBOSE: print(f"\tAfter operation = {worry_level}")
            worry_level //= self.worry_divider # Worry level drops after inspection
            if VERBOSE: print(f"\tAfter drop = {worry_level}")
            worry_level %= Monkey.lcm
            if VERBOSE: print(f"\tAfter reduction = {worry_level}")
            if self._test(worry_level):
                self.pass_on(worry_level, self.test_true)
                if VERBOSE: print(f"\t\tTest succesfull - item sent to monkey {self.test_true}")
            else:
                self.pass_on(worry_level, self.test_false)
                if VERBOSE: print(f"\t\tTest UNsuccesfull - item sent to monkey {self.test_false}")
            self.inspected_items +=1
            if VERBOSE: print(f"\t\t\tInspected_items = {self.inspected_items}")
    
    

class Solver:
    def read_data(self):
        filename = "input.txt" if self.test == False else "test_data.txt"
        data = []
        with open(filename, "r") as fin:
            self.monkeys = {}
            lines = [line.strip() for line in fin.readlines()]
            for line in lines:
                if line == "":
                    self.monkeys[current_monkey] = Monkey(current_monkey, self.monkeys, items, operation, test, test_true, test_false)
                else:
                    try:
                        current_monkey = int(re.match(r"^Monkey (\d)", line).group(1))
                    except AttributeError:
                        key, val = line.split(": ")
                        match key:
                            case "Starting items":
                                items = [int(item) for item in val.split(", ")]
                            case "Operation":
                                operation = val.split(" = ")[1]
                            case "Test":
                                test = int(val.split(" ")[2])
                            case "If true":
                                test_true = int(val.split(" ")[3])
                            case "If false":
                                test_false = int(val.split(" ")[3])
            self.monkeys[current_monkey] = Monkey(current_monkey, self.monkeys, items, operation, test, test_true, test_false)        
    
    def solve1(self):

        for _ in range(20):
            for monkey in self.monkeys.values():
                monkey.inspect_items()
        
        monkey_buisness =  {idx: monkey.inspected_items for idx, monkey in self.monkeys.items()}
        highest_values = [val for val in monkey_buisness.values()]
        highest_values.sort(reverse=True)
       
        return highest_values[0] * highest_values[1]
        
    def solve2(self):
        self.read_data()
        for monkey in self.monkeys.values():
            monkey.worry_divider = 1 # fjerner lettelsen fra opgave 1
            # m onkey.inspected_items = 0 #nulstiller tælleren fra opgave 1
            
        for round_num in range(1, 10_000+1):
            
            for monkey in self.monkeys.values():
                monkey.inspect_items()
                # print(f"{RED}{round_num} | Monkey {monkey.monkey_num} | {monkey.inspected_items}{RESET}")
                    
        monkey_buisness =  {idx: monkey.inspected_items for idx, monkey in self.monkeys.items()}
        highest_values = [val for val in monkey_buisness.values()]
        highest_values.sort(reverse=True)
        return highest_values[0] * highest_values[1]
    
    def __init__(self, testmode = False):
        self.test = testmode
        self.data = self.read_data()
        
        # print(f"svaret på opgave 1 er: {self.solve1()}")
        print(f"svaret på opgave 2 er: {self.solve2()}")
        
        

    
    
if __name__ == "__main__":
    CYAN = '\033[36m'   
    RED = '\033[31m'
    RESET = '\033[0m' # called to return to standard terminal text color

    
    
    print(f"{CYAN}{'#'*5} TESTMODE {'#'*5}")
    Solver(True) # testmode
    print(f"{RESET}\n\n{'#'*5} Final {'#'*5}")
    Solver() # Final

    
    
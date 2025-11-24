from rich import print

def load_data() -> list:
    with open("input05.txt", "r") as fin:
        return [line.rstrip() for line in fin.readlines()]

def passes_rule1(s: str) -> bool:
    vowels = list("aeiou")
    num_vowels = 0
    for char in list(s):
        if char in vowels:
            num_vowels += 1
    return num_vowels >= 3

def passes_rule2(s: str) -> bool:
    s_list=list(s)
    for i in range(len(s_list)-1):
        if s_list[i] == s_list[i+1]:
            return True
    return False

def passes_rule3(s: str) -> bool:
    patterns = ["ab", "cd", "pq", "xy"]
    s_list=list(s)
    pairs = [str(s_list[i]+s_list[i+1]) for i in range(len(s_list)-1)]
    if any([pattern in pairs for pattern in patterns]):
        return False
    else:
        return True


def solve_part1(data: list) -> int:
    nice_list = []
    for l in data:
        # print(f"[bold blue]{l}:[/bold blue]\n[italic green]Rule1: [/italic green]{passes_rule1(l)}\n[italic green]Rule2: [/italic green]{passes_rule2(l)}\n[italic green]Rule3: [/italic green]{passes_rule3(l)}")
        if all([passes_rule1(l), passes_rule2(l), passes_rule3(l)]):
            nice_list.append(l)

    return nice_list

def passes_new_rule1(s:str) -> bool:
    s = list(s)
    for i in range(len(s)):
        try:
            remaining_str = "".join(s[i+2:])
            pair = "".join(s[i] + s[i+1])
            if pair in remaining_str:
                return True
            # else:
                # print(f"{pair} not in {remaining_str}")
        except IndexError:
            pass
    return False

def passes_new_rule2(s: str) -> bool:
    s = list(s)
    for i in range(len(s)):
        try:
            if s[i] == s[i+2]:
                return True
        except IndexError:
            pass
    return False

def solve_part2(data: list) -> int:
    nice_list = []
    for l in data:
        if all([passes_new_rule1(l), passes_new_rule2(l)]):
            nice_list.append(l)

    return nice_list


if __name__ == "__main__":
    test_data = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy",]

    nice = solve_part1(load_data())
    print(f"[bold green] del 1:[/bold green] Der er {len(nice)} nice entries.")

    nice2 = solve_part2(load_data())
    print(f"[bold turqoise] del 2:[/bold turqoise] Der er {len(nice2)} nice entries.")
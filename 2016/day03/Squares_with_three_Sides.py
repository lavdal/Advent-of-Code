def main():
    # Read the file
    with open("inputdata.txt", "r") as fin:
        sets = [[int(x) for x in line.strip().split()] for line in fin.readlines()]

    ans1 = 0
    for set in sets:
        if all(
            [
                set[0] + set[1] > set[2],
                set[0] + set[2] > set[1],
                set[1] + set[2] > set[0],
            ]
        ):
            ans1 += 1
    print(ans1)


def main2():
    # Read the file
    with open("inputdata.txt", "r") as fin:
        sets = [[int(x) for x in line.strip().split()] for line in fin.readlines()]
    ans2 = 0
    ydx = 0
    new_sets = []
    while ydx < len(sets):
        for i in range(3):
            new_set = (sets[ydx][i], sets[ydx + 1][i], sets[ydx + 2][i])
            new_sets.append(new_set)
        ydx += 3

    for set in new_sets:
        if all(
            [
                set[0] + set[1] > set[2],
                set[0] + set[2] > set[1],
                set[1] + set[2] > set[0],
            ]
        ):
            ans2 += 1

    print(ans2)


if __name__ == "__main__":
    main()
    main2()

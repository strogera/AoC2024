from collections import defaultdict

with open("input.txt", "r") as inputFile:
    l1, l2 = [], []
    counts = defaultdict(int)

    for line in inputFile.readlines():
        x, y = [int(k) for k in line.split()]
        l1.append(x)
        l2.append(y)
        counts[y] += 1
    print(sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2))))
    print(sum(x*counts[x] for x in l1))




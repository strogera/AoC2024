from collections import defaultdict

with open("input.txt", "r") as inputFile:
    inp = inputFile.read().splitlines()
    computers = defaultdict(set)
    for line in inp:
        c1, c2 = line.split('-')
        computers[c1].add(c2)
        computers[c2].add(c1)

    p1 = set()
    for c1 in computers:
        if not c1.startswith('t'):
            continue
        for c2 in computers[c1]:
            if c1 not in computers[c2]:
                continue
            for c3 in computers[c2]:
                if c1 not in computers[c3] or c2 not in computers[c3]:
                    continue
                p1.add(tuple(sorted([c1, c2, c3])))

    p2 = set()
    for c in computers:
        connected = set((c, ))
        for c1 in computers[c]:
            if all(c1 in computers[x] for x in connected):
                connected.add(c1)
        p2 = connected if len(connected) > len(p2) else p2

    print(len(p1))
    print(','.join(sorted(list(p2))))
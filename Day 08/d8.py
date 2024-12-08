from itertools import permutations

with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    antennas = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] != '.']
    p1 = set()
    p2 = set()
    for (a1, a2), (b1, b2) in permutations(antennas, 2):
        if grid[a1][a2] == grid[b1][b2]:
            dx, dy = b1 - a1, b2 - a2
            x, y = a1 - dx, a2 - dy
            if x in range(len(grid)) and y in range(len(grid[x])):
                p1.add((x, y))
                p2.add((x, y))
            while (x := x - dx) in range(len(grid)) and (y := y - dy) in range(len(grid[x])):
                p2.add((x, y))
            p2.add((a1, a2))
            p2.add((b1, b2))

    print(len(p1))
    print(len(p2))


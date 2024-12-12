
def getAdjList(i, j):
    return [(i + a, j + b) for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]]

def solve(area, grid, partTwo = False):
    outside = set()
    perim = 4*len(area)
    for p in area:
        for i, j in getAdjList(*p):
            if i in range(len(grid)) and j in range(len(grid[i])) and grid[i][j] == grid[p[0]][p[1]]:
                perim -= 1
            else:
                dx, dy = i - p[0], j - p[1]
                outside.add((p, (dx, dy)))

    if not partTwo:
        return perim

    sides = set()
    for p, d in outside:
        if d == (1, 0) and ((p[0], p[1] + 1), d) in outside:
            continue
        if d == (-1, 0) and ((p[0], p[1] - 1), d) in outside:
            continue
        if d == (0, 1) and ((p[0] - 1, p[1]), d) in outside:
            continue
        if d == (0, -1) and ((p[0] + 1, p[1]), d) in outside:
            continue
        sides.add((p, d))
    return len(sides)

def getAreas(grid):
    areas = []
    visited = set()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in visited:
                continue
            stack = [(i, j)]
            area = set()
            area.add((i, j))
            while stack:
                curA, curB = stack.pop()
                if (curA, curB) in visited:
                    continue
                area.add((curA, curB))
                visited.add((curA, curB))
                for a, b in getAdjList(curA, curB):
                    if a in range(len(grid)) and b in range(len(grid[a])) and grid[a][b] == grid[i][j]:
                        stack.append((a, b))
            areas.append(area)
    return areas

with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    areas = getAreas(grid)
    print(sum(solve(a, grid)*len(a) for a in areas))
    print(sum(solve(a, grid, partTwo=True)*len(a) for a in areas))

    
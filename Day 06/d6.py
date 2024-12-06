
def rotate(direction):
    if direction == (-1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (1, 0)
    if direction == (1, 0):
        return (0, -1)
    return (-1, 0)

def part1(pos, direction, grid):
    visited = set()
    c = 0
    while pos[0] in range(len(grid)) and pos[1] in range(len(grid[pos[0]])):
        c += 1
        if (pos, direction) in visited:
            return []
        visited.add((pos, direction))
        nextPos = pos[0] + direction[0], pos[1] + direction[1]
        if nextPos[0] in range(len(grid)) and nextPos[1] in range(len(grid[pos[0]])) and grid[nextPos[0]][nextPos[1]] == '#':
            direction = rotate(direction)
        else:
            pos = nextPos
    return set(x[0] for x in visited)

with open("input.txt", "r") as inputFile:
    grid = [list(x) for x in inputFile.readlines()]
    pos = (0, 0)
    direction = (-1, 0)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                pos = (i, j)
    path = part1(pos, direction, grid)

    p2 = 0
    for npos in path:
        orig = grid[npos[0]][npos[1]]
        grid[npos[0]][npos[1]] = '#'
        if part1(pos, direction, grid) == []:
            p2 += 1
        grid[npos[0]][npos[1]] = orig
    print(len(path))
    print(p2)

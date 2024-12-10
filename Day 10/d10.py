def dfs(grid, start, part2 = False):
    stack = [start]
    visited = set()
    count = 0
    while stack:
        (i, j) = stack.pop()
        if not part2 and (i, j) in visited:
            continue
        visited.add((i, j))
        if grid[i][j] == 9:
            count += 1
            continue
        if i + 1 in range(len(grid)) and grid[i + 1][j] == grid[i][j] + 1:
            stack.append((i + 1, j))
        if i - 1 in range(len(grid)) and grid[i - 1][j] == grid[i][j] + 1:
            stack.append((i - 1, j))
        if j + 1 in range(len(grid[i])) and grid[i][j + 1] == grid[i][j] + 1:
            stack.append((i, j + 1))
        if j - 1 in range(len(grid[i])) and grid[i][j - 1] == grid[i][j] + 1:
            stack.append((i, j - 1))
    return count


with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    starts = [] 
    for i in range(len(grid)):
        grid[i] = [int(x) for x in grid[i]]
        starts += [(i, j) for j, x in enumerate(grid[i]) if x == 0]
    print(sum(dfs(grid, s) for s in starts))
    print(sum(dfs(grid, s, True) for s in starts))
    

import heapq

def findBest(grid, start, direction):
    # Dijkstra
    dist = {}
    queue = [(0, start, direction, [start])]
    heapq.heapify(queue)
    dist[start] = 0
    bestScore = 999999999
    isInBestPath = set()
    while queue:
        score, v, dire, path = heapq.heappop(queue)
        if grid[v[0]][v[1]] == 'E' and score <= bestScore:
            isInBestPath |= set(path)
            bestScore = score
            continue
        if (v, dire) in dist and score > dist[(v, dire)]:
            continue
        dist[(v, dire)] = score
        for cd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x, y = v[0] + cd[0], v[1] + cd[1]
            ns = score + (1001 if cd != dire else 1)
            if x in range(len(grid)) and y in range(len(grid[x])) and grid[x][y] != '#':
                heapq.heappush(queue, (ns, (x, y), cd, path + [(x, y)]))
    return bestScore, len(isInBestPath)


with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    start = 0, 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if grid[i][j] == 'S':
                start = (i, j)
    p1, p2 = findBest(grid, start, (0, 1))
    print(p1)
    print(p2)
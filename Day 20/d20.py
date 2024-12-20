import heapq

def findBest(grid, start, end):
    # Dijkstra
    queue = [(0, start, [start])]
    dist = {}
    dist[start] = 0
    heapq.heapify(queue)
    while queue:
        score, v, path = heapq.heappop(queue)
        if v == end:
            return path, dist
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = v[0] + dx, v[1] + dy
            if nx in range(len(grid)) and ny in range(len(grid[nx])) and grid[nx][ny] != '#':
                if (nx, ny) not in dist or score + 1 < dist[(nx, ny)]:
                    dist[(nx, ny)] = score + 1
                    heapq.heappush(queue, (score + 1, (nx, ny), path + [(nx, ny)]))
    return [], {}

def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()

    start, end = (0, 0), (0, 0)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    bestPath, distFromStart = findBest(grid, start, end)
    distFromEnd = {k: len(bestPath) - v for k, v in distFromStart.items()}

    part1 = 0
    part2 = 0
    for i, p1 in enumerate(bestPath):
        for p2 in bestPath[i + 1:]:
            curDist = manhattanDistance(p1, p2) 
            if  curDist <= 20:
                pathDist = distFromStart[p1] + distFromEnd[p2] + curDist
                if pathDist <= len(bestPath) - 100:
                    part1 += 1 if curDist == 2 else 0
                    part2 += 1

    print(part1)
    print(part2)
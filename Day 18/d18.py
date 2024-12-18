import heapq

def findBest(corrupted, start):
    # Dijkstra
    dist = {}
    queue = [(0, start)]
    heapq.heapify(queue)
    dist[start] = 0
    parent = {}
    end = (70, 70)
    steps = 0
    while queue:
        score, v = heapq.heappop(queue)
        if v == end:
            steps = score
            break
        for cd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x, y = v[0] + cd[0], v[1] + cd[1]
            if x in range(end[0] + 1) and y in range(end[1] + 1) and (x, y) not in corrupted:
                if (x, y) not in dist or score + 1 < dist[(x, y)]:
                    dist[(x, y)] = score + 1
                    parent[(x, y)] = v
                    heapq.heappush(queue, (score + 1, (x, y)))
    res = set()
    cur = end
    while cur in parent:
        res.add(cur)
        cur = parent[cur]
    return res, steps

with open("input.txt", "r") as inputFile:
    inp = [[int(x) for x in line.split(',')] for line in inputFile.read().splitlines()]
    curPath, p1 = findBest(set([(x, y) for x, y in inp[:1024]]), (0, 0))
    p2 = ''
    for i in range(1, len(inp)):
        if tuple(inp[i]) in curPath:
            corrupted = set([(x, y) for x, y in inp[:i]])
            curPath, _ = findBest(corrupted, (0, 0))
            if len(curPath) == 0:
                p2 = ','.join(str(x) for x in inp[i - 1])
                break
    print(p1)
    print(p2)
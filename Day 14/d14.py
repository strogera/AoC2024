from math import prod

lenx = 101
leny = 103

def printRobots(robots: set, sec):
    for i in range(leny):
        line = ''
        for j in range(lenx):
            line += '#' if (j, i) in robots else ' '
        print(line)
    print(sec)
    print('-----------------------------\n')

with open("input.txt", "r") as inputFile:
    inp = inputFile.read().splitlines()
    robots = []
    p2 = []
    q = [0]*4
    robotsOrig = set()
    for line in inp:
        p, v = line.split(' ')
        p = tuple(int(x) for x in p.split('=')[-1].split(','))
        v = tuple(int(x) for x in v.split('=')[-1].split(','))
        robots.append((p, v))
        robotsOrig.add((p, v))
    sec = 0
    while sec == 0 or set(robots) != robotsOrig:
        sec += 1
        for i, r in enumerate(robots):
            p, v = r
            np = ((p[0] + v[0])%lenx, (p[1] + v[1])%leny)
            robots[i] = (np, v)

        if sec == 100:
            for p, v in robots:
                if p[0] in range(lenx//2) and p[1] in range(leny//2):
                    q[0] += 1
                elif p[0] in range(lenx//2 + 1, lenx) and p[1] in range(leny//2):
                    q[1] += 1
                elif p[0] in range(lenx//2) and p[1] in range(leny//2 + 1, leny):
                    q[2] += 1
                elif p[0] in range(lenx//2 + 1, lenx) and p[1] in range(leny//2 + 1, leny):
                    q[3] += 1

        rob = set(x[0] for x in robots)

        for r in rob:
            if all([(r[0] + d, r[1]) in rob for d in range(20)]):
                #printRobots(rob, sec)
                p2.append(sec)
                break

    print(prod(q[i] for i in range(4)))
    print("Possible solutions", sorted(p2))



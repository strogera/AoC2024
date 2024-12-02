def isSafe(report):
    asc = report[0] < report[1]
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) not in range(1, 4):
            return False
        if asc and report[i] >= report[i + 1]:
            return False
        if not asc and report[i] <= report[i + 1]:
            return False
    return True


with open("input.txt", "r") as inputFile:
    data = [list(map(int, line.strip().split())) for line in inputFile.readlines()]
    p1, p2 = 0, 0
    for report in data:
        if isSafe(report):
            p1 += 1
            p2 += 1
            continue
        for i in range(len(report)):
            if isSafe(report[:i] + report[i + 1:]):
                p2 += 1
                break
    print(p1)
    print(p2)

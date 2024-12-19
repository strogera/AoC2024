memo = {}
def match(design, towelPatr):
    if len(design) == 0:
        return 1
    count = 0
    if design in memo:
        return memo[design]
    for patr in towelPatr:
        if design.startswith(patr):
            count += match(design[len(patr):], towelPatr)
    memo[design] = count
    return count

with open("input.txt", "r") as inputFile:
    towelPatr, designs = inputFile.read().split("\n\n") 
    towelPatr = towelPatr.split(', ')
    designs = designs.splitlines()
    maxlen = max(len(x) for x in towelPatr)
    p1 = 0
    p2 = 0
    for d in designs:
        res = match(d, towelPatr)
        p1 += 1 if res >= 1 else 0
        p2 += res
    print(p1)
    print(p2)

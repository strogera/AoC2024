def split(s):
    if s == '0':
        yield '1'
    elif len(s) % 2 == 0:
        yield s[:len(s)//2]
        yield str(int(s[len(s)//2:]))
    else:
        yield str(int(s)*2024)

memo = {}
def splitAll(s, i):
    if i == 0:
        return 1
    if (s, i) not in memo:
        memo[(s, i)] = sum(splitAll(x, i - 1) for x in split(s))
    return memo[(s, i)]


with open("input.txt", "r") as inputFile:
    stones = inputFile.read().strip().split()
    print(sum(splitAll(s, 25) for s in stones))
    print(sum(splitAll(s, 75) for s in stones))
from collections import defaultdict

def step(num):
    n = num*64
    num ^= n
    num %= 16777216
    n = num//32
    num ^= n
    num %= 16777216
    n = num*2048
    num ^= n
    return num%16777216


with open("input.txt", "r") as inputFile:
    inp = [int(x) for x in inputFile.read().splitlines()]
    p1 = 0
    seq = defaultdict(int)
    for num in inp:
        seen = set()
        deltas = []
        last = num%10
        for i in range(2000):
            num = step(num)
            deltas.append(num%10 - last)
            last = num%10
            deltas = deltas[-4:]
            cur = tuple(deltas)
            if cur not in seen:
                seen.add(cur)
                seq[cur] += last
        p1 += num

    print(p1)
    print(max(seq.values()))
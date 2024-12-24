with open("input.txt", "r") as inputFile:
    inp = inputFile.read().split('\n\n')
    cablesInp = inp[0].splitlines()
    gates = inp[1].splitlines()
    cables = {}
    for c in cablesInp:
        cable, value = c.split(': ')
        cables[cable] = int(value)

    operation = {
        'AND': lambda a: 1 if a[0] == a[1] == 1 else 0,
        'OR': lambda a: 0 if a[0] == a[1] == 0 else 1,
        'XOR': lambda a: 1 if a[0] != a[1] else 0
    }

    waiting = []
    for g in gates:
        gs = g.split()
        waiting.append((gs[0], gs[2], gs[1], gs[-1]))

    while waiting:
        op1, op2, op, out = waiting.pop(0)
        if op1 not in cables or op2 not in cables:
            waiting.append((op1, op2, op, out))
            continue
        cables[out] = operation[op]((cables[op1], cables[op2]))

    print(int(''.join(str(v) for k, v in sorted(cables.items()) if k[0] == 'z')[::-1], 2))
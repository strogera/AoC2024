
with open("input.txt", "r") as inputFile:
    mult = inputFile.read().strip().split('mul')
    p1 = 0
    p2 = 0
    doMode = 1
    for m in mult:
        if m[0] == '(' and ')' in m:
            mstr = m[1:m.find(')')]
            if len(mstr) <= 7 and ',' in mstr:
                x, y = mstr.split(',')
                if x.isnumeric() and y.isnumeric():
                    p1 += int(x)*int(y)
                    p2 += int(x)*int(y)*doMode

        while '()' in m:
            curstr = m[:m.find(')') + 1]
            if 'don\'t()' in curstr:
                doMode = 0
            elif 'do()' in curstr:
                doMode = 1
            m = m[len(curstr):]
    print(p1)
    print(p2)

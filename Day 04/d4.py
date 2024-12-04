from itertools import product 

def xmas(s):
    s = ''.join(s)
    return s == 'XMAS' or s == 'SAMX'

def xmasP2(w):
    s1 = w[0][0] + w[1][1] + w[2][2]
    s2 = w[0][2] + w[1][1] + w[2][0]
    return (s1 == 'MAS' or s1 == 'SAM') and (s2 == 'MAS' or s2 == 'SAM')

def getWindow(i, j, data):
    return [[data[i - 1][j - 1], '', data[i -1][j + 1]],
            ['', data[i][j], ''],
            [data[i + 1][j - 1], '', data[i + 1][j + 1]]]

with open("input.txt", "r") as inputFile:

    inp = inputFile.read().splitlines()
    for i in range(len(inp)):
        inp[i] = '###' + inp[i] + '###'
    inp = ['#'*len(inp[0])]*3 + inp + ['#'*len(inp[0])]*3

    directions = list(product([0, 1, -1], [0, 1, -1]))
    directions.remove((0, 0))

    p1 = 0
    p2 = 0
    for i in range(3, len(inp) - 3):
        for j in range(3, len(inp[i]) - 3):
            if inp[i][j] == 'X':
                for dx, dy in directions:
                    if xmas([inp[i + k*dx][j + k*dy] for k in range(4)]):
                        p1 += 1
            elif inp[i][j] == 'A' and xmasP2(getWindow(i, j, inp)):
                p2 += 1
                    
    print(p1)
    print(p2)



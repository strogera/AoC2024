
def solve(inp, part2 = False):
    result = 0
    x = 10000000000000
    for claw in inp:
        button1, button2 = [], []
        claw = claw.splitlines()
        button1.append(int(claw[0].split(',')[0].split('+')[-1]))
        button1.append(int(claw[0].split(',')[1].split('+')[-1]))
        button2.append(int(claw[1].split(',')[0].split('+')[-1]))
        button2.append(int(claw[1].split(',')[1].split('+')[-1]))
        goalx = int(claw[2].split(',')[0].split('=')[-1]) + (x if part2 else 0)
        goaly = int(claw[2].split(',')[1].split('=')[-1]) + (x if part2 else 0)
            
        aNumerator = goalx*button2[1] - goaly*button2[0]
        aDenominator = (button1[0]*button2[1] - button1[1]*button2[0])
        if aNumerator%aDenominator != 0:
            continue
        a = aNumerator//aDenominator
        bNumerator = (goaly - button1[1]*a)
        if bNumerator%button2[1] != 0:
            continue
        b = bNumerator//button2[1]
        result += a*3 + b
    return result

with open("input.txt", "r") as inputFile:
    inp = inputFile.read().split('\n\n')
    print(solve(inp))
    print(solve(inp, part2 = True))
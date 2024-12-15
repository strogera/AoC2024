
def canMove(pos, grid, instr):
    x, y = pos
    if grid[x][y] == '.':
        return True
    elif grid[x][y] == '#':
        return False
    if instr == '<':
        nx, ny = x, y - 1
        return canMove((nx, ny), grid, instr)
    elif instr == '>':
        nx, ny = x, y + 1
        return canMove((nx, ny), grid, instr)
    elif instr == '^':
        nx, ny = (x - 1, y)
        if grid[nx][ny] == '[':
            return canMove((nx, ny), grid, instr) and canMove((nx, ny + 1), grid, instr)
        elif grid[nx][ny] == ']':
            return canMove((nx, ny), grid, instr) and canMove((nx, ny - 1), grid, instr)
        elif grid[nx][ny] == '.':
            return canMove((nx, ny), grid, instr)
    elif instr == 'v':
        nx, ny = (x + 1, y)
        if grid[nx][ny] == '[':
            return canMove((nx, ny), grid, instr) and canMove((nx, ny + 1), grid, instr)
        elif grid[nx][ny] == ']':
            return canMove((nx, ny), grid, instr) and canMove((nx, ny - 1), grid, instr)
        elif grid[nx][ny] == '.':
            return canMove((nx, ny), grid, instr)
    return False

def move(pos, grid, instr):
    npos = []
    cpos = pos
    while instr == '>' and grid[cpos[0]][cpos[1]] != '#':
        npos.append(cpos)
        if grid[cpos[0]][cpos[1]]  == '.':
            for p in npos:
                grid[p[0]][p[1]] = 'O'
            grid[pos[0]][pos[1]] = '.'
            grid[pos[0]][pos[1] + 1] = '@'
            pos = pos[0], pos[1] + 1
            break
        cpos = cpos[0], cpos[1] + 1
    while  instr == '<' and grid[cpos[0]][cpos[1]] != '#':
        npos.append(cpos)
        if grid[cpos[0]][cpos[1]]  == '.':
            for p in npos:
                grid[p[0]][p[1]] = 'O'
            grid[pos[0]][pos[1]] = '.'
            grid[pos[0]][pos[1] - 1] = '@'
            pos = pos[0], pos[1] - 1
            break
        cpos = cpos[0], cpos[1] - 1
        
    while instr == '^' and grid[cpos[0]][cpos[1]] != '#':
        npos.append(cpos)
        if grid[cpos[0]][cpos[1]]  == '.':
            for p in npos:
                grid[p[0]][p[1]] = 'O'
            grid[pos[0]][pos[1]] = '.'
            grid[pos[0] - 1][pos[1]] = '@'
            pos = pos[0] - 1, pos[1] 
            break
        cpos = cpos[0] - 1, cpos[1]
    while instr == 'v' and grid[cpos[0]][cpos[1]] != '#':
        npos.append(cpos)
        if grid[cpos[0]][cpos[1]]  == '.':
            for p in npos:
                grid[p[0]][p[1]] = 'O'
            grid[pos[0]][pos[1]] = '.'
            grid[pos[0] + 1][pos[1]] = '@'
            pos = pos[0] + 1, pos[1] 
            break
        cpos = cpos[0] + 1, cpos[1]
    return pos, grid

def moveR(pos, grid, instr):
    x, y = pos
    nx, ny = 0, 0
    if grid[x][y] == '.':
        return (x, y)
    if instr == '<':
        nx, ny = (x, y - 1)
        if canMove((nx, ny), grid, instr):
            moveR((nx, ny), grid, instr)
            grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
    elif instr == '>':
        nx, ny = (x, y + 1)
        if canMove((nx, ny), grid, instr):
            moveR((nx, ny), grid, instr)
            grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
    elif instr == '^':
        nx, ny = (x - 1, y)
        if canMove((nx, ny), grid, instr):
            if grid[nx][ny] == '[':
                if canMove((nx, ny + 1), grid, instr):
                    moveR((nx, ny), grid, instr)
                    moveR((nx, ny + 1), grid, instr)
                    if grid[x][y] == '.':
                        grid[x][y + 1], grid[nx][ny + 1] = grid[nx][ny + 1], grid[x][y + 1]
                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
            elif grid[nx][ny] == ']':
                if canMove((nx, ny - 1), grid, instr):
                    moveR((nx, ny), grid, instr)
                    moveR((nx, ny - 1), grid, instr)
                    if grid[x][y] == '.':
                        grid[x][y - 1], grid[nx][ny - 1] = grid[nx][ny - 1], grid[x][y - 1]
                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
            elif grid[nx][ny] == '.':
                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
    elif instr == 'v':
        nx, ny = (x + 1, y)
        if canMove((nx, ny), grid, instr):
            if grid[nx][ny] == '[':
                if canMove((nx, ny + 1), grid, instr):
                    moveR((nx, ny), grid, instr)
                    moveR((nx, ny + 1), grid, instr)
                    if grid[x][y] == '.':
                        grid[x][y + 1], grid[nx][ny + 1] = grid[nx][ny + 1], grid[x][y + 1]
                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
            elif grid[nx][ny] == ']':
                if canMove((nx, ny - 1), grid, instr):
                    moveR((nx, ny), grid, instr)
                    moveR((nx, ny - 1), grid, instr)
                    if grid[x][y] == '.':
                        grid[x][y - 1], grid[nx][ny - 1] = grid[nx][ny - 1], grid[x][y - 1]
                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
            elif grid[nx][ny] == '.':
                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
    return (nx, ny) if grid[nx][ny] == '@' else (x, y)


with open("input.txt", "r") as inputFile:
    grid, instr = inputFile.read().split('\n\n')
    grid = [[*line] for line in grid.splitlines()]
    gridP2 = []
    for i, line in enumerate(grid):
        gridP2.append([])
        for j, c in enumerate(line):
            if c == '#':
                gridP2[-1] += ['#', '#']
            elif c == '.':
                gridP2[-1] += ['.', '.']
            elif c == 'O':
                gridP2[-1] += ['[', ']']
            elif c == '@':
                gridP2[-1] += ['@', '.']
    instr = instr.strip()
    pos = (0, 0)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == '@':
                pos = (i, j)
    for i in instr:
        pos, grid = move(pos, grid, i)

    pos = (0, 0)
    for i, line in enumerate(gridP2):
        for j, c in enumerate(line):
            if c == '@':
                pos = (i, j)

    for i in instr.strip():
        if i in '><v^':
            pos = moveR(pos, gridP2, i)

    p1 = sum(100*i + j if grid[i][j] == 'O' else 0 for i in range(len(grid)) for j in range(len(grid[i])))
    p2 = sum(100*i + j if gridP2[i][j] == '[' else 0 for i in range(len(gridP2)) for j in range(len(gridP2[i])))
    print(p1)
    print(p2)


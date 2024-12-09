
with open("input.txt", "r") as inputFile:
    data = inputFile.read().strip()
    disk = []
    for i in range(len(data)):
        id = i//2 
        for _ in range(int(data[i])):
            disk.append(str(id) if i%2 == 0 else '.')
    diskOrig = [x for x in disk]
    i = 0
    k = len(disk) - 1
    while k > i:
        if disk[k] == '.':
            k -= 1
            continue
        if disk[i] == '.':
            (disk[i], disk[k]) = (disk[k], disk[i])
            k -= 1
        i += 1

    files = []
    freeSpaces = []
    i = 0
    while i < len(diskOrig):
        if diskOrig[i] == '.':
            s = i
            while i < len(diskOrig) and diskOrig[i] == '.':
                i += 1
            freeSpaces.append(['.', s, i - s])
        else:
            s = i
            id = diskOrig[s]
            while i < len(diskOrig) and diskOrig[i] == id:
                i += 1
            files.append([id, s, i - s])
    for file in files[::-1]:
        i = 0
        while freeSpaces[i][1] < file[1]:
            space = freeSpaces[i]
            if file[2] <= space[2]:
                file[1] = space[1]
                space[1] = space[1] + file[2]
                space[2] = space[2] - file[2]
                break
            i += 1
    p2 = 0
    for file in files:
        for i in range(file[1], file[1] + file[2]):
            p2 += i*int(file[0])
    print(sum(i*int(x)  if x != '.' else 0 for i, x in enumerate(disk)))
    print(p2)
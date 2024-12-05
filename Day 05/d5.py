from collections import defaultdict

def isOrdered(nums, rules):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] not in rules[nums[i]]:
                return False
    return True

with open("input.txt", "r") as inputFile:
    d1,d2 = inputFile.read().split('\n\n')
    rules = defaultdict(list)
    for line in d1.splitlines():
        x, y = line.split('|')
        rules[x].append(y)
    p1 = 0
    p2 = 0
    for line in d2.splitlines():
        nums =  line.split(',')
        if isOrdered(nums, rules):
            p1 += int(nums[len(nums)//2])
        else:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] in rules[nums[j]] :
                        nums[i], nums[j] = nums[j], nums[i]
            p2 += int(nums[len(nums)//2])
            

    print(p1)
    print(p2)

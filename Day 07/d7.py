cacheP2 = set()

def hashable(x):
    return ''.join(map(str, x))

def solve(res, nums, part2):
    if len(nums) == 1:
        return res == nums[0]
    if (res, hashable(nums)) in cacheP2:
        return True
    addition = solve(res - nums[0], nums[1:], part2) if res - nums[0] > 0 else False
    multiplication = solve (res//nums[0], nums[1:], part2) if res%nums[0] == 0 else False
    concatination = False
    if str(res).endswith(str(nums[0])):
        res2 = ''.join(str(res).rsplit(str(nums[0]), 1)) #remove nums[0] from end of res
        concatination = solve(int(res2), nums[1:], part2) if res2 != '' else False
    if addition or multiplication or concatination:
        cacheP2.add((res, hashable(nums)))
    return addition or multiplication or (concatination and part2)

with open("input.txt", "r") as inputFile:
    p1 = 0
    p2 = 0
    for line in inputFile.readlines():
        res,rest = line.split(':')
        nums = rest.strip().split(' ')
        nums = [int(x) for x in nums][::-1]
        res = int(res)
        p1 += res if solve(res, nums, part2 = False) else 0
        p2 += res if solve(res, nums, part2 = True) else 0
    print(p1)
    print(p2)


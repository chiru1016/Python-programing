nums= [2,3,4,6,7,9]
target = 7
seen = {}
for i in range(len(nums)):
    need = target - nums[i]
    if need in seen:
        print([seen[need], i])
    seen[nums[i]] = i
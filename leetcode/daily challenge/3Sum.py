nums = [0,1,1]

nums.sort()
o = []
for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:
        continue

    l, r = i + 1, len(nums) - 1
    while l < r:
        temp = nums[l] + nums[r]
        if temp < a:
            l += 1
        elif temp > a:
            r -= 1
        else:
            o.append([a, nums[l], nums[r]])
            l += 1
            while nums[l-1] == nums[l] and l < r:
                l += 1
print(o)

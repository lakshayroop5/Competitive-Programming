nums = [2, 1, 1, 2]
i = len(nums) - 3
while i > -1:
    c1, c2 = 0, 0
    if i + 3 <= len(nums) - 1:
        c1 = nums[i] + nums[i + 3]
    if i + 2 <= len(nums) - 1:
        c2 = nums[i] + nums[i + 2]
    nums[i] = max(c1, c2)
    i -= 1
print(nums)
print(max(nums))

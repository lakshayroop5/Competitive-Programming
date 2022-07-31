nums = [2,7,11,15]
target = 9

# CODE
while len(nums) > 0:
    i = nums.pop()
    # print(i)
    temp = target - i
    # print(temp)
    if nums.__contains__(temp):
        print([nums.index(temp), len(nums)])
        break
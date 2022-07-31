nums = [10,4,-8,7]

#CODE
c = 0
s = sum(nums)
l = 0
r = 0
for i in range(len(nums)-1):
    l += nums[i]
    r = s - l
    if l >= r:
        c += 1

print(c)
nums = [10,1,2,3,4,5,11,1,2,3]

# CODE
i, j, c, l, r = 0, 1, 0, nums[0], 0
n = len(nums)
o = []
f = 0
while j < n:
    print(r, j)
    print(l)
    if l > nums[j] > nums[r]:
        c += 1
        j += 1
        r += 1
        f = 1
    elif nums[r] > nums[j] and l > nums[j]:
        c += 1
        o.append(c)
        r += 1
        j += 1
        c = 0
    elif nums[r] > nums[j] >= l:
        l = nums[j]
        o.append(c)
        r += 1
        j += 1
        c = 0
    elif nums[r] <= nums[j] and nums[j] >= l:


if f:
    o.append(c)
print(max(o))
    # if nums[r] >= nums[j] >= l:
    #     i = j
    #     r = j
    #     j += 1
    #     l = nums[i]
    #     o.append(c)
    #     c = 0
    #     f = 0
    # elif nums[r] >= nums[j] and l > nums[j] :
    #     i = j
    #     r = j
    #     j += 1
    #     c += 1
    #     l = nums[i]
    #     o.append(c)
    #     c = 0
    #     f = 0
    # else:
    #     r += 1
    #     j += 1
    #     c += 1
    #     f = 1

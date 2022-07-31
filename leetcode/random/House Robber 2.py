nums = [1, 2, 3, 1]
if len(nums) < 4:
     print(max(nums))
else:
    numst = nums[0:len(nums)-1]
    res1 = 0
    res2 = 0
    for i in range(2, len(numst)):
        if i - 2 >= 0:
            numst[i] = max(numst[i-1], numst[i]+numst[i-2])
    res1 = numst[-1]
    numst = nums[1:]
    for i in range(2, len(numst)):
        if i - 2 >= 0:
            numst[i] = max(numst[i - 1], numst[i] + numst[i - 2])
    res2 = numst[-1]
    print(max(res1, res2))

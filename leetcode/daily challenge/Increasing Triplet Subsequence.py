nums = [1,2,2,2,3,2,2]
if len(nums) < 3:
    print(False)
else:
    f = 1
    if nums[-2] == nums[-1]:
        k = -3
        f = 0
        while k > len(nums)-2:
            if nums[k] != nums[-1]:
                l, u = min(nums[-1], nums[k]), max(nums[-1], nums[k])
                f = 1
                break
            k -= 1
    else:
        l, u = min(nums[-1], nums[-2]), max(nums[-1], nums[-2])
    if not f:
        print(False)
    else:
        for i in nums[-3::-1]:
            print(l, u)
            if i < l:
                print(True)
                f = 0
                break
            else:
                if i > u:
                    u = i
                elif i != u:
                    l = i
        if f:
            print(False)
# c = 0
# x = nums[-3]
# for i in range(-2, 0, 1):
#     if x < nums[i]:
#         c += 1
#
# if c == 2:
#     print(True)
# elif c == 1:
#     for i in range(-3, 0-len(nums)-1, -1):
#         if x > nums[i]:
#             print(True)
#             break
# else:
#     ind = 0
#     for i in range(-3, 0-len(nums)-1, -1):
#         if x < nums[i]:
#             ind = i
#     if ind != 0:
#         for i in range(ind - 1, 0-len(nums)-1, -1):
#             if x > nums[i]:
#                 print(True)
#                 break
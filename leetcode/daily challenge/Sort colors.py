nums = [0, 0, 2, 2, 1, 2, 1]

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


l, r = 0, len(nums) - 1
# while nums[r] == 2:
#     r -= 1
i = 0
while i <= r:
    print(i, l, r)
    if nums[i] == 0:
        swap(i, l, nums)
        l += 1
    elif nums[i] == 2:
        swap(i, r, nums)
        r -= 1
        i -= 1
    i += 1
print(nums)
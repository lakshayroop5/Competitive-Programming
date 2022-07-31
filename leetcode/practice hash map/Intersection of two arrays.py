nums1 = [1,2,2,3,4]
nums2 = [2,2,2,4]

# CODE
numsA = set(nums1)
numsB = set(nums2)
numsO = numsA.intersection(numsB)
print(numsO)

# CODE USING HASH MAP
# d = {}
# for i in nums1:
#     if d.get(i) is None:
#         temp = {i: 1}
#         d.update(temp)
#
# # print(d)
# output = []
# for i in nums2:
#     if d.get(i) is not None:
#         output.append(i)
#         d.__delitem__(i)
# print(d)
# print(output)


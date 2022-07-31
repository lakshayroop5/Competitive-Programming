import heapq

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
k = int(input())

t1 = []
t2 = []
if k >= len(nums1):
    t1 = nums1.copy()
else:
    for i in range(k):
        t1.append(nums1[i])

if k >= len(nums2):
    t2 = nums2.copy()
else:
    for i in range(k):
        t2.append(nums2[i])

o = []
for i in t1:
    for j in t2:
        temp = [i, j]
        o.append(temp)

if k >= len(o):
    print(o)
else:
    tempo = []
    for i in o:
        tempo.append(i[0]+i[1])
    t = heapq.nsmallest(k, tempo)
    f = []
    n = nums1[-1] + nums2[-1] + 1
    for i in t:
        index = tempo.index(i)
        f.append(o[index])
        tempo[index] = n
    print(f)

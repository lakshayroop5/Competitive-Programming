import heapq
nums = list(map(int, input().split()))
k = int(input())
c = []
o = []

for i in nums:
    if not c.__contains__(i):
        temp = [nums.count(i), i]
        o.append(temp)
        c.append(i)

heapq.heapify(o)
f = heapq.nlargest(k, o)
fo = []
for i in f:
    fo.append(i[1])
print(fo)
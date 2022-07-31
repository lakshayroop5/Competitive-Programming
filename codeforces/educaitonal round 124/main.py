import heapq
a = [1,2,3]
l = heapq.nlargest(1,a)
a.remove(l[0])
print(l)
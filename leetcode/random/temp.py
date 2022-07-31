import heapq

l = [[1,5], [2,2], [3,1]]
heapq.heapify(l)
print(heapq.nlargest(1, l))
print(list(l))

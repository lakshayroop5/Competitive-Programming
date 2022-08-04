from collections import deque
n = 6
k = 5
q = deque([i for i in range(1, n+1)])
# q0 = deque([0,0])
c = 0


while len(q) > 1:
        temp = q.popleft()
        c += 1
        if c < k:
            q.append(temp)
        else:
            c = 0
        print(q)
print(q.pop())
# while len(q0) > 1:
#     q0.clear()
#     while len(q) > 0:
#         temp = q.popleft()
#         q0.append(temp)
#         c += 1
#         if c >= k:
#             q0.pop()
#             c = 0
#     q = q0.copy()

# print(q0.pop())

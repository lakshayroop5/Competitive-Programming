from collections import deque
n = int(input())

if n < 2:
    q = [1] * (n+1)
else:
    q = deque([1, 1])
    while len(q) < n + 1:
        q.append(q[0] + q[1])
        q.popleft()
        while q[0] != 1:
            q.append(q[0] + q[1])
            q.popleft()
        q.append(1)
print(list(q))


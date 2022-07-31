times = [[1,2,1],[2,3,2],[1,3,4]]
n = 3
k = 1

#CODE
visited = [0]*n
d  = {}
for i in times:
    if d.get(i[0]) is None:
        d.update({i[0]: {i[1]: i[2]}})
    else:
        d[i[0]].update({i[1]: i[2]})

stack = [k]
sum_ = 0
t = 0
while len(stack) != 0:
    t = stack[-1]
    if visited[t-1] == 1:
        stack.pop()
    else:
        visited[t-1] = 1
        print(visited)
        if not visited.__contains__(0):
            continue
        stack.pop()
        if d.get(t) is not None:
            stack.extend(list(d[t].keys()))
            sum_ += max(d[t].values())
if visited.__contains__(0):
    print(-1)
else:
    print(sum_)



cost = [1,100,1,1,1,100,1,1,100,1]
cost.append(0)
i = len(cost) - 2
while i > -1:
    c1, c2 = sum(cost), sum(cost)
    if i + 1 <= len(cost) - 1:
        c1 = cost[i] + cost[i+1]
    if i + 2 <= len(cost) - 1:
        c2 = cost[i] + cost[i+2]

    cost[i] = min(c1, c2)
    i -= 1

print(min(cost[0], cost[1]))


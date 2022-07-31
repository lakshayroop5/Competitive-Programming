intervals = [[1,4],[0,2],[3,5]]
intervals.sort()
o = [intervals[0]]

for i in range(1, len(intervals)):
    o.append(intervals[i])

    if o[-1][0] <= o[-2][1] <= o[-1][1]:
        temp = [o[-2][0], o[-1][1]]
        o.pop()
        o.pop()
        o.append(temp)

    elif o[-1][0] <= o[-2][1] and o[-1][1] <= o[-2][1]:
        temp = [o[-2][0], o[-2][1]]
        o.pop()
        o.pop()
        o.append(temp)

print(o)

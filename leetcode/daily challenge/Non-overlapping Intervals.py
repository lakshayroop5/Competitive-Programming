intervals = [[1,2],[1,3], [1,4]]

if len(intervals) < 2:
    print(0)
else:
    intervals.sort()
    i, c = 2, 0
    check = [intervals[0], intervals[1]]
    while i < len(intervals) + 1:
        print(check)
        if check[-1][0] < check[-2][1] < check[-1][1]:
            c += 1
            check.pop()
            # print(check)
        elif check[-2][1] > check[-1][0] and check[-2][1] >= check[-1][1]:
            check.pop(-2)
            c += 1
        if i < len(intervals):
            check.append(intervals[i])
        i += 1
    print(check)
    print(c)

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    l = []
    lc = []
    x, y = 0, 0
    t = {a[x]: 1}
    while y < n - 1:
        y += 1
        # print(t)
        if t.get(a[y]) is None:
            t.update({a[y]: 1})
        else:
            l.append(y - x)
            lc.append([x, y])
            temp = x
            x = a[x:y].index(a[y]) + 1 + x
            for i in a[temp:x-1]:
                t.pop(i)

    l.append(y - x + 1)
    lc.append([x, y + 1])
    # print(l, lc)

    mind = lc[l.index(max(l))]
    left = mind[0]
    right = n - mind[1]

    b = min(left, right)
    c = max((left, right))

    print(c + 2*b)

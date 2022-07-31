T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in a:
        if d.get(i) is None:
            d.update({i: 1})
        else:
            d[i] += 1
    v = list(d.values())
    if v.__contains__(1):
        print(-1)
    else:
        i = 1
        o = []
        while i < n + 1:
            for j in v:
                temp = i
                i += 1
                for k in range(j-1):
                    o.append(i)
                    i += 1
                o.append(temp)
        for i in o:
            print(i, end=' ')
        print()

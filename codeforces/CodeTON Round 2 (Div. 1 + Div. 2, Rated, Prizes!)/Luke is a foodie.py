T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}
    for i in a:
        if d.get(i) is None:
            d[i] = [i - x, i + x]
    c = 0
    v = []
    for i in a:
        v.append(d[i])
    # print(v)


    def ex(l: list) -> set:
        return set(i for i in range(l[0], l[1] + 1))


    t = ex(v[0])
    for i in v:
        temp = ex(i)
        t = t.intersection(temp)
        # print(t)
        if len(t) == 0:
            t = temp
            c += 1
            # print(t, 't')
            # print(c)


    print(c)

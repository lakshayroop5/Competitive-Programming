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
    for i in range(len(v)):
        if v[i] > 2:
            if v[i] & 1:
                v[i] = 1
            else:
                v[i] = 2
    # print(d)
    s = sum(v)
    c = v.count(2)
    if c & 1:
        s -= c + 1
    else:
        s -= c


    print(s)

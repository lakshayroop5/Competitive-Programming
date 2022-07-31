T = int(input())

for K in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    r = l+k
    d = {}
    while r < n:
        temp = tuple(a[l:r])
        if d.get(temp) is None:
            d.update({temp: 1})
        else:
            d[temp] += 1

    keys = list(d.keys())
    val = list(d.values())
    f = val.index(max(val))
    target = keys[f]

T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = {}
    r = {}
    for i in range(n):
        if d.get(b[i] // a[i]) is None:
            d.update({b[i] // a[i]: {a[i]: b[i] % a[i]}})
        else:
            d[b[i] // a[i]].update({a[i]: b[i] % a[i]})

    c = min(d.keys())
    while x > 0:
        m = min(d.keys())
        diff = sum(d[m].keys()) - sum(d[m].values())
        if diff > x:
            break
        x -= diff
        c += 1
        if d.get(m+1) is None:
            d.update({m+1: d[m]})
            d.pop(m)
        else:
            d[m+1].update(d[m])
            d.pop(m)

    print(c)

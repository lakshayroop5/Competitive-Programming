T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = {}
    for i in range(n):
        t = a[i] ^ b[i]
        if d.get(t) is None:
            d.update({t: 1})
        else:
            d[t] += 1

    v = list(d.values())
    s = 0
    for i in v:
        s += (((i)*(i-1))//2)
    print(s)
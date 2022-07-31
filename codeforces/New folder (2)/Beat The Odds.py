T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    e, o = 0, 0
    for i in a:
        if i & 1:
            o += 1
        else:
            e += 1

    m = min(e, o)
    print(m)

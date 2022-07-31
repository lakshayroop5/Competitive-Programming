T = int(input())

for _ in range(T):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    o = [f[0] - s[0]]

    for i in range(1, n):
        if s[i] < f[i-1]:
            s[i] = f[i-1]
        o.append(f[i] - s[i])

    for i in o:
        print(i, end=' ')
    print()

T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    s = []
    m = []
    for i in range(n):
        temp = 0
        m.append(a[i] * (n - 1))
        for j in range(n):
            if j != i:
                temp += a[j]
        s.append(temp)
    # print(s, m)
    f = 0
    for i in range(n):
        if s[i] == m[i]:
            f = 1

    if f:
        print('YES')
    else:
        print('NO')


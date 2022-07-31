T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    i, j, m = 0,0,0
    f = 0
    s = a[0]
    for k in range(1, n):
        if f == 0:
            temp = s
            s += a[k]
            if temp > s:
                i = k
                f = 1
                s = temp
            if i == n - 1:
                i = n - 3
                j = n - 2
                m = n - 1
                s = sum(a[:j])
                break
        elif f == 1:
            temp = s
            s -= a[k]
            if temp > s:
                j = k
                f = 2
                s = temp
            print(s, 's')
        elif f == 2:
            temp = s
            s -= a[k]
            if temp > s:
                m = k
                f = 3
                s = temp
        else:
            s += a[k]
    if i == n - 1:
        i = n - 3
        j = n - 2
        m = n - 1
    print(i,j,m)
    print(s)
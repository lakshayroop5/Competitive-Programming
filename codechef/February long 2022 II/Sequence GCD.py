T = int(input())

for K in range(T):
    x = list(map(int, input().split()))
    n = x[0]
    m = x[1]
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    f = 0
    l = 0
    for i in range(n):
        s += a[i]
        if s >= m:
            l = i
            break

    p = a[l]

    while p > 0:
        # print(p, 'p')
        s = 0
        if l > 0 and p > a[l-1]:
            s = sum(a[:l])
        elif l > 0 and p <= a[l-1]:
            l -= 1
            s = sum(a[:l])
        for i in range(l, n):
            if s > m:
                break
            s += a[i] % p
        if s == m:
            print(p)
            f = 1
            # print(s, 's')
            break
        elif s < m and (m - s) % p == 0:
            print(p)
            f = 1
            # print(s, 's')
            break
        # print(s, 's')
        p -= 1

    if f == 0:
        print(1)

    # if a[0] == a[n-1]:
    #     pass
    # else:
    #     while l >= 0:
    #         s = 0
    #         for r in range(n):
    #             s += a[r] % a[l]
    #
    #         if s == m:
    #             print(a[l])
    #             break
    #         elif s < m and m - s % a[l] == 0:
    #             i = a.index(m-s)
    #             a[i] = 0






T = int(input())

for _ in range(T):
    n = int(input())

    if n == 1:
        print(1)
        print(1)
    elif n & 1:
        print(-1)
    else:
        i = 0
        p = 0
        while p < n:
            p = pow(2, i)
            i += 1
        p -= 1

        print(p)
        a = []
        b = []
        for i in range(n):
            a.append(n - i)

        for i in a:
            if i & p == 0:
                b.append(p)
            elif not b.__contains__(i):
                t = i ^ p
                if t > n:
                    t = p - t - 1
                b.append(t)
            elif b.__contains__(i):
                b.append(a[b.index(i)])

        for i in a:
            print(i, end=' ')
        print()
        for i in b:
            print(i, end=' ')
        print()

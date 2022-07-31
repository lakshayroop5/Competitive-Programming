T = int(input())

for K in range(T):
    p = list(map(int, input().split()))
    n = p[0]
    k = p[1]

    if k > n:
        print(-1)
    else:
        o = [i for i in range(1, n + 1)]
        if n > 1 and k == 1:
            print(-1)
        elif n == k:
            for i in o:
                print(i, end=" ")
            print("\n", end="")
        else:
            o.remove(k)
            o.append(k)
            for i in o:
                print(i, end=" ")
            print("\n", end="")

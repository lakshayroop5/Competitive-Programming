T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    s = sum(b)
    if s < n:
        print(a[s])
    else:
        while s >= n:
            # print(s)
            s -= n
        print(a[s])

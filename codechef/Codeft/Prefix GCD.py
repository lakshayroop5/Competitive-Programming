T = int(input())

for K in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    f = 0
    for i in range(1, n):
        # print(f, 'f')
        # print(i, 'i')
        # print(p[i], 'p')
        if p[i] > p[i-1]:
            f = 1
            break
        else:
            if p[i-1] % p[i] != 0:
                # print(p[i-1] % p[i] )
                f = 1
                break
    if f == 0:
        print('YES')
    elif f == 1:
        print("NO")

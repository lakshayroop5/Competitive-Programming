T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c, j, i = 0, 0, 0
    for i in range(n):
        # print(i, 'i')
        if a[i] == i + j + 1:
            c += 1
            j += 1
    print(c)

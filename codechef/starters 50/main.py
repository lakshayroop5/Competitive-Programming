T = int(input())

for _ in range(T):
    n = int(input())

    print(n, end=' ')
    for i in range(1, n):
        print(i, end=' ')
    # print(n - 1, end='')
    print()
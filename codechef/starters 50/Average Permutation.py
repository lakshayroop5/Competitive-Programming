T = int(input())

for _ in range(T):
    n = int(input())
    if n == 3:
        print(3, 2, 1)
        continue
    print(n, n-2, end=' ')
    for i in range(1, n-2):
        if i == n-1:
            continue
        print(i, end=' ')
    print(n - 1, end='')
    print()
T = int(input())

for K in range(T):
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    if n == 1 and m == 1:
        print(0)
    elif (n == 1 or m == 1) and (n == 2 or m == 2):
        print(1)
    elif (n == 1 or m == 1) and (n > 2 or m > 2):
        print(-1)
    elif (n == 2) and (m >= 2):
        if m % 2 == 0:
            print(2 * m - 2)
        else:
            print(2 * m - 3)
    elif (m == 2) and (n >= 2):
        if n % 2 == 0:
            print(2 * n - 2)
        else:
            print(2 * n - 3)
    else:
        z = min(n, m)
        a = max(n, m) - z
        b = 2
        if a % 2 == 0:
            print(2 * (z - 1) + 2 * a )
        else:
            print(2 * (z - 1) + 2 * a - 1)

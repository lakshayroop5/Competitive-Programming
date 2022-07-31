T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    m, n = a % 3, b % 3

    if m == 0 or n == 0:
        print(0)
    elif m == n:
        print(1)
    else:
        print(2)

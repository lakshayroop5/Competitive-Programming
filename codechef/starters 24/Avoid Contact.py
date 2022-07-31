T = int(input())

for K in range(T):
    a = list(map(int, input().split()))
    x = a[0]
    y = a[1]
    if x == y:
        print(2*x - 1)
    else:
        t = x - y
        n = 2*y + t
        print(n)
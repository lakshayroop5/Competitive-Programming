T = int(input())

for K in range(T):
    x = int(input())
    n = x - 1

    if n == 0:
        print(0)
    elif n == 1 or n == 2 or n == 3:
        print(1)
    elif n == 4 or n == 5:
        print(2)
    else:
        n += 1
        o = 2 * (n // 5)
        t = n % 5
        if t == 2 or t == 3 or t == 4:
            o += 1
        print(o)

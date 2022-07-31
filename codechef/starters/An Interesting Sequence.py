T = int(input())

for K in range(T):
    n = int(input())
    c = 0
    if n % 2 != 0:
        print(0)
    else:
        while n != 1:
            if n % 2 != 0:
                break
            else:
                n = n // 2
                c += 1
        print(c)

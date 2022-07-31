import math

T = int(input())

for _ in range(T):
    n = int(input())

    c = 2
    for i in range(2, math.floor(n ** 0.5) + 1):
        if n % i == 0 and n == i * i:
            c += 2
        elif n % i == 0:
            c += 4

    if not n & 1:
        c -= 1
    if n == 2:
        c = 1

    print(c)
import math

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    c1, c0 = 0, 0
    for i in s:
        if i == '0':
            c0 += 1
        else:
            c1 += 1
    diff = c1 - c0
    if diff < 0:
        diff *= -1

    print(math.ceil(diff / k))

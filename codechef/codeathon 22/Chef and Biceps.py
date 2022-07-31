import math

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    if a > b :
        print(-1)
    elif a == b:
        print(1)
    else:
        u = c // 2
        diff = b - a + 1
        print(math.ceil(diff / u))

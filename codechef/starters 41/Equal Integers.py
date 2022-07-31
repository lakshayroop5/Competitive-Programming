T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    if x == y:
        print(0)
    elif y > x:
        print(y - x)
    else:
        d = x - y
        if d & 1:
            m = x + 1
            print(((m - y) // 2) + 1)
        else:
            print((x - y) // 2)

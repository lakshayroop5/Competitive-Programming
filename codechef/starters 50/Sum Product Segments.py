T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    l1 = x // 2
    r1 = x - l1
    l2 = r1 + 1
    r2 = y / l2
    # print(l2, r2)
    if r2 < l2:
        print(-1)
        continue
    while r2 >= l2 and r2 != y // l2:
        l2 += 1
        r2 = y / l2

    print(l1, r1)
    print(l2, int(r2))
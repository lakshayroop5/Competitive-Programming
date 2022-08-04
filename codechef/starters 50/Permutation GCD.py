T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    if n > x:
        print(-1)
        continue
    output = []
    t = x - n + 1
    # print(t)
    while t > n:
        output.append(n)
        # print(output)
        x -= n
        n -= 1
        t = x - n + 1
    output.append(t)
    for i in range(1, n+1):
        if i != t:
            output.append(i)
    # output.append(t)
    for i in output:
        print(i, end=' ')
    print()

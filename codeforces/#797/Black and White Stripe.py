T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    l = 0
    r = l + k
    c = [s[l:r].count('W')]
    t = c[0]
    f = 1
    while r < n:
        # print(s[l], s[r])
        if t == 0:
            print(0)
            f = 0
            break
        if s[l] == 'W':
            t -= 1
        if s[r] == 'W':
            t += 1
        l += 1
        r += 1
        c.append(t)

    c.append(t)

    if f:
        print(min(c))


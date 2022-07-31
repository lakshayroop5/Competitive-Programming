T = int(input())

for _ in range(T):
    n = int(input())
    s = input()

    l, r = 0, 1
    c = 1
    while r < n:
        if s[r] != s[l]:
            c += 1

        r += 1
        l += 1

    print(c)

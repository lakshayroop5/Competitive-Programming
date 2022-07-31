T = int(input())

for _ in range(T):
    n = int(input())
    s = input()

    r = 0
    l = 0
    for i in range(n):
        if i < n // 2:
            if s[i] == ')':
                l += 1
        else:
            if s[i] == '(':
                r += 1

    print(l + r)
    
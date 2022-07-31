T = int(input())

for K in range(T):
    n = int(input())
    o = [0] * n

    for i in range(n):
        if i % 2 == 0:
            o[i] = i + 2
        else:
            o[i] = i

    if n % 2 != 0:
        o.remove(n + 1)
        o.append(n)

    s = 0
    for i in range(n):
        s = s + (o[i] ^ (i + 1))

    print(s)

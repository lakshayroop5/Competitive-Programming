T = int(input())

for _ in range(T):
    n = int(input())
    q = n // 3
    r = n % 3
    o = [q, q, q]
    if r == 2:
        o[0] += 1
        o[1] += 2
        o[2] -= 1
    elif r == 1:
        o[1] += 2
        o[2] -= 1
    elif r == 0:
        o[1] += 1
        o[2] -= 1

    for i in o:
        print(i, end=' ')
    print()
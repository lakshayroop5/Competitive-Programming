T = int(input())

for _ in range(T):
    n = int(input())

    o = []
    for i in range(n):
        if i == 0:
            o.append(n)
        else:
            o.append(i)

    for i in o:
        print(i, end=' ')
    print()

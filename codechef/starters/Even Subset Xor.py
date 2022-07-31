T = int(input())

for K in range(T):
    n = int(input())
    o = []
    i = 3
    while len(o) != n:
        temp = format(i, 'b')
        if temp.count('1') % 2 == 0:
            o.append(i)
            i += 1
        else:
            i += 1

    for i in range(n):
        print(o[i], end=" ")
    print('\n', end="")


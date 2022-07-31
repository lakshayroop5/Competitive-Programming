T = int(input())

for K in range(T):
    n = int(input())
    s = input()
    l, r = 0, 0
    o = []
    for i in range(n):
        if s[i] == 'W':
            o.append(s[l:i])
            l = i + 1
    o.append(s[l:n])

    f = 0
    for i in o:
        if len(i) == 0:
            continue
        else:
            if i.__contains__('B') and i.__contains__('R'):
                continue
            else:
                print('NO')
                f = 1
                break
    if f == 0:
        print('YES')



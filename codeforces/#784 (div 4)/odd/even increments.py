T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    f = 0
    c1, c2 = 'x', 'x'
    if a[0] % 2 != 0:
        c1 = 'o'
    else:
        c1 = 'e'
    if a[1] % 2 != 0:
        c2 = 'o'
    else:
        c2 = 'e'

    if c1 == 'e' and c2 == 'e':
        for i in range(n):
            if a[i]%2 !=0:
                print('NO')
                f = 1
                break

    elif c1 == 'o' and c2 == 'o':
        for i in range(n):
            if a[i]%2 ==0:
                print('NO')
                f = 1
                break

    elif c1 == 'e' and c2 == 'o':
        for i in range(n):
            if i % 2 == 0:
                if a[i] % 2 != 0:
                    print('NO')
                    f = 1
                    break
            else:
                if a[i] % 2 == 0:
                    print('NO')
                    f = 1
                    break

    elif c1 == 'o' and c2 == 'e':
            for i in range(n):
                if i % 2 == 0:
                    if a[i] % 2 == 0:
                        print('NO')
                        f = 1
                        break
                else:
                    if a[i] % 2 != 0:
                        print('NO')
                        f = 1
                        break
    if f == 0:
        print('YES')

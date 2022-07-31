T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    def win(a, b):
        amax = max(a)
        bmax = max(b)
        if amax > bmax:
            return 'Alice'
        elif bmax > amax:
            return 'Bob'
        else:
            return 0

    if win(a, b) != 0:
        print(win(a, b))
        print(win(a, b))
    else:
        print('Alice')
        print('Bob')


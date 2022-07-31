T = int(input())

for _ in range(T):
    n, k = map(int, input().split())

    if n == 1:
        print('ODD')
    elif k == 1:
        if n & 1:
            print('ODD')
        else:
            print('EVEN')
    elif k == 2:
        print('ODD')
    else:
        print('EVEN')

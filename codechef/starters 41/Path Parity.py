T = int(input())

for _ in range(T):
    n, k = map(int, input().split())

    if n & 1:
        if k:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

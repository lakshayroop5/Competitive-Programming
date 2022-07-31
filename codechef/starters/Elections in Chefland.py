T = int(input())

for K in range(T):
    x = list(map(int, input().split()))

    if x[0] > 50:
        print('A')
    elif x[1] > 50:
        print('B')
    elif x[2] > 50:
        print('C')
    else:
        print('NOTA')
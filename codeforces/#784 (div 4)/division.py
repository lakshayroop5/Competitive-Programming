T = int(input())

for K in range(T):
    n = int(input())
    if n >= 1900:
        print('Division 1')
    elif 1600 <= n <= 1899:
        print('Division 2')
    elif 1400 <= n <= 1599:
        print('Division 3')
    elif n <= 1399:
        print('Division 4')

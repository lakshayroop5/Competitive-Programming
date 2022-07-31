T = int(input())

for K in range(T):
    s = input()
    i = 0
    a = 'YES'
    if len(s) == 1:
        print('NO')
    else:
        if s[0] != s[1]:
            a = 'NO'
        elif s[-2] != s[-1]:
            a = 'NO'
        elif s.__contains__('aba'):
            a = 'NO'
        elif s.__contains__('bab'):
            a = 'NO'
        print(a)

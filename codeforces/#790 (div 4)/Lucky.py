T = int(input())

for K in range(T):
    d = list(map(int, input()))
    s1 = sum(d[0:3])
    s2 = sum(d[3:6])
    if s1 == s2:
        print('YES')
    else:
        print('NO')

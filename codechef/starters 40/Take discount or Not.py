T = int(input())

for K in range(T):
    n, x, y = map(int, input().split())
    b = list(map(int, input().split()))
    sn, sy = 0, x
    for i in range(n):
        sn += b[i]
        if b[i] > y:
            sy += b[i] - y
    if sn > sy:
        print('COUPON')
    else:
        print('NO COUPON')
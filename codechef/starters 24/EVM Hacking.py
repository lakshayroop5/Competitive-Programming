T = int(input())

for K in range(T):
    x = list(map(int, input().split()))
    a = x[0]
    b = x[1]
    c, p, q, r = x[2], x[3], x[4], x[5]
    z = (p + q + r) // 2
    if (a + b + r) > z:
        print("YES")
    elif (a + q + c) > z:
        print("YES")
    elif (p + b + c) > z:
        print("YES")
    else:
        print("NO")

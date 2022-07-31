T = int(input())

for K in range(T):
    n = int(input())
    a = []
    x = n
    while x != 0:
        a.append(x % 10)
        x = x // 10
    if len(a) > 2:
        print(min(a))
    else:
        a.reverse()
        if a[0] == min(a):
            print(a[1])
        else:
            print(a[0])

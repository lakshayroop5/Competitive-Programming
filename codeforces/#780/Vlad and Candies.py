T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[:-1])

    if len(a) == 1 and a[0] == 1:
        print("YES")
    elif len(a) == 1 and a[0] > 1:
        print("NO")
    elif a[-1] - a[-2] <= 1:
        print("YES")
    else:
        print("NO")

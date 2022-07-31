T = int(input())

for K in range(T):
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    n = p[0]
    x = p[1]
    y = p[2]

    check = set()
    c = {x, y}
    for i in range(n):
        check.add(b[i] - a[i])

    if c.issuperset(check):
        print("YES")
    else:
        print("NO")
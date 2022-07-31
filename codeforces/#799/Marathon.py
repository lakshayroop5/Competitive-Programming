T = int(input())

for _ in range(T):
    a = list(map(int, input().split()))
    c = 0
    for i in a[1:]:
        if i > a[0]:
            c += 1
    print(c)
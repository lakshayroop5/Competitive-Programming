T = int(input())

for K in range(T):
    p = list(map(int, input().split()))

    f = 0
    for i in range(3):
        s = 0
        for j in range(3):
            if i == j:
                continue
            else:
                s = s + p[j]
        if s == p[i]:
            print("Yes")
            f = 1
            break
    if f == 0:
        print("No")

T = int(input())
print("\n")
for k in range(T):
    num = list(map(int, input().split()))
    p = []
    for i in range(num[0] + 1):
        p.append(input())
    print(len(p))
    l = 0
    r = 1
    f = 0
    c = 0
    while r < num[1]:
        for i in range(num[0]):
            if p[i].__contains__(p[num[0]][l:r + 1]):
                r += 1
                if f == 0:
                    c += 1
                    f = 1

            else:
                l = r
                r += 1
                f = 0

    print(c)
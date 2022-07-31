n, x = map(int, input().split())
a = []
c = -1
while len(a) != n:
    a = []
    temp = x
    check = x
    while temp != 0:
        a.append(temp % 10)
        temp = temp // 10
    x *= max(a)
    # print(x)
    # print(a)
    if check != x:
        c += 1
    else:
        break
print(c)

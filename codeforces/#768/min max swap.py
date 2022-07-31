T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = 1
    while f == 1:
        f = 0
        tempb = max(b)
        index = b.index(tempb)
        if tempb > a[index]:
            f = 1
            temp = tempb
            b[index] = a[index]
            a[index] = temp
    tempa = max(a)
    print(tempb * tempa)
T = int(input())

for K in range(T):
    x = list(map(int, input().split()))
    n, k, m = x[0], x[1], x[2]
    s = input()
    l = []
    for i in range(10):
        l.append(i*k)
    while m != 0:
        for i in range(n):
            s = s[1:] + str(l[int(s[0])] * k)
        n = len(s)
        m -= 1
    print(n)

T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    f = 'Yes'
    for i in range(1, n):
        if a[i] >= m:
            m = a[i]
        else:
            f = 'No'
    print(f)
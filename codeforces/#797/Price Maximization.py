T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    print(a)
    num = 1
    while a[0] + a[n - 1] > k * num:
        num += 1
    crr = []
    l, r = 0, n - 1
    while l < r:
        print(l, r)
        crr.append(a[l] + a[r])
        l += 1
        r -= 1

    drr = []
    for i in crr:
        drr.append(i // k)

    print(sum(drr))
T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    c = 0
    while i < n-1:
        i += 1
        j = n - 1
        while j > 0:
            j -= 1
            if a[i] & a[j] == 0:
                i += 1
                continue
            else:
                if a[i] > a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    c += 1
                    i += 1
                    j -= 1
                else:
                    i += 1
                    continue

    print(a)
    if c != 0:
        print("YES")
    else:
        print("NO")
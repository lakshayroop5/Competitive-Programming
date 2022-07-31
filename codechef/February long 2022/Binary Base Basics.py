T = int(input())

for K in range(T):
    x = list(map(int, input().split()))
    n = x[0]
    k = x[1]
    s = input()
    a = s[:n // 2]
    b = s[-(n // 2):]
    b = b[::-1]
    print(a)
    print(b)
    c = 0
    for i in range(n // 2):
        if a[i] != b[i]:
            c += 1

    if n % 2 == 0:
        if c <= k:
            m = k - c
            if m % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if c <= k:
            print("YES")
        else:
            print("NO")

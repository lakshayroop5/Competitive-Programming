T = int(input())

for k in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    m = max(a[0] + a[1], b[0] + b[1], c[0] + c[1])

    print(m)

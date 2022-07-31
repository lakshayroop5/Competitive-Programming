T = int(input())

for K in range(T):
    a = list(map(int, input().split()))
    o = [a[1] * a[2]]
    o.append(o[0] - a[0])
    o.append(a[2])
    for i in o:
        print(i, end=" ")
    print()


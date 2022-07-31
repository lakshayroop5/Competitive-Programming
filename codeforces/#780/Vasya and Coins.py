T = int(input())

for K in range(T):
    x, y = input().split()
    a, b = int(x), int(y)

    if a == 0:
        print(1)
    else:
        print(a+b*2+1)

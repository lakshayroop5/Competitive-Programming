T = int(input())

for k in range(T):
    x = list(map(int, input().split()))
    a = x[0]*x[1]
    b = x[0]*x[2]
    print(b - a)
T = int(input())

for k in range(T):
    x = list(map(int, input().split()))
    N = x[0]
    K = x[1]
    X = x[2]
    A = []
    if X > K:
        print(-1)
    else:
        o = []
        for i in range(X):
            o.append(i)
        while N >= X:
            A.extend(o)
            N = N - X
        for i in range(N):
            A.append(o[i])
        for i in A:
            print(i, end=" ")
        print("\n", end="")

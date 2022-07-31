T = int(input())

for K in range(T):
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    print(mat)

    for i in mat:
        ind = []
        f = 0
        c = []
        if m > 3:
            if i[j] < i[j-1] and len(c) == 0:
                temp = [j-1, j]
                c.append(temp)

        for j in range(1, m):





for i in range(1, 25):
    n = i
    p = []
    for i in range(n):
        p.append(i+1)
    for i in range(1, n):
        temp = []
        for j in range(i, n, i):
            temp.append(p[j])
        # print(temp)

        k = len(temp) - 1
        for j in range(i, n, i):
            p[j] = temp[k]
            k -= 1

    print(p)



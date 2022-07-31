T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in a:
        f = format(i, "b")[-1:]
        b.append(f)
        # print(b)
    if b.__contains__('1'):
        c1 = []
        c2 = []
        for i in range(n):
            if i % 2 == 0:
                c1.append('0')
                c2.append('1')
            if i % 2 != 0:
                c1.append('1')
                c2.append('0')

        count1 = 0
        count2 = 0
        for i in range(n):
            if b[i] != c1[i]:
                count1 += 1
            elif b[i] != c2[i]:
                count2 += 1
        if count1 <= count2:
            fs = c1
            print(count1)
        else:
            fs = c2
            print(count2)

        # print(fs)
        index1 = b.index('1')
        output = []
        for i in range(n):
            if fs[i] != b[i] and i != index1:
                b[i] = fs[i]
                temp = [i + 1, index1 + 1]
                output.append(temp)
            elif fs[i] != b[i] and i == index1:
                b[i] = fs[i]
                index1 = b.index('1')
                temp = [i + 1, index1 + 1]
                output.append(temp)
        for i in output:
            print(i[0], end=" ")
            print(i[1], end="\n")

    else:
        print(-1)

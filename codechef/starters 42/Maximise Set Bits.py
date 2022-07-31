T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    mrr = []
    d = {}
    for i in range(2, k):
        if pow(2, i) > k:
            break
        else:
            mrr.append(pow(2, i) - 1)
            d.update({mrr[-1]: i})

    index = 0
    for i in range(len(mrr)):
        if mrr[i] * n > k:
            index = i
            break
    mrr = mrr[0: index + 1]
    print(mrr)

    o = []
    i = n
    index -= 1
    x = k
    while i > 0:
        # print(o, 'o')
        if mrr[index] * i < x:
            o.append(mrr[index + 1])
            x -= mrr[index + 1]
            i -= 1
        elif mrr[index] * i == x:
            for j in range(i):
                o.append(mrr[index])
            i = 0
        else:
            for j in range(i):
                o.append(mrr[index])
            t = mrr[index] * i - x
            i = 0
            temp = o.pop()
            o.append(temp - t)
    print(o)

    s = 0
    for i in o:
        if d.get(i) is not None:
            s += d[i]
        else:
            temp = format(i, "b").count('1')
            s += temp
    print(s)
    # print()

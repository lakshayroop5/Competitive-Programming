T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    mrr = []
    d = {}
    o = {}
    for i in range(2, k):
        if pow(2, i) - 1 > k:
            break
        else:
            mrr.append(pow(2, i) - 1)
            d.update({mrr[-1]: i})
            o.update({mrr[-1]: 0})
    mrr.reverse()

    x = k
    for i in mrr:
        while x >= i:
            x -= i
            o[i] += 1
    print(o)

    temp = x
    index = 0
    tempo = o.copy()
    while sum(o.values()) < n:
        tempo = o.copy()
        if o[mrr[index]] > 0:
            o[mrr[index]] -= 1
            o[mrr[index + 1]] += 2
            temp += 1
            if o.get(temp) is not None:
                o[temp] += 1
                temp = 0
        else:
            index += 1
    print(temp)
    if sum(o.values()) > n:
        o = tempo

    print(o)


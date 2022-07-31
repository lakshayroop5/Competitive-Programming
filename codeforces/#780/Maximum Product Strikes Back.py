T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1 and a[0] <= 0:
        print(1, 0)
    else:
        m = 1
        s = []
        e = []
        o = []
        for i in a:
            m = m * i
            s.append(m)
            if m == 0:
                m = 1
        m = 1
        for i in a[::-1]:
            m = m * i
            e.append(m)
            if m == 0:
                m = 1
        S, E = max(s), max(e)
        # print(S, E)
        # print(s, e)
        # calculating output
        l = 0
        r = 0
        if S >= E:
            for i in range(n):
                if s[i] == 0:
                    l = i + 1
                elif s[i] == S:
                    r = n - (i + 1)
                    break
            o.append(l)
            o.append(r)
        else:
            for i in range(n):
                if e[i] == 0:
                    r = i + 1
                elif e[i] == E:
                    l = n - (i + 1)
                    break
            o.append(l)
            o.append(r)

        print(o[0], end=" ")
        print(o[1])


    # print(S,E)
    # if E >= S and E == 0:
    #     o.append(n)
    #     o.append(0)
    # elif E >= S:
    #     o.append(n - (e.index(E)+1))
    #     o.append(0)
    # elif S > E and S == 0:
    #     o.append(0)
    #     o.append(n)
    # else:
    #     o.append(0)
    #     o.append(n - (s.index(S) + 1))



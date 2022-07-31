T = int(input())

for K in range(T):
    a = input()
    l = []
    r = []
    f = 0
    for i in a:
        if not l.__contains__(i):
            l.append(i)

        else:
            # print(l)
            l.remove(i)
            r.extend(l)
            l.clear()
            # print(r,'r')
    # print(r)
    r.extend(l)
    # print(r)
    print(len(r))

T = int(input())

for K in range(T):
    v = input()
    a, b = input().split()
    n, m = int(a), int(b)
    x = []
    w = []

    for i in range(m):
        a, b = input().split()
        x.append(int(a))
        w.append(int(b))
    w.sort()
    print(sum(w[:2 * n]))
    #
    # w_sorted = [x for _, x in sorted(zip(x, w))]
    # x_sorted = x.sort()


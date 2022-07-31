T = int(input())

for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = min(b)
    l = max(b)
    diff = l & s
    f = diff
    for i in a:
        if b.__contains__((diff|i)):
            continue
        else:
            f = -1
            break
    print(f)

    # same = 0
    # for i in a:
    #     if b.__contains__(i):
    #         same += 1
    #
    # sa = sum(a)
    # sb = sum(b)
    # diff = sb - sa
    # if n == same:
    #     num = min(a)
    # else:
    #     num = diff // (n - same)
    # f = num
    # for i in a:
    #     if b.__contains__(i | num):
    #         continue
    #     else:
    #         f = -1
    #         break
    # print(f)

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    o = 'YES'
    arr = []
    zrr = []
    for i in range(n):
        if b[i] == 0:
            zrr.append(a[i] - b[i])
        else:
            arr.append(a[i] - b[i])

    o = 'YES'
    if len(arr):
        c = arr[0]
        f = 1
        for i in arr:
            if i != c or i < 0:
                f = 0
                o = 'NO'
                break

        if f:
            for i in zrr:
                if i > c:
                    o = 'NO'
                    break

    print(o)



    # adiff = []
    # for i in range(n):
    #     if b[i] != 0:
    #         adiff.append(a[i] - b[i])
    # if len(adiff):
    #     diff = min(adiff)
    # else:
    #     diff = min(a[i]) -
    # if diff < 0:
    #     o = 'NO'
    #     print(o)
    # else:
    #     f = 0
    #     for i in adiff:
    #         if i != diff:
    #             f = 1
    #             o = 'NO'
    #             break

    # if f == 0:
    #     for i in range(n):
    #         if b[i] == 0 and a[i] - b[i] > diff:
    #             o = 'NO'
    #             break
    # print(o)

    # for i in range(n):
    #     if a[i] < b[i]:
    #         o = 'NO'
    #         break
    #     elif b[i] != 0 and a[i] - b[i] != diff :
    #         o = 'NO'
    #         break
    #     elif b[i] == 0 and a[i] - b[i] > diff:
    #         o = 'NO'
    #         break
    # print(o)

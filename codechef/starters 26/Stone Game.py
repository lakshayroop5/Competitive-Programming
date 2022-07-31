T = int(input())

for K in range(T):
    # input
    n = int(input())
    x = input()
    y = input()

    # arranging input
    a = list(x)
    b = list(y)
    a.sort()
    b.sort()
    b = b[::-1]

    # process
    o = [0] * 2 * n
    # front, end, startA, endA, startB, endB = 0, 2*n - 1, 0, n - 1, 0, n - 1
    front, end = 0, 2*n - 1
    for i in range(2*n):

        # if i % 2 == 0:
        #     if startB <= endB and a[startA] >= b[startB]:
        #         o[end] = a[endA]
        #         end -= 1
        #         endA -= 1
        #     else:
        #         o[front] = a[startA]
        #         front += 1
        #         startA += 1
        #
        # else:
        #     if startA <= endA and a[startA] < b[startB]:
        #         o[front] = b[startB]
        #         front += 1
        #         startB += 1
        #
        #     else:
        #         o[end] = b[endB]
        #         end -= 1
        #         endB -= 1
        f = 0
        if i % 2 == 0:
            if a[0] < b[0]:
                f = 1
            if f == 1:
                o[front] = a[0]
                front += 1
                a.remove(a[0])
            else:
                o[end] = a[-1]
                end -= 1
                a.remove(a[-1])

        else:
            if len(a) == 0:
                o[o.index(0)] = b[0]
                continue

            elif b[0] > a[0]:
                f = 1

            if f == 1:
                o[front] = b[0]
                front += 1
                b.remove(b[0])
            else:
                o[end] = b[-1]
                end -= 1
                b.remove(b[-1])
    output = ""
    for i in o:
        output += i
    print(output)

T = int(input())

for K in range(T):
    n = int(input())
    bg = format(n, "b")
    b1 = ''
    b2 = ''
    temp = '1'
    for i in range(len(bg)):
        if i%2 == 0:
            b1 = b1 + '0'
            b2 = b2 + '1'
        else:
            b1 = b1 + '1'
            b2 = b2 + '0'
        ib1 = int(b1, 2)
        ib2 = int(b2, 2)
        if ib1 == n:
            b1 = '1' + b1
            ib1 = int(b1, 2)
        elif ib2 == n:
            b2 = '1' + b2
            ib2 = int(b2, 2)
    o = [n, ib1, ib2]
    for i in o:
        print(i, end=" ")
    print("\n", end="")

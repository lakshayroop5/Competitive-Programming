T = int(input())

for _ in range(T):
    n, q = map(int, input().split())
    qrr = []
    for i in range(q):
        temp = list(map(int, input().split()))
        qrr.append(temp)

    if n == 1:
        print(1)
    else:
        rooms = n + ((n - 1) * 3) - 1
        current = 1
        for i in qrr:
            if i[0] == 0:
                current = (i[1] + current) % rooms
            elif i[0] == 1:
                current = (rooms + current - (i[1] % rooms))
            elif i[0] == 2:
                current = 1
            # print(current)
        print(current)

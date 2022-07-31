t = int(input())

for i in range(t):
    N = int(input())
    a = list(map(int, input().split()))
    s = set()

    # making all the numbers in range
    for j in range(N):
        length = len(s)
        temp = length
        while a[j] > N:
            a[j] = a[j] // 2

        # adding the jth number to the set
        s.add(a[j])
        length = len(s)
        # avoiding repeated numbers
        while temp == length:
            temp = length
            a[j] = a[j] // 2
            s.add(a[j])
            if a[j] == 0:
                break
            length = len(s)

    f = 0
    for j in range(1, N + 1):
        if not s.__contains__(j):
            f = 1
            print("NO")
            break
    if f == 0:
        print("YES")

    # for j in range(N):
    #     while a[j] > N:
    #         a[j] = a[j]//2

    # a.sort()
    # print(a)

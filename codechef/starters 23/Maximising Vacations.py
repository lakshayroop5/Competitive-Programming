T = int(input())

for k in range(T):
    x = list(map(int, input().split()))
    N = x[0]
    X = x[1]
    s = input()
    count = []
    r = 0
    c = 0

    while r < N:
        if s[r] == '1':
            r += 1
        else:
            while r < N and s[r] != '1':
                c += 1
                r += 1
            count.append(c)
            c = 0
            r += 1
    c = 0
    for i in range(len(count)):
        if (count[i] + 1) % X == 0:
            count[i] += 1
            break
        elif i + 1 < len(count) and (count[i] + count[i+1] + 1) % X == 0:
            temp = count[i] + count[i+1] + 1
            count.remove(count[i])
            count.remove(count[i])
            count.append(temp)
            break
    for i in count:
        if i % X == 0:
            c = c + (i // X)
    print(c)

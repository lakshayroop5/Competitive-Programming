T = int(input())

for _ in range(T):
    n = int(input())
    b = list(map(int, input().split()))

    l, s = b[0], b[0]
    o = 'YES'
    for i in b:
        if s < i < l:
            o = 'NO'
            break
        else:
            if i < s:
                s = i
            elif i > l:
                l = i

    print(o)
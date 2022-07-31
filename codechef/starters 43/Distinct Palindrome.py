import math
import string
s = string.ascii_lowercase
T = int(input())
# print(s)

for _ in range(T):
    n, x = map(int, input().split())
    if math.ceil(n / 2) < x:
        print(-1)
    else:
        c = []
        for i in range(x):
            c.append(s[i])

        if n == 1:
            o = ['a']
        else:
            o = []
            for i in range(n):
                o.append(0)
            l, r, ind = 0, n - 1, 0
            for i in range(math.ceil(n / 2)):
                o[l], o[r] = c[ind], c[ind]
                ind += 1
                if ind > x - 1:
                    ind = 0
                l += 1
                r -= 1

        for i in o:
            print(i, end='')
        print()




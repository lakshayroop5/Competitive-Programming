import math
import string

alpha = string.ascii_lowercase
d = {}
for i in range(26):
    d.update({alpha[i]: i + 1})
# a = 'best'
# # b = 'cost'
# # # s = 0
# # # u = 0
# # # for i in range(len(a)):
# # #     s += alpha.index(a[i])
# # #     u += alpha.index(b[i])
# # # print(s)
# # print(u)

T = int(input())

for K in range(T):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())

    output = math.inf
    for i in range(n-1):
        for j in range(i+1, n):
            temps = 0
            for k in range(m):
                temps += abs(d[s[i][k]] - d[s[j][k]])
                # print(temps, 't')
            output = min(output, temps)

    print(output)

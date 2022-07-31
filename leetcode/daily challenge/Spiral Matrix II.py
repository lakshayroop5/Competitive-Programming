n = 4

o = []
temp = [0]*n
for i in range(n):
    o.append(temp.copy())
x = 1
s = -1
while x < n*n:
    s += 1
    i = s
    for j in range(i, n-s):
        # print(i,j)
        o[i][j] = x
        x += 1
        # print(o)
    if x == n*n:
        break
    j = -1-s
    for i in range(s+1, n-s):
        o[i][j] = x
        x += 1
    if x == n*n:
        break
    i = -1-s
    for j in range(n-s-2,-1+s,-1):
        # print(i, j)
        o[i][j] = x
        x += 1
        # print(o)
    if x == n*n:
        break
    j = s
    for i in range(n-s-2, s, -1):
        o[i][j] = x
        x += 1
        # print(o)
if n & 1:
    o[n//2][n//2] = n ** 2
else:
    o[n//2][(n-1)//2] = n**2
print(o)

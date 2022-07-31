prices = [3,3,5,0,0,3,1,4]
n = len(prices)
l = []
r = []
p = []

x = 0
lmin = prices[0]
y = 0
rmax = prices[n-1]
i = -1
j = n
while j > 0:
    i += 1
    j -= 1
    x = max(x, prices[i] - lmin)
    l.append(x)
    if prices[i] < lmin:
        lmin = prices[i]

    y = max(y, rmax - prices[j])
    r.append(y)
    if prices[j] > rmax:
        rmax = prices[j]

j = n
for i in range(n):
    j -= 1
    x = l[i] + r[j]
    p.append(x)
print(p)
print(l)
print(r[::-1])
p = list(dict.fromkeys(p))
print(sum(p))



# while r < n - 1 and l < n - 1:
#     print(l, 'l')
#     print(r, 'r')
#     if prices[r] <= prices[r + 1]:
#         r += 1
#     else:
#         p.append(prices[l])
#         p.append(prices[r])
#         l = r + 1
#         r = l + 1
#
# if l != n-1:
#     p.append(prices[l])
#     p.append(prices[r])
#
# print(p)

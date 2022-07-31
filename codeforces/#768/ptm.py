n = int(input())
x = list(map(int, input().split()))


def ind(num, arr):
    temp1 = len(arr) - arr[::-1].index(num) - 1
    return temp1


o = set()
s = set(x)
for i in s:
    minus = {x.index(i), ind(i, x)}
    tempset = {index for index in range(x.index(i), ind(i, x))}
    tunion = o.union(tempset)
    l = len(o)
    o.update(tunion)
    if l != len(o):
        o.difference_update(minus)
print(len(o))

# for i in s:
#     temp = [x.index(i), ind(i, x)]
#     if len(s) == 0:
#         o.extend(temp)
#     else:
#         if temp[0] < o[0]:
#             o[0] = temp[0]
#         elif temp[1] > o[len(o)-1]:
#             o[len(o)-1] = temp[1]
#         elif o[0] > temp[0] > temp[1] > o[len(o)-1]:
#             continue
#         elif o[0] > temp[0] > o[len(o)-1] > temp[1]:
#             o.remove()

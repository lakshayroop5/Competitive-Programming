import math

n = int(input())
k = int(input())


def gen(x, ind):
    if x == 1:
        return 0
    temp = ind
    parent = gen(x - 1, math.ceil(ind / 2))
    if parent:
        if temp % 2:
            return 1
        else:
            return 0
    else:
        if temp % 2:
            return 0
        else:
            return 1


print(gen(n, k))


# def gen(x=int(), s=None, st=None, r=None, y=int()):
#     if r is None:
#         r = []
#     if st is None:
#         st = []
#     if s is None:
#         s = []
#     if x < y:
#         x += 1
#         # print(x)
#         if x & 1:
#             s.extend(r)
#             # print(st, 's')
#         else:
#             # print(x)
#             s.extend(r)
#             s.extend(st)
#             st = s.copy()
#             r = s[::-1]
#         # print(x, s,st,r)
#         gen(x, s, st, r, y)
#
# if n == 1:
#     d = [0]
# elif n == 2:
#     d = [0,1]
# else:
#     d = [0, 1]
#     gen(2, d, [0, 1], [1, 0], n)
# # print(d)
# print(list(d)[k-1])
# for i in d:
#     print(i, end='')
# print()

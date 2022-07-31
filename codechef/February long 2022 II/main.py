# c = []
# for i in range(1, 10000):
#     f = 0
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             f = 1
#             break
#     if f == 0:
#         c.append(i)
c = []
for i in range(10000000):
    c.append(i)
c = c[::-1]
c.sort()
print(c)

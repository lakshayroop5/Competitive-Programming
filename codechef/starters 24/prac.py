# a = ['a', 'b', 'c']
# b = [4, 2, 1]
# c = zip(b, a)
# x = sorted(c)
# l = [e for  e in x]
# print(l)

s = 'abcde'
n = s
n = n[1:]
print(id(s))
print(id(n))
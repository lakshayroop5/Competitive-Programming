s = input()
c1 = ['(', '[', '{']
c2 = [')', ']', '}']
d = {')': '(', ']': '[', '}': '{'}
o = []
f = 0
for i in s:
    if c1.__contains__(i):
        o.append(i)
    else:
        if len(o) == 0:
            f = 1
            break
        else:
            if o[-1] != d[i]:
                f = 1
                break
            else:
                o.pop(len(o)-1)
print(o)
if f == 1:
    print('false')
elif len(o) != 0:
    print('false')
else:
    print('true')



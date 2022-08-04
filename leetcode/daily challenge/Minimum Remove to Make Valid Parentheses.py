s = "lee(t(c)o)de)"
s_ = []
stack = []
for i in s:
    if i == '(':
        stack.append(i)
        s_ += i
    elif i == ')' and not len(stack):
        continue
    elif i == ')':
        stack.pop()
        s_ += i
    else:
        s_ += i
# print(s_)
s_ = s_[::-1]
while len(stack):
    s_.pop(s_.index('('))
    stack.pop()

o = ''
while len(s_):
    o += s_.pop()
print(o)

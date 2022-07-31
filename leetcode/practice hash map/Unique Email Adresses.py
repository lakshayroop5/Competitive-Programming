emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]

# CODE
c = []
for i in emails:
    s = ""
    j = 0
    while j < len(i):
        if i[j] != '.' and i[j] != '+' and i[j] != '@':
            s += i[j]
            j += 1
        elif i[j] == '+' or i[j] == '@':
            j = i.index('@')
            s += i[j:]
            break
        elif i[j] == '.':
            j += 1
    c.append(s)
print(c)
d = {}
for i in c:
    if d.get(i) is None:
        temp = {i: 1}
        d.update(temp)
print(d)

print(sum(list(d.values())))

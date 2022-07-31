s = "abcba"
target = "abc"

# CODE
d = {}
c = {}
for i in target:
    d.update({i: 0})
    if c.get(i) is None:
        c.update({i: 1})
    else:
        c[i] += 1
for i in s:
    if target.__contains__(i):
        d[i] += 1
print(c, d)
o = []
for i in target:
    o.append(d[i] // c[i])

print(min(o))

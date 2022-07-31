s = "aabb"

# CODE
d = {}
for i in s:
    if d.get(i) is None:
        temp = {i: 1}
        d.update(temp)
    else:
        d[i] += 1

v = list(d.values())
k = list(d.keys())
ind = 0
if v.__contains__(1):
    ind = v.index(1)
    print(s.index(k[ind]))
else:
    print(-1)

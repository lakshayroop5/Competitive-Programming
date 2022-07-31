s = "eccbbbbdec"

d = {}
for i in range(len(s)):
    if d.get(s[i]) is None:
        d[s[i]] = [i, i]
    else:
        d[s[i]][-1] = i

v = list(d.values())
o = [v[0]]
for i in range(1, len(v)):
    o.append(v[i])
    if o[-2][1] > o[-1][0] and o[-2][1] > o[-1][1]:
        o.pop()
    elif o[-1][0] < o[-2][1] < o[-1][1]:
        temp = [o[-2][0], o[-1][1]]
        o.pop()
        o.pop()
        o.append(temp)

out = []
for i in o:
    out.append(i[1] - i[0] + 1)
print(out)
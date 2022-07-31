import string


def dic():
    x = {}
    for i in string.ascii_lowercase:
        temp = {i: 0}
        x.update(temp)
    return x


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  # REMOVE THIS FROM CODE
s = []
for i in strs:
    m = dic()
    for j in i:
        m[j] += 1
    s.append(tuple(m.values()))

d = {}
for i in range(len(strs)):
    if d.get(s[i]) is None:
        temp = {s[i]: [strs[i]]}
        d.update(temp)
    else:
        d.get(s[i]).append(strs[i])
output = list(d.values())
print(output)

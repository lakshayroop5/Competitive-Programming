pattern = "abba"
s = "dog cat cat dog"
sp = s.split()
d1, d2 = {}, {}
for i in range(len(pattern)):
    if d1.get(pattern[i]) is None:
        d1[pattern[i]] = [i]
    else:
        d1[pattern[i]].append(i)

    if d2.get(sp[i]) is None:
        d2[sp[i]] = [i]
    else:
        d2[sp[i]].append(i)
# print(d1, d2)
if list(d1.values()) == list(d2.values()):
    print(True)
else:
    print(False)

# import time

# start = time.time()
strs = ["ddddddddddg","dgggggggggg"]
s = []
for i in strs:
    temp = {}
    for j in i:
        # print(j, 'j')
        if temp.get(j) is None:
            u = {j: 1}
            temp.update(u)
            # print(temp, 't')
        else:
            temp[j] += 1
            # print(temp[j], 'temp')
    temp1 = []
    for j in temp:
        temp1.append(j)
        temp1.append(temp[j])
    s.append(frozenset(temp1))
print(s)
# end = time.time()
# print(end - start)
d = {}
for i in range(len(strs)):
    if d.get(s[i]) is None:
        temp = {s[i]: [strs[i]]}
        d.update(temp)
    else:
        d.get(s[i]).append(strs[i])
output = list(d.values())
print(output)
arr = [1,2,2,1,1,3]

#CODE
d = {}
for i in arr:
    if d.get(i) is None:
        d.update({i: 1})
    else:
        d[i] += 1

v = list(d.values())
check = {}
f = 0
for i in v:
    if check.get(i) is not None:
        print('false')
        f = 1
        break
    else:
        check.update({i: 1})
if f == 0:
    print('true')
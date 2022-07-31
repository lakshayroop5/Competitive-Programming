nums = [3,4,4,7,-4]
k = 7

# CODE
count = 0
s = 0
d = {}
for i in nums:
    s += i
    if d.get(s-k) is not None:
        count += d[s-k]
    if s == k:
        count += 1
    # print(count, s)

    # for storing the commulated sum in dict
    if d.get(s) is None:
        temp = {s: 1}
        d.update(temp)
    else:
        d[s] += 1

# print(d)
print(count)

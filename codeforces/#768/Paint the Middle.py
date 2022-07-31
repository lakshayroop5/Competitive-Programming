n = int(input())
x = list(map(int, input().split()))
xr = []
xr.extend(x[::-1])


def size(num, arr, arrr):
    temp1 = arr.index(num)
    temp2 = n - arrr.index(num) - 1
    return temp2 - temp1 - 1


def ind(num, arr):
    temp1 = len(arr) - arr.index(num) - 1
    return temp1


s = set()
for i in x:
    s.add(i)

d = {}
for i in x:
    temp = {i: size(i, x, xr)}
    d.update(temp)

L = 0
r = 0
i = 0
c = 0
done = set()
while L < len(x):
    done.add(x[L])
    r = ind(x[L], x)
    if L == r:
        L += 1
        continue
    i = L + 1
    while i < r:
        if d[x[i]] < d[x[L]] or (d[x[i]] == d[x[L]] and (done.__contains__(x[i] or x[i] == x[L]))):
            x.pop(i)
            r -= 1
            c += 1
        else:
            i += 1

    if r == L + 1:
        L = r + 1
    else:
        L = L + 1

for i in range(1, len(x) - 1):
    if x.count(x[i]) == 1:
        c += 1

print(c)

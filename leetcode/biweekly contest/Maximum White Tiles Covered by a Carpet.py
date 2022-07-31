tiles = [[8051, 8057], [8074, 8089], [7994, 7995], [7969, 7987], [8013, 8020], [8123, 8139], [7930, 7950], [8096, 8104],
         [7917, 7925], [8027, 8035], [8003, 8011]]

carpetLen = 9854

# CODE
tiles.sort()
print(tiles)
a = []
for i in range(len(tiles)):
    print(i)
    w = tiles[i][1] - tiles[i][0] + 1
    print(tiles[i][1], 'x')
    print(tiles[i][0], 'y')
    print(w)
    a.append(w)
    if i < len(tiles) - 1:
        g = tiles[i + 1][0] - tiles[i][1] - 1
        if g > 0:
            a.append(g)
        else:
            a.append(0)

print(a)
j = 0
s = 0
cov = 0
gap = 0
o = 0
c = 0
while j < len(a):
    if s < carpetLen:
        s += a[j]
        if j % 2 == 0 and s <= carpetLen:
            cov += a[j]
        else:
            gap += a[j]
        j += 1
    if s > carpetLen:
        o = max(o, cov)
        s, cov, gap = 0, 0, 0
        c += 2
        j = c
    elif s == carpetLen:
        o = max(o, cov)
        s, cov, gap = 0, 0, 0
        c += 2
        j = c
        # j += 1
        # print(j)
# print(s, 's')
# print(cov, 'c')

if o == 0:
    for i in range(0, len(a), 2):
        o += a[i]
print(o)

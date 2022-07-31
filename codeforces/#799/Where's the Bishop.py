T = int(input())

for _ in range(T):
    n = input()
    c = []
    for i in range(8):
        a = input()
        c.append(a)

    count = []
    for i in c:
        count.append(i.count('#'))

    row = [count.index(2), 7 - count[::-1].index(2)]
    col = [c[row[0]].index('#'), 7 - c[row[0]][::-1].index('#')]
    o = [(row[1] + row[0])//2 + 1, (col[1] + col[0])//2 + 1]
    print(o[0], o[1])


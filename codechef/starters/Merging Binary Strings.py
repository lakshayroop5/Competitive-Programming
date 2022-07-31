T = int(input())

for K in range(T):
    N = int(input())
    a = input()
    b = input()
    o = str()


    def shift(s, l, r, so):
        while r < N and l < N:
            if s[r] == '0':
                r += 1
            elif s[r - 1] == '1' and s[r] == '1':
                r += 1
            elif s[r] == '1':
                so.join(s[l:r])
                return
        so.join(s[l:r])
        return


    x = min(a, b)
    y = max(a, b)
    lx = 0
    ly = 0
    rx = 1
    ry = 1
    while rx < N and ry < N:
        shift(x, lx, rx, o)
        rx = len(o) - ry
        lx = rx - 1
        shift(y, ly, ry, o)
        ry = len(o) - rx + 1

T = int(input())

for K in range(T):
    f = int(input())
    s = input()
    m = int(input())
    x = f+1

    def atz(a):
        st = ''
        i = 97
        while a != 0:
            st += chr(i)
            i += 1
            if i > 122:
                i = 97
            a -= 1
        return st

    c = atz(m)
    b = 0
    if not s.__contains__('a'):
        b = 1
        print(-1)
    else:
        l = s.index('a')
        r = 0
        s = s[l:]
        n = s
        while len(s) >= m:
            for i in c:
                if n.__contains__(i):
                    r = n.index(i)
                    n = n[r:]
                else:
                    break

            count = (len(s)+1) - (len(n)+m)
            x = min(x, count)
            if s[1:].__contains__('a'):
                l = s[1:].index('a') + 1
                r = 0
                s = s[l:]
                n = s
            else:
                break

    if x > f and b != 1:
        print(-1)
    elif b != 1:
        print(x)






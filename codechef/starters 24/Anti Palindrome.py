T = int(input())

for K in range(T):
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("NO")
    else:
        ns = list(dict.fromkeys(s))
        count = []
        for i in ns:
            c = s.count(i)
            count.append(c)

        if max(count) > n//2:
            print("NO")
        else:
            print("YES")
            zlist = zip(count, ns)
            l = sorted(zlist)
            o = [i for _, i in l]
            o.reverse()
            count.sort()
            count.reverse()
            output = []
            for i in range(len(count)):
                output.append(o[i]*count[i])
            os = "".join(i for i in output)
            l1 = [i for i in os[:n//2]]
            l2 = [i for i in os[n//2:]]
            l1.reverse()
            ind = n//2 - 1
            for i in range(n//2):
                if l1[i] == l2[i]:
                    temp = l1[i]
                    l1[i] = l2[ind]
                    l2[ind] = temp
                    ind -= 1
                else:
                    break
            ol = ''
            for i in l1:
                ol = ol + i
            for i in l2:
                ol = ol + i
            print(ol)

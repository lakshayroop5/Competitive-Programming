T = int(input())

for k in range(T):
    X = list(map(int, input().split()))
    o = []

    for i in range(1, X[1] + 1):
        s = []
        for j in range(i):
            s.append(j+1)

        j = 1
        while len(s) != 1:
            j = j + (X[0] - 1)
            if j <= len(s):
                s.remove(s[j - 1])
                j = 1
            else:
                while j > len(s):
                    j = j-len(s)
                s.remove(s[j-1])
                j = 1

        o.append(s.pop())
        l = []
        a = {
            "lakshay" : 1,
            "aryan" : [1, 2, 3]
        }
        s = set()


    for i in range(X[1]):
        print(o[i], end=" ")
    print(end="\n")

T = int(input())

for k in range(T):
    n = int(input())
    o = []
    i = 0

    def xor(a, b):
        return (a | b) & (~a | ~b)

    while len(o) != n:
        o.append(xor(i, i+1))
        i += 1

    for j in o:
        print(j, end=" ")
    print("\n", end="")
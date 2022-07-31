T = int(input())

for K in range(T):
    n = int(input())
    o = []

    if n % 2 != 0:
        for i in range(1, n//2+1):
            o.append(i)
        i = n
        while i != n//2:
            o.append(i)
            i -= 1
        print("Yes")
        for i in range(n):
            print(o[i], end=" ")
        print("\n", end="")

    elif n%2==0 and n!=2:
        o.append(n//2)
        for i in range(1, n//2):
            o.append(i)
        i = n
        while i != n//2:
            o.append(i)
            i -= 1
        print("Yes")
        for i in range(n):
            print(o[i], end=" ")
        print("\n", end="")
    else:
        print("No")

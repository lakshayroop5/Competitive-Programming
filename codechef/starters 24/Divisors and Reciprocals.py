T = int(input())

for K in range(T):
    y = list(map(int, input().split()))
    x, a, b = y[0], y[1], y[2]
    if a < b:
        print(-1)
    else:
        if (x * b) % a == 0:
            c = (x * b) // a
            s = 0
            for i in range(1, int(c ** 0.5) + 1):
                if c % i == 0:
                    s += i
                    if c // i != i:
                        s += c//i
            if x == s:
                print(c)
            else:
                print(-1)

        else:
            print(-1)

        
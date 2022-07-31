T = int(input())

for k in range(T):
    X = list(map(float, input().split()))

    if X[0] == 1:
        if X[1] % 2 == 0:
            print("Even")
        else:
            print("Odd")

    elif X[1] % 2 == 1:
        if X[0] % 2 == 0:
            print("Even")
        else:
            print("Odd")

    else:
        print("Impossible")

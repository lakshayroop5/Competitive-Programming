T = int(input())

for K in range(T):
    n = int(input())
    d = list(map(int, input().split()))
    m = min(d)
    eatd = []
    for i in d:
        eatd.append(i - m)

    print(sum(eatd))

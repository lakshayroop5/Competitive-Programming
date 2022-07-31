import collections

T = int(input())


for K in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    if n < 3:
        print(-1)
    else:
        f = -1
        counter = collections.Counter(a)
        for key, value in counter.items():
            if value>=3:
                f = key
                break
        print(f)

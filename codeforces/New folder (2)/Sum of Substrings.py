T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    s = input()

    j = 0
    srr = []
    for i in range(2, n+1):
        srr.append(s[j:i])
        j += 1

    for i in range(k):
        if srr.__contains__('10'):
            srr[srr.index('10')] = '01'

    sum_ = 0
    for i in srr:
        sum_ += int(i)
    print(srr)
    print(sum_)
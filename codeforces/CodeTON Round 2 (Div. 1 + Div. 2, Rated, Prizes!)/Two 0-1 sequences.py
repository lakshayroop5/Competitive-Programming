T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = input()
    b = input()

    if b[1:] != a[len(a) - len(b) + 1:]:
        print('No')
        continue
    if not a[:len(a) - len(b) + 1].__contains__(b[0]):
        print('No')
        continue
    print('Yes')

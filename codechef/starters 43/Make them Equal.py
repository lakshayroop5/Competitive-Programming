T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    m = max(a, b, c)
    x, y, z = m - a, m - b, m - c

    
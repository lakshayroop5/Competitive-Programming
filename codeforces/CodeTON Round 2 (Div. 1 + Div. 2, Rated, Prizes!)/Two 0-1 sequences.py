T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = input()
    b = input()
    x = list(a)
    o = []


    def func(s: list, c):
        # global m
        # print(s)
        if len(s) == m or len(s) < 2:
            # print(s, 'a')
            o.append(s)
            return

        if c == '1':
            # print(s, 'n')
            temp = min(int(s[-1]), int(s[-2]))
            s.pop()
            s.pop()
            s += str(temp)

        if c == '0':
            # print(s, 'm')
            temp = max(int(s[-1]), int(s[-2]))
            s.pop()
            s.pop()
            s += str(temp)
        func(s.copy(), '1')
        # print('v', s)
        func(s.copy(), '0')


    func(x[::-1], '1')
    func(x[::-1], '0')
    if o.__contains__(list(b)[::-1]):
        print('Yes')
    else:
        print('No')

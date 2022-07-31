T = int(input())

for _ in range(T):
    startTime, x = input().split()
    hh = startTime[0:2]
    intHH = int(hh)
    mm = startTime[3:]
    intMM = int(mm)
    x = int(x)
    hrs = x // 60
    min = x % 60
    d = {}

    while d.get(f'{hh}{mm}') is None:
        d.update({f'{hh}{mm}': 1})
        # print(f'{hh}{mm}')
        intHH += hrs
        intMM += min

        if intMM > 59:
            intHH += 1
            intMM -= 60
        if intHH > 23:
            intHH -= 24

        if intHH < 10:
            hh = f'0{intHH}'
        else:
            hh = f'{intHH}'

        if intMM < 10:
            mm = f'0{intMM}'
        else:
            mm = f'{intMM}'

        # if intHH < 10 and intMM < 10:
        #     d.update({f'0{intHH}0{intMM}': 1})
        # elif intHH < 10:
        #     d.update({f'0{intHH}{intMM}': 1})
        # elif intMM < 10:
        #     d.update({f'{intHH}0{intMM}': 1})
    # print(d)
    c = 0
    k = list(d.keys())
    for i in k:
        if i[0] == i[3] and i[1] == i[2]:
            c += 1

    print(c)
k = 2
prices = [2,4,1]

if k == 0 or len(prices) == 1:
    print(0)
else:
    newPrices = []
    i = 0
    while prices[i+1] < prices[i]:
        i += 1

    l = i
    r = l + 1
    for i in range(l+1, len(prices)):
        if prices[i] <= prices[i+1]:
            r += 1
        else:
            newPrices.append(l)
            newPrices.append(r)
            l = r + 1

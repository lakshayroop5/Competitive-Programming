num = 2994

d = {'I': 0,
     'IV': 0,
     'V': 0,
     'IX': 0,
     'X': 0,
     'XL': 0,
     'L': 0,
     'XC': 0,
     'C': 0,
     'CD': 0,
     'D': 0,
     'CM': 0,
     'M': 0}

n = num
r = 0
while n > 0:
    if n >= 1000:
        n //= 1000
        d.update({'M': n})
        r %= 1000
        n = r
    elif n >= 900:
        d.update({'CM': 1})



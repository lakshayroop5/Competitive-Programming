num1 = "123"
num2 = "456"

def toNum(n: str)->int:
    x = len(n)
    temp = 0
    for i in range(x):
        temp += (ord(n[i]) - 48) * pow(10, x - i - 1)
    return temp

def toStr(n: int) -> str:
    if n == 0:
        return '0'
    d = {}
    for i in range(10):
        d[i] = str(i)
    o = ''
    while n > 0:
        o += d[n % 10]
        n //= 10
    return o[::-1]

print(toStr(toNum(num1) * toNum(num2)))
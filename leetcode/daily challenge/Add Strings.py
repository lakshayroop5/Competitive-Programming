class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        s = list(d.keys())
        if len(num1) < len(num2):
            m = num2
            n = num1
        else:
            m = num1
            n = num2
        n1, n2 = 0, 0
        i = 0
        while i < len(n):
            n1 += d[n[i]] * pow(10, len(n) - i - 1)
            n2 += d[m[i]] * pow(10, len(m) - i - 1)
            i += 1
        while i < len(m):
            n2 += d[m[i]] * pow(10, len(m) - i - 1)
            i += 1
        # print(n1, n2)
        sum_ = n1 + n2
        # print(sum_)
        o = ''
        if sum_ == 0:
            o += '0'
        while sum_ > 0:
            o += s[sum_ % 10]
            sum_ //= 10

        return o[::-1]

num = 240
k = 2

# CODE
s = str(num)
a = []
for i in range(len(s) - k + 1):
    a.append(s[i:i + k])

c = 0
for i in a:
    x = int(i)
    if x != 0 and num % x == 0:
        c += 1

print(c)

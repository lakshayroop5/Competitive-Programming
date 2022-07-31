import math

sentence = "there are $1 $2 and 5$ candies in the shop"
discount = 50

# CODE
d = "{:.2f}".format(50/100)
print(d)
n = len(sentence)
i = sentence.find(' $')
i += 2
o = sentence[0:i]
j = sentence[i:].find(' ')
while i != -1:
    num = sentence[i:j]
    f = 1
    try:
        num = float(num)
    except:
        f = 0

    if f:
        num = "{:.2f}".format(num * float(d))
        o += num
    else:
        o += num

    i = j
    sentence = sentence[i:]
    n = len(sentence)
    i = sentence.find(' $')
    i += 2
    o += sentence[0:i]
    j = sentence[i:].find(' ')
print(o)




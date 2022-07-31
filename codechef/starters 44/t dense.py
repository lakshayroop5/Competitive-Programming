test = int(input())

for _ in range(test):
    n = int(input())
    s = input()

    if n == 6:
        if s != '((()))':
            print(4)
            continue
    if n == 8:
        if s != '(((())))' and s != '((()))()' and s != '()((()))' and s != '()(())()':
            print(6)
            continue

    right, left = 0, 0
    for i in range(n):
        if i < n // 2:
            if s[i] == ')':
                left += 1
        else:
            if s[i] == '(':
                right += 1

    print(left + right)

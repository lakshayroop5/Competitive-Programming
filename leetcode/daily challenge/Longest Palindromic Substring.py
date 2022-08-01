s = "bacabab"
n = len(s)
res = ''
resLen = 0
for i in range(n):
    # odd length
    l, r = i, i
    while l > -1 and r < n and s[l] == s[r]:

        if resLen < r - l + 1:
            res = s[l:r+1]
            resLen = len(res)
        l -= 1
        r += 1

    # even length
    l, r = i, i+1
    while l > -1 and r < n and s[l] == s[r]:
        if resLen < r - l + 1:
            res = s[l:r+1]
            resLen = r - l + 1
        l -= 1
        r += 1

print(res)

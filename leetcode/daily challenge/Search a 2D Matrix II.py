matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
f = 1

def search(i, j, a, dr):
    global f
    # print(a[i][j])
    if a[i][j] == target:
        f = 0
        # print('a')
        return True
    elif a[i][j] > target:
        return
    elif i == len(a) - 1 and j == len(a[i]) - 1 and f:
        return False

    if dr == 'r' and j < len(a[i]) - 1 and f:
        b = search(i, j+1, a, 'r')
        print(b)
    else:
        if j < len(a[i]) - 1 and f:
            b = search(i, j+1, a, 'r')
            print(b)

        if i < len(a) - 1 and f:
            b = search(i+1, j, a, 'd')
            print(b)
    return b

print(search(0,0,matrix,'s'))
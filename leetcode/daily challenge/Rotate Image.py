matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def swap(i, j, arr):
    temp = arr[i][j]
    arr[i][j] = arr[j][i]
    arr[j][i] = temp


for i in range(len(matrix)):
    for j in range(i, len(matrix[i])):
        swap(i, j, matrix)

for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]

print(matrix)

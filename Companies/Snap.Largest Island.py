def largest_island(matrix):
    def helper(i, j, tmp):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] > 0:
            tmp[0] += matrix[i][j]
            matrix[i][j] = 0
            helper(i - 1, j, tmp)
            helper(i + 1, j, tmp)
            helper(i, j - 1, tmp)
            helper(i, j + 1, tmp)

    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                tmp = [0]
                helper(i, j, tmp)
                res = max(res, tmp[0])

    return res


islands = [[2, 2, 1], [0, 0, 0], [0, 0, 1]]
print(largest_island(islands))

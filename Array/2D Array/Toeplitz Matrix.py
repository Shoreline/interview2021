# No need to worry about checking in diagonal sequence.
# Simply compare the value of matrix[i][j] and matrix[i+1][j+1].
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True        
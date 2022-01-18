# Use the first row and first column of input matrix as cache to save whether we shall clean a col/row.
#
# Can't modify the buffer zone using to cache whether a row/col shall be zero out unless all other area has been modified. -> So, must treat the first row and column separately.
# Whether to clean the first row/column themselves are saved into two variables

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        r1, c1 = False, False  # whether the first row / column shall be set to zero

        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == 0:
                    if i > 0 and j > 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    if i == 0:
                        r1 = True
                    if j == 0:
                        c1 = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if c1:
            for i in range(rows):
                matrix[i][0] = 0
        if r1:
            for j in range(cols):
                matrix[0][j] = 0

# Consise code
# class Solution:
#     def setZeroes(self, M):
#         m, n = len(M[0]), len(M)
#         r1 = any(M[0][j] == 0 for j in range(m))
#         c1 = any(M[i][0] == 0 for i in range(n))
#         for i in range(1, n):
#             for j in range(1, m):
#                 if M[i][j] == 0: M[i][0] = M[0][j] = 0

#         for i in range(1, n):
#             for j in range(1, m):
#                 if M[i][0] * M[0][j] == 0: M[i][j] = 0

#         if r1:
#             for i in range(m): M[0][i] = 0

#         if c1:
#             for j in range(n): M[j][0] = 0

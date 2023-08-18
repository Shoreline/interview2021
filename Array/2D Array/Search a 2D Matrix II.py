# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# O(m + n)
# Start from top right conner -> always stays at the top-right conner, it is just that the matrix keeps being shrinked each round
#   - Why? Since it is a perfect spot that the top row and rightmost column
#     together form a perfect asscending sequence
#   - Every time we drop one row or one column. And naturally matrix[i][j] will
#     be the top right of the new matrix. So a new pefect series of asscending numbers
#     will be automatically formed
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target: # all elements in the row of matrix[i] are smaller than the target
                i += 1
            else:
                j -= 1
        return False

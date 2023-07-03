# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# Note that the given matrix is row-sorted
#
# Using the information that the rows are sorted, if we start searching from the right top corner(1st row,
# last column) and every time when we get a 1, as the row is sorted in non-decreasing order, there is a chance of
# getting 1 in the more left column, so go to previous column on the left of the same row. And if we get 0,
# there is no chance that in that row we can find a 1 on a more left column, so go to next row.
# T: O(M + N)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()

        x, y = 0, N - 1  # The top-right corner
        leftmost_col = -1
        while x < M and y >= 0:
            if binaryMatrix.get(x, y) == 1:
                leftmost_col = y
                y -= 1  # try if the left cell is also 1 in the next round
            else:
                x += 1  # go check the next row
        return leftmost_col

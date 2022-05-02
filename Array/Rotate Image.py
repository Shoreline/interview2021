# Time O(n*n): n*n is the number of cells in matrix
# Rotate from outer rings to inner rings;
# Each ring contatins of multiple steps; each step update 4 values in the ring.
# space O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # top, bottom always equals to left, right. Using two sets of variables just to be more comprehensive
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while left < right:
            for i in range(right - left):
                tmp = matrix[top][left + i]  # element in upper row

                # element in upper row replaced by element of left column
                matrix[top][left + i] = matrix[bottom - i][left]

                # ele of left column <- ele of bottom row
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # ele of bottom row <- ele of right column
                matrix[bottom][right - i] = matrix[top + i][right]

                # ele of right column <- ele of upper row
                matrix[top + i][right] = tmp

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         # Four corners of the current hollow square to be rotated
#         top = 0
#         bottom = len(matrix) - 1
#         left = 0
#         right = len(matrix[0]) - 1

#         while (top < bottom and left < right):
#             for i in range(0, right - left):
#                 tmp = matrix[top][left + i]
#                 matrix[top][left + i] = matrix[bottom - i][left]
#                 matrix[bottom - i][left] = matrix[bottom][right - i]
#                 matrix[bottom][right - i] = matrix[top+i][right]
#                 matrix[top+i][right] = tmp

#             top += 1
#             bottom -=1
#             left +=1
#             right -=1

#         return
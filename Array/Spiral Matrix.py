# /* * Unlike rotate image problem, here there is a chance that top == bottom or left==right. For these cases,
# need to avoid duplicate adding elements. * * (For rotating image, top and bottom will never be equal, same for *
# left and right) */
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        res = []
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])

            for row in range(top + 1, bottom):
                res.append(matrix[row][right])

            if top != bottom:  # corner case!
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
            if left != right:
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return res

# Wrong
# 1. each for loop ignores the last element. So will miss the center piece of a square
# 2. duplicate adding elements when top == bottom
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         top,left = 0,0
#         bottom, right = len(matrix) - 1, len(matrix[0]) -1

#         res = []
#         while top <= bottom and left <= right:
#             for col in range(left, right):
#                 res.append(matrix[top][col])

#             for row in range(top, bottom):
#                 res.append(matrix[row][right])

#             for col in range(right, left,-1):
#                 res.append(matrix[bottom][col])

#             for row in range(bottom, top,-1):
#                 res.append(matrix[row][left])

#             top += 1
#             right -= 1
#             bottom -= 1
#             left += 1

#         return res



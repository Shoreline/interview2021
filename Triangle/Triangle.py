# Triangle: each row has one more element than previous row.
#   Two special cases are the first and last elements
#   For the rest: triangle[i][j] = foobar(triangle[i-1][j-1], triangle[i-1][j])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                pre_min_path = 0
                if 0 < j < len(triangle[i]) - 1:
                    pre_min_path = min(triangle[i - 1][j - 1], triangle[i - 1][j])
                elif j == 0:
                    pre_min_path = triangle[i - 1][j]
                else:
                    pre_min_path = triangle[i - 1][j - 1]

                triangle[i][j] += pre_min_path

        return min(triangle[-1])

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         res = triangle[0][0]
#         for i in range(1, len(triangle)):
#             res = float('inf')  # reset res for every row
#             for j in range(len(triangle[i])):
#                 if j == 0:
#                     triangle[i][j] += triangle[i - 1][0]
#                 elif j == len(triangle[i]) - 1:
#                     triangle[i][j] += triangle[i - 1][j - 1]
#                 else:
#                     triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
#
#                 res = min(res, triangle[i][j])
#
#         return res
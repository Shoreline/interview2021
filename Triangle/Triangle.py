# Triangle: each row has one more element than previous row.
#   Two special cases are the first and last elements
#   For the rest: triangle[i][j] = foobar(triangle[i-1][j-1], triangle[i-1][j])
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[0][0]
        for i in range(1, len(triangle)):
            res = float('inf')  # reset res for every row
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

                res = min(res, triangle[i][j])

        return res
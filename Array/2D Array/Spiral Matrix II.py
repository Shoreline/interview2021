# Traverse a 2D matrix in spiral way
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1

            for i in range(top + 1, bottom):
                res[i][right] = num
                num += 1

            if bottom != top:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = num
                    num += 1
            if left != right:
                for i in range(bottom - 1, top, -1):
                    res[i][left] = num
                    num += 1

            top += 1
            left += 1
            right -= 1
            bottom -= 1

        return res
# DP
# dp[i][j]: the length of the maximum square having bottom right corner at matrix[i][j]
# dp[i][j] =
#   1) 0 if matrix[i][j] == 0
#   2) 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
# -> Those 3 squares overlapp with each other if side length > 1.
# -> if we want to +1 for any one of the 3 surrounding squares, then the side length of the other two squres cannot be smaller than that square
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or (not matrix[0]):
            return 0

        dp = [0] * len(matrix[0])
        diagonal = 0  # need an additional tmp variable
        max_len = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[j], diagonal = 0, dp[j]
                else:
                    dp[j], diagonal = 1 + min(dp[j - 1] if j > 0 else 0, dp[j], diagonal), dp[j]
                    max_len = max(max_len, dp[j])

        return max_len * max_len

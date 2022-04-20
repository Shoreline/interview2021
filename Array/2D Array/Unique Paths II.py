class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0] * len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j - 1] + dp[j]

        return dp[-1]
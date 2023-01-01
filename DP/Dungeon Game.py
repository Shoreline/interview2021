# /*
#  * DP from bottom right corner.
#  *
#  * dp[i][j]: the lowest HP needed to reach bottom right corner (m-1,n-1) from
#  * (i,j). (allow zero hp. so eventually return dp[0][0] + 1)
#  *
#  * dp[i][j] = max(0, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]);
#  *
#  * For point (i,j), pick the route needs smaller HP from (i+1,j) and (i,j+1). If
#  * at point (i,j) there is an orb to heal, the hero needs even less HP (minus
#  * positive), otherwise needs more (minus negative)
#  */

# dp[i][j]: the lowest health needed to rescue the princess from cell (i,j)
# dp[i][j] = survive (i,j), and the best path after (i,j)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [0] * n

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[j] = max(0, - dungeon[i][j])
                elif j == n - 1:
                    dp[j] = max(0, dp[j] - dungeon[i][j])
                elif i == m - 1:
                    dp[j] = max(0, dp[j + 1] - dungeon[i][j])
                else:
                    dp[j] = max(0, min(dp[j], dp[j + 1]) - dungeon[i][j])

        return dp[0] + 1

# Wrong solution
# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         if not dungeon:
#             return 1

#         dp = [0] * len(dungeon[0])
#         smallest = float('inf')

#         for i in range(len(dungeon)):
#             for j in range(len(dungeon[0])):
#                 if j > 0:
#                     dp[j] = dungeon[i][j] + max(dp[j-1], dp[j])
#                 else:
#                     dp[j] = dungeon[i][j] + dp[j]

#                 smallest = min(smallest, dp[j])

#         return abs(smallest) + 1

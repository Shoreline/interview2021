# T: O(m * n); S: O(1)
# Pick the less path: either from left cell or from above cell
# If on the top row / leftmost column: can only pick left / top cell.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                else:
                    grid[i][j] += grid[i - 1][j]

        return grid[-1][-1]

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == 0 and j == 0:
#                     continue
#                 elif i == 0:
#                     grid[i][j] = grid[i][j-1] + grid[i][j]
#                 elif j == 0:
#                     grid[i][j] = grid[i-1][j] + grid[i][j]
#                 else:
#                     grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]

#         return grid[-1][-1]

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         dp = [sys.maxsize] * len(grid[0])
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == 0 and j == 0:
#                     dp[j] = grid[i][j]
#                 elif j == 0:
#                     dp[j] = dp[j] + grid[i][j]
#                 else:
#                     dp[j] = min(dp[j-1], dp[j]) + grid[i][j]

#         return dp[-1]
# Backtrack instead of DP
# T: O(3^N) each cell has 3 directions to actually explore next round (not 4 since one is the original direction it is
# from)
# S: O(N)
# Backtrack instead of DP
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = -1, -1
        non_obstacles = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 0:
                    non_obstacles += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j

        res = 0

        # @lru_cache() Cannot use lru_cache, leads to wrong answer!
        def dfs(x: int, y: int, non_obstacles: int):
            nonlocal res
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            elif grid[x][y] == 2 and non_obstacles == 1:
                res += 1
                return
            elif grid[x][y] < 0:
                return

            non_obstacles -= 1
            tmp = grid[x][y]
            grid[x][y] = -2 # visited
            dfs(x - 1, y, non_obstacles)
            dfs(x + 1, y, non_obstacles)
            dfs(x, y - 1, non_obstacles)
            dfs(x, y + 1, non_obstacles)
            grid[x][y] = tmp

        dfs(start_x, start_y, non_obstacles)
        return res


# Note: Label the starting tile to be an empty tile before running dfs
# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
#         start_x, start_y = -1, -1
#         empty_count = 1
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0:
#                     empty_count += 1
#                 elif grid[i][j] == 1:
#                     start_x, start_y = i, j
#
#         grid[start_x][start_y] = 0
#         res = 0
#
#         # @lru_cache() Cannot use lru_cache, leads to wrong answer!
#         def dfs(x: int, y: int, empty_count: int):
#             nonlocal res
#             if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
#                 return
#             elif grid[x][y] == 2 and empty_count == 0:
#                 res += 1
#                 return
#             elif grid[x][y] != 0:
#                 return
#
#             empty_count -= 1
#             grid[x][y] = -2
#             dfs(x - 1, y, empty_count)
#             dfs(x + 1, y, empty_count)
#             dfs(x, y - 1, empty_count)
#             dfs(x, y + 1, empty_count)
#             grid[x][y] = 0
#
#         dfs(start_x, start_y, empty_count)
#         return res
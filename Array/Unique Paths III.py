# Backtrack insteaed of DP
# Note: Label the starting tile to be an empty tile before running dfs
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = -1, -1
        empty_count = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empty_count += 1
                elif grid[i][j] == 1:
                    start_x, start_y = i, j

        res = 0

        def dfs(x: int, y: int, empty_count: int):
            nonlocal res
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            elif grid[x][y] == 2 and empty_count == 0:
                res += 1
                return
            elif grid[x][y] != 0:
                return

            grid[x][y] = -2
            dfs(x - 1, y, empty_count - 1)
            dfs(x + 1, y, empty_count - 1)
            dfs(x, y - 1, empty_count - 1)
            dfs(x, y + 1, empty_count - 1)
            grid[x][y] = 0

        grid[start_x][start_y] = 0
        dfs(start_x, start_y, empty_count)
        return res
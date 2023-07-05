class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def helper(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + helper(x + 1, y) + helper(x - 1, y) + helper(x, y + 1) + helper(x, y - 1)
            else:
                return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, helper(i, j))

        return res

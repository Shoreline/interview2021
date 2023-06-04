# Note that in this problem '0' is land, '1' is water
#

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def mark(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
                return
            grid[i][j] = 1
            mark(i - 1, j)
            mark(i + 1, j)
            mark(i, j - 1)
            mark(i, j + 1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i in (0, len(grid) - 1) or j in (0, len(grid[0])-1) and grid[i][j] == 0:
                    mark(i,j)
                else:
                    continue

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res += 1
                    mark(i,j)
        return res
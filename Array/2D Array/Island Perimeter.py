# perimeter: /pəˈrɪmɪtər/ 周长
# We can evaluate perimeters off all squares first, and then subtract all sides of cells, which need to be removed, and that is all!
#   4 * num_island_tiles - num_inner_sides
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4 * grid[i][j]

                    # check 4 adjacent cells
                    # if an adjacent cell is also an island, minus res by 1
                    if i > 0:
                        res -= grid[i - 1][j]
                    if i < m - 1:
                        res -= grid[i + 1][j]
                    if j > 0:
                        res -= grid[i][j - 1]
                    if j < n - 1:
                        res -= grid[i][j + 1]

        return res
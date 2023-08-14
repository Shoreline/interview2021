# Same islands = exact shape, WITH any rotation nor reflection
# There are 4 possible rotations and 4 possible reflections
# The 8 rotations and reflections of each point are (against the (0,0) point):
#   (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x).
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = -1
                path.append([i, j])
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)

        # Note: path still saves the absolute coordinates
        def extend():
            variants = [[] for _ in range(8)]  # in total 8 possible rotations + reflections
            for x, y in path:
                variants[0].append([x, y])
                variants[1].append([x, -y])
                variants[2].append([-x, y])
                variants[3].append([-x, -y])
                variants[4].append([y, x])
                variants[5].append([y, -x])
                variants[6].append([-y, x])
                variants[7].append([-y, -x])

            # Convert absolute coordinates into relative coordinates
            for var in variants:
                var.sort()
                x0, y0 = var[0]  # the base cell, picked by a universal rule (first element after sorting).
                for cell in var:
                    cell[0] -= x0
                    cell[1] -= y0

            # Encoding: pick the first variant after sorting the variants, then make a tuple of (c1_x, c1_y, c2_x, c2_y,
            # ...)
            variants.sort()
            encoding = []
            for cell in variants[0]:
                encoding.append(cell[0])
                encoding.append(cell[1])

            return tuple(encoding)

        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []  # reset path
                    dfs(i, j)
                    res.add(extend())
        return len(res)

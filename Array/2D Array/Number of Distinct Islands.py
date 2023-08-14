# Same islands = exact shape, without any rotation nor reflection

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # path: a list saving island cell's relative coordinates
        # Islands of the same shape has the same path
        def dfs(i, j, relative_pos):
            grid[i][j] = -1
            for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                next_i, next_j = i + direction[0], j + direction[1]
                if (0 <= next_i < rows and 0 <= next_j < cols) and grid[next_i][next_j] == 1:
                    new_rel_pos = (relative_pos[0] + direction[0], relative_pos[1] + direction[1])
                    path.append(new_rel_pos)
                    dfs(next_i, next_j, new_rel_pos)

        island_shapes = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, (0, 0))
                    island_shapes.add(tuple(path))
        return len(island_shapes)

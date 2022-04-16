# Label each island: by giving them a unique value
# 1. Explore every island using DFS, count its area, replace its cell value with another "island_index" and save the result to a {index: area} map.
# Loop every cell == 0, check its connected islands and calculate total islands area.

# T and S: O(n^2)
# Refactored.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        # re-lable a island with given island_id, and returns island's area
        def dfs(x, y, island_id):
            area = 0
            if 0 <= x < N and 0 <= y < N and grid[x][y] == 1:
                area = 1
                grid[x][y] = island_id
                area += dfs(x + 1, y, island_id)
                area += dfs(x - 1, y, island_id)
                area += dfs(x, y + 1, island_id)
                area += dfs(x, y - 1, island_id)

            return area

        # DFS every island and give it an index of island
        island_id = 2
        island_area = {0: 0}  # <island_id, area>
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    island_area[island_id] = dfs(x, y, island_id)
                    island_id += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(island_area.values())  # corner case: all n x n board is one island
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    areas_get_connected = 1  # grid[x][y] itself
                    unique_islands = set()

                    for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if 0 <= x + a < N and 0 <= y + b < N and grid[x + a][y + b] > 0 and grid[x + a][
                            y + b] not in unique_islands:
                            areas_get_connected += island_area[grid[x + a][y + b]]
                            unique_islands.add(grid[x + a][y + b])

                    res = max(res, areas_get_connected)
        return res

    # copied
# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         N = len(grid)

#         def move(x, y):
#             for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                 if 0 <= x + i < N and 0 <= y + j < N:
#                     yield x + i, y + j

#         def dfs(x, y, index):
#             res = 0
#             grid[x][y] = index
#             for i, j in move(x, y):
#                 if grid[i][j] == 1:
#                     res += dfs(i, j, index)
#             return res + 1

#         # DFS every island and give it an index of island
#         index = 2
#         areas = {0: 0}
#         for x in range(N):
#             for y in range(N):
#                 if grid[x][y] == 1:
#                     areas[index] = dfs(x, y, index)
#                     index += 1

#         # traverse every 0 cell and count biggest island it can conntect
#         res = max(areas.values())
#         for x in range(N):
#             for y in range(N):
#                 if grid[x][y] == 0:
#                     possible = set(grid[i][j] for i, j in move(x, y))
#                     res = max(res, sum(areas[index] for index in possible) + 1)
#         return res        
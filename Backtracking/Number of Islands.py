# Backtracking
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            mark(i - 1, j)
            mark(i + 1, j)
            mark(i, j - 1)
            mark(i, j + 1)
            return

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    mark(i, j)
        return res

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     count +=1
#                     self.mark(grid, i, j)
#         return count

#     def mark(self, grid:List[List[str]], i: int, j:int) -> None:
#         if i<0 or i >= len(grid) or j<0 or j >= len(grid[0]) or grid[i][j] == '0':
#             return
#         grid[i][j] = '0'

#         self.mark(grid, i-1,j)
#         self.mark(grid, i+1,j)
#         self.mark(grid, i,j-1)
#         self.mark(grid, i,j+1)
# BFS: TLE, used to pass until a new test was added
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m, n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = deque()
                    queue.append((i,j))
                    lvl_len, next_lvl_len = 1, 0
                    step = 0
                    while queue:
                        r, c = queue.popleft()
                        lvl_len -= 1

                        for x, y in [[1,0], [-1,0], [0,1], [0,-1]]:
                            if 0<= r + x< m and 0<= c + y <n and rooms[r+x][c+y] >0 and step+1 < rooms[r+x][c+y] :
                                queue.append((r + x, c + y))
                                next_lvl_len += 1

                        rooms[r][c] = step
                        if lvl_len == 0:
                            lvl_len, next_lvl_len = next_lvl_len, 0
                            step += 1

# DFS: TLE, used to pass until a new test was added
# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         m, n = len(rooms), len(rooms[0])

#         def dfs(x:int, y:int, step:int):
#             if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] < 0 or rooms[x][y] < step:
#                 return

#             rooms[x][y] = step
#             dfs( x+1, y, step + 1)
#             dfs( x-1, y, step + 1)
#             dfs( x, y+1, step + 1)
#             dfs( x, y-1, step + 1)


#         for i in range(m):
#             for j in range(n):
#                 # for each gate, label cloest step
#                 if rooms[i][j] == 0:
#                     dfs(i, j, 0)

# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         m, n = len(rooms), len(rooms[0])

#         for i in range(m):
#             for j in range(n):
#                 # for each gate, label cloest step
#                 if rooms[i][j] == 0:
#                     self.dfs(rooms, i, j, 0)


#     def dfs(self, rooms:list[list[int]], x:int, y:int, step:int):
#         if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] < 0 or rooms[x][y] < step:
#             return

#         rooms[x][y] = step
#         self.dfs(rooms, x+1, y, step + 1)
#         self.dfs(rooms, x-1, y, step + 1)
#         self.dfs(rooms, x, y+1, step + 1)
#         self.dfs(rooms, x, y-1, step + 1)
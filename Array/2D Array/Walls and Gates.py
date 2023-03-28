# BFS from each gate
# Avoid duplicate adding the same node to queue -> use tobe_visited(), not visited()!
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] != 0:
                    continue
                queue = deque([(i, j)])

                while queue:
                    size = len(queue)
                    for _ in range(size):
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            if 0 <= x + dx < m and 0 <= y + dy < n and rooms[x][y] + 1 < rooms[x + dx][y + dy]:
                                # Set new cell val while adding in to queue, not while populating it from queue!
                                # Otherwise it's inefficient and TLE
                                rooms[x + dx][y + dy] = rooms[x][y] + 1
                                queue.append((x + dx, y + dy))

        return

class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # when sees a gate, start a BFS
                    queue = deque()
                    queue.append((i,j))
                    lvl_len, next_lvl_len = 1, 0  # lvl_len: size of this level. Increment step while a level is done.
                    dist = 0
                    added_to_queue = set((i,j))

                    while queue:
                        x, y = queue.popleft()
                        lvl_len -= 1
                        rooms[x][y] = dist

                        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            r, c = x + d[0], y + d[1]
                            if 0 <= r < m and 0 <= c < n and rooms[r][c] not in (-1, 0) and rooms[r][c] > dist + 1 and (
                            r, c) not in added_to_queue:
                                queue.append((r, c))
                                added_to_queue.add((r,c))
                                next_lvl_len += 1

                        if lvl_len == 0:
                            lvl_len, next_lvl_len = next_lvl_len, 0
                            dist += 1



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

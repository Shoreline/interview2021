# https://leetcode.com/problems/trapping-rain-water-ii/solutions/1138028/python3-visualization-bfs-solution-with-explanation/
# BFS with min heap
# Keep expending the "edge cells". Start with the initial edge cells (the most outer circule cells), then expend inwoards. 
#   level: water level 
#   Each time, expand from the lowest edge cell: -> any unvisited neighboring cell with lower height than cur_level (not the lowest edge cell height!) can trap water
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
			
			
		# Initial
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
			
		# Add edge cells first
    # Obviously, all edge cells cannot contain any water
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1 # Use -1 to label visited cells
					
					
		# Start from level 0
        level, res = 0, 0
        while heap:
            height, x, y = heapq.heappop(heap) # get the edge cell with lowest height
            level = max(height, level)
            
            # Only visit the neighboring 4 cells.
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
					  # Increment trapped water right after a cell is added to heap
					  # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]
						
					  # Set the height to -1 if the cell is visited
                    heightMap[i][j] = -1

        return res

# simple
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = -float('inf')
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > cur_max:
                res.append(i)
                cur_max = heights[i]

        return res[::-1]

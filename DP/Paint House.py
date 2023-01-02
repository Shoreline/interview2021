# DP

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0  # Total cost of painting the current house with red/blue/green
        for r, b, g in costs:
            # Must update red/blue/green with one line, so we can use their previous values
            red, blue, green = r + min(blue, green), b + min(red, green), g + min(red, blue)

        return min(red, blue, green)

 # O(1) space, shorter version, can be applied
# for more than 3 colors
# class Solution:
#     def minCost(self, costs):
#         if not costs:
#             return 0
#         dp = costs[0]
#         for i in range(1, len(costs)):
#             pre = dp[:] # here should take care
#             for j in range(len(costs[0])):
#                 dp[j] = costs[i][j] + min(pre[:j]+pre[j+1:])
#         return min(dp)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        cur_house_color = [0] * len(costs[0])

        for i in range(len(costs)):
            pre_house_color = cur_house_color[:]
            for color, cost in enumerate(costs[i]):
                cur_house_color[color] = cost + min(pre_house_color[0:color] + pre_house_color[color + 1:])

        return min(cur_house_color)

# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:
#         min_costs = costs[0][:]
#
#         for i in range(1, len(costs)):
#             pre_min = min_costs[:]
#             for j in range(0, len(costs[i])):
#                 min_costs[j] = costs[i][j] + min(pre_min[:j] + pre_min[j + 1:])
#
#         return min(min_costs)
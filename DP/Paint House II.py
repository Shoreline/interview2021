class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        min_costs = costs[0][:]

        for i in range(1, len(costs)):
            pre_min = min_costs[:]
            for j in range(0, len(costs[i])):
                min_costs[j] = costs[i][j] + min(pre_min[:j] + pre_min[j + 1:])

        return min(min_costs)
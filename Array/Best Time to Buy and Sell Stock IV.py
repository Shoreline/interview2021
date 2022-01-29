# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        costs = [float('inf')] * (k)
        max_profits = [0] * (k)  # max_profit[i] : max profit for i+1 separated transactions

        for price in prices:
            profit_after = 0
            for i in range(k):
                costs[i] = min(costs[i], price - profit_after)
                max_profits[i] = max(max_profits[i], price - costs[i])
                profit_after = max_profits[i]
        return max_profits[-1]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# one transaction contains two operations: buy and sell.
# But we are not allow buying again before selling.
#
# We are looking for most profitable of k-separated transactions
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        min_costs = [float('inf')] * k # min_costs[i]: min cost after i-1 transactions (so far)
        max_profits = [0] * k  # max_profit[i] : max profit after i transactions (so far)
        pre_profit = 0  # max profit so far after previous transactions

        for p in prices:
            for i in range(k):
                min_costs[i] = min(min_costs[i], p if i == 0 else p - pre_profit)  # price adjusted by earlier best profit
                max_profits[i] = max(max_profits[i], p - min_costs[i])
                pre_profit = max_profits[i]
        return max_profits[-1]
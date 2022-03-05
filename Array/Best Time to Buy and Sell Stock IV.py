# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# one transaction contains two operations: buy and sell.
# But we are not allow to buy again before selling.
#
# We are looking for most profitable of k-separated transactions
#
# k: the merged transaction of k transactions
# cost[k]: So far (till price[today]), the dip after the overall most profitable k-1 transactions
# profit[k]: So far (till price[today]), the highest overall profit for k transactions
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        costs = [float('inf')] * k
        max_profits = [0] * k  # max_profit[i] : max profit for i+1 separated transactions

        for p in prices:
            profit = 0  # max profit after previous i - 1 transactions
            for i in range(k):
                costs[i] = min(costs[i], p - profit)  # price in earlier best profit
                max_profits[i] = max(max_profits[i], p - costs[i])
                profit = max_profits[i]
        return max_profits[-1]
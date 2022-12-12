# Only allow one [buy-sell] pair
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_sofar = min(min_sofar, prices[i])
            max_profit = max(max_profit, prices[i] - min_sofar)
        return max_profit
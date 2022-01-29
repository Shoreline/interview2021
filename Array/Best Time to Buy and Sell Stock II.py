# The profit is the sum of all positive increment between prices[i] and prices[i-1]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit

    # class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         buy_price = prices[0]
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > buy_price:
#                 profit += (prices[i] - buy_price)

#             buy_price = prices[i]

#         return profit    
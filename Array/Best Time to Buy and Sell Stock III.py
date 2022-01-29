# can only allow to do [buy, sell, buy, sell], cannot do [buy, buy, sell, sell]
# Note: ok to do <= 2 transactions. So if the stock keeps going south then just return 0
# [5, 85, 84, 105, 110] -> 106
# 1st traction is not necessarily the most profitable transaction.
# We are not seeking most and 2nd most profitable transactions (can't do that since we can only hold one share at a time)
#
# We are looking for most profitable of two-separated transactions
#
# t_k: the merged transaction of k transactions
# t_k_cost: So far (till price[i]), the dip after the overall most profitable k-1 transactions
# t_k_profit: So far (till price[i]), the highest overall profit for k transactions
#
# t1 is the most profitable singular transaction
# t2 is the most overall profitable two-seprated transactions. It dost NOT ensure the 2nd buy in t2 happens after t1 (the most profitable one). And we shall NOT seek that sort of ensurance
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the first transaction
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            # compute the most profitable two-separated transactions
            # For the 2nd transaction, the cost of a stock can be treated in this way:
            # - Since I already got some profit from the first transaction, the cost of 2nd buy is cheaper FOR ME: it will be price[i] - current_profit
            t2_cost = min(t2_cost, price - t1_profit)  # t2_cost can be negative
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

    # General solution of for k transactions
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if k == 0:
#             return 0

#         costs = [float('inf')] * (k)
#         max_profits = [0] * (k) # max_profit[i] : max profit for i+1 separated transactions

#         for price in prices:
#             profit_after = 0
#             for i in range(k):
#                 costs[i] = min(costs[i], price - profit_after)
#                 max_profits[i] = max(max_profits[i], price - costs[i])
#                 profit_after = max_profits[i]
#         return max_profits[-1]

#     /*
#      * DP, time O(kN), space O(2kN), works for any k transactions
#      *
#      * Can reduce space to O(2N)
#      *
#      * global[i][j]: the maximum profit after day i and j transactions (i from 0 to prices.length-1; j from 0 to k. Both inclusively)
#      * local[i][j]:  the maximum profit after day i and j transactions. Particularly, the j-th sell must happen on day i.
#      *
#      * A transaction can be to buy and sell on the same day -> profit is 0
#      *
#      * Initialization:
#      * global[0][j] = 0: after the first day, profit always 0 (all buys and sells happen on the same day)
#      * global[i][0] = 0: obviously, with 0 transaction the profit will always be 0
#      * Same for local[][].
#      *
#      * global[i][j] = Math.max( global[i-1][j], local[i][j] )
#      * Two possible situations: ( these situations may have overlap, which is fine. As long as they can cover all possible cases)
#      * 1) the last sell is not finished on day i: global[i-1][j]
#      * 2) the last sell is finished on day i: local[i][j]
#      *
#      * local[i][j] = Math.max( global[i-1][j-1] + Math.max(dailyDiff,0), local[i-1][j] + dailyDiff )
#      * Two possible situations:
#      * 1) The j-th buy happens on or before day i-1: local[i-1][j] + dailyDiff
#      * Since local[i][j] must sell on day j, so we have to extend the j-th sell of local[i-1][j] and include dailyDiff. No matter dailyDiff is positive or negative
#      *
#      * 2) The j-th buy happens on or after day i-1: global[i-1][j-1] + Math.max(dailyDiff,0)
#      * If dailyDiff is negative, we can choose to both buy and sell on day j
#      *
#      */
#     public class Solution_N {
# 	public int maxProfit(int[] prices) {
# 	    if (prices == null || prices.length < 2) {
# 		  return 0;
# 	    }

# 	    int k = 2;
# 	    int[][] global = new int[prices.length][k + 1];
# 	    int[][] local = new int[prices.length][k + 1];

# 	    for (int i = 1; i < prices.length; i++) {
#             int dailyDiff = prices[i] - prices[i - 1];
#             for (int j = 1; j <= k; j++) {
#                 local[i][j] = Math.max(global[i - 1][j - 1] + Math.max(dailyDiff, 0), local[i - 1][j] + dailyDiff);
#                 global[i][j] = Math.max(local[i][j], global[i - 1][j]);
#             }
# 	    }

# 	    return global[global.length - 1][k];
# 	    }
#     }
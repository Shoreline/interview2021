# bottom up dp
# dp[i]: the least number of coins to sum up to i dollars
# dp[i] = min(dp[i], dp[i- c1] + 1, dp[i- c2] + 1, ...). c1,c2,... is the denomination of different coin types
# time: O(n*c). n is the amount needs to be sum up, c is the number of coin types
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # Need 0 coins to get $0.

        for amt in range(amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

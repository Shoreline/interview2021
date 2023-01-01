# Combination sum problem
# bottom-up DP
# Switched the inner/outer order of the for loops, as in combination sum IV (the permutation sum version of this problem.)
#   If iterate amount first, we will double count.
#   E.g. amount= 3, and coins = [1,2]. Then [1,2] and [2,1] are counted as two ways to get 3.
# dp[i]: ways to make up i amount

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(amount + 1):
                # one way to get amt from amt - coin: amt - coin + coin
                # So if there is dp[amt-coin] ways to come up amt - coin;
                #   then there dp[amt] = sigma(dp[amt-coin]), while coin is every type of coin denomination
                if amt - coin >= 0:
                    dp[amt] += dp[amt - coin]
        return dp[amount]
